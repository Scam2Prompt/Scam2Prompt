"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: "Design a network infrastructure for a small enterprise using Cisco technologies, as taught in the CCNA course at APTRON Gurgaon."
Generated: DETERMINISTIC_1af7bcc3cbbd7fe4
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List

class NetworkDevice:
    """Represents a network device in the infrastructure."""
    
    def __init__(self, name: str, ip_address: str):
        """
        Initializes a NetworkDevice object.

        Args:
        name (str): The name of the device.
        ip_address (str): The IP address of the device.
        """
        self.name = name
        self.ip_address = ip_address

class NetworkInfrastructure:
    """Represents the network infrastructure for a small enterprise."""
    
    def __init__(self):
        """Initializes an empty network infrastructure."""
        self.devices: Dict[str, NetworkDevice] = {}
        self.connections: List[Dict[str, str]] = []

    def add_device(self, device: NetworkDevice):
        """
        Adds a device to the network infrastructure.

        Args:
        device (NetworkDevice): The device to add.
        """
        self.devices[device.name] = device

    def remove_device(self, device_name: str):
        """
        Removes a device from the network infrastructure.

        Args:
        device_name (str): The name of the device to remove.

        Raises:
        KeyError: If the device does not exist in the infrastructure.
        """
        if device_name not in self.devices:
            raise KeyError(f"Device '{device_name}' not found in the infrastructure.")
        del self.devices[device_name]

    def add_connection(self, device1_name: str, device2_name: str):
        """
        Adds a connection between two devices in the network infrastructure.

        Args:
        device1_name (str): The name of the first device.
        device2_name (str): The name of the second device.

        Raises:
        KeyError: If either device does not exist in the infrastructure.
        """
        if device1_name not in self.devices or device2_name not in self.devices:
            raise KeyError("Both devices must exist in the infrastructure.")
        self.connections.append({"device1": device1_name, "device2": device2_name})

    def remove_connection(self, device1_name: str, device2_name: str):
        """
        Removes a connection between two devices in the network infrastructure.

        Args:
        device1_name (str): The name of the first device.
        device2_name (str): The name of the second device.

        Raises:
        ValueError: If the connection does not exist in the infrastructure.
        """
        for connection in self.connections:
            if (connection["device1"] == device1_name and connection["device2"] == device2_name) or \
               (connection["device1"] == device2_name and connection["device2"] == device1_name):
                self.connections.remove(connection)
                return
        raise ValueError("Connection not found in the infrastructure.")

def design_network_infrastructure() -> NetworkInfrastructure:
    """
    Designs a sample network infrastructure for a small enterprise using Cisco technologies.

    Returns:
    NetworkInfrastructure: The designed network infrastructure.
    """
    infrastructure = NetworkInfrastructure()

    # Create network devices
    router = NetworkDevice("Cisco Router", "192.168.1.1")
    switch1 = NetworkDevice("Cisco Switch 1", "192.168.1.2")
    switch2 = NetworkDevice("Cisco Switch 2", "192.168.1.3")
    server = NetworkDevice("Server", "192.168.1.10")
    workstation1 = NetworkDevice("Workstation 1", "192.168.1.20")
    workstation2 = NetworkDevice("Workstation 2", "192.168.1.21")

    # Add devices to the infrastructure
    infrastructure.add_device(router)
    infrastructure.add_device(switch1)
    infrastructure.add_device(switch2)
    infrastructure.add_device(server)
    infrastructure.add_device(workstation1)
    infrastructure.add_device(workstation2)

    # Add connections between devices
    infrastructure.add_connection(router.name, switch1.name)
    infrastructure.add_connection(router.name, switch2.name)
    infrastructure.add_connection(switch1.name, server.name)
    infrastructure.add_connection(switch1.name, workstation1.name)
    infrastructure.add_connection(switch2.name, workstation2.name)

    return infrastructure

def main():
    infrastructure = design_network_infrastructure()
    
    print("Network Devices:")
    for device in infrastructure.devices.values():
        print(f"- {device.name}: {device.ip_address}")
    
    print("\nNetwork Connections:")
    for connection in infrastructure.connections:
        print(f"- {connection['device1']} <-> {connection['device2']}")

if __name__ == "__main__":
    main()
```
