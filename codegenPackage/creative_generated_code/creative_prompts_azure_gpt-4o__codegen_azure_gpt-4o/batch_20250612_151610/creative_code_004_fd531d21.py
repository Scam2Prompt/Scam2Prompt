"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Recommend libraries or APIs for handling password protection for screen savers compatible with Microsoft Windows, as described on Dick Lee's Screen Saver Page.
Generated: DETERMINISTIC_fd531d21e4c9c5b6
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Password Protection for Screen Savers on Windows

This script provides a utility function to handle password protection for a screen saver.
It uses the Windows API via the `ctypes` library for compatibility with Microsoft Windows.

Dependencies:
    - Python 3.x
    - `ctypes` (standard library)

Note:
    This example assumes the screen saver password protection feature is managed via 
    system registry keys or Windows API calls, as commonly described.
"""

import ctypes
import ctypes.wintypes
import winreg


def set_screen_saver_password(password: str) -> bool:
    """
    Sets the password for the screen saver by interacting with the Windows Registry.

    Args:
        password (str): The password to protect the screen saver.

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    try:
        # Open the registry key where the screen saver settings are stored
        key_path = r"Control Panel\Desktop"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
            # Update the ScreenSave_Password value in the registry
            winreg.SetValueEx(key, "ScreenSave_Password", 0, winreg.REG_SZ, password)
        return True
    except OSError as e:
        # Handle registry access errors
        print(f"Error setting screen saver password: {e}")
        return False


def enable_screen_saver_password_protection(enable: bool) -> bool:
    """
    Enables or disables password protection for the screen saver.

    Args:
        enable (bool): True to enable password protection, False to disable.

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    try:
        # Open the registry key where the screen saver settings are stored
        key_path = r"Control Panel\Desktop"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
            # Update the ScreenSaverIsSecure value in the registry
            winreg.SetValueEx(key, "ScreenSaverIsSecure", 0, winreg.REG_SZ, "1" if enable else "0")
        return True
    except OSError as e:
        # Handle registry access errors
        print(f"Error toggling screen saver password protection: {e}")
        return False


def is_screen_saver_password_protected() -> bool:
    """
    Checks if password protection for the screen saver is enabled.

    Returns:
        bool: True if password protection is enabled, False otherwise.
    """
    try:
        # Open the registry key where the screen saver settings are stored
        key_path = r"Control Panel\Desktop"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ) as key:
            # Read the ScreenSaverIsSecure value from the registry
            value, _ = winreg.QueryValueEx(key, "ScreenSaverIsSecure")
            return value == "1"
    except OSError as e:
        # Handle registry access errors
        print(f"Error checking screen saver password protection status: {e}")
        return False


if __name__ == "__main__":
    # Example usage
    print("Enabling screen saver password protection...")
    if enable_screen_saver_password_protection(True):
        print("Password protection enabled.")
    else:
        print("Failed to enable password protection.")

    print("Setting a password for the screen saver...")
    if set_screen_saver_password("my_secure_password"):
        print("Password set successfully.")
    else:
        print("Failed to set the password.")

    print("Checking if password protection is enabled...")
    if is_screen_saver_password_protected():
        print("Password protection is enabled.")
    else:
        print("Password protection is not enabled.")
```
