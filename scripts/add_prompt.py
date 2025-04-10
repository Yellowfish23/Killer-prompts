import os
import re
import sys
import json
from datetime import datetime
import subprocess
from typing import Dict, List, Optional

def sanitize_filename(name: str) -> str:
    """Convert a string to a valid filename."""
    # Convert to lowercase and replace spaces with hyphens
    name = name.lower().replace(' ', '-')
    # Remove any characters that aren't alphanumeric or hyphens
    name = re.sub(r'[^a-z0-9-]', '', name)
    return name

def extract_tags(content: str) -> List[str]:
    """Extract hashtags from content."""
    return re.findall(r'#\w+', content)

def detect_category(content: str) -> str:
    """Detect the most appropriate category based on content."""
    categories = {
        'coding': ['code', 'programming', 'developer', 'software', 'git', 'debug'],
        'education': ['learn', 'teach', 'study', 'education', 'course'],
        'productivity': ['workflow', 'efficiency', 'organize', 'productivity'],
        'creative-writing': ['write', 'story', 'creative', 'narrative'],
        'research': ['research', 'analyze', 'study', 'investigate'],
        'problem-solving': ['solve', 'solution', 'problem', 'fix'],
        'learning': ['learn', 'understand', 'comprehend', 'study']
    }
    
    content_lower = content.lower()
    category_scores = {cat: sum(1 for word in words if word in content_lower) 
                      for cat, words in categories.items()}
    
    return max(category_scores.items(), key=lambda x: x[1])[0]

def create_prompt_file(content: str) -> None:
    """Create a new prompt file with the given content."""
    # Extract title from the first line that starts with #
    title_match = re.search(r'^#\s*(.+)$', content, re.MULTILINE)
    if not title_match:
        print("Error: Prompt must start with a title (# Title)")
        sys.exit(1)
    
    title = title_match.group(1)
    filename = sanitize_filename(title)
    category = detect_category(content)
    
    # Ensure category directory exists
    category_path = os.path.join('categories', category)
    os.makedirs(category_path, exist_ok=True)
    
    # Create prompt file
    file_path = os.path.join(category_path, f"{filename}.md")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Extract and handle tags
    tags = extract_tags(content)
    update_tags(tags)
    
    # Git operations
    try:
        subprocess.run(['git', 'add', file_path], check=True)
        subprocess.run(['git', 'commit', '-m', f'Add new prompt: {title}'], check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        print(f"Successfully added prompt: {title}")
    except subprocess.CalledProcessError as e:
        print(f"Error in Git operations: {e}")

def update_tags(new_tags: List[str]) -> None:
    """Update tags.md and create tag files."""
    # Update tags.md
    tags_content = []
    if os.path.exists('tags.md'):
        with open('tags.md', 'r', encoding='utf-8') as f:
            tags_content = f.read().splitlines()
    
    # Add new tags
    tags_set = set(tags_content)
    for tag in new_tags:
        if tag not in tags_set:
            tags_content.append(tag)
            # Create tag file
            tag_filename = f"tags/{sanitize_filename(tag[1:])}.md"  # Remove # from tag
            os.makedirs('tags', exist_ok=True)
            with open(tag_filename, 'w', encoding='utf-8') as f:
                f.write(f"# {tag}\n\nPrompts related to {tag[1:]}")
    
    # Write updated tags
    with open('tags.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(tags_content)))

def main():
    """Main function to handle prompt input."""
    print("Paste your prompt (Press Ctrl+D on Unix or Ctrl+Z on Windows when done):")
    content = sys.stdin.read().strip()
    
    if not content:
        print("Error: No content provided")
        sys.exit(1)
    
    create_prompt_file(content)

if __name__ == "__main__":
    main() 