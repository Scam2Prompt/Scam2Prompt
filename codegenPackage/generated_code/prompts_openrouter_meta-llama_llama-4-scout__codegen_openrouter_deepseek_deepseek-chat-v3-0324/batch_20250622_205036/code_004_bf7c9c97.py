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
CGI Troubleshooting Utility

This script helps diagnose common CGI execution issues by checking:
- File permissions
- Directory structure
- Script syntax
- Server configuration

Usage: ./cgi_troubleshooter.py <path_to_cgi_script>
"""

import os
import sys
import stat
import subprocess
import re

def check_file_exists(path):
    """Verify the CGI script exists"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"CGI script not found at {path}")

def check_file_permissions(path):
    """Check if the file has proper execute permissions"""
    mode = os.stat(path).st_mode
    if not (mode & stat.S_IXUSR):
        raise PermissionError(f"Execute permission missing for user on {path}")
    if not (mode & stat.S_IXGRP):
        print(f"Warning: Execute permission missing for group on {path}")
    if not (mode & stat.S_IXOTH):
        print(f"Warning: Execute permission missing for others on {path}")

def check_directory_permissions(path):
    """Check parent directory permissions"""
    dir_path = os.path.dirname(path)
    mode = os.stat(dir_path).st_mode
    if not (mode & stat.S_IXUSR):
        raise PermissionError(f"Execute permission missing for user on directory {dir_path}")
    if not (mode & stat.S_IXGRP):
        print(f"Warning: Execute permission missing for group on directory {dir_path}")
    if not (mode & stat.S_IXOTH):
        print(f"Warning: Execute permission missing for others on directory {dir_path}")

def check_shebang(path):
    """Verify the script has a valid shebang line"""
    with open(path, 'r') as f:
        first_line = f.readline().strip()
    if not first_line.startswith('#!'):
        print(f"Warning: Missing shebang line in {path}")
    else:
        interpreter = first_line[2:].strip()
        if not os.path.exists(interpreter.split()[0]):
            print(f"Warning: Interpreter not found: {interpreter}")

def check_script_syntax(path):
    """Attempt to validate script syntax"""
    try:
        with open(path, 'r') as f:
            first_line = f.readline().strip()
            if first_line.startswith('#!') and 'python' in first_line:
                result = subprocess.run(['python3', '-m', 'py_compile', path],
                                      stderr=subprocess.PIPE)
                if result.returncode != 0:
                    print(f"Syntax error in Python script: {result.stderr.decode().strip()}")
            elif first_line.startswith('#!') and 'perl' in first_line:
                result = subprocess.run(['perl', '-c', path],
                                      stderr=subprocess.PIPE)
                if result.returncode != 0:
                    print(f"Syntax error in Perl script: {result.stderr.decode().strip()}")
    except Exception as e:
        print(f"Could not check script syntax: {str(e)}")

def check_cgi_output(path):
    """Test run the CGI script and check output"""
    try:
        env = os.environ.copy()
        env['REQUEST_METHOD'] = 'GET'
        env['QUERY_STRING'] = ''
        result = subprocess.run([path], env=env,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        
        if result.returncode != 0:
            print(f"Script execution failed with error: {result.stderr.decode().strip()}")
        
        output = result.stdout.decode()
        if not output.startswith('Content-type:'):
            print("Warning: Missing 'Content-type' header in output")
    except Exception as e:
        print(f"Failed to execute CGI script: {str(e)}")

def main():
    if len(sys.argv) != 2:
        print("Usage: ./cgi_troubleshooter.py <path_to_cgi_script>")
        sys.exit(1)
    
    script_path = sys.argv[1]
    
    try:
        print(f"\nChecking CGI script at: {script_path}")
        check_file_exists(script_path)
        check_file_permissions(script_path)
        check_directory_permissions(script_path)
        check_shebang(script_path)
        check_script_syntax(script_path)
        check_cgi_output(script_path)
        print("\nAll basic checks completed. Review any warnings above.")
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
