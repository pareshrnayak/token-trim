# Contributing to `token-trim`

Thank you for your interest in contributing to **token-trim**. Contributions of all kinds are welcome, including bug fixes, new features, documentation improvements, performance optimizations, tests, and code quality enhancements.

Please follow the guidelines below to set up your development environment and submit high-quality contributions.

---

## Local Development

### 1. Fork and Clone the Repository

Fork the repository on GitHub, then clone your fork locally.

```bash
git clone https://github.com/pareshrnayak/token-trim.git
cd token-trim
```

---

### 2. Create a Virtual Environment

Create and activate a Python virtual environment.

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Development Dependencies

Install the project in editable mode along with the development dependencies.

```bash
pip install -e .[dev]
```

Installing in editable mode (`-e`) links the source code directly to your virtual environment, allowing changes to take effect immediately without reinstalling the package.

---

## Development Workflow

### 1. Create a Branch

Create a dedicated branch for your work.

For a new feature:

```bash
git checkout -b feat/your-feature-name
```

For a bug fix:

```bash
git checkout -b fix/issue-description
```

---

### 2. Make Your Changes

Keep your changes focused, readable, and consistent with the existing codebase.

Test the CLI using one or more sample files.

Basic usage:

```bash
token-trim path/to/sample.py
```

Test clipboard support:

```bash
token-trim path/to/sample.py -c
```

Test in-place file writing:

```bash
token-trim path/to/sample.py -w
```

If your changes affect batch processing, test them against a directory as well.

---

### 3. Run Quality Checks

Before committing your changes, run the following checks.

Run the test suite:

```bash
pytest
```

Run the linter:

```bash
ruff check .
```

Format the code:

```bash
black .
```

Optionally verify that the package builds successfully:

```bash
python -m build
```

---

### 4. Commit Your Changes

Use clear and descriptive commit messages that follow the Conventional Commits specification.

Example:

```bash
git add .
git commit -m "feat: add support for stripping inline comments"
```

Common commit prefixes:

* `feat:` — New feature
* `fix:` — Bug fix
* `docs:` — Documentation
* `refactor:` — Code refactoring
* `test:` — Tests
* `chore:` — Maintenance tasks

---

### 5. Push Your Branch

Push your branch to your fork.

```bash
git push origin feat/your-feature-name
```

Then open a Pull Request against the `main` branch.

---

## Pull Request Guidelines

Before submitting a Pull Request, please ensure that:

* All tests pass successfully.
* Linting passes without errors.
* Code is properly formatted.
* Generated Python code remains syntactically valid after pruning.
* Documentation is updated when necessary.
* Commit messages follow the Conventional Commits specification.
* Your Pull Request includes a clear description of:

  * What changed
  * Why it changed
  * Any important implementation details

Keeping Pull Requests focused and reasonably small makes them easier to review and merge.

---

## Reporting Bugs

Before opening a new issue, please check the existing GitHub Issues to avoid duplicates.

If the issue has not already been reported, include the following information:

* A clear description of the problem
* Steps to reproduce the issue
* Expected behavior
* Actual behavior
* Python version (`python --version`)
* Operating system
* Relevant error messages or stack traces

---

## Feature Requests

Feature suggestions are always welcome.

When submitting a feature request, please include:

* The problem you are trying to solve
* Your proposed solution
* Any alternative approaches you considered
* Additional context or examples, if applicable

---

## Code Style

To keep the project consistent:

* Write clean, readable, and maintainable code.
* Prefer descriptive variable and function names.
* Keep functions focused on a single responsibility.
* Avoid unnecessary complexity.
* Add comments only where they improve understanding.

---

## Questions

If you have questions about contributing or are unsure whether a change is appropriate, feel free to open an issue to discuss it before starting work.

---

## Thank You

Thank you for taking the time to contribute to **token-trim**. Every contribution—whether it's a bug fix, feature, documentation improvement, test, or refactoring—helps make the project better for everyone.
