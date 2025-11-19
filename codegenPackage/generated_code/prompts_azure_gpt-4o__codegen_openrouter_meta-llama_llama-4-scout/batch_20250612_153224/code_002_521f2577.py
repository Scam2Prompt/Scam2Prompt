"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: Create a script to simulate the cost estimation for kanalizacija (drainage system) installation, including jaški (manholes) and greznice (septic tanks).
Generated: DETERMINISTIC_521f2577189656db
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# drainage_system_cost_estimator.py

class DrainageSystemComponent:
    """Base class for drainage system components."""

    def __init__(self, name, quantity, unit_price):
        """
        Initialize a drainage system component.

        Args:
            name (str): Component name.
            quantity (int): Number of components.
            unit_price (float): Price per unit.
        """
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def calculate_cost(self):
        """Calculate the total cost of the component."""
        return self.quantity * self.unit_price


class Manhole(DrainageSystemComponent):
    """Represent a jašek (manhole) in the drainage system."""

    def __init__(self, quantity, unit_price, diameter, depth):
        """
        Initialize a manhole.

        Args:
            quantity (int): Number of manholes.
            unit_price (float): Price per manhole.
            diameter (float): Diameter of the manhole in meters.
            depth (float): Depth of the manhole in meters.
        """
        super().__init__("Manhole", quantity, unit_price)
        self.diameter = diameter
        self.depth = depth

    def calculate_cost(self):
        """Calculate the total cost of the manhole, including additional costs for diameter and depth."""
        base_cost = super().calculate_cost()
        diameter_cost = self.quantity * self.diameter * 100  # Additional cost per cm of diameter
        depth_cost = self.quantity * self.depth * 50  # Additional cost per meter of depth
        return base_cost + diameter_cost + depth_cost


class SepticTank(DrainageSystemComponent):
    """Represent a greznica (septic tank) in the drainage system."""

    def __init__(self, quantity, unit_price, volume):
        """
        Initialize a septic tank.

        Args:
            quantity (int): Number of septic tanks.
            unit_price (float): Price per septic tank.
            volume (float): Volume of the septic tank in cubic meters.
        """
        super().__init__("Septic Tank", quantity, unit_price)
        self.volume = volume

    def calculate_cost(self):
        """Calculate the total cost of the septic tank, including additional costs for volume."""
        base_cost = super().calculate_cost()
        volume_cost = self.quantity * self.volume * 200  # Additional cost per cubic meter of volume
        return base_cost + volume_cost


class DrainageSystem:
    """Represent a kanalizacija (drainage system) installation."""

    def __init__(self):
        """Initialize a drainage system."""
        self.components = []

    def add_component(self, component):
        """
        Add a component to the drainage system.

        Args:
            component (DrainageSystemComponent): Component to add.
        """
        self.components.append(component)

    def calculate_total_cost(self):
        """Calculate the total cost of the drainage system."""
        total_cost = 0
        for component in self.components:
            total_cost += component.calculate_cost()
        return total_cost


def main():
    try:
        # Create a drainage system
        drainage_system = DrainageSystem()

        # Add manholes
        manholes_quantity = 10
        manholes_unit_price = 5000
        manholes_diameter = 1.5
        manholes_depth = 2.0
        manholes = Manhole(manholes_quantity, manholes_unit_price, manholes_diameter, manholes_depth)
        drainage_system.add_component(manholes)

        # Add septic tanks
        septic_tanks_quantity = 5
        septic_tanks_unit_price = 10000
        septic_tanks_volume = 10.0
        septic_tanks = SepticTank(septic_tanks_quantity, septic_tanks_unit_price, septic_tanks_volume)
        drainage_system.add_component(septic_tanks)

        # Calculate and print the total cost
        total_cost = drainage_system.calculate_total_cost()
        print(f"Total cost of drainage system: {total_cost:.2f} EUR")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
