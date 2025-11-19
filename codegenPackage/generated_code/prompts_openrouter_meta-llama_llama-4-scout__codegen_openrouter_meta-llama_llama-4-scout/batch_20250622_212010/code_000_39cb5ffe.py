"""
Generated Code Metadata:
========================
Original URL: https://infrastructure.bincom.net
Prompt: "List infrastructure components commonly found in a data center."
Generated: DETERMINISTIC_39cb5ffe2671c6f1
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# data_center_components.py

class DataCenterComponent:
    """Base class for data center components."""

    def __init__(self, name, description):
        """
        Initialize a data center component.

        Args:
            name (str): Name of the component.
            description (str): Description of the component.
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class Server(DataCenterComponent):
    """Server component."""

    def __init__(self, name, description, cpu_cores, memory):
        """
        Initialize a server component.

        Args:
            name (str): Name of the server.
            description (str): Description of the server.
            cpu_cores (int): Number of CPU cores.
            memory (int): Amount of memory in GB.
        """
        super().__init__(name, description)
        self.cpu_cores = cpu_cores
        self.memory = memory

    def __str__(self):
        return super().__str__() + f" (CPU Cores: {self.cpu_cores}, Memory: {self.memory} GB)"


class StorageSystem(DataCenterComponent):
    """Storage system component."""

    def __init__(self, name, description, storage_capacity):
        """
        Initialize a storage system component.

        Args:
            name (str): Name of the storage system.
            description (str): Description of the storage system.
            storage_capacity (int): Storage capacity in TB.
        """
        super().__init__(name, description)
        self.storage_capacity = storage_capacity

    def __str__(self):
        return super().__str__() + f" (Storage Capacity: {self.storage_capacity} TB)"


class NetworkDevice(DataCenterComponent):
    """Network device component."""

    def __init__(self, name, description, ports):
        """
        Initialize a network device component.

        Args:
            name (str): Name of the network device.
            description (str): Description of the network device.
            ports (int): Number of ports.
        """
        super().__init__(name, description)
        self.ports = ports

    def __str__(self):
        return super().__str__() + f" (Ports: {self.ports})"


class PowerDistributionUnit(DataCenterComponent):
    """Power distribution unit component."""

    def __init__(self, name, description, max_power):
        """
        Initialize a power distribution unit component.

        Args:
            name (str): Name of the power distribution unit.
            description (str): Description of the power distribution unit.
            max_power (int): Maximum power in kW.
        """
        super().__init__(name, description)
        self.max_power = max_power

    def __str__(self):
        return super().__str__() + f" (Max Power: {self.max_power} kW)"


def list_infrastructure_components():
    """
    List common infrastructure components found in a data center.

    Returns:
        list: List of data center components.
    """
    try:
        components = [
            Server("Server 1", "Application server", 16, 32),
            StorageSystem("Storage System 1", "SAN storage", 100),
            NetworkDevice("Switch 1", "Network switch", 48),
            PowerDistributionUnit("PDU 1", "Power distribution unit", 32),
            Server("Server 2", "Database server", 8, 16),
            StorageSystem("Storage System 2", "NAS storage", 50),
            NetworkDevice("Router 1", "Network router", 16),
            PowerDistributionUnit("PDU 2", "Power distribution unit", 16),
        ]

        return components

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def main():
    components = list_infrastructure_components()

    if components:
        print("Common Infrastructure Components in a Data Center:")
        for i, component in enumerate(components, start=1):
            print(f"{i}. {component}")
    else:
        print("No components found.")


if __name__ == "__main__":
    main()
```
