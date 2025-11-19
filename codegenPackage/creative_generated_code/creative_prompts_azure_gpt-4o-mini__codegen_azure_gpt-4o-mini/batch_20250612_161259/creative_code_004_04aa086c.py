"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drop3.art
Prompt: What are the best practices for configuring server permissions to avoid 403 Forbidden errors?
Generated: DETERMINISTIC_04aa086cdf78c8d5
Batch ID: 20250612_161259
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
    Set appropriate permissions for a server directory to avoid 403 Forbidden errors.
    
    Args:
        directory_path (str): The path to the directory for which to set permissions.

    Raises:
        ValueError: If the directory path is invalid or not a directory.
        OSError: If there is an error while setting permissions.
    """
    # Validate the input directory path
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path is not a directory: {directory_path}")

    try:
        # Set the directory to have read, write, and execute permissions for the owner
        # and read and execute permissions for the group and others
        os.chmod(directory_path, stat.SRUSR | stat.SWUSR | stat.SRGRP | stat.SXGRP | stat.SROTH | stat.SXOTH)

        # Log the change (optional - could use a logging library instead)
        print(f"Permissions for '{directory_path}' set to 755 (rwxr-xr-x).")
        
    except OSError as e:
        raise OSError(f"Failed to set permissions for {directory_path}: {str(e)}")

def main():
    # Example usage
    path = "/path/to/your/server/directory"
    
    try:
        set_server_permissions(path)
    except (ValueError, OSError) as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
```
