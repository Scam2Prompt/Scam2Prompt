"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rudekidz.top
Prompt: What are best practices for configuring server permissions to avoid "403 Forbidden" errors?
Generated: DETERMINISTIC_be08df3610fbb569
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import stat

def set_server_permissions(directory_path):
    """
    Configures server permissions for a given directory to avoid '403 Forbidden' errors.

    Args:
        directory_path (str): The path to the directory for which to set permissions.

    Raises:
        ValueError: If the directory does not exist or is not a directory.
    """
    # Check if the directory exists
    if not os.path.exists(directory_path):
        raise ValueError(f"The specified path does not exist: {directory_path}")

    # Check if the path is indeed a directory
    if not os.path.isdir(directory_path):
        raise ValueError(f"The specified path is not a directory: {directory_path}")

    try:
        # Set directory permissions to 755 (rwxr-xr-x)
        # Owner can read, write, and execute; group and others can read and execute
        os.chmod(directory_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | 
                         stat.S_IRGRP | stat.S_IXGRP | 
                         stat.S_IROTH | stat.S_IXOTH)

        # Set permissions for all files within the directory to 644 (rw-r--r--)
        for dirpath, dirnames, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR | 
                                   stat.S_IRGRP | 
                                   stat.S_IROTH)

    except Exception as e:
        # Log the error and raise it for further handling
        print(f"Error occurred while setting permissions: {e}")
        raise

# Example usage:
# set_server_permissions('/path/to/your/directory')
```
