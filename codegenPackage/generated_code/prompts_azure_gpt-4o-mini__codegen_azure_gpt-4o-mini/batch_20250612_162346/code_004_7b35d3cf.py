"""
Generated Code Metadata:
========================
Original URL: https://stonegarden.dev
Prompt: Create a sample project structure for using GitHub Actions alongside GitLab CI, inspired by the content on Stonegarden.dev.
Generated: DETERMINISTIC_7b35d3cf05677c8a
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```plaintext
my-sample-project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitlab-ci.yml
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── test_main.py
│   └── test_utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest tests/
```

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test

build:
  stage: build
  script:
    - echo "Building the project..."
    - python -m pip install --upgrade pip
    - pip install -r requirements.txt

test:
  stage: test
  script:
    - echo "Running tests..."
    - pytest tests/
```

```python
# src/main.py
def main():
    """Main entry point of the application."""
    print("Hello, World!")

if __name__ == "__main__":
    main()
```

```python
# src/utils.py
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

```python
# tests/test_main.py
import pytest
from src.main import main

def test_main(capsys):
    """Test the main function output."""
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
```

```python
# tests/test_utils.py
import pytest
from src.utils import add

def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

```plaintext
# requirements.txt
pytest
```

```markdown
# README.md
# My Sample Project

This is a sample project demonstrating the use of GitHub Actions and GitLab CI for continuous integration.

## Project Structure

- `src/`: Contains the source code.
- `tests/`: Contains the test cases.
- `.github/workflows/ci.yml`: GitHub Actions workflow configuration.
- `.gitlab-ci.yml`: GitLab CI configuration.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## Getting Started

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the application with `python src/main.py`.
4. Run tests with `pytest tests/`.
```

```plaintext
# .gitignore
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
*.sqlite3
```
