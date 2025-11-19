"""
Generated Code Metadata:
========================
Original URL: https://gegetastycakes-353.pages.dev
Prompt: "Write a script to determine the total cost of a specialty cake order with a 2-week notice period and an additional $25 convenience fee for rush orders."
Generated: DETERMINISTIC_4ac373fac93512fa
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CakeOrder:
    def __init__(self, base_price, rush_order=False):
        """
        Initialize a CakeOrder instance.

        :param base_price: float, the base price of the cake
        :param rush_order: bool, indicates if the order is a rush order
        """
        self.base_price = base_price
        self.rush_order = rush_order
        self.convenience_fee = 25.00  # Fixed convenience fee for rush orders

    def calculate_total_cost(self):
        """
        Calculate the total cost of the cake order.

        :return: float, total cost including any applicable fees
        """
        total_cost = self.base_price
        if self.rush_order:
            total_cost += self.convenience_fee
        return total_cost

def main():
    """
    Main function to execute the cake order calculation.
    """
    try:
        # Input: base price of the cake
        base_price = float(input("Enter the base price of the cake: $"))
        
        # Input: whether the order is a rush order
        rush_order_input = input("Is this a rush order? (yes/no): ").strip().lower()
        rush_order = rush_order_input == 'yes'

        # Create a CakeOrder instance
        order = CakeOrder(base_price, rush_order)

        # Calculate and display the total cost
        total_cost = order.calculate_total_cost()
        print(f"The total cost of your cake order is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number for the base price.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
