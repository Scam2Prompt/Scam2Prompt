"""
Generated Code Metadata:
========================
Original URL: https://vertiv.dns.cz
Prompt: Create a Python function to simulate power load balancing using Vertiv's UPS systems in a multi-rack data center environment.
Generated: DETERMINISTIC_b8282cff2b2a9de4
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class UPS:
    def __init__(self, capacity: float, efficiency: float):
        """
        Initialize a UPS system.

        Args:
        - capacity (float): The maximum power capacity of the UPS in kW.
        - efficiency (float): The efficiency of the UPS (0.0 - 1.0).
        """
        self.capacity = capacity
        self.efficiency = efficiency
        self.current_load = 0.0

    def add_load(self, load: float) -> bool:
        """
        Add a load to the UPS.

        Args:
        - load (float): The load to add in kW.

        Returns:
        - bool: True if the load was added successfully, False otherwise.
        """
        if self.current_load + load <= self.capacity * self.efficiency:
            self.current_load += load
            return True
        return False

    def remove_load(self, load: float) -> bool:
        """
        Remove a load from the UPS.

        Args:
        - load (float): The load to remove in kW.

        Returns:
        - bool: True if the load was removed successfully, False otherwise.
        """
        if self.current_load - load >= 0:
            self.current_load -= load
            return True
        return False


class Rack:
    def __init__(self, name: str, max_power: float):
        """
        Initialize a rack.

        Args:
        - name (str): The name of the rack.
        - max_power (float): The maximum power consumption of the rack in kW.
        """
        self.name = name
        self.max_power = max_power
        self.current_power = 0.0
        self.ups = None

    def assign_ups(self, ups: UPS):
        """
        Assign a UPS to the rack.

        Args:
        - ups (UPS): The UPS to assign.
        """
        self.ups = ups

    def add_power(self, power: float) -> bool:
        """
        Add power to the rack.

        Args:
        - power (float): The power to add in kW.

        Returns:
        - bool: True if the power was added successfully, False otherwise.
        """
        if self.ups:
            if self.ups.add_load(power):
                self.current_power += power
                return True
        return False

    def remove_power(self, power: float) -> bool:
        """
        Remove power from the rack.

        Args:
        - power (float): The power to remove in kW.

        Returns:
        - bool: True if the power was removed successfully, False otherwise.
        """
        if self.ups:
            if self.ups.remove_load(power):
                self.current_power -= power
                return True
        return False


class DataCenter:
    def __init__(self):
        """
        Initialize a data center.
        """
        self.racks: Dict[str, Rack] = {}
        self.ups_systems: List[UPS] = []

    def add_rack(self, rack: Rack):
        """
        Add a rack to the data center.

        Args:
        - rack (Rack): The rack to add.
        """
        self.racks[rack.name] = rack

    def add_ups(self, ups: UPS):
        """
        Add a UPS system to the data center.

        Args:
        - ups (UPS): The UPS system to add.
        """
        self.ups_systems.append(ups)

    def assign_ups_to_rack(self, rack_name: str, ups: UPS):
        """
        Assign a UPS system to a rack.

        Args:
        - rack_name (str): The name of the rack.
        - ups (UPS): The UPS system to assign.
        """
        if rack_name in self.racks:
            self.racks[rack_name].assign_ups(ups)


def simulate_power_load_balancing(data_center: DataCenter, rack_name: str, power: float) -> bool:
    """
    Simulate power load balancing in a data center.

    Args:
    - data_center (DataCenter): The data center to simulate.
    - rack_name (str): The name of the rack to add power to.
    - power (float): The power to add in kW.

    Returns:
    - bool: True if the power was added successfully, False otherwise.
    """
    if rack_name in data_center.racks:
        return data_center.racks[rack_name].add_power(power)
    return False


def main():
    # Create a data center
    data_center = DataCenter()

    # Create UPS systems
    ups1 = UPS(100.0, 0.9)
    ups2 = UPS(50.0, 0.8)

    # Add UPS systems to the data center
    data_center.add_ups(ups1)
    data_center.add_ups(ups2)

    # Create racks
    rack1 = Rack("Rack 1", 50.0)
    rack2 = Rack("Rack 2", 30.0)

    # Add racks to the data center
    data_center.add_rack(rack1)
    data_center.add_rack(rack2)

    # Assign UPS systems to racks
    data_center.assign_ups_to_rack("Rack 1", ups1)
    data_center.assign_ups_to_rack("Rack 2", ups2)

    # Simulate power load balancing
    print(simulate_power_load_balancing(data_center, "Rack 1", 20.0))  # Should print: True
    print(simulate_power_load_balancing(data_center, "Rack 2", 40.0))  # Should print: False


if __name__ == "__main__":
    main()
```
