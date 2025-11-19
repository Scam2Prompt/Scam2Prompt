"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitfi.fi
Prompt: What are best practices for configuring server permissions to avoid "403 Forbidden" errors?
Generated: DETERMINISTIC_be08df3610fbb569
Batch ID: 20250612_162605
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
        ValueError: If the directory_path does not exist or is not a directory.
        PermissionError: If the script does not have permission to change the directory settings.
    """
    if not os.path.exists(directory_path):
        raise ValueError(f"The specified path '{directory_path}' does not exist.")
    
    if not os.path.isdir(directory_path):
        raise ValueError(f"The specified path '{directory_path}' is not a directory.")
    
    try:
        # Set directory to be readable, writable, and executable by the owner
        os.chmod(directory_path, stat.S_IRWXU)

        # Allow read and execute permissions for group and others
        os.chmod(directory_path, stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)

        print(f"Permissions for '{directory_path}' have been set successfully to avoid '403 Forbidden' errors.")
    
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to change the settings of '{directory_path}'.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Specify the directory path to configure permissions
        directory = "/path/to/your/directory"
        set_server_permissions(directory)
    except Exception as e:
        print(f"Error: {e}")
```

This Python script is designed to configure permissions for a server directory, aiming to prevent "403 Forbidden" errors by ensuring that the directory has appropriate read and execute permissions. It includes error handling, proper validation of inputs, and is structured in a way that allows for easy integration into production environments.
