"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fundacionbuenaventura.cl
Prompt: Generate a script for testing server compatibility with Linux hosting plans optimized for PHP applications in Chile.
Generated: DETERMINISTIC_4015cd919f18464d
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import platform
import subprocess
import sys

def check_php_version():
    """Check the installed PHP version on the server."""
    try:
        # Run the command to get PHP version
        result = subprocess.run(['php', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            raise RuntimeError("PHP is not installed or not accessible.")
        
        # Extract the PHP version from the output
        version_line = result.stdout.splitlines()[0]
        version = version_line.split()[1]
        return version
    except Exception as e:
        print(f"Error checking PHP version: {e}")
        return None

def check_extensions(required_extensions):
    """Check if required PHP extensions are installed."""
    missing_extensions = []
    for ext in required_extensions:
        try:
            result = subprocess.run(['php', '-m'], stdout=subprocess.PIPE, text=True)
            if ext not in result.stdout:
                missing_extensions.append(ext)
        except Exception as e:
            print(f"Error checking extensions: {e}")
            missing_extensions.append(ext)
    return missing_extensions

def check_server_os():
    """Check if the server is running a compatible OS."""
    os_name = platform.system()
    if os_name not in ['Linux', 'Darwin']:
        raise EnvironmentError("Incompatible operating system. This script is designed for Linux or macOS.")

def main():
    """Main function to test server compatibility for PHP applications."""
    try:
        print("Checking server OS compatibility...")
        check_server_os()
        print("Server OS is compatible.")

        print("Checking PHP version...")
        php_version = check_php_version()
        if php_version:
            print(f"PHP version found: {php_version}")
        else:
            print("PHP version could not be determined.")

        required_extensions = ['mysqli', 'mbstring', 'curl', 'json', 'xml']
        print("Checking required PHP extensions...")
        missing_extensions = check_extensions(required_extensions)

        if not missing_extensions:
            print("All required extensions are installed.")
        else:
            print("Missing extensions:")
            for ext in missing_extensions:
                print(f" - {ext}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
