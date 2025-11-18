"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idsmac-apple.com
Prompt: Write a Python script to deploy a CGI script in the "cgi-bin/" directory of a server, ensuring proper permissions and execution.
Generated: DETERMINISTIC_beac4b8de65e8fe7
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import stat
import sys

def deploy_cgi_script(script_content, script_name="script.cgi", cgi_bin_path="cgi-bin"):
    """
    Deploy a CGI script to the specified CGI-bin directory.

    Args:
        script_content (str): The content of the CGI script to deploy.
        script_name (str): The name of the CGI script file. Default is "script.cgi".
        cgi_bin_path (str): The path to the cgi-bin directory. Default is "cgi-bin".

    Raises:
        OSError: If there are issues creating the directory or writing the file.
        ValueError: If invalid parameters are provided.
    """
    # Validate input parameters
    if not script_content or not script_name.strip():
        raise ValueError("Script content and script name must not be empty.")
    if not cgi_bin_path.strip():
        raise ValueError("CGI-bin path must not be empty.")

    # Ensure the cgi-bin directory exists
    try:
        os.makedirs(cgi_bin_path, exist_ok=True)
        print(f"Directory '{cgi_bin_path}' is ready.")
    except OSError as e:
        print(f"Error creating directory '{cgi_bin_path}': {e}")
        raise

    # Define the full path to the CGI script
    script_path = os.path.join(cgi_bin_path, script_name)

    # Write the CGI script to the file
    try:
        with open(script_path, 'w') as script_file:
            script_file.write(script_content)
            print(f"Script written to '{script_path}'.")
    except OSError as e:
        print(f"Error writing to file '{script_path}': {e}")
        raise

    # Set correct permissions for the CGI script
    try:
        # Set file to be executable by its owner, group, and others
        os.chmod(script_path, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
        print(f"Permissions set for '{script_path}' to be executable.")
    except OSError as e:
        print(f"Error setting permissions for '{script_path}': {e}")
        raise

    print(f"CGI script '{script_name}' successfully deployed to '{cgi_bin_path}'.")

if __name__ == "__main__":
    # Example CGI script content
    example_script = """#!/usr/bin/env python3
print("Content-Type: text/html")
print()
print("<html><body><h1>Hello, World from CGI!</h1></body></html>")
"""

    try:
        # Deploy the example script to the "cgi-bin" directory
        deploy_cgi_script(script_content=example_script, script_name="hello.cgi", cgi_bin_path="cgi-bin")
    except Exception as e:
        print(f"An error occurred during deployment: {e}")
        sys.exit(1)
```
