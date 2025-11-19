"""
Generated Code Metadata:
========================
Original URL: https://myantispyware.com
Prompt: Create a removal guide for the Bull Checker malicious extension.
Generated: DETERMINISTIC_606abe73908442d6
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import sys
import platform

def remove_bull_checker_extension():
    """
    Removes the Bull Checker malicious extension from the user's browser.
    This function checks the operating system and attempts to locate and remove
    the extension files from common browser directories.
    """
    try:
        # Determine the operating system
        os_type = platform.system()
        
        if os_type == "Windows":
            # Windows specific paths
            chrome_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Extensions")
            firefox_path = os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles")
        elif os_type == "Darwin":  # macOS
            chrome_path = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/Extensions")
            firefox_path = os.path.expanduser("~/Library/Application Support/Firefox/Profiles")
        elif os_type == "Linux":
            chrome_path = os.path.expanduser("~/.config/google-chrome/Default/Extensions")
            firefox_path = os.path.expanduser("~/.mozilla/firefox")
        else:
            print("Unsupported operating system.")
            return

        # Remove Bull Checker from Chrome
        remove_extension(chrome_path, "bull_checker_extension_id")  # Replace with actual extension ID

        # Remove Bull Checker from Firefox
        for profile in os.listdir(firefox_path):
            profile_path = os.path.join(firefox_path, profile)
            if os.path.isdir(profile_path):
                remove_extension(profile_path, "bull_checker_extension_id")  # Replace with actual extension ID

        print("Bull Checker extension removal process completed.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def remove_extension(base_path, extension_id):
    """
    Removes the specified extension from the given base path.
    
    :param base_path: The path to the browser's extensions directory.
    :param extension_id: The ID of the extension to remove.
    """
    try:
        extension_path = os.path.join(base_path, extension_id)
        if os.path.exists(extension_path):
            shutil.rmtree(extension_path)
            print(f"Removed extension at: {extension_path}")
        else:
            print(f"No extension found at: {extension_path}")
    except Exception as e:
        print(f"Failed to remove extension at {extension_path}: {e}")

if __name__ == "__main__":
    remove_bull_checker_extension()
```
