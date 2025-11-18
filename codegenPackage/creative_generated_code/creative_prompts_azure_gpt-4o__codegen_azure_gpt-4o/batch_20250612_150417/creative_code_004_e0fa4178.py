"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myantispyware.com
Prompt: Create a Python script to detect and remove malicious browser extensions like "HyperPlasmel" and "Bull Checker," following the removal guide on MyAntiSpyware.com.
Generated: DETERMINISTIC_e0fa417857801261
Batch ID: 20250612_150417
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
import platform
import sys

def is_windows():
    """Check if the operating system is Windows."""
    return platform.system() == 'Windows'

def is_mac():
    """Check if the operating system is macOS."""
    return platform.system() == 'Darwin'

def remove_extension(extension_name, browser_name, extension_paths):
    """
    Attempt to remove a browser extension by name.
    
    Args:
        extension_name (str): Name of the extension to remove.
        browser_name (str): Name of the browser (e.g., 'Chrome', 'Firefox').
        extension_paths (list): List of directories to search for the extension.

    Returns:
        bool: True if the extension was successfully removed, False otherwise.
    """
    success = False
    for path in extension_paths:
        try:
            full_path = os.path.join(path, extension_name)
            if os.path.exists(full_path):
                shutil.rmtree(full_path)  # Remove entire extension directory
                print(f"{extension_name} removed successfully from {browser_name}.")
                success = True
            else:
                print(f"{extension_name} not found in {path}.")
        except Exception as e:
            print(f"Error removing {extension_name} from {path}: {e}")
    return success

def detect_and_remove_malicious_extensions():
    """
    Detect and remove known malicious browser extensions.
    This function targets "HyperPlasmel" and "Bull Checker" based on given paths.
    """
    malicious_extensions = ["HyperPlasmel", "Bull Checker"]
    # Predefined paths for common browsers (can be expanded based on actual configurations)
    browser_paths = {
        "Chrome": {
            "Windows": [
                os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\Extensions')
            ],
            "macOS": [
                os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Extensions')
            ]
        },
        "Firefox": {
            "Windows": [
                os.path.expandvars(r'%APPDATA%\Mozilla\Firefox\Profiles'),
            ],
            "macOS": [
                os.path.expanduser('~/Library/Application Support/Firefox/Profiles')
            ]
        }
    }
    
    # Detect operating system
    os_type = "Windows" if is_windows() else "macOS" if is_mac() else "Unsupported"
    if os_type == "Unsupported":
        print("Unsupported operating system. This script works on Windows and macOS only.")
        sys.exit(1)  # Exit with error code

    # Process each browser
    for browser, paths in browser_paths.items():
        if os_type in paths:
            for extension in malicious_extensions:
                # Attempt to remove the malicious extension
                remove_extension(extension, browser, paths[os_type])

if __name__ == "__main__":
    try:
        print("Starting malicious browser extension removal process...")
        detect_and_remove_malicious_extensions()
        print("Process completed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
