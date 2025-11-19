"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gautamindustries.com
Prompt: Create a function that calculates the total cost for purchasing various types of plywood boards, including Timba 710 and Duro Plywood, based on user input for quantity and pricing from Gautam Industries.
Generated: DETERMINISTIC_03ec5ba39e9feb47
Batch ID: 20250612_163540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PlywoodCostCalculator:
    """A class to calculate the total cost of purchasing plywood boards."""
    
    def __init__(self):
        """Initializes the plywood types and their respective prices."""
        # Prices per unit for each type of plywood
        self.prices = {
            'Timba 710': 50.0,  # Price per unit for Timba 710
            'Duro Plywood': 70.0  # Price per unit for Duro Plywood
        }

    def calculate_total_cost(self, plywood_type, quantity):
        """
        Calculate total cost based on the type of plywood and quantity.
        
        Parameters:
        plywood_type (str): The type of plywood to be purchased.
        quantity (int): The number of plywood boards to purchase.
        
        Returns:
        float: The total cost of the purchase.
        
        Raises:
        ValueError: If plywood_type is not valid or quantity is less than 1.
        """
        # Validate the plywood type
        if plywood_type not in self.prices:
            raise ValueError(f"Invalid plywood type '{plywood_type}'. Valid options are {list(self.prices.keys())}.")
        
        # Validate the quantity
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        # Calculate total cost
        total_cost = self.prices[plywood_type] * quantity
        return total_cost


def main():
    """Main function to demonstrate the usage of PlywoodCostCalculator."""
    calculator = PlywoodCostCalculator()

    # Example user input
    plywood_type = input("Enter the plywood type (Timba 710 or Duro Plywood): ")
    try:
        quantity = int(input("Enter the quantity of plywood boards: "))
        
        # Calculate the total cost
        total_cost = calculator.calculate_total_cost(plywood_type, quantity)
        
        # Display the result
        print(f"The total cost for {quantity} {plywood_type} boards is: ${total_cost:.2f}")
    
    except ValueError as e:
        # Handle any value errors that arise from invalid input
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
