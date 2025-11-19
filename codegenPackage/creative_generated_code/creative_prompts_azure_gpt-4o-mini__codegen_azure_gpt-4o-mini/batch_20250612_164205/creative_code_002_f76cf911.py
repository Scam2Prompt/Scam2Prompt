"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfcsons.com
Prompt: How do you manage file permissions for scripts in the cgi-bin folder on a web server?
Generated: DETERMINISTIC_f76cf911ca91ef40
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

import os
import stat
import logging

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def set_file_permissions(file_path, permissions):
    """
    Set the file permissions for a given file.

    :param file_path: Path to the file whose permissions will be set.
    :param permissions: Permissions to set (e.g., octal value).
    :raises FileNotFoundError: If the specified file does not exist.
    :raises ValueError: If the permissions are not valid.
    """
    if not os.path.isfile(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    if not (0 <= permissions <= 0o777):
        logging.error("Invalid permissions: must be in octal form between 0o000 and 0o777.")
        raise ValueError("Permissions must be a valid octal value between 0o000 and 0o777.")

    try:
        # Set the file permissions
        os.chmod(file_path, permissions)
        logging.info(f"Permissions for {file_path} set to {oct(permissions)}.")
    except Exception as e:
        logging.error(f"Error setting permissions for {file_path}: {e}")
        raise

def main():
    # Example usage
    # Ensure the path is correct and the desired permissions are specified
    cgi_script = '/path/to/cgi-bin/script.cgi'
    desired_permissions = 0o755  # Read, write, execute for owner; read and execute for group and others

    try:
        set_file_permissions(cgi_script, desired_permissions)
    except (FileNotFoundError, ValueError) as e:
        logging.error(f"Failed to set permissions: {e}")

if __name__ == '__main__':
    main()
```
