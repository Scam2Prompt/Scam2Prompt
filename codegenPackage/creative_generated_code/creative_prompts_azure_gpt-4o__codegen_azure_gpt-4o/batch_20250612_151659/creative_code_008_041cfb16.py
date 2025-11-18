"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defluo.hr
Prompt: Write a guide for debugging CGI scripts located in the "cgi-bin/" directory of a web server.
Generated: DETERMINISTIC_041cfb162a299639
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3

"""
Debugging CGI Scripts Guide

This script helps debug CGI scripts located in the 'cgi-bin/' directory on a web server.
It includes methods for testing CGI script output, checking server configurations, and logging errors.

Usage:
Run this script manually to test the CGI environment and diagnose issues with scripts.
"""

import os
import sys
import subprocess
import traceback

def check_environment_variables():
    """
    Checks the environment variables required by CGI scripts.
    """
    print("\n=== CGI Environment Variables ===")
    for key, value in os.environ.items():
        print(f"{key}: {value}")

def execute_cgi_script(script_path):
    """
    Executes a CGI script and prints its output for debugging.

    :param script_path: Path to the CGI script located in the 'cgi-bin/' directory.
    """
    print("\n=== CGI Script Execution ===")
    try:
        # Check if the script exists and is executable
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Script not found: {script_path}")
        if not os.access(script_path, os.X_OK):
            raise PermissionError(f"Script is not executable: {script_path}")

        # Execute the CGI script using subprocess
        result = subprocess.run(
            [script_path],
            text=True,
            capture_output=True,
            env=os.environ  # Pass the current environment variables
        )

        # Output the script's stdout and stderr
        print("=== Script STDOUT ===")
        print(result.stdout)
        print("=== Script STDERR ===")
        print(result.stderr)

        # Check the return code
        if result.returncode != 0:
            print(f"Error: Script exited with code {result.returncode}")
    except Exception as e:
        print(f"Exception while executing script: {e}")
        print(traceback.format_exc())

def verify_web_server_config():
    """
    Verifies common web server configurations for CGI scripts.

    This is a placeholder function that provides suggestions for debugging server issues.
    """
    print("\n=== Web Server Configuration Debugging ===")
    print("1. Ensure the 'cgi-bin/' directory is correctly configured in the server.")
    print("2. Verify the server has permissions to execute scripts in the 'cgi-bin/' directory.")
    print("3. Check the server's error logs for more details.")
    print("4. Confirm the scripts have proper shebang lines (e.g., '#!/usr/bin/env python3').")
    print("5. Ensure correct 'Content-Type' headers are sent in the CGI script output.")

def main():
    """
    Main function to initiate debugging.
    """
    print("\n=== CGI Debugging Tool ===")

    # Get script path from user input
    script_path = input("Enter the path to the CGI script in 'cgi-bin/': ").strip()

    # Debugging steps
    check_environment_variables()
    execute_cgi_script(script_path)
    verify_web_server_config()

    print("\n=== Debugging Complete ===")

if __name__ == "__main__":
    main()
```
