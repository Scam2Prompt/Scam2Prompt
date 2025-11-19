"""
Generated Code Metadata:
========================
Original URL: https://metamax.ir
Prompt: "Explain the concept of a data center and its components as described on https://metamax.ir, and provide a simple network diagram using ASCII art."
Generated: DETERMINISTIC_e41852e7a7e533e7
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Data Center Components and Network Diagram

class DataCenter:
    """Represents a data center with its components."""

    def __init__(self, name, location):
        """
        Initializes a DataCenter object.

        Args:
            name (str): The name of the data center.
            location (str): The physical location of the data center.
        """
        self.name = name
        self.location = location
        self.servers = []
        self.storage = []
        self.network_devices = []

    def add_server(self, server):
        """Adds a server to the data center."""
        self.servers.append(server)

    def add_storage(self, storage):
        """Adds storage to the data center."""
        self.storage.append(storage)

    def add_network_device(self, device):
        """Adds a network device to the data center."""
        self.network_devices.append(device)


class Server:
    """Represents a server in the data center."""

    def __init__(self, name, cpu, ram):
        """
        Initializes a Server object.

        Args:
            name (str): The name of the server.
            cpu (int): The number of CPU cores.
            ram (int): The amount of RAM in GB.
        """
        self.name = name
        self.cpu = cpu
        self.ram = ram


class Storage:
    """Represents storage in the data center."""

    def __init__(self, name, capacity):
        """
        Initializes a Storage object.

        Args:
            name (str): The name of the storage.
            capacity (int): The storage capacity in GB.
        """
        self.name = name
        self.capacity = capacity


class NetworkDevice:
    """Represents a network device in the data center."""

    def __init__(self, name, type):
        """
        Initializes a NetworkDevice object.

        Args:
            name (str): The name of the network device.
            type (str): The type of network device (e.g., router, switch).
        """
        self.name = name
        self.type = type


def print_network_diagram(data_center):
    """Prints a simple network diagram using ASCII art."""
    print("  +---------------+")
    print(f"  |  {data_center.name}  |")
    print("  +---------------+")
    print("           |")
    print("           |")
    for device in data_center.network_devices:
        print(f"  +---------------+       {device.name} ({device.type})")
        print("  |               |")
        print("  +---------------+")
        print("           |")
        print("           |")
    for server in data_center.servers:
        print(f"  +---------------+       {server.name} (Server)")
        print(f"  |  CPU: {server.cpu}  |")
        print(f"  |  RAM: {server.ram}GB |")
        print("  +---------------+")
    for storage in data_center.storage:
        print(f"  +---------------+       {storage.name} (Storage)")
        print(f"  |  Capacity: {storage.capacity}GB |")
        print("  +---------------+")


def main():
    try:
        # Create a data center
        data_center = DataCenter("Meta Max Data Center", "Tehran, Iran")

        # Create servers
        server1 = Server("Server 1", 4, 16)
        server2 = Server("Server 2", 8, 32)

        # Create storage
        storage1 = Storage("Storage 1", 1000)
        storage2 = Storage("Storage 2", 2000)

        # Create network devices
        router = NetworkDevice("Router", "Router")
        switch = NetworkDevice("Switch", "Switch")

        # Add components to the data center
        data_center.add_server(server1)
        data_center.add_server(server2)
        data_center.add_storage(storage1)
        data_center.add_storage(storage2)
        data_center.add_network_device(router)
        data_center.add_network_device(switch)

        # Print network diagram
        print_network_diagram(data_center)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
