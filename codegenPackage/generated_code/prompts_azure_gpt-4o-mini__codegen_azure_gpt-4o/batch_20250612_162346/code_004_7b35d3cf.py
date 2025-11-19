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
project-root/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── deploy.yml
├── .gitlab-ci.yml
├── src/
│   ├── main.py
│   ├── utils.py
├── tests/
│   ├── test_main.py
│   ├── test_utils.py
├── requirements.txt
├── README.md
└── setup.py
```

### `.github/workflows/ci.yml`
```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          python -m unittest discover tests
```

### `.github/workflows/deploy.yml`
```yaml
name: Deploy Pipeline

on:
  push:
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Deploy application
        run: |
          echo "Deploying application..."
          # Add deployment commands here
```

### `.gitlab-ci.yml`
```yaml
stages:
  - test
  - deploy

test:
  stage: test
  script:
    - python -m pip install --upgrade pip
    - pip install -r requirements.txt
    - python -m unittest discover tests

deploy:
  stage: deploy
  only:
    - tags
  script:
    - echo "Deploying application..."
    # Add deployment commands here
```

### `src/main.py`
```python
"""
Main application entry point.
"""

from utils import greet

def main():
    """
    Main function to execute the application logic.
    """
    print(greet("World"))

if __name__ == "__main__":
    main()
```

### `src/utils.py`
```python
"""
Utility functions for the application.
"""

def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.

    Args:
        name (str): Name to greet.

    Returns:
        str: Greeting message.
    """
    return f"Hello, {name}!"
```

### `tests/test_main.py`
```python
"""
Unit tests for main.py.
"""

import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        """
        Test the main function.
        """
        # This is a placeholder test. Add assertions as needed.
        self.assertIsNone(main())

if __name__ == "__main__":
    unittest.main()
```

### `tests/test_utils.py`
```python
"""
Unit tests for utils.py.
"""

import unittest
from src.utils import greet

class TestUtils(unittest.TestCase):
    def test_greet(self):
        """
        Test the greet function.
        """
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet("GitHub"), "Hello, GitHub!")

if __name__ == "__main__":
    unittest.main()
```

### `requirements.txt`
```plaintext
# Python dependencies
unittest
```

### `README.md`
```markdown
# Sample Project with GitHub Actions and GitLab CI

This is a sample project demonstrating the use of GitHub Actions and GitLab CI for CI/CD pipelines.

## Project Structure

- `.github/workflows/`: Contains GitHub Actions workflows.
- `.gitlab-ci.yml`: GitLab CI configuration file.
- `src/`: Source code for the application.
- `tests/`: Unit tests for the application.
- `requirements.txt`: Python dependencies.
- `setup.py`: Package setup file.

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python src/main.py
   ```

3. Run tests:
   ```bash
   python -m unittest discover tests
   ```
```

### `setup.py`
```python
"""
Setup script for the project.
"""

from setuptools import setup, find_packages

setup(
    name="sample_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add dependencies here
    ],
    entry_points={
        "console_scripts": [
            "sample_project=src.main:main",
        ],
    },
)
```
