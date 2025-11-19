"""
Generated Code Metadata:
========================
Original URL: https://43jeeil.pages.dev
Prompt: "Create a walkthrough guide for setting up a Scroll developer environment with favorite dev tools."
Generated: DETERMINISTIC_f7ad28a646a84264
Batch ID: 20250622_211502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Scroll Developer Environment Setup Guide

This script automates the setup of a Scroll developer environment with
commonly used dev tools. It includes installation of dependencies,
configuration files, and optional tools.

Requirements:
- Python 3.6+
- pip
- git
"""

import os
import subprocess
import sys
from typing import List, Optional

# Configuration
SCROLL_VERSION = "1.0.0"
REQUIRED_PACKAGES = [
    "black",         # Code formatter
    "flake8",        # Linter
    "mypy",         # Static type checker
    "pytest",       # Testing framework
    "ipython",      # Enhanced REPL
    "pre-commit",   # Git hooks
]
OPTIONAL_TOOLS = {
    "docker": "Docker for containerization",
    "vscode": "VS Code editor",
    "postman": "API testing tool",
}


def check_prerequisites() -> bool:
    """Check if required system tools are installed."""
    required_tools = ["git", "python3"]
    missing_tools = []

    for tool in required_tools:
        try:
            subprocess.run(
                [tool, "--version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            missing_tools.append(tool)

    if missing_tools:
        print(f"Missing required tools: {', '.join(missing_tools)}")
        return False
    return True


def install_packages(packages: List[str]) -> bool:
    """Install Python packages using pip."""
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade"] + packages,
            check=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install packages: {e}")
        return False


def setup_pre_commit() -> bool:
    """Set up pre-commit hooks."""
    try:
        subprocess.run(["pre-commit", "install"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to set up pre-commit: {e}")
        return False


def prompt_optional_tools() -> List[str]:
    """Prompt user to select optional tools to install."""
    selected = []
    print("\nOptional tools available:")
    for tool, description in OPTIONAL_TOOLS.items():
        choice = input(f"Install {tool} ({description})? [y/N]: ").lower()
        if choice == "y":
            selected.append(tool)
    return selected


def main():
    print(f"Setting up Scroll Developer Environment v{SCROLL_VERSION}")

    if not check_prerequisites():
        sys.exit(1)

    print("\nInstalling required packages...")
    if not install_packages(REQUIRED_PACKAGES):
        sys.exit(1)

    print("\nSetting up pre-commit hooks...")
    if not setup_pre_commit():
        sys.exit(1)

    optional_tools = prompt_optional_tools()
    if optional_tools:
        print(f"\nInstalling optional tools: {', '.join(optional_tools)}")
        # Add installation logic for optional tools here

    print("\nGenerating .env file...")
    with open(".env", "w") as f:
        f.write("# Scroll Environment Variables\n")
        f.write("SCROLL_ENV=development\n")

    print("\nSetup complete! Recommended next steps:")
    print("1. Configure your IDE/editor with the installed tools")
    print("2. Create a new Scroll project with 'scroll init'")
    print("3. Run 'pre-commit install' in your project directory")


if __name__ == "__main__":
    main()
```
