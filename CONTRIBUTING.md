````markdown
# Contributing to `token-trim`

Thank you for your interest in contributing to **token-trim**. Contributions of all kinds are welcome, including bug fixes, new features, documentation improvements, performance optimizations, and code quality enhancements.

Please follow the guidelines below to ensure a smooth development and review process.

---

# Local Development

## 1. Fork and Clone the Repository

Fork the repository on GitHub, then clone your fork locally.

```bash
git clone https://github.com/your-username/token-trim.git
cd token-trim
```

---

## 2. Create a Virtual Environment

Create and activate a Python virtual environment.

### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

Install all required packages.

```bash
pip install -r requirements.txt
```

---

# Development Workflow

## 1. Create a Branch

Create a dedicated branch for your work.

For new features:

```bash
git checkout -b feat/your-feature-name
```

For bug fixes:

```bash
git checkout -b fix/issue-description
```

---

## 2. Make Your Changes

Implement your changes while keeping the codebase clean, readable, and consistent with the existing style.

After making changes, test the CLI against one or more sample Python files.

Example:

```bash
python app.py prune test_file.py
```

Verify that:

- Python syntax remains valid
- Output is correct
- No unexpected behavior is introduced

---

## 3. Commit Your Changes

Use clear and descriptive commit messages following the Conventional Commits specification.

Example:

```bash
git add .
git commit -m "feat: add support for stripping inline comments"
```

Common commit prefixes:

- `feat:` — New feature
- `fix:` — Bug fix
- `docs:` — Documentation
- `refactor:` — Code refactoring
- `test:` — Tests
- `chore:` — Maintenance tasks

---

## 4. Push Your Branch

Push your branch to your fork.

```bash
git push origin feat/your-feature-name
```

Then open a Pull Request on GitHub.

---

# Pull Request Guidelines

Before opening a Pull Request, please ensure that:

- Your code follows the existing project style.
- The project runs without errors.
- Generated Python code remains syntactically valid.
- Your changes have been tested with real `.py` files.
- Documentation is updated where necessary.
- Commit messages follow the Conventional Commits format.
- Your Pull Request clearly explains:
  - What changed
  - Why it was changed
  - Any important implementation details

Keeping Pull Requests focused and reasonably small helps reviewers provide faster feedback.

---

# Reporting Bugs

If you discover a bug, please check whether it has already been reported.

If not, open a new GitHub Issue and include:

- A clear description of the problem
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Python version
- Operating system
- Relevant error messages or screenshots (if applicable)

---

# Feature Requests

Feature suggestions are welcome.

When creating a feature request, please include:

- The problem you are trying to solve
- Your proposed solution
- Any alternative approaches you considered
- Additional context, if applicable

---

# Code Style

Please keep contributions consistent with the existing codebase.

General recommendations:

- Write readable, maintainable code.
- Keep functions focused and concise.
- Avoid unnecessary complexity.
- Add comments only where they improve clarity.
- Prefer descriptive variable and function names.

---

# Testing

Before submitting your contribution, verify that:

```bash
python app.py prune sample.py
```

Test with multiple Python files whenever possible to ensure the output remains correct.

---

# Submitting Your Contribution

Once everything is ready:

```bash
git add .
git commit -m "feat: your concise description"
git push origin your-branch-name
```

Finally, open a Pull Request and provide a clear description of your contribution.

---

# Thank You

Thank you for taking the time to contribute to **token-trim**. Every contribution, whether it is a bug fix, feature improvement, documentation update, or code cleanup, helps make the project better for everyone.
````
