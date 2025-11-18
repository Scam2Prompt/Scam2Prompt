"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmakers.co.nz
Prompt: Write a troubleshooting guide to resolve the issue "The Remote Session was disconnected because there are no Remote Desktop License Servers available to provide a license" for Windows Server 2012 or 2016, as detailed on Webmakers.
Generated: DETERMINISTIC_c9d3826decb32320
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Troubleshooting Guide: Resolve "The Remote Session was disconnected because there are no Remote Desktop License Servers available to provide a license" issue.

This Python script automates the process of diagnosing and resolving the issue on Windows Server 2012 or 2016.
The script performs the following steps:
1. Checks if Remote Desktop Licensing is installed and running.
2. Updates Group Policy settings to point to the correct RD License Server.
3. Verifies license server configuration.
4. Restarts necessary services.

Prerequisites:
- Python installed on your system.
- Run the script as Administrator.
"""

import os
import subprocess
import sys

def check_admin_privileges():
    """
    Check if the script is running with Administrator privileges.
    """
    try:
        # Windows command to check admin privileges
        admin_check = subprocess.check_output("net session", shell=True, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

def check_license_server_role():
    """
    Check if the Remote Desktop Licensing role is installed.
    """
    try:
        print("Checking if Remote Desktop Licensing is installed...")
        output = subprocess.check_output("powershell.exe Get-WindowsFeature | FindStr 'Remote Desktop Services'", shell=True)
        if b"RD Licensing" in output:
            print("Remote Desktop Licensing role is installed.")
            return True
        else:
            print("Remote Desktop Licensing role is NOT installed.")
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error checking RD Licensing role: {e}")
        return False

def configure_group_policy(license_server):
    """
    Configure Group Policy to point to the correct Remote Desktop License Server.
    """
    try:
        print(f"Configuring Group Policy to use license server: {license_server}")
        subprocess.check_call(f"powershell.exe Set-RDLicenseConfiguration -LicenseServer {license_server} -Mode PerUser", shell=True)
        print("Group Policy configuration updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error configuring Group Policy: {e}")
        sys.exit(1)

def restart_services():
    """
    Restart Remote Desktop Services to apply changes.
    """
    try:
        print("Restarting Remote Desktop Services...")
        subprocess.check_call("powershell.exe Restart-Service TermService", shell=True)
        print("Services restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting services: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute troubleshooting steps.
    """
    if not check_admin_privileges():
        print("This script must be run as Administrator. Please restart with elevated privileges.")
        sys.exit(1)

    if not check_license_server_role():
        print("Please install the Remote Desktop Licensing role on the server.")
        sys.exit(1)

    license_server = input("Enter the hostname or IP address of the Remote Desktop License Server: ").strip()
    if not license_server:
        print("Invalid license server input. Exiting.")
        sys.exit(1)

    configure_group_policy(license_server)
    restart_services()

    print("Troubleshooting steps completed successfully. Verify the Remote Desktop connection again.")

if __name__ == "__main__":
    main()
```
