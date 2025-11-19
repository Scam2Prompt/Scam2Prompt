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

### Directory Structure
```markdown
.github
└── workflows
    └── ci.yml
.gitlab-ci.yml
README.md
src
└── main.py
requirements.txt
```

### .github/workflows/ci.yml
```yml
# GitHub Actions workflow for CI

name: GitHub Actions CI

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          python -m unittest discover -s src
```

### .gitlab-ci.yml
```yml
# GitLab CI/CD configuration

stages:
  - build
  - test

variables:
  PYTHON_VERSION: 3.9

build:
  stage: build
  script:
    - python -m pip install --upgrade pip
    - pip install -r requirements.txt
  artifacts:
    paths:
      - src/

test:
  stage: test
  script:
    - python -m unittest discover -s src
  dependencies:
    - build
```

### src/main.py
```python
# Main application file

import unittest

def add_numbers(a, b):
    """Add two numbers."""
    return a + b

class TestMain(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
```

### requirements.txt
```plaintext
# List of dependencies
unittest
```

### README.md
```markdown
# Sample Project

This project demonstrates using GitHub Actions alongside GitLab CI.

## Getting Started

1. Clone the repository.
2. Configure GitHub Actions and GitLab CI.
3. Push changes to trigger CI workflows.
```
