"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owjkade.com
Prompt: Generate a script to block users from installing software on a Windows computer, based on the steps outlined on اوج کده.
Generated: DETERMINISTIC_4c97ff3263292ce5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to block users from installing software on a Windows computer.
This script modifies specific registry keys to restrict software installations.
Ensure to run this script with Administrator privileges.

WARNING: Modifying registry keys can affect the system's behavior. Proceed with caution.

Language: Python
Dependencies: winreg (built-in module)
"""

import winreg as reg
import ctypes

def is_admin():
    """
    Check if the script is running with administrator privileges.
    Returns True if the script has admin rights, False otherwise.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def block_software_installation():
    """
    Block users from installing software by modifying the registry keys.
    """
    try:
        # Path to the registry key to restrict software installations.
        registry_path = r"SOFTWARE\Policies\Microsoft\Windows\Installer"
        
        # Open or create the registry key
        with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, registry_path) as key:
            # Set the DisableMSI value to 1 (Disable Windows Installer for all users)
            reg.SetValueEx(key, "DisableMSI", 0, reg.REG_DWORD, 1)
        
        print("Software installation has been successfully blocked.")
    except PermissionError:
        print("Error: Insufficient permissions. Please run the script as an administrator.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Entry point for the script.
    """
    if not is_admin():
        print("This script requires administrator privileges to run.")
        print("Please run the script as an administrator and try again.")
        return
    
    block_software_installation()

if __name__ == "__main__":
    main()
```
