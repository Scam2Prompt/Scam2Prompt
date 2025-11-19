"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Develop a script to scan and list all screen savers installed on a Windows system, ensuring compatibility with the formats provided on Dick Lee's Screen Saver Page.
Generated: DETERMINISTIC_e90ef8305fda2fb2
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import ctypes
import winreg

def get_screensaver_directory():
    """
    Retrieves the directory where Windows screen savers are typically stored.
    Returns:
        str: The path to the screen saver directory.
    """
    # Common screen saver directory for Windows
    return os.path.join(os.environ['WINDIR'], 'System32')

def is_valid_screensaver(file_name):
    """
    Checks if the given file name is a valid screen saver format.
    Valid formats are .scr and .exe.
    
    Args:
        file_name (str): The name of the file to check.
    
    Returns:
        bool: True if the file is a valid screen saver, False otherwise.
    """
    valid_extensions = ['.scr', '.exe']
    return any(file_name.lower().endswith(ext) for ext in valid_extensions)

def list_installed_screensavers():
    """
    Scans the screen saver directory and lists all installed screen savers
    that are compatible with Dick Lee's Screen Saver Page formats.
    
    Returns:
        list: A list of valid screen saver file names.
    """
    screensaver_dir = get_screensaver_directory()
    screensavers = []

    try:
        # List all files in the screen saver directory
        for file_name in os.listdir(screensaver_dir):
            file_path = os.path.join(screensaver_dir, file_name)
            if os.path.isfile(file_path) and is_valid_screensaver(file_name):
                screensavers.append(file_name)
    except FileNotFoundError:
        print(f"Error: The directory {screensaver_dir} was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing {screensaver_dir}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return screensavers

def main():
    """
    Main function to execute the screen saver listing.
    """
    print("Scanning for installed screen savers...")
    screensavers = list_installed_screensavers()
    
    if screensavers:
        print("Installed Screen Savers:")
        for screensaver in screensavers:
            print(f"- {screensaver}")
    else:
        print("No valid screen savers found.")

if __name__ == "__main__":
    main()
```
