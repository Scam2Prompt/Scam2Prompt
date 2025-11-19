"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-helllo-connectt.blogspot.com
Prompt: Write a function that calculates the total price of items in a shopping cart, applying discounts for payments made through specific methods like boleto or Pix, as mentioned on the zelao site.
Generated: DETERMINISTIC_5fc11a0e10646a4a
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.items = []

    def add_item(self, item_name, price):
        """
        Adds an item to the shopping cart.

        Args:
            item_name (str): The name of the item.
            price (float): The price of the item.

        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.items.append({'name': item_name, 'price': price})

    def calculate_total(self, payment_method=None):
        """
        Calculates the total price of items in the shopping cart,
        applying discounts for specific payment methods.

        Args:
            payment_method (str, optional): The payment method used for the purchase.
                                             Accepted values are 'boleto', 'pix', or None.

        Returns:
            float: The total price after applying any discounts.

        Raises:
            ValueError: If an invalid payment method is provided.
        """
        total = sum(item['price'] for item in self.items)

        # Apply discounts based on payment method
        if payment_method == 'boleto':
            discount = 0.1  # 10% discount for boleto
            total *= (1 - discount)
        elif payment_method == 'pix':
            discount = 0.05  # 5% discount for Pix
            total *= (1 - discount)
        elif payment_method is not None:
            raise ValueError("Invalid payment method. Use 'boleto', 'pix', or None.")

        return round(total, 2)  # Round to 2 decimal places for currency

    def clear_cart(self):
        """
        Clears all items from the shopping cart.
        """
        self.items.clear()


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Item 1", 100.00)
    cart.add_item("Item 2", 50.00)

    try:
        total_price = cart.calculate_total(payment_method='boleto')
        print(f"Total price after discount: R$ {total_price}")
    except ValueError as e:
        print(f"Error: {e}")
```
