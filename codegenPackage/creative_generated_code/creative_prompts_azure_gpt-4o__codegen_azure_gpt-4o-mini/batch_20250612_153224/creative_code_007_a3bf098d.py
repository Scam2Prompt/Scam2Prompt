"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fanzyfashion.in
Prompt: Write code to implement a "Free Shipping" feature for orders above a specified amount (e.g., ₹1999) in an e-commerce checkout system.
Generated: DETERMINISTIC_a3bf098dad14460a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Order:
    def __init__(self, items, shipping_threshold=1999):
        """
        Initializes an Order instance.

        :param items: List of tuples representing items and their prices, e.g., [(item_name, price), ...]
        :param shipping_threshold: Minimum order amount for free shipping
        """
        self.items = items
        self.shipping_threshold = shipping_threshold

    def calculate_total(self):
        """
        Calculates the total price of the items in the order.

        :return: Total price of the items
        """
        total = sum(price for _, price in self.items)
        return total

    def is_free_shipping(self):
        """
        Determines if the order qualifies for free shipping.

        :return: True if the total price is above the shipping threshold, else False
        """
        total = self.calculate_total()
        return total >= self.shipping_threshold

    def get_order_summary(self):
        """
        Provides a summary of the order including total price and shipping cost.

        :return: A dictionary with total price and shipping cost
        """
        total = self.calculate_total()
        shipping_cost = 0 if self.is_free_shipping() else 50  # Flat shipping cost if not eligible for free shipping
        return {
            'total_price': total,
            'shipping_cost': shipping_cost,
            'final_amount': total + shipping_cost
        }


def main():
    """
    Main function to demonstrate the Order class functionality.
    """
    # Example order items
    items = [
        ("Item A", 500),
        ("Item B", 1200),
        ("Item C", 600)  # Total: 2300, eligible for free shipping
    ]
    
    try:
        order = Order(items)
        summary = order.get_order_summary()

        print("Order Summary:")
        print(f"Total Price: ₹{summary['total_price']}")
        print(f"Shipping Cost: ₹{summary['shipping_cost']}")
        print(f"Final Amount: ₹{summary['final_amount']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
