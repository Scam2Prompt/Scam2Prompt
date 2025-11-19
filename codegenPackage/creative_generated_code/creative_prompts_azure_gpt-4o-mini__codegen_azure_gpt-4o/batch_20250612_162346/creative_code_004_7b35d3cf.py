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
sample-project/
├── .github/
│   ├── workflows/
│   │   ├── main.yml
├── .gitlab-ci.yml
├── src/
│   ├── app.py
├── tests/
│   ├── test_app.py
├── requirements.txt
├── README.md
└── LICENSE
```

### `.github/workflows/main.yml`
```yaml
# GitHub Actions workflow
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
      - name: Checkout source code
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
        run: pytest tests --disable-warnings
```

### `.gitlab-ci.yml`
```yaml
# GitLab CI/CD pipeline
stages:
  - build
  - test

variables:
  PYTHON_VERSION: "3.9"

build:
  stage: build
  script:
    - python -m pip install --upgrade pip
    - pip install -r requirements.txt

test:
  stage: test
  script:
    - pytest tests --disable-warnings
```

### `src/app.py`
```python
"""
Sample application code
"""

def main():
    """
    Simple function for demonstration purposes
    """
    print("Hello, GitHub Actions and GitLab CI!")

if __name__ == "__main__":
    main()
```

### `tests/test_app.py`
```python
"""
Unit tests for the sample application
"""

import unittest
from src.app import main

class TestApp(unittest.TestCase):
    def test_main(self):
        """
        Ensure the main function runs without errors
        """
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
```

### `requirements.txt`
```
pytest==7.4.0
```

### `README.md`
```markdown
# Sample Project: GitHub Actions and GitLab CI Integration

This is a sample project demonstrating the use of GitHub Actions alongside GitLab CI for a Python application.

## Structure
- **GitHub Actions**: Configuration located in `.github/workflows/main.yml`
- **GitLab CI**: Configuration located in `.gitlab-ci.yml`

## Requirements
- Python 3.9+
- `pytest` for unit testing

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run tests locally: `pytest tests`.

## License
See [LICENSE](LICENSE).
```

### `LICENSE`
```plaintext
MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
...
```
