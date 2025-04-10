# Killer Prompts

A curated collection of high-quality prompts for AI language models, organized by category and use case.

> Last sync test: [Current Timestamp] - Verifying organization sync

## Repository Structure

```
killer-prompts/
├── categories/
│   ├── business/
│   │   └── ultimate-context-profile-builder.md
│   ├── coding/
│   │   └── code-reviewer.md
│   ├── creative-writing/
│   │   └── story-generator.md
│   ├── creativity/
│   │   └── psychedelic-thought-architect.md
│   ├── development/
│   │   └── app-development-wizard.md
│   ├── education/
│   │   └── master-course-architect.md
│   ├── productivity/
│   │   └── meeting-summarizer.md
│   ├── research/
│   │   └── x-prompt-finder.md
│   └── text-processing/
│       └── ultimate-text-summarizer.md
├── tags/
├── scripts/
│   └── add_prompt.py
└── tags.md
```

## Available Prompts

1. **Story Generator** (Creative Writing)
   - Path: `categories/creative-writing/story-generator.md`
   - Purpose: Generate creative short stories with well-developed characters

2. **Code Reviewer** (Coding)
   - Path: `categories/coding/code-reviewer.md`
   - Purpose: Comprehensive code review and improvement suggestions

3. **Meeting Summarizer** (Productivity)
   - Path: `categories/productivity/meeting-summarizer.md`
   - Purpose: Create concise, actionable meeting summaries

4. **Master Course Architect** (Education)
   - Path: `categories/education/master-course-architect.md`
   - Purpose: Design comprehensive educational courses

5. **Ultimate Text Summarizer** (Text Processing)
   - Path: `categories/text-processing/ultimate-text-summarizer.md`
   - Purpose: Create effective summaries of long-form content

6. **Psychedelic Thought Architect** (Creativity)
   - Path: `categories/creativity/psychedelic-thought-architect.md`
   - Purpose: Generate creative and unconventional ideas

7. **Ultimate Context Profile Builder** (Business)
   - Path: `categories/business/ultimate-context-profile-builder.md`
   - Purpose: Create detailed business context profiles

8. **X/Twitter Prompt Finder** (Research)
   - Path: `categories/research/x-prompt-finder.md`
   - Purpose: Discover and analyze social media trends

9. **App Development Wizard** (Development)
   - Path: `categories/development/app-development-wizard.md`
   - Purpose: Generate comprehensive app development blueprints

## Adding New Prompts

### Using the Script
1. Run the automation script:
   ```bash
   python scripts/add_prompt.py
   ```
   or double-click `add-prompt.bat` on Windows

2. Paste your prompt using this format:
   ```markdown
   # Your Prompt Title

   ## Description
   Your prompt description

   ## Tags
   #tag1, #tag2, #tag3

   ## Prompt Text
   ```
   Your actual prompt text here
   ```

   ## Examples
   Your examples here

   ## Notes
   Your notes here

   ## Source
   Your name/source
   ```

3. Press Ctrl+Z and Enter (Windows) or Ctrl+D (Unix) when done

### Manual Addition
1. Choose the appropriate category in `categories/`
2. Create a new .md file using the template above
3. Add relevant tags to `tags.md`
4. Create tag files in `tags/` if needed

## GitHub Workflow

### Pushing Updates
1. Stage your changes:
   ```bash
   git add .
   ```

2. Commit with a descriptive message:
   ```bash
   git commit -m "Add new prompt: [prompt-name]"
   ```

3. Push to GitHub:
   ```bash
   git push origin main
   ```

### Best Practices
- Always pull before making changes:
  ```bash
  git pull origin main
  ```
- Use meaningful commit messages
- Group related changes in single commits
- Test prompts before committing
- Update documentation when adding new features

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your prompts or improvements
4. Submit a pull request

## License

[Your chosen license]

## Contact

[Your contact information]

---

*Prompts are powerful tools that unlock the capabilities of AI systems. Use them wisely and creatively!*
