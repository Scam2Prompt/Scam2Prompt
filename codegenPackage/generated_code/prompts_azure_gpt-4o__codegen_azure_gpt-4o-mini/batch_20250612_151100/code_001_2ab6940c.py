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
import os
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkConfigurator:
    def __init__(self, device_ip, username, password):
        """
        Initialize the NetworkConfigurator with device credentials.

        :param device_ip: IP address of the network device
        :param username: Username for device authentication
        :param password: Password for device authentication
        """
        self.device_ip = device_ip
        self.username = username
        self.password = password

    def execute_command(self, command):
        """
        Execute a command on the network device using SSH.

        :param command: Command to be executed
        :return: Output of the command
        """
        try:
            # Using subprocess to execute SSH command
            ssh_command = f"ssh {self.username}@{self.device_ip} '{command}'"
            result = subprocess.run(ssh_command, shell=True, capture_output=True, text=True)
            result.check_returncode()  # Raise an error for non-zero exit codes
            logging.info(f"Command executed successfully: {command}")
            return result.stdout
        except subprocess.CalledProcessError as e:
            logging.error(f"Error executing command '{command}': {e.stderr}")
            return None

    def configure_interface(self, interface, ip_address, subnet_mask):
        """
        Configure a network interface with the specified IP address and subnet mask.

        :param interface: Interface to configure (e.g., 'GigabitEthernet0/1')
        :param ip_address: IP address to assign to the interface
        :param subnet_mask: Subnet mask for the IP address
        """
        command = f"interface {interface}\n ip address {ip_address} {subnet_mask}\n no shutdown"
        output = self.execute_command(command)
        if output:
            logging.info(f"Configured {interface} with IP {ip_address}/{subnet_mask}")

    def set_hostname(self, hostname):
        """
        Set the hostname of the network device.

        :param hostname: New hostname for the device
        """
        command = f"hostname {hostname}"
        output = self.execute_command(command)
        if output:
            logging.info(f"Hostname set to {hostname}")

    def save_configuration(self):
        """
        Save the current configuration to the device's startup configuration.
        """
        command = "write memory"
        output = self.execute_command(command)
        if output:
            logging.info("Configuration saved successfully.")

def main():
    # Example usage of the NetworkConfigurator class
    device_ip = "192.168.1.1"  # Replace with your device's IP
    username = "admin"          # Replace with your username
    password = "password"       # Replace with your password

    # Create an instance of NetworkConfigurator
    configurator = NetworkConfigurator(device_ip, username, password)

    # Configure network tasks
    configurator.set_hostname("Router1")
    configurator.configure_interface("GigabitEthernet0/1", "192.168.1.10", "255.255.255.0")
    configurator.save_configuration()

if __name__ == "__main__":
    main()
```
