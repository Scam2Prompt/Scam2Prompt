"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createxpro.com
Prompt: Write code to calculate the cost of personalized promotional items based on customization techniques such as serigraphy, vinyl printing, and sublimation, as described on CreatexPro.
Generated: DETERMINISTIC_45388d7a1d30698a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PromotionalItem:
    """
    A class to represent a promotional item and calculate its cost based on customization techniques.
    """

    def __init__(self, base_price: float):
        """
        Initializes a new PromotionalItem with a given base price.

        Args:
            base_price (float): The base price of the promotional item.
        """
        if base_price < 0:
            raise ValueError("Base price cannot be negative.")
        
        self.base_price = base_price
        self.customization_cost = 0.0

    def add_customization(self, technique: str, quantity: int):
        """
        Adds customization cost based on the technique used.

        Args:
            technique (str): The customization technique ('serigraphy', 'vinyl', 'sublimation').
            quantity (int): The quantity to be customized.

        Raises:
            ValueError: If an unsupported technique is provided or if quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        # Define customization costs per technique
        TECHNIQUE_COSTS = {
            'serigraphy': 2.00,  # Cost per item for serigraphy
            'vinyl': 1.50,       # Cost per item for vinyl printing
            'sublimation': 3.00   # Cost per item for sublimation
        }

        if technique not in TECHNIQUE_COSTS:
            raise ValueError(f"Unsupported customization technique: {technique}")

        # Calculate total customization cost based on chosen technique and quantity
        self.customization_cost += TECHNIQUE_COSTS[technique] * quantity

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the promotional item including customizations.

        Returns:
            float: The total cost of the promotional item.
        """
        total_cost = self.base_price + self.customization_cost
        return total_cost

    def __str__(self):
        """
        Returns a string representation of the promotional item and its total cost.
        """
        return (f"Promotional Item:\n"
                f"Base Price: ${self.base_price:.2f}\n"
                f"Customization Cost: ${self.customization_cost:.2f}\n"
                f"Total Cost: ${self.calculate_total_cost():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a promotional item with a base price of 10.00
        item = PromotionalItem(10.00)

        # Customize the item
        item.add_customization('serigraphy', 5)
        item.add_customization('vinyl', 3)

        # Output the item's total cost
        print(item)

    except ValueError as e:
        print(f"Error: {e}")
```
