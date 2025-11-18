"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cc-community.net
Prompt: Recommend tools or libraries for customizing the context menu in WinRAR, as discussed in the CC-Community Board forums.
Generated: DETERMINISTIC_7f8ac09035d01a42
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to customize the context menu in WinRAR by modifying the Windows Registry.
This script uses the `winreg` module to add, modify, or remove custom context menu entries for WinRAR.
Ensure you run this script with administrative privileges, as modifying the registry requires elevated permissions.
"""

import winreg

def create_context_menu_entry(label, command):
    """
    Creates or modifies a custom context menu entry for WinRAR.
    
    Parameters:
    label (str): The name of the context menu item (e.g., "Compress with WinRAR").
    command (str): The command to execute when the menu item is clicked.
    """
    try:
        # Open the registry key for WinRAR's shell integration
        key_path = r"SOFTWARE\Classes\WinRAR\shell"
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as shell_key:
            # Create or modify the subkey for the menu item
            menu_key_path = f"{key_path}\\{label}"
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, menu_key_path) as menu_key:
                # Set the command for the menu item
                with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"{menu_key_path}\\command") as command_key:
                    winreg.SetValueEx(command_key, "", 0, winreg.REG_SZ, command)
        print(f"Context menu entry '{label}' created successfully.")
    except PermissionError:
        print("Error: You must run this script with administrative privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_context_menu_entry(label):
    """
    Removes a custom context menu entry for WinRAR.
    
    Parameters:
    label (str): The name of the context menu item to remove.
    """
    try:
        # Open the registry key for WinRAR's shell integration
        key_path = r"SOFTWARE\Classes\WinRAR\shell"
        menu_key_path = f"{key_path}\\{label}"
        
        # Delete the registry key for the context menu entry
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, f"{menu_key_path}\\command")
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, menu_key_path)
        print(f"Context menu entry '{label}' removed successfully.")
    except FileNotFoundError:
        print(f"Context menu entry '{label}' does not exist.")
    except PermissionError:
        print("Error: You must run this script with administrative privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    # Adding a context menu entry
    create_context_menu_entry("Compress with WinRAR", '"C:\\Program Files\\WinRAR\\WinRAR.exe" a "%1.rar" "%1"')
    
    # Removing a context menu entry
    # remove_context_menu_entry("Compress with WinRAR")
```
