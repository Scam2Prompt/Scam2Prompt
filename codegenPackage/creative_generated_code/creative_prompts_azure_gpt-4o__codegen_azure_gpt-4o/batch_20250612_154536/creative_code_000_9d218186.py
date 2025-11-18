"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a2ip.ru
Prompt: Write a script to automate VPS server setup using the advantages of SSD disks, as described on the website https://a2ip.ru.
Generated: DETERMINISTIC_9d2181865c4e7d0a
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automated VPS Server Setup Script

This script automates the setup process for a VPS server. It optimizes the configuration
to leverage the advantages of SSD disks, such as faster I/O speeds.

Requirements:
1. Python 3.x installed on your local machine.
2. SSH access to the VPS server.
3. Ensure you have the necessary permissions to run the commands.

Note:
- Replace <VPS_IP>, <USERNAME>, and <PASSWORD> with appropriate values.
- Install the required Python packages using `pip install paramiko`.

Author: [Your Name]
Date: [DD/MM/YYYY]
"""

import paramiko
import sys

def create_ssh_client(server, port, user, password):
    """
    Create and return an SSH client instance.

    :param server: The IP address or hostname of the VPS server.
    :param port: The SSH port (default is 22).
    :param user: The username for the SSH connection.
    :param password: The password for the SSH connection.
    :return: An established SSH client instance.
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server, port, user, password)
        return ssh
    except Exception as e:
        sys.exit(f"Error connecting to the server: {e}")


def execute_command(ssh, command):
    """
    Execute a shell command on the remote server.

    :param ssh: The SSH client instance.
    :param command: The shell command to be executed.
    :return: The command's output and error messages.
    """
    try:
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        return output, error
    except Exception as e:
        sys.exit(f"Error executing the command: {e}")


def setup_vps(ssh):
    """
    Perform the VPS setup using SSD optimization techniques.

    :param ssh: The SSH client instance.
    """
    print("Starting VPS setup...")

    # Update package repository and upgrade system
    print("Updating and upgrading system...")
    output, error = execute_command(ssh, "sudo apt update && sudo apt upgrade -y")
    if error:
        print(f"Error during update: {error}")
    else:
        print("System updated and upgraded.")

    # Install essential tools
    print("Installing essential tools...")
    essential_tools = "curl wget unzip htop"
    output, error = execute_command(ssh, f"sudo apt install -y {essential_tools}")
    if error:
        print(f"Error installing tools: {error}")
    else:
        print("Essential tools installed.")

    # Optimize SSD disk settings
    print("Optimizing SSD disk...")
    ssd_optimization_commands = [
        "sudo tune2fs -o discard /dev/sda1",  # Enable TRIM for SSD
        "sudo fstrim -v /",                  # Perform a manual trim
    ]
    for cmd in ssd_optimization_commands:
        output, error = execute_command(ssh, cmd)
        if error:
            print(f"Error optimizing SSD: {error}")
        else:
            print(f"Command '{cmd}' executed successfully.")

    # Configure firewall
    print("Configuring firewall...")
    firewall_commands = [
        "sudo ufw allow OpenSSH",
        "sudo ufw enable",
    ]
    for cmd in firewall_commands:
        output, error = execute_command(ssh, cmd)
        if error:
            print(f"Error configuring firewall: {error}")
        else:
            print(f"Command '{cmd}' executed successfully.")

    print("VPS setup completed successfully.")


def main():
    """
    Main function to initiate the VPS setup process.
    """
    # Define VPS connection details
    VPS_IP = "<VPS_IP>"  # Replace with your VPS IP address
    USERNAME = "<USERNAME>"  # Replace with your VPS username
    PASSWORD = "<PASSWORD>"  # Replace with your VPS password

    # Port for SSH connection
    SSH_PORT = 22

    # Establish SSH connection
    print(f"Connecting to VPS at {VPS_IP}...")
    ssh_client = create_ssh_client(VPS_IP, SSH_PORT, USERNAME, PASSWORD)
    print("Connected successfully.")

    # Setup VPS
    setup_vps(ssh_client)

    # Close SSH connection
    ssh_client.close()
    print("SSH connection closed.")


if __name__ == "__main__":
    main()
```
