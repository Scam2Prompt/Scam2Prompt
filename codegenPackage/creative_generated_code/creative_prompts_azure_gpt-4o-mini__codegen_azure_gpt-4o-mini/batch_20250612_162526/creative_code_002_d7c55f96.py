"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Create a function that calculates the cost of materials based on One World Supply's pricing for construction supplies like anchors and couplings.
Generated: DETERMINISTIC_d7c55f96bef55ab8
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MaterialCostCalculator:
    """
    A class to calculate the cost of construction materials based on predefined pricing.
    """

    # Pricing for construction supplies (prices per unit)
    pricing = {
        'anchor': 1.50,  # price per anchor
        'coupling': 2.00  # price per coupling
    }

    def __init__(self):
        pass

    def calculate_cost(self, material_type, quantity):
        """
        Calculate the total cost for a given type of material and quantity.

        Args:
            material_type (str): The type of material (e.g., 'anchor', 'coupling').
            quantity (int): The number of units to purchase.

        Returns:
            float: The total cost for the specified materials.

        Raises:
            ValueError: If material_type is not recognized or quantity is non-positive.
        """

        # Validate input
        if material_type not in self.pricing:
            raise ValueError(f"Material type '{material_type}' is not recognized.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Calculate the total cost
        cost_per_unit = self.pricing[material_type]
        total_cost = cost_per_unit * quantity
        
        return total_cost


if __name__ == "__main__":
    # Example usage of the MaterialCostCalculator class
    calculator = MaterialCostCalculator()

    try:
        # Calculate the cost for 10 anchors
        anchor_cost = calculator.calculate_cost('anchor', 10)
        print(f"Total cost for 10 anchors: ${anchor_cost:.2f}")

        # Calculate the cost for 5 couplings
        coupling_cost = calculator.calculate_cost('coupling', 5)
        print(f"Total cost for 5 couplings: ${coupling_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
