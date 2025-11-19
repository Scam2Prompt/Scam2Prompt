"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfcsons.com
Prompt: Explain how to troubleshoot issues related to scripts not executing in the cgi-bin directory.
Generated: DETERMINISTIC_4af07bf49e962dae
Batch ID: 20250612_164205
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
Script Title: CGI Script Troubleshooter
Description: A Python script to troubleshoot common issues related to scripts failing to execute in the cgi-bin directory.
Author: [Your Name]
Date: [Date]
"""

import os
import sys
import stat
import subprocess

def check_permissions(script_path):
    """
    Check if the script has the correct permissions (must be executable).
    """
    try:
        # Get file permissions
        file_stat = os.stat(script_path)
        is_executable = file_stat.st_mode & stat.S_IXUSR

        if not is_executable:
            print(f"ERROR: {script_path} is not executable. Use 'chmod +x {script_path}' to fix this.")
            return False
        print(f"SUCCESS: {script_path} has executable permissions.")
        return True
    except FileNotFoundError:
        print(f"ERROR: File {script_path} not found.")
        return False
    except Exception as e:
        print(f"ERROR: Unable to check permissions of {script_path}. Details: {str(e)}")
        return False

def check_shebang(script_path):
    """
    Verify the script's shebang line is correct.
    """
    try:
        with open(script_path, 'r') as file:
            first_line = file.readline().strip()

            if not first_line.startswith("#!"):
                print(f"ERROR: No shebang line found in {script_path}. Add '#!/usr/bin/env python3' or similar to the first line.")
                return False

            if not os.path.exists(first_line[2:]):
                print(f"ERROR: Interpreter specified in shebang ({first_line}) doesn't exist.")
                return False

            print(f"SUCCESS: Shebang line in {script_path} is valid ({first_line}).")
            return True
    except Exception as e:
        print(f"ERROR: Unable to check shebang line for {script_path}. Details: {str(e)}")
        return False

def check_execution(script_path):
    """
    Attempt to execute the script and capture any errors.
    """
    try:
        result = subprocess.run(["python3", script_path], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"ERROR: Script execution failed for {script_path}. Output:\n{result.stderr}")
            return False

        print(f"SUCCESS: Script executed successfully. Output:\n{result.stdout}")
        return True
    except FileNotFoundError:
        print(f"ERROR: Python interpreter not found.")
        return False
    except Exception as e:
        print(f"ERROR: Unable to execute {script_path}. Details: {str(e)}")
        return False

def troubleshoot_cgi_script(script_path):
    """
    Run all troubleshooting checks on the CGI script.
    """
    print(f"Starting troubleshooting for {script_path}...\n")

    if not check_permissions(script_path):
        return

    if not check_shebang(script_path):
        return

    if not check_execution(script_path):
        return

    print(f"\nAll checks passed for {script_path}. Ensure that your server is properly configured to execute CGI scripts.")

if __name__ == "__main__":
    # Check if script path is provided
    if len(sys.argv) != 2:
        print("Usage: python3 troubleshoot_cgi.py <script_path>")
        sys.exit(1)

    script_path = sys.argv[1]
    troubleshoot_cgi_script(script_path)
```
