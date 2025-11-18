"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syr-whistler.com
Prompt: Recommend libraries or tools for debugging CGI scripts in the "cgi-bin" directory on a Linux server.
Generated: DETERMINISTIC_bb9fcef97529c78a
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# debug_cgi.py
"""
This script provides tools and recommendations for debugging CGI scripts
located in the "cgi-bin" directory on a Linux server. It performs checks 
on CGI scripts and offers debugging helpers.
"""

import os
import subprocess

def list_cgi_scripts(cgi_bin_path):
    """
    List all CGI scripts in the 'cgi-bin' directory.

    Args:
        cgi_bin_path (str): Path to the cgi-bin directory.

    Returns:
        list: A list of CGI scripts with full paths.
    """
    try:
        # Validate the cgi-bin path
        if not os.path.isdir(cgi_bin_path):
            raise FileNotFoundError(f"Directory not found: {cgi_bin_path}")
        
        # List CGI scripts (typically ending with '.cgi' or '.pl')
        cgi_scripts = [os.path.join(cgi_bin_path, f) for f in os.listdir(cgi_bin_path)
                       if f.endswith(('.cgi', '.pl'))]
        return cgi_scripts
    except Exception as e:
        print(f"Error listing CGI scripts: {e}")
        return []

def check_permissions(script_path):
    """
    Check if a CGI script has correct permissions (readable and executable).

    Args:
        script_path (str): Path to the CGI script.

    Returns:
        bool: True if permissions are correct, False otherwise.
    """
    try:
        # Check if the script is readable and executable
        is_readable = os.access(script_path, os.R_OK)
        is_executable = os.access(script_path, os.X_OK)
        return is_readable and is_executable
    except Exception as e:
        print(f"Error checking permissions for {script_path}: {e}")
        return False

def run_cgi_script(script_path, env_variables=None):
    """
    Run a CGI script with optional environment variables for debugging purposes.

    Args:
        script_path (str): Path to the CGI script.
        env_variables (dict): Optional dictionary of environment variables.

    Returns:
        tuple: (stdout, stderr) output from the script.
    """
    try:
        # Validate the script path
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Script not found: {script_path}")

        # Prepare environment variables
        env = os.environ.copy()
        if env_variables:
            env.update(env_variables)

        # Run the CGI script using subprocess
        result = subprocess.run(
            [script_path],
            env=env,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print(f"Error running script {script_path}: {e}")
        return e.stdout, e.stderr
    except Exception as e:
        print(f"Unexpected error running script {script_path}: {e}")
        return "", str(e)

if __name__ == "__main__":
    # Example usage of the debugging tools
    CGI_BIN_PATH = "/var/www/cgi-bin"

    print("Listing CGI scripts...")
    scripts = list_cgi_scripts(CGI_BIN_PATH)
    for script in scripts:
        print(f"Found script: {script}")
        if check_permissions(script):
            print(f"Permissions OK for: {script}")
            print(f"Running {script} for debugging...")
            stdout, stderr = run_cgi_script(script, env_variables={"DEBUG": "1"})
            print("Script output:")
            print(stdout)
            if stderr:
                print("Script errors:")
                print(stderr)
        else:
            print(f"Permissions NOT OK for: {script}")
```
