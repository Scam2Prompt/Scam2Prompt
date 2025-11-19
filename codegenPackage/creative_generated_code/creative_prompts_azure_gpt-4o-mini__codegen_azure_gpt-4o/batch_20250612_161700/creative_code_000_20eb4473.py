"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://utterlybaked.com
Prompt: Generate a code snippet for an online ordering system that offers discounts, similar to the 50% OFF promotion mentioned on utterlybaked.com.
Generated: DETERMINISTIC_20eb447371df3cb8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
import datetime

class OnlineOrderingSystem:
    """
    A class representing an online ordering system that applies
    discounts to orders, including a 50% OFF promotion.
    """

    def __init__(self):
        """
        Initializes the ordering system with a catalog of items.
        """
        self.catalog = {
            "Chocolate Cake": 20.0,   # Price in USD
            "Vanilla Muffin": 5.0,    # Price in USD
            "Berry Tart": 12.0        # Price in USD
        }
        self.orders = []  # Stores placed orders

    def calculate_discount(self, total, discount_percentage):
        """
        Calculate the discount amount based on the given percentage.

        :param total: The total price of the order before discount
        :param discount_percentage: Discount percentage to apply
        :return: Discounted price
        """
        try:
            if discount_percentage < 0 or discount_percentage > 100:
                raise ValueError("Discount percentage must be between 0 and 100.")
            return total * (1 - discount_percentage / 100)
        except Exception as e:
            print(f"Error calculating discount: {e}")
            return total

    def place_order(self, items, discount_percentage=0):
        """
        Places an order with an optional discount.

        :param items: List of item names ordered
        :param discount_percentage: Discount percentage to apply (default: 0)
        :return: Order summary
        """
        try:
            # Validate that all items exist in the catalog
            for item in items:
                if item not in self.catalog:
                    raise ValueError(f"Item '{item}' not found in catalog.")

            # Calculate total price
            total_price = sum([self.catalog[item] for item in items])

            # Apply discount
            final_price = self.calculate_discount(total_price, discount_percentage)

            # Record order
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            order_details = {
                "items": items,
                "total_price": total_price,
                "final_price": final_price,
                "timestamp": timestamp
            }
            self.orders.append(order_details)

            # Return order summary
            return order_details

        except Exception as e:
            print(f"Error placing order: {e}")
            return None

    def get_order_history(self):
        """
        Retrieve the history of all placed orders.

        :return: List of all orders
        """
        return self.orders


# Example usage:
if __name__ == "__main__":
    # Create an instance of the ordering system
    system = OnlineOrderingSystem()

    # Place an order with a 50% OFF discount
    order = system.place_order(["Chocolate Cake", "Vanilla Muffin"], discount_percentage=50)

    # Print order summary
    if order:
        print("Order Summary:")
        print(order)

    # Retrieve and print order history
    print("\nOrder History:")
    for history in system.get_order_history():
        print(history)
```
