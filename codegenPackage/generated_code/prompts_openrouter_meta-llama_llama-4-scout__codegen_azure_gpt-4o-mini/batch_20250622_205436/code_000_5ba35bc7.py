"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Write a Python script to manage inventory for a menuiserie distribution company like Distribution Menuiserie, including classes for products (e.g., Fenêtres, Portes, Volets) and methods for tracking stock levels."
Generated: DETERMINISTIC_5ba35bc78ec29057
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """
    A class to represent a product in the inventory.

    Attributes:
    ----------
    name : str
        The name of the product.
    stock : int
        The current stock level of the product.
    price : float
        The price of the product.

    Methods:
    -------
    add_stock(amount: int):
        Increases the stock level by the specified amount.
    remove_stock(amount: int):
        Decreases the stock level by the specified amount, ensuring it doesn't go negative.
    get_stock() -> int:
        Returns the current stock level.
    get_price() -> float:
        Returns the price of the product.
    """

    def __init__(self, name: str, stock: int, price: float):
        self.name = name
        self.stock = stock
        self.price = price

    def add_stock(self, amount: int):
        """Increase the stock level by the specified amount."""
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        self.stock += amount

    def remove_stock(self, amount: int):
        """Decrease the stock level by the specified amount."""
        if amount < 0:
            raise ValueError("Amount to remove must be non-negative.")
        if amount > self.stock:
            raise ValueError("Cannot remove more stock than available.")
        self.stock -= amount

    def get_stock(self) -> int:
        """Return the current stock level."""
        return self.stock

    def get_price(self) -> float:
        """Return the price of the product."""
        return self.price


class Inventory:
    """
    A class to manage the inventory of products.

    Attributes:
    ----------
    products : dict
        A dictionary to hold products with their names as keys.

    Methods:
    -------
    add_product(product: Product):
        Adds a new product to the inventory.
    remove_product(name: str):
        Removes a product from the inventory by name.
    update_stock(name: str, amount: int):
        Updates the stock level of a product by name.
    get_product_stock(name: str) -> int:
        Returns the stock level of a product by name.
    list_products() -> dict:
        Returns a dictionary of all products in the inventory.
    """

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        """Add a new product to the inventory."""
        if product.name in self.products:
            raise ValueError("Product already exists in inventory.")
        self.products[product.name] = product

    def remove_product(self, name: str):
        """Remove a product from the inventory by name."""
        if name not in self.products:
            raise KeyError("Product not found in inventory.")
        del self.products[name]

    def update_stock(self, name: str, amount: int):
        """Update the stock level of a product by name."""
        if name not in self.products:
            raise KeyError("Product not found in inventory.")
        if amount < 0:
            self.products[name].remove_stock(-amount)
        else:
            self.products[name].add_stock(amount)

    def get_product_stock(self, name: str) -> int:
        """Return the stock level of a product by name."""
        if name not in self.products:
            raise KeyError("Product not found in inventory.")
        return self.products[name].get_stock()

    def list_products(self) -> dict:
        """Return a dictionary of all products in the inventory."""
        return {name: product.get_stock() for name, product in self.products.items()}


# Example usage
if __name__ == "__main__":
    try:
        # Create an inventory instance
        inventory = Inventory()

        # Create some products
        window = Product("Fenêtres", 10, 150.0)
        door = Product("Portes", 5, 200.0)
        shutter = Product("Volets", 20, 75.0)

        # Add products to inventory
        inventory.add_product(window)
        inventory.add_product(door)
        inventory.add_product(shutter)

        # Update stock
        inventory.update_stock("Fenêtres", 5)  # Add 5 windows
        inventory.update_stock("Portes", -2)   # Remove 2 doors

        # List current inventory
        print("Current Inventory:", inventory.list_products())

    except Exception as e:
        print(f"An error occurred: {e}")
```
