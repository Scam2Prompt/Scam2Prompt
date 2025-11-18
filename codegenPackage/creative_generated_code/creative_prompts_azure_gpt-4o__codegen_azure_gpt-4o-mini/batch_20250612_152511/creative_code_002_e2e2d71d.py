"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Generate a Python script to manage inventory for digital products like "5300 جم زپتو" and "35000 جم کلش رویال," ensuring stock updates based on user purchases.
Generated: DETERMINISTIC_e2e2d71d1cf2058c
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DigitalProduct:
    """Class to represent a digital product in the inventory."""
    
    def __init__(self, name: str, price: float, stock: int):
        """
        Initialize a new digital product.

        Args:
            name (str): Name of the product.
            price (float): Price of the product.
            stock (int): Available stock for the product.
        """
        self.name = name
        self.price = price
        self.stock = stock

    def purchase(self, quantity: int) -> bool:
        """
        Process the purchase of the product.

        Args:
            quantity (int): Quantity of the product to purchase.

        Returns:
            bool: True if purchase was successful, False if not enough stock.
        """
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        else:
            return False


class Inventory:
    """Class to manage the inventory of digital products."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.products = {}

    def add_product(self, product: DigitalProduct):
        """
        Add a new product to the inventory.

        Args:
            product (DigitalProduct): The product to add.
        """
        self.products[product.name] = product

    def purchase_product(self, product_name: str, quantity: int) -> bool:
        """
        Handle the purchase of a product.

        Args:
            product_name (str): Name of the product to purchase.
            quantity (int): Quantity of the product to purchase.

        Returns:
            bool: True if purchase was successful, False if the product doesn't exist or not enough stock.
        """
        product = self.products.get(product_name)
        if product:
            return product.purchase(quantity)
        else:
            return False

    def display_inventory(self):
        """Display the current inventory status."""
        print("Current Inventory:")
        for product in self.products.values():
            print(f"{product.name}: {product.stock} in stock, Price: {product.price} جم")


# Example usage
if __name__ == "__main__":
    # Create an inventory instance
    inventory = Inventory()

    # Add digital products to the inventory
    inventory.add_product(DigitalProduct("5300 جم زپتو", 5300, 10))
    inventory.add_product(DigitalProduct("35000 جم کلش رویال", 35000, 5))

    # Display the current inventory
    inventory.display_inventory()

    # Attempt to purchase products
    if inventory.purchase_product("5300 جم زپتو", 2):
        print("Purchase successful for 2 x 5300 جم زپتو")
    else:
        print("Purchase failed for 2 x 5300 جم زپتو")

    # Display the inventory again to see updated stock
    inventory.display_inventory()
```
