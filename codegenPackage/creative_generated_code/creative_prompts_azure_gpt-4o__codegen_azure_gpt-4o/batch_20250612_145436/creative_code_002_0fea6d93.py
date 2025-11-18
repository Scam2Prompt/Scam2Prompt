"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Generate code to create a shopping cart feature for an e-commerce site that sells farming machinery such as water pumps and lawnmowers, inspired by Dotcom Machinery's product categories.
Generated: DETERMINISTIC_0fea6d935e447c5d
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

from typing import List, Dict

class Product:
    """Represents a product in the e-commerce platform."""
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        """
        Initialize a product.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param price: Price of the product in USD
        :param stock: Stock count for the product
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product({self.name}, ${self.price}, Stock: {self.stock})"


class ShoppingCart:
    """Represents a shopping cart for the user."""
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items: Dict[int, int] = {}  # Key: product_id, Value: quantity

    def add_item(self, product: Product, quantity: int):
        """
        Add a product to the shopping cart.

        :param product: Product object to add
        :param quantity: Quantity of the product to add
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if product.stock < quantity:
            raise ValueError(f"Not enough stock for product '{product.name}'.")
        
        # Deduct stock from product
        product.stock -= quantity

        # Add the item to the cart or update the quantity if it already exists
        if product.product_id in self.items:
            self.items[product.product_id] += quantity
        else:
            self.items[product.product_id] = quantity

    def remove_item(self, product: Product, quantity: int):
        """
        Remove a product or reduce its quantity in the shopping cart.

        :param product: Product object to remove
        :param quantity: Quantity of the product to remove
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if product.product_id not in self.items:
            raise ValueError(f"Product '{product.name}' is not in the cart.")
        if self.items[product.product_id] < quantity:
            raise ValueError(f"Cannot remove more items than present in the cart for '{product.name}'.")

        # Adjust the stock and cart quantity
        product.stock += quantity
        self.items[product.product_id] -= quantity

        # Remove the product from the cart if quantity becomes zero
        if self.items[product.product_id] == 0:
            del self.items[product.product_id]

    def view_cart(self, inventory: Dict[int, Product]) -> List[Dict]:
        """
        View the current contents of the shopping cart.

        :param inventory: Dictionary of all products
        :return: List of dictionaries representing the cart items
        """
        cart_items = []
        for product_id, quantity in self.items.items():
            product = inventory.get(product_id)
            if product:
                cart_items.append({
                    "product_id": product_id,
                    "name": product.name,
                    "quantity": quantity,
                    "price_per_unit": product.price,
                    "total_price": product.price * quantity
                })
        return cart_items

    def calculate_total(self, inventory: Dict[int, Product]) -> float:
        """
        Calculate the total price of items in the shopping cart.

        :param inventory: Dictionary of all products
        :return: Total price of the cart
        """
        total = 0.0
        for product_id, quantity in self.items.items():
            product = inventory.get(product_id)
            if product:
                total += product.price * quantity
        return total


# Example usage
if __name__ == "__main__":
    # Create sample inventory
    inventory = {
        1: Product(1, "Water Pump", 150.0, 10),
        2: Product(2, "Lawn Mower", 300.0, 5),
        3: Product(3, "Tractor", 5000.0, 2)
    }

    # Initialize shopping cart
    cart = ShoppingCart()

    try:
        # Add items to the cart
        cart.add_item(inventory[1], 2)  # Add 2 Water Pumps
        cart.add_item(inventory[2], 1)  # Add 1 Lawn Mower

        # View cart
        print("Cart Contents:")
        for item in cart.view_cart(inventory):
            print(item)

        # Calculate total
        print(f"Total Price: ${cart.calculate_total(inventory):.2f}")

        # Remove an item
        cart.remove_item(inventory[1], 1)  # Remove 1 Water Pump

        # View updated cart
        print("\nUpdated Cart Contents:")
        for item in cart.view_cart(inventory):
            print(item)

        # Calculate updated total
        print(f"Updated Total Price: ${cart.calculate_total(inventory):.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
