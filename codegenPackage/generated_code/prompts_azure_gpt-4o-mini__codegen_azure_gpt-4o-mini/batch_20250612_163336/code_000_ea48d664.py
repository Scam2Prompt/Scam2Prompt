"""
Generated Code Metadata:
========================
Original URL: https://startec.com.my
Prompt: Generate a code snippet for a simple inventory management system that could help a computer hardware retailer like StarTec Computer System Sdn Bhd manage their products effectively.
Generated: DETERMINISTIC_ea48d6649a5d8b55
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """Class to represent a product in the inventory."""
    
    def __init__(self, product_id, name, quantity, price):
        """
        Initialize a new product.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param quantity: Quantity of the product in stock
        :param price: Price of the product
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        """
        Update the quantity of the product.

        :param amount: Amount to add (positive) or remove (negative) from stock
        :raises ValueError: If the resulting quantity is negative
        """
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity += amount

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name} (ID: {self.product_id}) - Quantity: {self.quantity}, Price: ${self.price:.2f}"


class Inventory:
    """Class to manage the inventory of products."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Add a new product to the inventory.

        :param product: Product object to add
        :raises ValueError: If the product ID already exists
        """
        if product.product_id in self.products:
            raise ValueError("Product ID already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Remove a product from the inventory.

        :param product_id: Unique identifier of the product to remove
        :raises KeyError: If the product ID does not exist
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist.")
        del self.products[product_id]

    def update_product_quantity(self, product_id, amount):
        """
        Update the quantity of a product in the inventory.

        :param product_id: Unique identifier of the product
        :param amount: Amount to add (positive) or remove (negative)
        :raises KeyError: If the product ID does not exist
        :raises ValueError: If the resulting quantity is negative
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist.")
        self.products[product_id].update_quantity(amount)

    def list_products(self):
        """Return a list of all products in the inventory."""
        return [str(product) for product in self.products.values()]


# Example usage
if __name__ == "__main__":
    inventory = Inventory()

    # Adding products
    try:
        inventory.add_product(Product(1, "Gaming Laptop", 10, 1500.00))
        inventory.add_product(Product(2, "Mechanical Keyboard", 25, 100.00))
        inventory.add_product(Product(3, "Gaming Mouse", 15, 50.00))
    except ValueError as e:
        print(f"Error adding product: {e}")

    # Listing products
    print("Current Inventory:")
    for product in inventory.list_products():
        print(product)

    # Updating product quantity
    try:
        inventory.update_product_quantity(1, -2)  # Sell 2 Gaming Laptops
        inventory.update_product_quantity(2, 5)   # Restock 5 Mechanical Keyboards
    except (KeyError, ValueError) as e:
        print(f"Error updating product quantity: {e}")

    # Listing products after updates
    print("\nUpdated Inventory:")
    for product in inventory.list_products():
        print(product)

    # Removing a product
    try:
        inventory.remove_product(3)  # Remove Gaming Mouse
    except KeyError as e:
        print(f"Error removing product: {e}")

    # Final inventory listing
    print("\nFinal Inventory:")
    for product in inventory.list_products():
        print(product)
```
