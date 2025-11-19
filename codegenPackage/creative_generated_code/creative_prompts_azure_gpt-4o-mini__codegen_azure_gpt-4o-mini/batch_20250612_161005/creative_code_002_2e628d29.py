"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landoparafusos.blogspot.com
Prompt: Write a Python function that calculates the total cost of solar panel installation materials, including items like Porcas and Arruelas from Lando Parafusos.
Generated: DETERMINISTIC_2e628d29a02416e4
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SolarPanelInstallationCostCalculator:
    """
    A class to calculate the total cost of solar panel installation materials.
    """

    def __init__(self):
        # Dictionary to hold the costs of different materials
        self.material_costs = {
            'porcas': 0.10,  # cost per unit of porcas in currency
            'arruelas': 0.05,  # cost per unit of arruelas in currency
            # More materials can be added here
        }

    def calculate_total_cost(self, quantities):
        """
        Calculate the total cost of installation materials.

        Args:
            quantities (dict): A dictionary where keys are material names and values are their quantities.

        Returns:
            float: The total cost of the materials.

        Raises:
            ValueError: If any material in quantities is not recognized or if the quantity is negative.
        """
        total_cost = 0.0
        
        for material, quantity in quantities.items():
            if material not in self.material_costs:
                raise ValueError(f"Material '{material}' is not recognized.")
            if quantity < 0:
                raise ValueError(f"Quantity for '{material}' cannot be negative.")
            
            # Calculate the cost for the current material
            cost_for_material = self.material_costs[material] * quantity
            total_cost += cost_for_material
            
        return total_cost


# Example usage
if __name__ == "__main__":
    calculator = SolarPanelInstallationCostCalculator()
    
    # Quantities of materials required
    quantities = {
        'porcas': 100,
        'arruelas': 200,
    }
    
    try:
        total_cost = calculator.calculate_total_cost(quantities)
        print(f"The total cost of solar panel installation materials is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
