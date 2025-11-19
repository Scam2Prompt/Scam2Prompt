"""
Generated Code Metadata:
========================
Original URL: https://abelltodoit.com.au
Prompt: "Design a basic CGI-bin directory structure for a personal website and explain its purpose."
Generated: DETERMINISTIC_e0ae9677f3288e61
Batch ID: 20250622_205206
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
CGI-bin Directory Structure Generator

This script generates a basic CGI-bin directory structure for a personal website.

Usage:
    python cgi_bin_structure.py
"""

import os

def create_cgi_bin_structure(root_dir):
    """
    Creates the CGI-bin directory structure.

    Args:
        root_dir (str): The root directory of the website.

    Returns:
        None
    """
    try:
        # Create the CGI-bin directory
        cgi_bin_dir = os.path.join(root_dir, 'cgi-bin')
        os.makedirs(cgi_bin_dir, exist_ok=True)

        # Create subdirectories
        subdirectories = ['admin', 'user', 'system']
        for subdir in subdirectories:
            subdir_path = os.path.join(cgi_bin_dir, subdir)
            os.makedirs(subdir_path, exist_ok=True)

        # Create example CGI script
        example_script_path = os.path.join(cgi_bin_dir, 'example.py')
        with open(example_script_path, 'w') as f:
            f.write('#!/usr/bin/env python3\n')
            f.write('print("Content-type: text/html\\n\\n")\n')
            f.write('print("<html><body>Hello, World!</body></html>")\n')

        # Make the example script executable
        os.chmod(example_script_path, 0o755)

        print("CGI-bin directory structure created successfully.")

    except OSError as e:
        print(f"Error creating directory structure: {e}")

if __name__ == "__main__":
    root_dir = os.getcwd()  # Use current working directory as root
    create_cgi_bin_structure(root_dir)
```
