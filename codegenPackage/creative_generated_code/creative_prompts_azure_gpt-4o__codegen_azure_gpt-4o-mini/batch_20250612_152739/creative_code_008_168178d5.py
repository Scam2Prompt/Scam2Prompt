"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fotopoint.com.ar
Prompt: Create a program to calculate the shipping cost for items purchased from Fotopoint, factoring in categories like "cables and chargers" and "mobility electric devices."
Generated: DETERMINISTIC_168178d500694b6c
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCostCalculator:
    """
    A class to calculate the shipping cost based on item categories.
    """

    # Define shipping costs for each category
    SHIPPING_COSTS = {
        "cables and chargers": 5.00,
        "mobility electric devices": 15.00,
        "default": 10.00  # Default shipping cost for unlisted categories
    }

    def __init__(self):
        """Initialize the shipping cost calculator."""
        pass

    def calculate_shipping_cost(self, category: str, quantity: int) -> float:
        """
        Calculate the shipping cost for a given category and quantity of items.

        Parameters:
            category (str): The category of the item.
            quantity (int): The number of items being shipped.

        Returns:
            float: The total shipping cost.

        Raises:
            ValueError: If quantity is less than or equal to zero.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        # Get the shipping cost for the specified category, defaulting if not found
        cost_per_item = self.SHIPPING_COSTS.get(category.lower(), self.SHIPPING_COSTS["default"])
        
        # Calculate total shipping cost
        total_cost = cost_per_item * quantity
        return total_cost

def main():
    """Main function to execute the shipping cost calculator."""
    calculator = ShippingCostCalculator()

    try:
        # Example usage: calculating shipping costs
        category = input("Enter the item category (cables and chargers, mobility electric devices): ")
        quantity = int(input("Enter the quantity of items: "))
        
        # Calculate the shipping cost
        total_shipping_cost = calculator.calculate_shipping_cost(category, quantity)
        
        print(f"The total shipping cost for {quantity} '{category}' is: ${total_shipping_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
