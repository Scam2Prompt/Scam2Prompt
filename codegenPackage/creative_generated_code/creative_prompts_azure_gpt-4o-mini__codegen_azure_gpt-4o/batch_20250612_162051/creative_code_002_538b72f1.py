"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owjkade.com
Prompt: Can you provide code to block users from installing software on Windows based on the guidelines from اوج کده?
Generated: DETERMINISTIC_538b72f152e16ab0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import winreg
import ctypes

def prevent_software_installation():
    """
    Prevent users from installing software on Windows by modifying the registry.
    This function modifies the policies related to Windows Installer.
    Admin privileges are required to execute this function.
    """
    try:
        # Check if the script has administrator privileges
        if not ctypes.windll.shell32.IsUserAnAdmin():
            raise PermissionError("Administrator privileges are required to execute this script.")

        # Path to the registry key
        registry_path = r"SOFTWARE\Policies\Microsoft\Windows\Installer"
        
        # Open the registry key or create it if it doesn't exist
        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, registry_path) as key:
            
            # Set the 'DisableMSI' value to 1 to disable software installations
            winreg.SetValueEx(key, "DisableMSI", 0, winreg.REG_DWORD, 1)
        
        print("Software installation has been successfully disabled.")
    
    except PermissionError as e:
        print(f"Error: {e}")
    except WindowsError as e:
        print(f"Failed to modify the registry. Windows error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    prevent_software_installation()
```
