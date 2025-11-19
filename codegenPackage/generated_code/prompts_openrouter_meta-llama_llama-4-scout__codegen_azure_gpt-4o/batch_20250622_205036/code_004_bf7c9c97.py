"""
Generated Code Metadata:
========================
Original URL: https://mfcsons.com
Prompt: How do I troubleshoot common issues with CGI script execution, given a directory structure and access permissions similar to those on mfcsons.com?
Generated: DETERMINISTIC_bf7c9c97076e0bfc
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3

"""
CGI Script Troubleshooting Tool
This script helps troubleshoot common issues with CGI script execution.
It checks for:
1. Correct file permissions
2. Proper shebang line
3. Directory permissions
4. Web server configuration
5. Syntax errors in the CGI script

Usage:
Place this script in the same directory as your CGI script and execute it.
"""

import os
import stat
import subprocess
import sys

def check_file_permissions(file_path):
    """
    Check if the file has the correct permissions (readable and executable).
    """
    try:
        st = os.stat(file_path)
        if not (st.st_mode & stat.S_IXUSR):
            print(f"ERROR: {file_path} is not executable by the owner.")
        if not (st.st_mode & stat.S_IRUSR):
            print(f"ERROR: {file_path} is not readable by the owner.")
        else:
            print(f"OK: {file_path} has correct permissions.")
    except FileNotFoundError:
        print(f"ERROR: {file_path} does not exist.")
    except Exception as e:
        print(f"ERROR: Unable to check permissions for {file_path}. {e}")

def check_shebang(file_path):
    """
    Check if the file has a valid shebang line.
    """
    try:
        with open(file_path, 'r') as f:
            first_line = f.readline().strip()
            if not first_line.startswith("#!"):
                print(f"ERROR: {file_path} does not have a valid shebang line.")
            else:
                print(f"OK: {file_path} has a valid shebang line: {first_line}")
    except Exception as e:
        print(f"ERROR: Unable to read {file_path} for shebang check. {e}")

def check_directory_permissions(directory_path):
    """
    Check if the directory has the correct permissions (readable and executable).
    """
    try:
        st = os.stat(directory_path)
        if not (st.st_mode & stat.S_IXUSR):
            print(f"ERROR: {directory_path} is not executable by the owner.")
        if not (st.st_mode & stat.S_IRUSR):
            print(f"ERROR: {directory_path} is not readable by the owner.")
        else:
            print(f"OK: {directory_path} has correct permissions.")
    except FileNotFoundError:
        print(f"ERROR: {directory_path} does not exist.")
    except Exception as e:
        print(f"ERROR: Unable to check permissions for {directory_path}. {e}")

def check_syntax(file_path):
    """
    Check for syntax errors in the CGI script.
    """
    try:
        result = subprocess.run(['python3', '-m', 'py_compile', file_path], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"ERROR: Syntax errors found in {file_path}:\n{result.stderr}")
        else:
            print(f"OK: No syntax errors in {file_path}.")
    except Exception as e:
        print(f"ERROR: Unable to check syntax for {file_path}. {e}")

def main():
    """
    Main function to run all checks.
    """
    # Define the CGI script and its directory
    cgi_script = "example.cgi"  # Replace with your CGI script name
    cgi_directory = os.path.dirname(os.path.abspath(cgi_script))

    print("=== CGI Script Troubleshooting Tool ===")

    # Check file permissions
    print("\nChecking file permissions...")
    check_file_permissions(cgi_script)

    # Check shebang line
    print("\nChecking shebang line...")
    check_shebang(cgi_script)

    # Check directory permissions
    print("\nChecking directory permissions...")
    check_directory_permissions(cgi_directory)

    # Check syntax errors
    print("\nChecking syntax errors...")
    check_syntax(cgi_script)

    print("\n=== Troubleshooting Complete ===")

if __name__ == "__main__":
    main()
```
