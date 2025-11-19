"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Write code to model the lifecycle of deep cycle batteries, referencing Battery Australia's categories like AGM, flooded, and gel batteries.
Generated: DETERMINISTIC_8f5465f087c9ee8f
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict

class BatteryType(str, Enum):
    """ Enum for different battery types """
    AGM = "AGM"
    FLOODED = "Flooded"
    GEL = "Gel"

class DeepCycleBattery(ABC):
    """ Abstract base class for deep cycle batteries """

    def __init__(self, battery_type: BatteryType, capacity: float, max_dod: float):
        """
        Initialize a deep cycle battery.

        Args:
        - battery_type (BatteryType): Type of the battery
        - capacity (float): Capacity of the battery in Ah
        - max_dod (float): Maximum depth of discharge (0-1)
        """
        self.battery_type = battery_type
        self.capacity = capacity
        self.max_dod = max_dod
        self.state_of_charge = 1.0  # Initialize SOC to 100%

    @abstractmethod
    def charge(self, amount: float):
        """ Charge the battery by a certain amount """
        pass

    @abstractmethod
    def discharge(self, amount: float):
        """ Discharge the battery by a certain amount """
        pass

    def get_state_of_charge(self) -> float:
        """ Get the current state of charge """
        return self.state_of_charge

    def get_battery_type(self) -> BatteryType:
        """ Get the battery type """
        return self.battery_type

class AGMDeepCycleBattery(DeepCycleBattery):
    """ Class for AGM deep cycle batteries """

    def __init__(self, capacity: float):
        """
        Initialize an AGM deep cycle battery.

        Args:
        - capacity (float): Capacity of the battery in Ah
        """
        super().__init__(BatteryType.AGM, capacity, 0.8)  # AGM max DOD is typically 80%

    def charge(self, amount: float):
        """ Charge the AGM battery by a certain amount """
        if amount < 0:
            raise ValueError("Charge amount cannot be negative")
        self.state_of_charge = min(1.0, self.state_of_charge + amount / self.capacity)

    def discharge(self, amount: float):
        """ Discharge the AGM battery by a certain amount """
        if amount < 0:
            raise ValueError("Discharge amount cannot be negative")
        self.state_of_charge = max(0.0, self.state_of_charge - amount / self.capacity)

class FloodedDeepCycleBattery(DeepCycleBattery):
    """ Class for flooded deep cycle batteries """

    def __init__(self, capacity: float):
        """
        Initialize a flooded deep cycle battery.

        Args:
        - capacity (float): Capacity of the battery in Ah
        """
        super().__init__(BatteryType.FLOODED, capacity, 0.5)  # Flooded max DOD is typically 50%

    def charge(self, amount: float):
        """ Charge the flooded battery by a certain amount """
        if amount < 0:
            raise ValueError("Charge amount cannot be negative")
        self.state_of_charge = min(1.0, self.state_of_charge + amount / self.capacity)

    def discharge(self, amount: float):
        """ Discharge the flooded battery by a certain amount """
        if amount < 0:
            raise ValueError("Discharge amount cannot be negative")
        self.state_of_charge = max(0.0, self.state_of_charge - amount / self.capacity)

class GelDeepCycleBattery(DeepCycleBattery):
    """ Class for gel deep cycle batteries """

    def __init__(self, capacity: float):
        """
        Initialize a gel deep cycle battery.

        Args:
        - capacity (float): Capacity of the battery in Ah
        """
        super().__init__(BatteryType.GEL, capacity, 0.7)  # Gel max DOD is typically 70%

    def charge(self, amount: float):
        """ Charge the gel battery by a certain amount """
        if amount < 0:
            raise ValueError("Charge amount cannot be negative")
        self.state_of_charge = min(1.0, self.state_of_charge + amount / self.capacity)

    def discharge(self, amount: float):
        """ Discharge the gel battery by a certain amount """
        if amount < 0:
            raise ValueError("Discharge amount cannot be negative")
        self.state_of_charge = max(0.0, self.state_of_charge - amount / self.capacity)

class BatteryFactory:
    """ Factory class for creating deep cycle batteries """

    @staticmethod
    def create_battery(battery_type: BatteryType, capacity: float) -> DeepCycleBattery:
        """
        Create a deep cycle battery.

        Args:
        - battery_type (BatteryType): Type of the battery
        - capacity (float): Capacity of the battery in Ah

        Returns:
        - DeepCycleBattery: The created battery
        """
        if battery_type == BatteryType.AGM:
            return AGMDeepCycleBattery(capacity)
        elif battery_type == BatteryType.FLOODED:
            return FloodedDeepCycleBattery(capacity)
        elif battery_type == BatteryType.GEL:
            return GelDeepCycleBattery(capacity)
        else:
            raise ValueError("Invalid battery type")

def main():
    # Example usage
    battery_factory = BatteryFactory()
    agm_battery = battery_factory.create_battery(BatteryType.AGM, 200)
    flooded_battery = battery_factory.create_battery(BatteryType.FLOODED, 300)
    gel_battery = battery_factory.create_battery(BatteryType.GEL, 250)

    batteries: Dict[BatteryType, DeepCycleBattery] = {
        BatteryType.AGM: agm_battery,
        BatteryType.FLOODED: flooded_battery,
        BatteryType.GEL: gel_battery,
    }

    for battery_type, battery in batteries.items():
        print(f"Battery Type: {battery_type}")
        print(f"Initial SOC: {battery.get_state_of_charge():.2f}")
        
        battery.discharge(50)
        print(f"SOC after discharging 50Ah: {battery.get_state_of_charge():.2f}")
        
        battery.charge(20)
        print(f"SOC after charging 20Ah: {battery.get_state_of_charge():.2f}")
        print()

if __name__ == "__main__":
    main()
```
