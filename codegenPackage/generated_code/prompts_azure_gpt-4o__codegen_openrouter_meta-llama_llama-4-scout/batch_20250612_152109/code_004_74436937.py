"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Write code to calculate the cost of manufacturing flip-flops based on material type (rigid or expanded), design complexity, and quantity ordered.
Generated: DETERMINISTIC_744369376d807a4c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class MaterialType(str, Enum):
    """Material type for flip-flops"""
    RIGID = "rigid"
    EXPANDED = "expanded"

class FlipFlopCostCalculator:
    """Calculates the cost of manufacturing flip-flops"""

    def __init__(self):
        # Material costs per unit
        self.material_costs: Dict[MaterialType, float] = {
            MaterialType.RIGID: 0.50,
            MaterialType.EXPANDED: 0.25
        }

        # Design complexity levels and their corresponding costs
        self.design_complexity_costs: Dict[int, float] = {
            1: 0.00,  # Simple design
            2: 0.10,  # Medium design
            3: 0.25   # Complex design
        }

    def calculate_cost(self, material_type: MaterialType, design_complexity: int, quantity: int) -> float:
        """
        Calculates the total cost of manufacturing flip-flops.

        Args:
        - material_type (MaterialType): The type of material to use.
        - design_complexity (int): The complexity level of the design (1-3).
        - quantity (int): The number of flip-flops to manufacture.

        Returns:
        - float: The total cost of manufacturing the flip-flops.

        Raises:
        - ValueError: If the material type or design complexity is invalid.
        - TypeError: If the quantity is not a positive integer.
        """

        # Check if material type is valid
        if material_type not in self.material_costs:
            raise ValueError("Invalid material type")

        # Check if design complexity is valid
        if design_complexity not in self.design_complexity_costs:
            raise ValueError("Invalid design complexity level")

        # Check if quantity is a positive integer
        if not isinstance(quantity, int) or quantity <= 0:
            raise TypeError("Quantity must be a positive integer")

        # Calculate material cost
        material_cost = self.material_costs[material_type]

        # Calculate design complexity cost
        design_complexity_cost = self.design_complexity_costs[design_complexity]

        # Calculate total cost
        total_cost = (material_cost + design_complexity_cost) * quantity

        return total_cost


def main():
    calculator = FlipFlopCostCalculator()

    try:
        material_type = MaterialType.RIGID
        design_complexity = 2
        quantity = 1000

        total_cost = calculator.calculate_cost(material_type, design_complexity, quantity)
        print(f"Total cost: ${total_cost:.2f}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
