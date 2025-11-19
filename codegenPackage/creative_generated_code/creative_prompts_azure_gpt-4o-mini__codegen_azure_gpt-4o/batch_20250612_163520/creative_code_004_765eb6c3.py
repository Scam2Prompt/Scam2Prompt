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
import winreg

def add_context_menu_option(menu_name: str, command: str):
    """
    Adds a custom option to the Windows context menu for all files.
    
    Parameters:
    menu_name (str): The name of the context menu item.
    command (str): The command to execute when the menu item is clicked.
    """
    try:
        # Open the registry key for all file types
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"*\\shell", 0, winreg.KEY_WRITE) as shell_key:
            # Create a new key for the custom menu
            with winreg.CreateKey(shell_key, menu_name) as menu_key:
                # Set the default value of the menu key (menu name)
                winreg.SetValueEx(menu_key, "", 0, winreg.REG_SZ, menu_name)
                
                # Create the command sub-key
                with winreg.CreateKey(menu_key, "command") as command_key:
                    # Set the default value of the command key (command to execute)
                    winreg.SetValueEx(command_key, "", 0, winreg.REG_SZ, command)
        
        print(f"Successfully added context menu option: '{menu_name}'")
    except Exception as e:
        print(f"Error while adding context menu option: {e}")


def remove_context_menu_option(menu_name: str):
    """
    Removes a custom option from the Windows context menu for all files.
    
    Parameters:
    menu_name (str): The name of the context menu item to remove.
    """
    try:
        # Open the registry key for all file types
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"*\\shell", 0, winreg.KEY_WRITE) as shell_key:
            # Delete the menu key
            winreg.DeleteKey(shell_key, menu_name)
        
        print(f"Successfully removed context menu option: '{menu_name}'")
    except FileNotFoundError:
        print(f"Context menu option '{menu_name}' not found.")
    except Exception as e:
        print(f"Error while removing context menu option: {e}")


if __name__ == "__main__":
    # Example usage:
    # Adding a context menu option
    menu_name = "Open with MyApp"
    command = r"C:\Path\To\YourApp.exe \"%1\""  # %1 passes the selected file path as an argument
    add_context_menu_option(menu_name, command)

    # Uncomment the line below to test removing the context menu option
    # remove_context_menu_option(menu_name)
```

### Notes:
- Save and run this script with administrator privileges to modify the Windows registry.
- The `command` should point to your application's executable path and include `%1` to pass the file path as an argument.
- Be cautious when editing the registry; incorrect changes can harm your system.
