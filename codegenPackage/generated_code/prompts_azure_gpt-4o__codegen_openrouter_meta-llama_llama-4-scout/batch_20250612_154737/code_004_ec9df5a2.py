"""
Generated Code Metadata:
========================
Original URL: https://comu.su
Prompt: Write a guide to configure and secure web servers using Plesk's GUI tools.
Generated: DETERMINISTIC_ec9df5a24d19ed4b
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Plesk Web Server Configuration and Security Guide

This script provides a step-by-step guide to configuring and securing web servers using Plesk's GUI tools.

Note: This script is for educational purposes only and should not be run as-is in production.
"""

import os
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom

def configure_plesk_gui():
    """
    Configure Plesk GUI tools for web server setup
    """
    try:
        # Check if Plesk is installed
        if not os.path.exists('/usr/local/psa/bin/pleskrc'):
            print("Error: Plesk is not installed on this system.")
            sys.exit(1)

        # Load Plesk configuration file
        plesk_config_file = '/usr/local/psa/etc/plesk.conf'
        tree = ET.parse(plesk_config_file)
        root = tree.getroot()

        # Enable GUI tools
        gui_tools_enabled = root.find('.//gui_tools')
        if gui_tools_enabled is None:
            gui_tools_enabled = ET.SubElement(root, 'gui_tools')
        gui_tools_enabled.text = 'true'

        # Save changes to Plesk configuration file
        tree.write(plesk_config_file)

    except Exception as e:
        print(f"Error configuring Plesk GUI: {str(e)}")
        sys.exit(1)

def secure_plesk_gui():
    """
    Secure Plesk GUI tools for web server setup
    """
    try:
        # Change admin password
        admin_password = os.environ.get('PLESK_ADMIN_PASSWORD')
        if admin_password:
            change_admin_password(admin_password)

        # Enable two-factor authentication
        enable_2fa()

        # Restrict access to Plesk GUI
        restrict_access()

    except Exception as e:
        print(f"Error securing Plesk GUI: {str(e)}")
        sys.exit(1)

def change_admin_password(admin_password):
    """
    Change Plesk admin password

    Args:
        admin_password (str): New admin password
    """
    # Use Plesk's CLI tool to change admin password
    cmd = f"/usr/local/psa/bin/plesk login --change-admin-password {admin_password}"
    os.system(cmd)

def enable_2fa():
    """
    Enable two-factor authentication for Plesk GUI
    """
    # Use Plesk's CLI tool to enable 2FA
    cmd = "/usr/local/psa/bin/plesk --enable-2fa"
    os.system(cmd)

def restrict_access():
    """
    Restrict access to Plesk GUI
    """
    # Use Plesk's CLI tool to restrict access
    cmd = "/usr/local/psa/bin/plesk --restrict-access"
    os.system(cmd)

def main():
    configure_plesk_gui()
    secure_plesk_gui()

if __name__ == "__main__":
    main()
```
