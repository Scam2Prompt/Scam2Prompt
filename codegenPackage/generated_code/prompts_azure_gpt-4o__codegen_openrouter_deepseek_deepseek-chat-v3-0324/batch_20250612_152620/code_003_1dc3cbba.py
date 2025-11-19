"""
Generated Code Metadata:
========================
Original URL: https://segrepin.com
Prompt: Create a Python script to automate the verification of necessary project requirements, inspired by SEGREPIN's "Vérifications nécessaires" service.
Generated: DETERMINISTIC_1dc3cbbad809e948
Batch ID: 20250612_152620
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
Project Requirements Verification Script

This script automates the verification of necessary project requirements.
It checks for required tools, dependencies, configurations, and permissions.
"""

import os
import sys
import subprocess
import platform
import shutil
from typing import List, Dict, Tuple, Optional

# Constants
REQUIRED_TOOLS = ['git', 'python3', 'pip']
MIN_PYTHON_VERSION = (3, 7)
REQUIRED_PYTHON_PACKAGES = {
    'requests': '2.25.1',
    'pyyaml': '5.4.1'
}
REQUIRED_DIRS = ['src', 'tests', 'docs']
REQUIRED_FILES = ['README.md', 'requirements.txt']
CONFIG_FILES = ['.gitignore', 'setup.cfg']
PERMISSION_FILES = []

class VerificationError(Exception):
    """Custom exception for verification failures."""
    pass

def check_python_version() -> None:
    """Verify the Python version meets minimum requirements."""
    if sys.version_info < MIN_PYTHON_VERSION:
        raise VerificationError(
            f"Python version {MIN_PYTHON_VERSION[0]}.{MIN_PYTHON_VERSION[1]} or higher required. "
            f"Current version: {platform.python_version()}"
        )

def check_system_tools() -> None:
    """Check if required system tools are installed and available in PATH."""
    missing_tools = []
    for tool in REQUIRED_TOOLS:
        if not shutil.which(tool):
            missing_tools.append(tool)
    
    if missing_tools:
        raise VerificationError(
            f"Missing required system tools: {', '.join(missing_tools)}"
        )

def check_python_packages() -> None:
    """Verify required Python packages are installed with correct versions."""
    missing_packages = []
    wrong_version_packages = []
    
    for package, required_version in REQUIRED_PYTHON_PACKAGES.items():
        try:
            import importlib.metadata
            installed_version = importlib.metadata.version(package)
        except ImportError:
            # Fallback for Python < 3.8
            import pkg_resources
            try:
                installed_version = pkg_resources.get_distribution(package).version
            except pkg_resources.DistributionNotFound:
                missing_packages.append(package)
                continue
        
        if installed_version != required_version:
            wrong_version_packages.append(
                f"{package} (required: {required_version}, installed: {installed_version})"
            )
    
    errors = []
    if missing_packages:
        errors.append(f"Missing packages: {', '.join(missing_packages)}")
    if wrong_version_packages:
        errors.append(f"Wrong version packages: {', '.join(wrong_version_packages)}")
    
    if errors:
        raise VerificationError("\n".join(errors))

def check_project_structure() -> None:
    """Verify the project directory structure."""
    missing_dirs = []
    for directory in REQUIRED_DIRS:
        if not os.path.isdir(directory):
            missing_dirs.append(directory)
    
    missing_files = []
    for file in REQUIRED_FILES:
        if not os.path.isfile(file):
            missing_files.append(file)
    
    errors = []
    if missing_dirs:
        errors.append(f"Missing directories: {', '.join(missing_dirs)}")
    if missing_files:
        errors.append(f"Missing files: {', '.join(missing_files)}")
    
    if errors:
        raise VerificationError("\n".join(errors))

def check_config_files() -> None:
    """Verify presence of important configuration files."""
    missing_configs = []
    for config_file in CONFIG_FILES:
        if not os.path.isfile(config_file):
            missing_configs.append(config_file)
    
    if missing_configs:
        raise VerificationError(
            f"Missing configuration files: {', '.join(missing_configs)}"
        )

def check_file_permissions() -> None:
    """Verify file permissions for sensitive files."""
    permission_issues = []
    for file in PERMISSION_FILES:
        if os.path.exists(file):
            if os.stat(file).st_mode & 0o777 > 0o600:
                permission_issues.append(
                    f"File {file} has overly permissive permissions"
                )
    
    if permission_issues:
        raise VerificationError("\n".join(permission_issues))

def run_git_checks() -> None:
    """Run git-related checks."""
    try:
        # Check if current directory is a git repository
        subprocess.run(
            ['git', 'rev-parse', '--is-inside-work-tree'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Check for uncommitted changes
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.stdout.strip():
            raise VerificationError("There are uncommitted changes in the repository")
            
    except subprocess.CalledProcessError:
        raise VerificationError("Current directory is not a git repository")

def perform_all_checks() -> Dict[str, Tuple[bool, Optional[str]]]:
    """Perform all verification checks and return results."""
    checks = {
        'Python Version': check_python_version,
        'System Tools': check_system_tools,
        'Python Packages': check_python_packages,
        'Project Structure': check_project_structure,
        'Config Files': check_config_files,
        'File Permissions': check_file_permissions,
        'Git Checks': run_git_checks
    }
    
    results = {}
    for name, check_func in checks.items():
        try:
            check_func()
            results[name] = (True, None)
        except VerificationError as e:
            results[name] = (False, str(e))
        except Exception as e:
            results[name] = (False, f"Unexpected error: {str(e)}")
    
    return results

def print_results(results: Dict[str, Tuple[bool, Optional[str]]]) -> None:
    """Print verification results in a readable format."""
    print("\nProject Requirements Verification Results:")
    print("=" * 50)
    
    max_name_length = max(len(name) for name in results.keys())
    
    for name, (success, message) in results.items():
        status = "PASS" if success else "FAIL"
        color_code = "\033[92m" if success else "\033[91m"
        reset_code = "\033[0m"
        
        print(f"{name.ljust(max_name_length)}: {color_code}{status}{reset_code}")
        if not success and message:
            print(f"  {message}")
    
    print("=" * 50)
    
    total_checks = len(results)
    passed_checks = sum(1 for result in results.values() if result[0])
    
    print(f"\nSummary: {passed_checks}/{total_checks} checks passed")
    if passed_checks < total_checks:
        print("\033[91mSome requirements are not met. Please address the issues above.\033[0m")
        sys.exit(1)
    else:
        print("\033[92mAll requirements are met. Project is ready!\033[0m")
        sys.exit(0)

def main() -> None:
    """Main function to run all verifications."""
    try:
        results = perform_all_checks()
        print_results(results)
    except KeyboardInterrupt:
        print("\nVerification interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
