"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cc-community.net
Prompt: Provide an example of how to enhance the context menu in Windows using tips from the CC-Community Board's Tech forum.
Generated: DETERMINISTIC_765eb6c3e8786a7e
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import winreg as reg
import ctypes

# Constants
HKCU = reg.HKEY_CURRENT_USER
KEY_PATH = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"

def add_context_menu_item(name, command):
    """
    Adds a new item to the Windows context menu.

    :param name: The name of the context menu item.
    :param command: The command that will be executed when the item is clicked.
    """
    try:
        # Create the key for the new context menu item
        reg_key_path = fr"{KEY_PATH}\{name}"
        with reg.OpenKey(HKCU, KEY_PATH, 0, reg.KEY_WRITE) as key:
            # Create a new subkey for the context menu item
            reg.CreateKey(key, name)
            # Set the command to be executed
            with reg.OpenKey(key, name, 0, reg.KEY_SET_VALUE) as subkey:
                reg.SetValueEx(subkey, "command", 0, reg.REG_SZ, command)
                print(f"Successfully added '{name}' to the context menu.")
    except PermissionError:
        print("Permission denied. Please run this script as administrator.")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_context_menu_item(name):
    """
    Removes an item from the Windows context menu.

    :param name: The name of the context menu item to be removed.
    """
    try:
        with reg.OpenKey(HKCU, KEY_PATH, 0, reg.KEY_WRITE) as key:
            reg.DeleteKey(key, name)
            print(f"Successfully removed '{name}' from the context menu.")
    except FileNotFoundError:
        print(f"The context menu item '{name}' does not exist.")
    except PermissionError:
        print("Permission denied. Please run this script as administrator.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Example usage
    context_menu_item_name = "My Custom Action"
    command_to_execute = r"C:\Path\To\Your\Application.exe"

    # Add a new context menu item
    add_context_menu_item(context_menu_item_name, command_to_execute)

    # Uncomment the line below to remove the context menu item
    # remove_context_menu_item(context_menu_item_name)

if __name__ == "__main__":
    # Check if the script is run with administrator privileges
    if ctypes.windll.shell32.IsUserAnAdmin():
        main()
    else:
        print("This script requires administrator privileges. Please run as administrator.")
```

Make sure to replace `C:\Path\To\Your\Application.exe` with the actual path to the application you wish to execute from the context menu.
