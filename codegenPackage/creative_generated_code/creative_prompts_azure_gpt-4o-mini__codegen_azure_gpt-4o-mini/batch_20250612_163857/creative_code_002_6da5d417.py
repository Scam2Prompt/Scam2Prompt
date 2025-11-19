"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flaviadossantos.co
Prompt: How can I implement a shopping cart feature that includes the "Huk Icon Hoodie - Men's Night Owl" and calculates the total price?
Generated: DETERMINISTIC_6da5d417b5fa0d43
Batch ID: 20250612_163857
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
        """Initialize an empty shopping cart."""
        self.cart = {}
        self.total_price = 0.0

    def add_item(self, item_name, price, quantity=1):
        """Add an item to the shopping cart.

        Args:
            item_name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item to add.

        Raises:
            ValueError: If the price is negative or quantity is less than 1.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        # Add item to the cart or update the quantity if it already exists
        if item_name in self.cart:
            self.cart[item_name]['quantity'] += quantity
        else:
            self.cart[item_name] = {'price': price, 'quantity': quantity}

        # Recalculate total price
        self.update_total_price()

    def update_total_price(self):
        """Update the total price of the shopping cart based on items added."""
        self.total_price = sum(item['price'] * item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Get the total price of the shopping cart.

        Returns:
            float: The total price of the shopping cart.
        """
        return self.total_price

    def show_cart(self):
        """Display the current items in the shopping cart."""
        if not self.cart:
            print("Shopping cart is empty.")
        else:
            print("Shopping Cart Contents:")
            for item, details in self.cart.items():
                print(f"{item}: {details['quantity']} x ${details['price']} = ${details['quantity'] * details['price']:.2f}")
            print(f"Total Price: ${self.total_price:.2f}")


# Example usage:
if __name__ == "__main__":
    try:
        hoodie_name = "Huk Icon Hoodie - Men's Night Owl"
        hoodie_price = 49.99
        cart = ShoppingCart()
        
        # Add items to the cart
        cart.add_item(hoodie_name, hoodie_price, quantity=2)
        
        # Show the cart and total price
        cart.show_cart()
        
    except ValueError as e:
        print(f"Error: {e}")
```
