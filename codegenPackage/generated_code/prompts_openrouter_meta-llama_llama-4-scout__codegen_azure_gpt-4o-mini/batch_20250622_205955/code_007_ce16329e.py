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
class WorkbenchCalculator:
    """
    A simple calculator to estimate the total cost of a custom workbench configuration.
    """

    def __init__(self):
        # Initialize the cost components
        self.material_cost = 0.0
        self.drawer_cost = 0.0
        self.accessory_cost = 0.0

    def set_material_cost(self, cost: float):
        """
        Set the cost of materials for the workbench.

        :param cost: The cost of materials
        :raises ValueError: If the cost is negative
        """
        if cost < 0:
            raise ValueError("Material cost cannot be negative.")
        self.material_cost = cost

    def set_drawer_cost(self, cost: float):
        """
        Set the cost of drawers for the workbench.

        :param cost: The cost of drawers
        :raises ValueError: If the cost is negative
        """
        if cost < 0:
            raise ValueError("Drawer cost cannot be negative.")
        self.drawer_cost = cost

    def set_accessory_cost(self, cost: float):
        """
        Set the cost of accessories for the workbench.

        :param cost: The cost of accessories
        :raises ValueError: If the cost is negative
        """
        if cost < 0:
            raise ValueError("Accessory cost cannot be negative.")
        self.accessory_cost = cost

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of the custom workbench configuration.

        :return: The total cost
        """
        total_cost = self.material_cost + self.drawer_cost + self.accessory_cost
        return total_cost

    def display_cost_summary(self):
        """
        Display a summary of the costs associated with the workbench.
        """
        print("Cost Summary:")
        print(f"Material Cost: ${self.material_cost:.2f}")
        print(f"Drawer Cost: ${self.drawer_cost:.2f}")
        print(f"Accessory Cost: ${self.accessory_cost:.2f}")
        print(f"Total Cost: ${self.calculate_total_cost():.2f}")


if __name__ == "__main__":
    # Example usage of the WorkbenchCalculator
    calculator = WorkbenchCalculator()

    try:
        # Set costs (these values can be modified as needed)
        calculator.set_material_cost(150.00)
        calculator.set_drawer_cost(75.00)
        calculator.set_accessory_cost(30.00)

        # Display the cost summary
        calculator.display_cost_summary()

    except ValueError as e:
        print(f"Error: {e}")
```
