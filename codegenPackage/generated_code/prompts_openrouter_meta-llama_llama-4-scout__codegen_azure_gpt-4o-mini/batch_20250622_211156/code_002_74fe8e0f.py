"""
Generated Code Metadata:
========================
Original URL: https://rhinoag.com
Prompt: "Generate code to calculate the cost savings of purchasing RhinoAg equipment with up to $1,000 off and a 10-year limited gearbox warranty."
Generated: DETERMINISTIC_74fe8e0f297ac4e7
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RhinoAgEquipment:
    """
    A class to represent RhinoAg equipment and calculate cost savings.
    """

    def __init__(self, original_price: float, discount: float = 1000.0):
        """
        Initializes the RhinoAgEquipment with the original price and discount.

        :param original_price: The original price of the equipment.
        :param discount: The discount amount (default is $1,000).
        """
        if original_price < 0:
            raise ValueError("Original price must be a non-negative value.")
        if discount < 0:
            raise ValueError("Discount must be a non-negative value.")

        self.original_price = original_price
        self.discount = discount

    def calculate_discounted_price(self) -> float:
        """
        Calculates the discounted price after applying the discount.

        :return: The price after discount.
        """
        discounted_price = self.original_price - self.discount
        return max(discounted_price, 0)  # Ensure price does not go below zero

    def calculate_cost_savings(self) -> float:
        """
        Calculates the cost savings from purchasing the equipment.

        :return: The cost savings amount.
        """
        savings = self.discount
        return savings

    def display_equipment_info(self):
        """
        Displays the information about the equipment and cost savings.
        """
        discounted_price = self.calculate_discounted_price()
        savings = self.calculate_cost_savings()

        print(f"Original Price: ${self.original_price:.2f}")
        print(f"Discount: ${self.discount:.2f}")
        print(f"Discounted Price: ${discounted_price:.2f}")
        print(f"Total Cost Savings: ${savings:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of RhinoAgEquipment with an original price
        equipment = RhinoAgEquipment(original_price=5000.0)
        # Display the equipment information and cost savings
        equipment.display_equipment_info()
    except ValueError as e:
        print(f"Error: {e}")
```
