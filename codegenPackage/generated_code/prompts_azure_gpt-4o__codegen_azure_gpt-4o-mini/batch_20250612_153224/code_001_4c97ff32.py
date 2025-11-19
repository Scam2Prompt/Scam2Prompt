"""
Generated Code Metadata:
========================
Original URL: https://owjkade.com
Prompt: Generate a script to block users from installing software on a Windows computer, based on the steps outlined on اوج کده.
Generated: DETERMINISTIC_4c97ff3263292ce5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(filename='block_software_installation.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def block_software_installation():
    """
    Blocks users from installing software on a Windows computer by modifying Group Policy settings.
    This function will create a registry key that prevents software installations.
    """
    try:
        # Define the registry path for software installation settings
        registry_path = r"SOFTWARE\Policies\Microsoft\Windows\Installer"
        
        # Create the registry key to block software installation
        subprocess.run(['reg', 'add', registry_path, '/v', 'DisableMSI', '/t', 'REG_DWORD', '/d', '2', '/f'], check=True)
        
        logging.info("Successfully blocked software installation.")
        print("Software installation has been successfully blocked.")
        
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to modify registry: {e}")
        print("Error: Failed to block software installation. Check the log for details.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print("An unexpected error occurred. Check the log for details.")
        sys.exit(1)

if __name__ == "__main__":
    # Check if the script is run with administrative privileges
    if not os.geteuid() == 0:
        print("This script must be run as an administrator.")
        sys.exit(1)

    block_software_installation()
```

**Note:** This script must be run with administrative privileges to modify the Windows registry. Ensure to test in a safe environment before deploying in production.
