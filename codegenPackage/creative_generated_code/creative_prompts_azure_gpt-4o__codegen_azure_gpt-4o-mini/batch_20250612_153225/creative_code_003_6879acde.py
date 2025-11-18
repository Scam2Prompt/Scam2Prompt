"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayzentreprise.com
Prompt: Create a step-by-step guide for installing and configuring a structured network system, including routers, switches, firewalls, and servers, based on the solutions offered by Ray-Z Entreprise.
Generated: DETERMINISTIC_6879acde18d7f09a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Structured Network Configuration Script for Ray-Z Enterprise Solutions

This script automates the process of configuring network devices including
routers, switches, firewalls, and servers. It assumes that necessary libraries 
and dependencies are installed and that the devices are accessible over the network.

Requirements:
- Python 3.x
- Network device SDKs or APIs
- Access credentials for network devices
"""

import paramiko
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkDevice:
    def __init__(self, ip: str, username: str, password: str, device_type: str):
        self.ip = ip
        self.username = username
        self.password = password
        self.device_type = device_type
        self.ssh_client = None

    def connect(self):
        """Establish an SSH connection to the network device."""
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(self.ip, username=self.username, password=self.password)
            logging.info(f"Connected to {self.device_type} at {self.ip}")
        except Exception as e:
            logging.error(f"Failed to connect to {self.device_type} at {self.ip}: {e}")
            raise

    def execute_command(self, command: str) -> str:
        """Execute a command on the network device and return the output."""
        if not self.ssh_client:
            raise ConnectionError("SSH client is not connected.")
        
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            if error:
                logging.error(f"Error executing command '{command}': {error}")
                raise RuntimeError(f"Command failed: {error}")
            return output
        except Exception as e:
            logging.error(f"Command execution failed: {e}")
            raise

    def close(self):
        """Close the SSH connection."""
        if self.ssh_client:
            self.ssh_client.close()
            logging.info(f"Closed connection to {self.device_type} at {self.ip}")


def configure_router(router: NetworkDevice):
    """Configure a router with basic settings."""
    try:
        router.connect()
        router.execute_command("configure terminal")
        router.execute_command("hostname RayZ-Router")
        router.execute_command("interface GigabitEthernet0/0")
        router.execute_command("ip address 192.168.1.1 255.255.255.0")
        router.execute_command("no shutdown")
        router.close()
    except Exception as e:
        logging.error(f"Router configuration failed: {e}")


def configure_switch(switch: NetworkDevice):
    """Configure a switch with basic settings."""
    try:
        switch.connect()
        switch.execute_command("configure terminal")
        switch.execute_command("hostname RayZ-Switch")
        switch.execute_command("vlan 10")
        switch.execute_command("name Sales")
        switch.execute_command("exit")
        switch.execute_command("interface range GigabitEthernet0/1 - 24")
        switch.execute_command("switchport mode access")
        switch.execute_command("switchport access vlan 10")
        switch.execute_command("no shutdown")
        switch.close()
    except Exception as e:
        logging.error(f"Switch configuration failed: {e}")


def configure_firewall(firewall: NetworkDevice):
    """Configure a firewall with basic settings."""
    try:
        firewall.connect()
        firewall.execute_command("configure terminal")
        firewall.execute_command("hostname RayZ-Firewall")
        firewall.execute_command("access-list 100 permit ip any any")
        firewall.execute_command("interface outside")
        firewall.execute_command("ip address 203.0.113.1 255.255.255.0")
        firewall.execute_command("no shutdown")
        firewall.close()
    except Exception as e:
        logging.error(f"Firewall configuration failed: {e}")


def configure_server(server: NetworkDevice):
    """Configure a server with basic settings."""
    try:
        server.connect()
        server.execute_command("hostname RayZ-Server")
        server.execute_command("ip address 192.168.1.10 255.255.255.0")
        server.execute_command("service start")
        server.close()
    except Exception as e:
        logging.error(f"Server configuration failed: {e}")


def main():
    """Main function to execute network configuration."""
    devices = [
        NetworkDevice("192.168.1.254", "admin", "password", "Router"),
        NetworkDevice("192.168.1.253", "admin", "password", "Switch"),
        NetworkDevice("192.168.1.252", "admin", "password", "Firewall"),
        NetworkDevice("192.168.1.251", "admin", "password", "Server"),
    ]

    for device in devices:
        if device.device_type == "Router":
            configure_router(device)
        elif device.device_type == "Switch":
            configure_switch(device)
        elif device.device_type == "Firewall":
            configure_firewall(device)
        elif device.device_type == "Server":
            configure_server(device)

if __name__ == "__main__":
    main()
```
