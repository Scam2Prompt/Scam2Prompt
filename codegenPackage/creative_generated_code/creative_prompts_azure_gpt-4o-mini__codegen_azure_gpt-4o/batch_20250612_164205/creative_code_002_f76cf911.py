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

Here is a Python script that manages file permissions for scripts in the cgi-bin folder on a web server. The script identifies `.cgi` files in the folder, ensures proper permissions, and provides error handling.

```python
import os
import stat

def manage_cgi_permissions(cgi_bin_path):
    """
    Manage file permissions for scripts in the cgi-bin folder.
    
    Args:
        cgi_bin_path (str): Path to the cgi-bin directory.
    
    Raises:
        FileNotFoundError: If the cgi-bin directory does not exist.
        PermissionError: If permissions cannot be updated for a file.
    """
    # Check if the cgi-bin folder exists
    if not os.path.exists(cgi_bin_path):
        raise FileNotFoundError(f"cgi-bin directory not found: {cgi_bin_path}")
    
    # Iterate over files in the cgi-bin folder
    for file_name in os.listdir(cgi_bin_path):
        file_path = os.path.join(cgi_bin_path, file_name)
        
        # Ensure it's a regular file and ends with ".cgi"
        if os.path.isfile(file_path) and file_name.endswith(".cgi"):
            try:
                # Get the current permissions
                current_permissions = os.stat(file_path).st_mode
                
                # Set permissions to 755 (-rwxr-xr-x)
                new_permissions = stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH
                os.chmod(file_path, new_permissions)
                print(f"Updated permissions for: {file_path}")
            
            except PermissionError as e:
                print(f"Error setting permissions for {file_path}: {e}")
            except Exception as e:
                print(f"Unexpected error for {file_path}: {e}")
        else:
            print(f"Skipping non-CGI file: {file_path}")

if __name__ == "__main__":
    # Example cgi-bin folder path
    cgi_bin_folder = "/path/to/cgi-bin"
    
    try:
        manage_cgi_permissions(cgi_bin_folder)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

Make sure to replace `"/path/to/cgi-bin"` with the actual path to your `cgi-bin` directory. To execute the script, ensure Python has proper permissions to modify files in the specified directory.
