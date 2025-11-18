"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumpromo.epizy.com
Prompt: Provide Python code to test the compatibility of a web application with multiple PHP versions and Node.js support on a hosting platform like iFastNet.
Generated: DETERMINISTIC_de22ffe405617095
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys


def check_php_version(version):
    """
    Check if a specific PHP version is supported on the hosting platform.

    :param version: PHP version to check (e.g., "7.4", "8.1").
    :return: Boolean indicating whether the PHP version is supported.
    """
    try:
        result = subprocess.run(
            ["php", f"-v{version}"],  # Command to check PHP version
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0 and version in result.stdout:
            return True
        return False
    except FileNotFoundError:
        print(f"PHP version {version} is not installed or unavailable.")
        return False
    except Exception as e:
        print(f"An error occurred while checking PHP version {version}: {e}")
        return False


def check_node_js_support():
    """
    Check if Node.js is installed and supported on the hosting platform.

    :return: Boolean indicating whether Node.js is supported.
    """
    try:
        result = subprocess.run(
            ["node", "--version"],  # Command to check Node.js version
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            return True
        return False
    except FileNotFoundError:
        print("Node.js is not installed or unavailable.")
        return False
    except Exception as e:
        print(f"An error occurred while checking Node.js support: {e}")
        return False


def main():
    """
    Main function to test compatibility of the hosting platform with multiple PHP versions
    and Node.js support.
    """
    # List of PHP versions to check
    php_versions = ["7.4", "8.0", "8.1"]

    print("\nChecking PHP version compatibility:")
    for version in php_versions:
        if check_php_version(version):
            print(f"PHP {version}: Supported")
        else:
            print(f"PHP {version}: Not Supported")

    print("\nChecking Node.js compatibility:")
    if check_node_js_support():
        print("Node.js: Supported")
    else:
        print("Node.js: Not Supported")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
