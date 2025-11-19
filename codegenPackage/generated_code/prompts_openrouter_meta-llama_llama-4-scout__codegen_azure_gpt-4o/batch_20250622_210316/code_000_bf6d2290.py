"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: "Write a Python code snippet to manage inventory of refractory products, including bricks, mortars, and ceramic fibers, with attributes like product name, quantity, and temperature resistance."
Generated: DETERMINISTIC_bf6d2290ee2bb3a9
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class Product:
    """
    Represents a refractory product with attributes for name, quantity, and temperature resistance.
    """
    def __init__(self, name: str, quantity: int, temperature_resistance: int):
        """
        Initialize a Product instance.

        :param name: Name of the product
        :param quantity: Quantity of the product in stock
        :param temperature_resistance: Maximum temperature resistance of the product in Celsius
        """
        self.name = name
        self.quantity = quantity
        self.temperature_resistance = temperature_resistance

    def __str__(self):
        """
        String representation of the product.
        """
        return f"{self.name} - Quantity: {self.quantity}, Temp Resistance: {self.temperature_resistance}°C"


class Inventory:
    """
    Manages the inventory of refractory products.
    """
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.products = {}

    def add_product(self, product: Product):
        """
        Add a product to the inventory. If the product already exists, update its quantity.

        :param product: Product instance to add
        """
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product

    def remove_product(self, product_name: str, quantity: int):
        """
        Remove a specified quantity of a product from the inventory.

        :param product_name: Name of the product to remove
        :param quantity: Quantity to remove
        :raises ValueError: If the product does not exist or insufficient quantity is available
        """
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not found in inventory.")
        
        product = self.products[product_name]
        if product.quantity < quantity:
            raise ValueError(f"Insufficient quantity of '{product_name}' in inventory.")
        
        product.quantity -= quantity
        if product.quantity == 0:
            del self.products[product_name]  # Remove product if quantity reaches zero

    def list_products(self):
        """
        List all products in the inventory.

        :return: List of product details
        """
        if not self.products:
            return "Inventory is empty."
        return "\n".join(str(product) for product in self.products.values())

    def find_product(self, product_name: str):
        """
        Find a product by name.

        :param product_name: Name of the product to find
        :return: Product instance if found, else None
        """
        return self.products.get(product_name, None)


# Example usage
if __name__ == "__main__":
    try:
        # Create inventory instance
        inventory = Inventory()

        # Add products to inventory
        inventory.add_product(Product("Fire Brick", 100, 1500))
        inventory.add_product(Product("Ceramic Fiber Blanket", 50, 1200))
        inventory.add_product(Product("Refractory Mortar", 200, 1600))

        # List all products
        print("Current Inventory:")
        print(inventory.list_products())

        # Remove some products
        inventory.remove_product("Fire Brick", 20)
        print("\nAfter removing 20 Fire Bricks:")
        print(inventory.list_products())

        # Find a specific product
        product = inventory.find_product("Ceramic Fiber Blanket")
        if product:
            print("\nFound Product:")
            print(product)
        else:
            print("\nProduct not found.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
