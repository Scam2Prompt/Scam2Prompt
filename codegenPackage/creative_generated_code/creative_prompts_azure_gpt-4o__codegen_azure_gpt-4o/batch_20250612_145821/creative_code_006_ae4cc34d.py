"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev-metamask.wuaze.com
Prompt: Write a Python script to test compatibility with the multiple PHP versions available on iFastNet hosting.
Generated: DETERMINISTIC_ae4cc34d9458131f
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess

def check_php_version(php_executable):
    """
    Check PHP version using the provided PHP executable path.

    Args:
        php_executable (str): Path to the PHP executable.

    Returns:
        str: PHP version if successful, else an error message.
    """
    try:
        # Run the PHP executable with `--version` to get the version information
        result = subprocess.run(
            [php_executable, '--version'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            # Extract first line of output which contains the version
            return result.stdout.split('\n')[0]
        else:
            return f"Error: Failed to get version from {php_executable}. {result.stderr.strip()}"
    except FileNotFoundError:
        return f"Error: PHP executable not found at path '{php_executable}'"
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"

def main():
    """
    Main function to test compatibility with multiple PHP versions.

    This script assumes that different PHP versions are available as executables
    named 'php', 'php7', 'php8', etc., or with full paths specified.
    """
    # List of PHP executable paths to test
    php_executables = [
        '/usr/bin/php',    # Default PHP executable
        '/usr/bin/php7',   # PHP 7 executable
        '/usr/bin/php8',   # PHP 8 executable
        '/usr/bin/php5.6', # PHP 5.6 executable
        '/usr/bin/php8.1'  # PHP 8.1 executable
    ]

    # Iterate through each PHP executable and check its version
    print("Testing compatibility with available PHP versions...")
    for php_executable in php_executables:
        version_info = check_php_version(php_executable)
        print(f"{php_executable}: {version_info}")

if __name__ == "__main__":
    main()
```
