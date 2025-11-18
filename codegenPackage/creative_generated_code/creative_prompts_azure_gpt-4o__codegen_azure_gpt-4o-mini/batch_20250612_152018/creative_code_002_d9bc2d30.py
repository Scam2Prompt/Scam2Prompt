"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Create a script to calculate shipping costs for promotional items based on the free shipping threshold of Rp. 10,000,000 mentioned on the Merchandiso website.
Generated: DETERMINISTIC_d9bc2d30705a1acd
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCalculator:
    """
    A class to calculate shipping costs for promotional items based on the 
    free shipping threshold.
    """

    FREE_SHIPPING_THRESHOLD = 10000000  # Free shipping threshold in Rp
    SHIPPING_COST_PER_ITEM = 50000       # Shipping cost per item in Rp

    def __init__(self):
        """
        Initializes the ShippingCalculator class.
        """
        pass

    def calculate_shipping_cost(self, total_amount: float, num_items: int) -> float:
        """
        Calculate the total shipping cost based on the total amount and number of items.

        Parameters:
        total_amount (float): The total amount of the order in Rp.
        num_items (int): The number of items being ordered.

        Returns:
        float: The total shipping cost in Rp.
        """

        # Validate inputs
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative.")
        if num_items < 0:
            raise ValueError("Number of items cannot be negative.")

        # Check if the order qualifies for free shipping
        if total_amount >= self.FREE_SHIPPING_THRESHOLD:
            return 0.0  # Free shipping

        # Calculate shipping cost based on the number of items
        shipping_cost = num_items * self.SHIPPING_COST_PER_ITEM
        return shipping_cost

    def display_shipping_cost(self, total_amount: float, num_items: int):
        """
        Display the shipping cost based on the inputs.

        Parameters:
        total_amount (float): The total amount of the order in Rp.
        num_items (int): The number of items being ordered.
        """

        try:
            shipping_cost = self.calculate_shipping_cost(total_amount, num_items)
            print(f"Total Amount: Rp. {total_amount}")
            print(f"Number of Items: {num_items}")
            print(f"Shipping Cost: Rp. {shipping_cost}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    calculator = ShippingCalculator()
    
    # Sample data
    total_amount = 9000000  # Example total amount in Rp
    num_items = 3           # Example number of items

    # Display the shipping cost
    calculator.display_shipping_cost(total_amount, num_items)
```
