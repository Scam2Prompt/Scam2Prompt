"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: How can you set up permissions for the "cgi-bin/" directory to allow execution of scripts while preventing unauthorized access?
Generated: DETERMINISTIC_fe77eebbc9a71efa
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import stat
from pathlib import Path

def setup_permissions(directory):
    """
    Set up permissions for the given directory to allow execution of scripts
    while preventing unauthorized access.

    Args:
        directory (str): The path to the directory.

    Raises:
        FileNotFoundError: If the directory does not exist.
        PermissionError: If the permissions cannot be set.
    """

    # Check if the directory exists
    dir_path = Path(directory)
    if not dir_path.exists():
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    # Check if the directory is a directory
    if not dir_path.is_dir():
        raise ValueError(f"'{directory}' is not a directory.")

    try:
        # Set the owner and group to the current user and group
        # This may need to be adjusted based on your specific system configuration
        # For security, do not use 777 or similar open permissions
        permissions = stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH

        # Apply permissions to the directory
        os.chmod(directory, permissions)

        # Recursively apply permissions to all files and subdirectories
        for root, dirs, files in os.walk(directory):
            for d in dirs:
                os.chmod(os.path.join(root, d), permissions)
            for f in files:
                # Make files readable and executable by owner, and readable by others
                file_permissions = stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IROTH
                os.chmod(os.path.join(root, f), file_permissions)

    except PermissionError as e:
        raise PermissionError(f"Failed to set permissions: {e}")

if __name__ == "__main__":
    directory = "cgi-bin/"
    try:
        setup_permissions(directory)
        print(f"Permissions set for '{directory}'")
    except Exception as e:
        print(f"An error occurred: {e}")
```
