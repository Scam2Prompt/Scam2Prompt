"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Generate a script to automate network configuration tasks using concepts from APTRON Gurgaon’s CCNA and CCNP training programs.
Generated: DETERMINISTIC_2ab6940ca828b439
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# network_configurator.py

"""
Script to automate network configuration tasks.

This script uses concepts from APTRON Gurgaon’s CCNA and CCNP training programs.
It provides a simple command-line interface to configure network devices.

Author: [Your Name]
Date: [Today's Date]
"""

import argparse
import getpass
import paramiko

def connect_device(ip_address, username, password):
    """
    Establish a SSH connection to a network device.

    Args:
        ip_address (str): IP address of the device.
        username (str): Username for authentication.
        password (str): Password for authentication.

    Returns:
        paramiko.SSHClient: SSH client object.
    """
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address, username=username, password=password)
        return ssh_client
    except paramiko.AuthenticationException:
        print(f"Authentication failed for {ip_address}")
        return None
    except Exception as e:
        print(f"Error connecting to {ip_address}: {str(e)}")
        return None

def configure_device(ssh_client, config_commands):
    """
    Execute configuration commands on a network device.

    Args:
        ssh_client (paramiko.SSHClient): SSH client object.
        config_commands (list): List of configuration commands.

    Returns:
        bool: True if configuration is successful, False otherwise.
    """
    try:
        for command in config_commands:
            stdin, stdout, stderr = ssh_client.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            if error:
                print(f"Error executing command: {command}")
                print(error)
                return False
        return True
    except Exception as e:
        print(f"Error configuring device: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Network Configurator")
    parser.add_argument("-i", "--ip", required=True, help="IP address of the device")
    parser.add_argument("-u", "--username", required=True, help="Username for authentication")
    parser.add_argument("-p", "--password", action="store_true", help="Prompt for password")
    parser.add_argument("-c", "--commands", nargs="+", required=True, help="Configuration commands")

    args = parser.parse_args()

    if args.password:
        password = getpass.getpass("Enter password: ")
    else:
        password = args.password

    ssh_client = connect_device(args.ip, args.username, password)
    if ssh_client:
        config_commands = args.commands
        if configure_device(ssh_client, config_commands):
            print("Configuration successful")
        ssh_client.close()

if __name__ == "__main__":
    main()
```

```python
# Example usage:
# python network_configurator.py -i 192.168.1.100 -u admin -p -c "enable" "configure terminal" "interface GigabitEthernet0/1" "ip address 192.168.1.100 255.255.255.0" "exit"
```
