"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Generate a code snippet to create a shopping cart feature for an online jewelry store similar to Malkeenz, including functionalities for adding items, removing items, and applying discount codes like "WELCOME5".
Generated: DETERMINISTIC_b0b179db096c382e
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    """
    A class to represent a shopping cart for an online jewelry store.
    """

    def __init__(self):
        """
        Initializes a new instance of ShoppingCart.
        """
        self.items = {}  # Dictionary to hold cart items and their quantities.
        self.discount_code = None  # Stores the applied discount code.
        self.discount_value = 0  # Stores the discount value.

    def add_item(self, item_name, price, quantity=1):
        """
        Adds an item to the shopping cart.

        :param item_name: Name of the item to add.
        :param price: Price of the item.
        :param quantity: Quantity of the item to add, defaults to 1.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name):
        """
        Removes an item from the shopping cart.

        :param item_name: Name of the item to remove.
        """
        if item_name in self.items:
            del self.items[item_name]
        else:
            raise KeyError(f"Item '{item_name}' not found in the cart.")

    def apply_discount(self, code):
        """
        Applies a discount code to the shopping cart.

        :param code: Discount code to apply.
        """
        valid_discount_codes = {
            'WELCOME5': 5,  # 5% discount
            'SUMMER10': 10,  # 10% discount
        }
        
        if code in valid_discount_codes:
            self.discount_code = code
            self.discount_value = valid_discount_codes[code]
        else:
            raise ValueError("Invalid discount code.")

    def calculate_total(self):
        """
        Calculates the total price of the items in the cart, applying any discounts.

        :return: Total price after applying discounts.
        """
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        
        if self.discount_value > 0:
            discount_amount = (total * self.discount_value) / 100
            total -= discount_amount
        
        return total

    def clear_cart(self):
        """
        Clears all items from the shopping cart.
        """
        self.items.clear()
        self.discount_code = None
        self.discount_value = 0

    def __str__(self):
        """
        Returns a string representation of the shopping cart's contents.

        :return: List of items in the cart.
        """
        return f"Shopping Cart: {self.items}, Total: {self.calculate_total()}"

# Example usage:
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Gold Necklace", 150.00, 1)
    cart.add_item("Silver Ring", 50.00, 2)
    print(cart)  # Display cart contents and total

    cart.apply_discount("WELCOME5")
    print(cart)  # Display cart contents and total after discount
    
    cart.remove_item("Silver Ring")
    print(cart)  # Display cart contents after removing an item
```
