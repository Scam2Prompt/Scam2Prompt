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
# shopping_cart.py

class ShoppingCart:
    """
    A class to represent a Shopping Cart.

    Attributes:
        items (dict): Stores items in the cart with their quantities.
        discount_codes (dict): Stores valid discount codes and their respective discount percentages.
    """
    
    def __init__(self):
        """Initialize an empty shopping cart and discount codes."""
        self.items = {}
        self.discount_codes = {
            'WELCOME5': 0.05  # 5% discount for first-time users
        }

    def add_item(self, item_name, price, quantity=1):
        """
        Add an item to the shopping cart.

        Args:
            item_name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The number of items to add (default is 1).
        """
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity=1):
        """
        Remove an item from the shopping cart.

        Args:
            item_name (str): The name of the item.
            quantity (int): The number of items to remove (default is 1).

        Raises:
            ValueError: If the item is not in the cart or quantity is invalid.
        """
        if item_name not in self.items:
            raise ValueError(f"Item '{item_name}' is not in the cart.")
        
        if self.items[item_name]['quantity'] < quantity:
            raise ValueError(f"Cannot remove {quantity} '{item_name}'. Only {self.items[item_name]['quantity']} available.")
        
        self.items[item_name]['quantity'] -= quantity
        
        # Remove item entirely if quantity becomes 0
        if self.items[item_name]['quantity'] == 0:
            del self.items[item_name]

    def apply_discount_code(self, code):
        """
        Apply a discount code to the total price.

        Args:
            code (str): The discount code.

        Returns:
            float: The discounted total price.

        Raises:
            ValueError: If the discount code is invalid.
        """
        if code not in self.discount_codes:
            raise ValueError(f"Invalid discount code '{code}'.")
        
        discount_percentage = self.discount_codes[code]
        total_price = self.calculate_total_price()
        return total_price * (1 - discount_percentage)

    def calculate_total_price(self):
        """
        Calculate the total price of the items in the cart.

        Returns:
            float: The total price.
        """
        return sum(item['price'] * item['quantity'] for item in self.items.values())

    def view_cart(self):
        """
        View the contents of the shopping cart.

        Returns:
            dict: The items in the cart with their details.
        """
        return self.items


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Gold Necklace", 500.00, 1)
    cart.add_item("Silver Bracelet", 150.00, 2)
    print("Cart contents:", cart.view_cart())
    print("Total price:", cart.calculate_total_price())

    # Apply discount code
    try:
        discounted_price = cart.apply_discount_code("WELCOME5")
        print("Discounted price:", discounted_price)
    except ValueError as e:
        print(e)

    # Remove an item from the cart
    try:
        cart.remove_item("Silver Bracelet", 1)
        print("Cart contents after removal:", cart.view_cart())
    except ValueError as e:
        print(e)
```
