"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgendreau.fr
Prompt: How can I use LWS to create an e-commerce site? Provide code examples for setting up a shopping cart.
Generated: DETERMINISTIC_136deddc1810dba8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_cart.py

class ShoppingCart:
    """
    A class to represent a shopping cart for an e-commerce application.
    """

    def __init__(self):
        """
        Initializes a new shopping cart with an empty product list and total amount.
        """
        self.cart_items = {}
        self.total_amount = 0.0

    def add_item(self, product_id, product_name, price, quantity=1):
        """
        Adds a product to the shopping cart.

        :param product_id: Unique identifier for the product
        :param product_name: Name of the product
        :param price: Price of the product
        :param quantity: Quantity of the product to add
        :raises ValueError: If the price or quantity is negative
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be at least 1.")
        
        if product_id in self.cart_items:
            self.cart_items[product_id]['quantity'] += quantity
        else:
            self.cart_items[product_id] = {
                'name': product_name,
                'price': price,
                'quantity': quantity
            }
        
        self.update_total()

    def remove_item(self, product_id):
        """
        Removes a product from the shopping cart.

        :param product_id: Unique identifier for the product
        :raises KeyError: If the product ID does not exist in the cart
        """
        if product_id not in self.cart_items:
            raise KeyError("Product ID not found in the cart.")
        
        del self.cart_items[product_id]
        self.update_total()

    def update_total(self):
        """
        Updates the total amount for the shopping cart.
        """
        self.total_amount = sum(item['price'] * item['quantity'] for item in self.cart_items.values())

    def get_cart_items(self):
        """
        Returns a list of items in the cart.

        :return: A dictionary of cart items
        """
        return self.cart_items

    def get_total_amount(self):
        """
        Returns the total amount of the shopping cart.

        :return: Total amount as a float
        """
        return self.total_amount

    def clear_cart(self):
        """
        Clears all items from the shopping cart.
        """
        self.cart_items.clear()
        self.total_amount = 0.0


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    
    try:
        # Adding items to the cart
        cart.add_item(product_id=1, product_name="Laptop", price=999.99, quantity=1)
        cart.add_item(product_id=2, product_name="Mouse", price=19.99, quantity=2)
        
        # Displaying cart items and total amount
        print("Cart Items:", cart.get_cart_items())
        print("Total Amount:", cart.get_total_amount())

        # Removing an item from the cart
        cart.remove_item(product_id=2)
        print("Cart Items after removal:", cart.get_cart_items())
        print("Total Amount after removal:", cart.get_total_amount())

        # Clear the cart
        cart.clear_cart()
        print("Cart Items after clearing:", cart.get_cart_items())
    
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
