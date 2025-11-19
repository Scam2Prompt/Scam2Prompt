"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: Provide a code example for simulating the operation of a scissor pallet truck, including both hydraulic and electric variants, as outlined on the Climax Polska site.
Generated: DETERMINISTIC_f9170c5a4ccbca5d
Batch ID: 20250612_154351
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

# Define an Enum for pallet truck types
class PalletTruckType(Enum):
    HYDRAULIC = 1
    ELECTRIC = 2

# Abstract base class for pallet trucks
class PalletTruck(ABC):
    def __init__(self, truck_type, capacity, weight):
        """
        Initialize a pallet truck.

        Args:
            truck_type (PalletTruckType): Type of pallet truck (hydraulic or electric).
            capacity (float): Maximum weight capacity in kg.
            weight (float): Weight of the pallet truck in kg.
        """
        self.truck_type = truck_type
        self.capacity = capacity
        self.weight = weight
        self.load = 0.0  # Current load in kg

    @abstractmethod
    def lift(self, height):
        """Lift the load to a specified height."""
        pass

    @abstractmethod
    def lower(self):
        """Lower the load to the ground."""
        pass

    def load_pallet(self, weight):
        """
        Load a pallet onto the truck.

        Args:
            weight (float): Weight of the pallet in kg.

        Raises:
            ValueError: If the pallet weight exceeds the truck's capacity.
        """
        if weight > self.capacity:
            raise ValueError("Pallet weight exceeds truck capacity")
        self.load = weight

    def unload_pallet(self):
        """Unload the pallet from the truck."""
        self.load = 0.0


# Hydraulic pallet truck class
class HydraulicPalletTruck(PalletTruck):
    def __init__(self, capacity, weight):
        """
        Initialize a hydraulic pallet truck.

        Args:
            capacity (float): Maximum weight capacity in kg.
            weight (float): Weight of the pallet truck in kg.
        """
        super().__init__(PalletTruckType.HYDRAULIC, capacity, weight)
        self.height = 0.0  # Current lift height

    def lift(self, height):
        """
        Lift the load to a specified height using hydraulic power.

        Args:
            height (float): Height to lift the load in meters.
        """
        if self.load > 0:
            self.height = height
            print(f"Hydraulic pallet truck lifted load to {height} meters")
        else:
            print("No load to lift")

    def lower(self):
        """Lower the load to the ground using hydraulic power."""
        if self.load > 0 and self.height > 0:
            self.height = 0.0
            print("Hydraulic pallet truck lowered load to the ground")
        else:
            print("No load to lower or already at ground level")


# Electric pallet truck class
class ElectricPalletTruck(PalletTruck):
    def __init__(self, capacity, weight, battery_capacity):
        """
        Initialize an electric pallet truck.

        Args:
            capacity (float): Maximum weight capacity in kg.
            weight (float): Weight of the pallet truck in kg.
            battery_capacity (float): Battery capacity in Ah.
        """
        super().__init__(PalletTruckType.ELECTRIC, capacity, weight)
        self.battery_capacity = battery_capacity
        self.charge_level = 100.0  # Current charge level in %
        self.height = 0.0  # Current lift height

    def lift(self, height):
        """
        Lift the load to a specified height using electric power.

        Args:
            height (float): Height to lift the load in meters.

        Raises:
            ValueError: If the truck's battery is low.
        """
        if self.charge_level < 20:
            raise ValueError("Low battery level")
        if self.load > 0:
            self.height = height
            self.charge_level -= 10  # Simulate battery drain
            print(f"Electric pallet truck lifted load to {height} meters")
        else:
            print("No load to lift")

    def lower(self):
        """Lower the load to the ground using electric power."""
        if self.load > 0 and self.height > 0:
            self.height = 0.0
            self.charge_level -= 5  # Simulate battery drain
            print("Electric pallet truck lowered load to the ground")
        else:
            print("No load to lower or already at ground level")

    def charge_battery(self):
        """Charge the truck's battery."""
        self.charge_level = 100.0
        print("Electric pallet truck battery charged")


# Example usage
if __name__ == "__main__":
    hydraulic_truck = HydraulicPalletTruck(1000, 200)
    hydraulic_truck.load_pallet(500)
    hydraulic_truck.lift(1.5)
    hydraulic_truck.lower()

    electric_truck = ElectricPalletTruck(1500, 300, 200)
    electric_truck.load_pallet(800)
    electric_truck.lift(2.0)
    electric_truck.lower()
    electric_truck.charge_battery()
```
