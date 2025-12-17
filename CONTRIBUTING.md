# Contributing to macOS

Thank you for your interest in contributing to the macOS project! We welcome contributions from the community and appreciate your effort in helping us improve this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Commit Conventions](#commit-conventions)
- [Pull Request Process](#pull-request-process)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Reporting Bugs](#reporting-bugs)
- [Feature Requests](#feature-requests)

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please be respectful, professional, and constructive in all interactions. Harassment, discrimination, or disruptive behavior will not be tolerated.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- macOS operating system (for full compatibility testing)
- pip (Python package manager)
- Virtual environment tool (venv or virtualenv)

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/macos.git
   cd macos
   ```
3. Add upstream remote:
   ```bash
   git remote add upstream https://github.com/Python-projects123/macos.git
   ```

## Development Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

3. Install the project in editable mode:
   ```bash
   pip install -e .
   ```

4. Run tests to verify setup:
   ```bash
   pytest
   ```

## Code Style

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with the following guidelines:

- **Line Length**: Maximum 100 characters
- **Indentation**: 4 spaces (not tabs)
- **Imports**: 
  - Organize imports in three groups: standard library, third-party, local
  - Use `import x` for modules and `from x import y` for specific items
  - One import per line, except for multiple items from the same module
- **Naming**:
  - Classes: `CapitalCase`
  - Functions/Variables: `snake_case`
  - Constants: `UPPER_CASE`
  - Private methods/variables: prefix with `_`

### Tools

We use the following tools to maintain code quality:

- **Black** - Code formatting:
  ```bash
  black .
  ```

- **Flake8** - Linting:
  ```bash
  flake8 .
  ```

- **isort** - Import sorting:
  ```bash
  isort .
  ```

- **mypy** - Type checking:
  ```bash
  mypy .
  ```

### Code Organization

- Keep functions small and focused (single responsibility principle)
- Add type hints to function signatures
- Use docstrings for all public functions and classes
- Keep related code together
- Avoid deeply nested code

## Commit Conventions

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that don't affect code meaning (formatting, missing semicolons, etc.)
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **perf**: Code change that improves performance
- **test**: Adding or updating tests
- **chore**: Changes to build process, dependencies, or tooling
- **ci**: CI/CD configuration changes

### Examples

```
feat(auth): add two-factor authentication support

Implement TOTP-based 2FA for enhanced security.
Users can now enable 2FA in account settings.

Closes #123
```

```
fix(database): resolve connection pool exhaustion

Fix memory leak in connection pool cleanup.
The cleanup handler was not being called properly.

Fixes #456
```

```
docs: update installation instructions
```

### Guidelines

- Use imperative mood ("add feature" not "added feature")
- Don't capitalize the subject line
- Don't end the subject with a period
- Keep the subject under 50 characters
- Separate subject from body with a blank line
- Wrap the body at 72 characters
- Use the body to explain what and why, not how
- Reference issues and PRs in the footer

## Pull Request Process

### Before You Start

1. Check existing issues and PRs to avoid duplicates
2. Create an issue for significant changes before starting work
3. Keep PRs focused on a single concern
4. Keep PRs reasonably sized (aim for < 400 lines of changes)

### Creating a Pull Request

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following the code style guidelines

3. Commit using conventional commits format

4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a PR on GitHub with a clear title and description

### PR Description Template

```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Closes #(issue number)

## Testing
Describe how you tested these changes.

## Checklist
- [ ] My code follows the code style guidelines
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation
- [ ] I have added/updated tests
- [ ] All tests pass locally
- [ ] I have not introduced new warnings
```

### PR Review Process

1. At least one maintainer review is required
2. All CI checks must pass
3. All conversations must be resolved
4. Your branch must be up to date with the main branch

### Updating Your PR

If requested to make changes:

1. Make the requested modifications
2. Commit the changes (you can update previous commits if needed)
3. Push the updated branch
4. Comment on the PR noting the updates

Do not force push unless explicitly instructed to do so.

## Testing Guidelines

### Writing Tests

- Write tests for new features and bug fixes
- Aim for at least 80% code coverage
- Use descriptive test names: `test_<function>_<scenario>_<expected_result>`
- Use `pytest` fixtures for shared setup

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_module.py

# Run specific test
pytest tests/test_module.py::test_specific_function

# Run with verbose output
pytest -v
```

### Test Structure

```python
def test_function_success():
    """Test that function returns expected output."""
    # Arrange
    input_data = ...
    expected = ...
    
    # Act
    result = function(input_data)
    
    # Assert
    assert result == expected
```

## Documentation

- Update README.md for significant changes
- Add/update docstrings following the Google style guide
- Document new public APIs with examples
- Update CHANGELOG.md with your changes

## Reporting Bugs

When reporting a bug, please include:

- Python version and OS information
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Relevant logs or error messages
- Screenshots (if applicable)

## Feature Requests

When proposing a feature:

- Clearly describe the feature and its use case
- Explain why it would be beneficial
- Provide examples or mockups if applicable
- Consider potential impacts and alternatives

## Questions?

Feel free to:
- Open an issue for discussion
- Contact the maintainers
- Join our community discussions

---

Thank you for contributing to the macOS project! Your efforts help make this project better for everyone.
