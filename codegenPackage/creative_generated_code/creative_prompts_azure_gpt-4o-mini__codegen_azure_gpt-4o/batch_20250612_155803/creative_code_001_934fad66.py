"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-lab.info
Prompt: What are the setup steps for using SSH and VNC with the Raspberry Pi 5 Starter Kit as detailed on すいラボ?
Generated: DETERMINISTIC_934fad664e8268a0
Batch ID: 20250612_155803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that automates the setup of SSH and VNC for the Raspberry Pi 5 Starter Kit. This script assumes it is being run on the Raspberry Pi itself and that Python 3 is installed.

```python
#!/usr/bin/env python3

"""
Setup Script for SSH and VNC on Raspberry Pi 5 Starter Kit.

This script automates enabling SSH and VNC services, ensuring they are installed, 
and configuring firewall rules for secure remote access.
"""

import os
import subprocess
import sys

def run_command(command):
    """
    Run a shell command and handle errors gracefully.
    :param command: List of command arguments.
    :return: None
    """
    try:
        subprocess.run(command, check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while executing command: {' '.join(command)}")
        print(f"Error details: {e}")
        sys.exit(1)

def enable_service(service_name):
    """
    Enable and start a systemd service.
    :param service_name: Name of the service to enable.
    :return: None
    """
    print(f"Enabling and starting {service_name} service...")
    run_command(["sudo", "systemctl", "enable", service_name])
    run_command(["sudo", "systemctl", "start", service_name])

def setup_ssh():
    """
    Enable SSH service on the Raspberry Pi.
    :return: None
    """
    print("Setting up SSH...")
    enable_service("ssh")
    print("SSH setup complete.")

def setup_vnc():
    """
    Enable VNC service on the Raspberry Pi using `raspi-config`.
    :return: None
    """
    print("Setting up VNC...")
    # Raspi-config does not return error codes, so we rely on output messages
    try:
        subprocess.run(["sudo", "raspi-config", "nonint", "do_vnc", "0"], check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to enable VNC via raspi-config.")
        print(f"Error details: {e}")
        sys.exit(1)

    enable_service("vncserver-x11-serviced")
    print("VNC setup complete.")

def configure_firewall():
    """
    Set up ufw (Uncomplicated Firewall) for allowing SSH and VNC traffic.
    :return: None
    """
    print("Configuring firewall rules...")
    run_command(["sudo", "apt-get", "update"])
    run_command(["sudo", "apt-get", "install", "-y", "ufw"])
    run_command(["sudo", "ufw", "allow", "22"])  # Allow SSH
    run_command(["sudo", "ufw", "allow", "5900"])  # Allow VNC
    run_command(["sudo", "ufw", "enable"])
    print("Firewall configuration complete.")

def main():
    """
    Main function to set up SSH and VNC on the Raspberry Pi 5 Starter Kit.
    """
    print("Starting setup for SSH and VNC...")
    setup_ssh()
    setup_vnc()
    configure_firewall()
    print("Setup complete. You can now remotely access your Raspberry Pi via SSH or VNC.")

if __name__ == "__main__":
    main()
```

### Instructions
1. Save the script as `setup_ssh_vnc.py` on your Raspberry Pi.
2. Run the script with `python3 setup_ssh_vnc.py`.
3. Follow the printed instructions/output for any additional steps.

This script assumes that you have already installed the Raspberry Pi OS on your Raspberry Pi 5 and are logged into it locally or via a monitor and keyboard. It automates SSH and VNC setup for remote access convenience.
