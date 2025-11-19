"""
Generated Code Metadata:
========================
Original URL: https://gautamindustries.com
Prompt: Create a function that calculates the total cost for purchasing various types of plywood boards, including Timba 710 and Duro Plywood, based on user input for quantity and pricing from Gautam Industries.
Generated: DETERMINISTIC_03ec5ba39e9feb47
Batch ID: 20250612_163540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PlywoodCostCalculator:
    def __init__(self):
        # Initialize the pricing for different types of plywood
        self.pricing = {
            "Timba 710": 50.0,  # Price per unit for Timba 710
            "Duro Plywood": 75.0  # Price per unit for Duro Plywood
        }

    def calculate_total_cost(self, plywood_type, quantity):
        """
        Calculate the total cost for purchasing plywood.

        :param plywood_type: str - The type of plywood (e.g., "Timba 710", "Duro Plywood")
        :param quantity: int - The quantity of plywood boards to purchase
        :return: float - The total cost for the specified plywood type and quantity
        :raises ValueError: If the plywood type is invalid or quantity is not a positive integer
        """
        # Validate the plywood type
        if plywood_type not in self.pricing:
            raise ValueError(f"Invalid plywood type: {plywood_type}. Available types: {', '.join(self.pricing.keys())}")

        # Validate the quantity
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Calculate total cost
        total_cost = self.pricing[plywood_type] * quantity
        return total_cost

def main():
    calculator = PlywoodCostCalculator()
    
    # User input for plywood type and quantity
    plywood_type = input("Enter the type of plywood (Timba 710 or Duro Plywood): ")
    try:
        quantity = int(input("Enter the quantity of plywood boards: "))
        
        # Calculate total cost
        total_cost = calculator.calculate_total_cost(plywood_type, quantity)
        print(f"The total cost for {quantity} {plywood_type} boards is: ${total_cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
