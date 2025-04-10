# Code Reviewer Prompt

## Description
An advanced prompt that helps identify bugs, security vulnerabilities, inefficiencies, and style issues in your code. Acts as a professional peer reviewer to improve code quality and maintainability.

## Tags
#coding, #development, #code-review, #debugging, #security

## Prompt Text
```
Act as an expert software developer with deep knowledge of [language/framework] and best practices in software engineering. I need you to review the following code and provide comprehensive feedback.

```[language]
[paste your code here]
```

Please analyze the code for:

1. **Functionality**: Does the code work as intended? Are there any logical errors or bugs?
2. **Performance**: Are there any performance bottlenecks or inefficiencies that could be improved?
3. **Security**: Are there any security vulnerabilities or potential exploits?
4. **Readability**: Is the code easy to understand? Are there clear comments and consistent naming conventions?
5. **Maintainability**: How easy would it be to modify or extend this code in the future?
6. **Code Style**: Does the code follow standard conventions for [language/framework]?
7. **Testing**: What test cases would you recommend to verify this code works correctly?

For each issue identified:
- Explain what the issue is and why it's a problem
- Provide a specific code example of how to fix it
- If relevant, explain the underlying principle or best practice

After the detailed review, provide a summary of the 3-5 most important changes that should be made, in order of priority.
```

## Examples
When used to review a Python function with inefficient list operations, the AI identified:
1. A potential out-of-bounds error in a list access
2. An O(n²) operation that could be reduced to O(n) with a better algorithm
3. Variable names that didn't follow PEP 8 conventions
4. Missing error handling for edge cases
5. Suggestions for adding docstrings and type hints

## Notes
- Be specific about the language or framework to get more relevant feedback
- This prompt works well for code snippets up to a few hundred lines
- For larger codebases, break down the review into multiple components
- You can focus the review by removing categories you're not concerned about

## Source
Developed by [Your Name/Handle], based on professional code review processes
