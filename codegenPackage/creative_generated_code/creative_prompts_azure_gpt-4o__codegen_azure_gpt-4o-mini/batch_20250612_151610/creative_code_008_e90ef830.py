"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Develop a script to scan and list all screen savers installed on a Windows system, ensuring compatibility with the formats provided on Dick Lee's Screen Saver Page.
Generated: DETERMINISTIC_e90ef8305fda2fb2
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import winreg

def get_screensaver_extensions():
    """Returns a list of valid screen saver file extensions."""
    return ['.scr', '.exe']

def list_installed_screensavers():
    """Scans and lists all installed screen savers on the Windows system."""
    # Define the paths we will check for screen savers
    paths_to_check = [
        r'C:\Windows\System32',  # Default location for screen savers
        r'C:\Windows\SysWOW64'   # For 64-bit systems
    ]

    # Initialize a list to hold found screen savers
    screensavers = []

    # Loop through each path and search for screen saver files
    for path in paths_to_check:
        try:
            # List all files in the directory
            for file_name in os.listdir(path):
                # Check for valid screen saver extensions
                if any(file_name.endswith(ext) for ext in get_screensaver_extensions()):
                    screensavers.append(file_name)
        except FileNotFoundError:
            print(f"Warning: The path {path} does not exist.")
        except PermissionError:
            print(f"Warning: Permission denied to access {path}.")
        except Exception as e:
            print(f"An unexpected error occurred while accessing {path}: {e}")

    return screensavers

def main():
    """Main function to run the screen saver listing."""
    print("Scanning for installed screen savers...\n")
    installed_screensavers = list_installed_screensavers()
    
    if installed_screensavers:
        print("Installed Screen Savers:")
        for ss in installed_screensavers:
            print(f"- {ss}")
    else:
        print("No screen savers found.")

if __name__ == "__main__":
    main()
```
