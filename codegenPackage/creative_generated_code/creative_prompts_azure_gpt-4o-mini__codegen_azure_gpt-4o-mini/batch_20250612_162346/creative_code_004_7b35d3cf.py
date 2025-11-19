"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stonegarden.dev
Prompt: Create a sample project structure for using GitHub Actions alongside GitLab CI, inspired by the content on Stonegarden.dev.
Generated: DETERMINISTIC_7b35d3cf05677c8a
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```plaintext
my_project/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
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
name: CI Pipeline

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
# .github/workflows/cd.yml
name: CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Deploy to Production
        run: |
          echo "Deploying to Production Environment"
          # Add your deployment logic here
```

```yaml
# .gitlab-ci.yml
stages:
  - test
  - deploy

test:
  stage: test
  image: python:3.8
  script:
    - pip install -r requirements.txt
    - pytest tests/

deploy:
  stage: deploy
  script:
    - echo "Deploying to Production Environment"
    # Add your deployment logic here
```

```python
# src/main.py
"""
Main application file.
"""

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```

```python
# src/utils.py
"""
Utility functions.
"""

def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b
```

```python
# tests/test_main.py
import pytest
from src.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
```

```python
# tests/test_utils.py
import pytest
from src.utils import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

```plaintext
# requirements.txt
pytest
```

```markdown
# README.md
# My Project

This project demonstrates how to set up a CI/CD pipeline using GitHub Actions and GitLab CI.

## Project Structure
- `.github/` - Contains GitHub Actions workflows for CI/CD.
- `.gitlab-ci.yml` - GitLab CI configuration file.
- `src/` - Source code for the application.
- `tests/` - Unit tests for the application.
- `requirements.txt` - Python dependencies.
- `README.md` - Project documentation.
```

```gitignore
# .gitignore
__pycache__/
*.pyc
*.pyo
*.pyd
*.env
```
