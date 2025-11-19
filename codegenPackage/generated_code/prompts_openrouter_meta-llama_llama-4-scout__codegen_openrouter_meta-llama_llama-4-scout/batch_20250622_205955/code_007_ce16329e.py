"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: "Develop a simple calculator to estimate the total cost of a custom workbench configuration from Karma Dolap, including the cost of drawers, materials, and accessories."
Generated: DETERMINISTIC_ce16329e0c97c08a
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# workbench_calculator.py

class WorkbenchCalculator:
    """
    Estimates the total cost of a custom workbench configuration.

    Attributes:
        material_costs (dict): Material costs per unit.
        drawer_cost (float): Cost of a single drawer.
        accessory_costs (dict): Accessory costs.
    """

    def __init__(self):
        # Define material costs per unit
        self.material_costs = {
            "wood": 50.0,
            "steel": 75.0,
            "aluminum": 40.0
        }

        # Define cost of a single drawer
        self.drawer_cost = 100.0

        # Define accessory costs
        self.accessory_costs = {
            "lighting": 50.0,
            "outlets": 75.0,
            "cabinets": 200.0
        }

    def calculate_material_cost(self, material, quantity):
        """
        Calculates the cost of materials.

        Args:
            material (str): Material type.
            quantity (int): Quantity of material.

        Returns:
            float: Material cost.

        Raises:
            ValueError: If material is not supported.
        """
        if material not in self.material_costs:
            raise ValueError(f"Unsupported material: {material}")

        return self.material_costs[material] * quantity

    def calculate_drawer_cost(self, num_drawers):
        """
        Calculates the cost of drawers.

        Args:
            num_drawers (int): Number of drawers.

        Returns:
            float: Drawer cost.
        """
        return self.drawer_cost * num_drawers

    def calculate_accessory_cost(self, accessories):
        """
        Calculates the cost of accessories.

        Args:
            accessories (list): List of accessory names.

        Returns:
            float: Accessory cost.

        Raises:
            ValueError: If an accessory is not supported.
        """
        accessory_cost = 0.0
        for accessory in accessories:
            if accessory not in self.accessory_costs:
                raise ValueError(f"Unsupported accessory: {accessory}")
            accessory_cost += self.accessory_costs[accessory]

        return accessory_cost

    def estimate_total_cost(self, material, quantity, num_drawers, accessories):
        """
        Estimates the total cost of a custom workbench configuration.

        Args:
            material (str): Material type.
            quantity (int): Quantity of material.
            num_drawers (int): Number of drawers.
            accessories (list): List of accessory names.

        Returns:
            float: Total cost.

        Raises:
            ValueError: If material or accessory is not supported.
        """
        material_cost = self.calculate_material_cost(material, quantity)
        drawer_cost = self.calculate_drawer_cost(num_drawers)
        accessory_cost = self.calculate_accessory_cost(accessories)

        return material_cost + drawer_cost + accessory_cost


def main():
    calculator = WorkbenchCalculator()

    # Example usage
    material = "wood"
    quantity = 2
    num_drawers = 3
    accessories = ["lighting", "outlets"]

    try:
        total_cost = calculator.estimate_total_cost(material, quantity, num_drawers, accessories)
        print(f"Estimated total cost: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
