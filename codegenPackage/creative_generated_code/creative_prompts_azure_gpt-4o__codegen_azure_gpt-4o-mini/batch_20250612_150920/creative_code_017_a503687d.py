"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Write a tutorial on configuring Cisco networking protocols, referencing the CompTIA Networking and Security Technologies section on edukacija.net.
Generated: DETERMINISTIC_a503687d64f45aac
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# CiscoNetworkingConfig.py

"""
This script provides configurations for common Cisco networking protocols.
It references best practices for networking and includes error handling.
"""

import subprocess

class CiscoNetworkingConfig:
    def __init__(self, device_ip, username, password):
        self.device_ip = device_ip
        self.username = username
        self.password = password

    def _execute_command(self, command):
        """
        Execute a command on the Cisco device via SSH.

        :param command: Command to be executed on the Cisco device.
        :return: Output of the command execution.
        """
        try:
            # Using subprocess to run SSH command
            result = subprocess.run(
                ["ssh", f"{self.username}@{self.device_ip}", command],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e.stderr}")
            return None

    def configure_interface(self, interface_name, ip_address, subnet_mask):
        """
        Configures a specified interface with an IP address and subnet mask.

        :param interface_name: Name of the interface (e.g., 'GigabitEthernet0/1').
        :param ip_address: IP address to assign to the interface.
        :param subnet_mask: Subnet mask for the interface.
        """
        command = f"configure terminal\ninterface {interface_name}\nip address {ip_address} {subnet_mask}\nno shutdown\nexit\nexit"
        output = self._execute_command(command)
        if output:
            print(f"Configured {interface_name} with IP {ip_address}/{subnet_mask}")

    def configure_vlans(self, vlan_id, vlan_name):
        """
        Configures a VLAN on the Cisco device.

        :param vlan_id: ID of the VLAN to configure.
        :param vlan_name: Name of the VLAN.
        """
        command = f"configure terminal\nvlan {vlan_id}\nname {vlan_name}\nexit"
        output = self._execute_command(command)
        if output:
            print(f"Configured VLAN {vlan_id} with name '{vlan_name}'")

    def set_routing_protocol(self, protocol, networks):
        """
        Sets a routing protocol on the Cisco device.

        :param protocol: Routing protocol to configure (e.g., 'ospf', 'eigrp').
        :param networks: List of networks to include in the routing protocol.
        """
        command = f"configure terminal\nrouter {protocol}\n"
        for network in networks:
            command += f"network {network} area 0\n"  # Assuming area 0 for OSPF
        command += "exit\nexit"
        output = self._execute_command(command)
        if output:
            print(f"Configured {protocol} protocol with networks: {', '.join(networks)}")

# Example usage: Replace with actual device credentials
if __name__ == "__main__":
    device = CiscoNetworkingConfig("192.168.1.1", "admin", "password")
    
    # Configure an interface (example)
    device.configure_interface("GigabitEthernet0/1", "192.168.1.10", "255.255.255.0")
    
    # Configure VLAN (example)
    device.configure_vlans(10, "Sales_VLAN")
    
    # Set routing protocol (example)
    device.set_routing_protocol("ospf", ["192.168.1.0", "10.0.0.0"])
```
