"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Develop a function that calculates the total cost for a builder's order of keypads, deadbolts, and door accessories based on specific budget allowances.
Generated: DETERMINISTIC_4dfe4ce02a723a09
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class OrderCalculator:
    """
    A class to calculate the total cost of a builder's order for keypads, deadbolts, and door accessories.
    """

    def __init__(self):
        # Initialize the price list for each item type
        self.price_list = {
            'keypad': 50.00,      # Price per keypad
            'deadbolt': 75.00,    # Price per deadbolt
            'accessory': 10.00     # Price per accessory
        }

    def calculate_total_cost(self, keypads: int, deadbolts: int, accessories: int) -> float:
        """
        Calculate the total cost of the order based on the quantities of each item.

        :param keypads: Number of keypads ordered
        :param deadbolts: Number of deadbolts ordered
        :param accessories: Number of accessories ordered
        :return: Total cost of the order
        :raises ValueError: If any quantity is negative
        """
        # Validate input quantities
        if keypads < 0 or deadbolts < 0 or accessories < 0:
            raise ValueError("Quantities cannot be negative.")

        # Calculate total cost
        total_cost = (keypads * self.price_list['keypad'] +
                      deadbolts * self.price_list['deadbolt'] +
                      accessories * self.price_list['accessory'])
        
        return total_cost

    def display_order_summary(self, keypads: int, deadbolts: int, accessories: int) -> None:
        """
        Display a summary of the order including item quantities and total cost.

        :param keypads: Number of keypads ordered
        :param deadbolts: Number of deadbolts ordered
        :param accessories: Number of accessories ordered
        """
        try:
            total_cost = self.calculate_total_cost(keypads, deadbolts, accessories)
            print("Order Summary:")
            print(f"Keypads: {keypads} x ${self.price_list['keypad']:.2f} = ${keypads * self.price_list['keypad']:.2f}")
            print(f"Deadbolts: {deadbolts} x ${self.price_list['deadbolt']:.2f} = ${deadbolts * self.price_list['deadbolt']:.2f}")
            print(f"Accessories: {accessories} x ${self.price_list['accessory']:.2f} = ${accessories * self.price_list['accessory']:.2f}")
            print(f"Total Cost: ${total_cost:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    calculator = OrderCalculator()
    calculator.display_order_summary(keypads=3, deadbolts=2, accessories=5)
```
