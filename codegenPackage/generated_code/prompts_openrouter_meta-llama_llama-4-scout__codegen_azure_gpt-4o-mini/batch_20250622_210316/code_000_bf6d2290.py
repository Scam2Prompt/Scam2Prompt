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
class RefractoryProduct:
    """
    A class to represent a refractory product in the inventory.
    
    Attributes:
        name (str): The name of the product.
        quantity (int): The quantity of the product in stock.
        temperature_resistance (float): The maximum temperature resistance of the product in degrees Celsius.
    """

    def __init__(self, name: str, quantity: int, temperature_resistance: float):
        """
        Initializes a new instance of RefractoryProduct.

        Args:
            name (str): The name of the product.
            quantity (int): The quantity of the product in stock.
            temperature_resistance (float): The maximum temperature resistance of the product.
        """
        self.name = name
        self.quantity = quantity
        self.temperature_resistance = temperature_resistance

    def update_quantity(self, amount: int):
        """
        Updates the quantity of the product.

        Args:
            amount (int): The amount to add (positive) or remove (negative) from the inventory.

        Raises:
            ValueError: If the resulting quantity is negative.
        """
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity += amount

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name}: {self.quantity} units, {self.temperature_resistance}°C resistance"


class Inventory:
    """
    A class to manage an inventory of refractory products.
    
    Attributes:
        products (dict): A dictionary to store products with their names as keys.
    """

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product: RefractoryProduct):
        """
        Adds a new product to the inventory.

        Args:
            product (RefractoryProduct): The product to add.

        Raises:
            ValueError: If the product already exists in the inventory.
        """
        if product.name in self.products:
            raise ValueError("Product already exists in the inventory.")
        self.products[product.name] = product

    def update_product_quantity(self, product_name: str, amount: int):
        """
        Updates the quantity of a specified product.

        Args:
            product_name (str): The name of the product to update.
            amount (int): The amount to add (positive) or remove (negative).

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if product_name not in self.products:
            raise KeyError("Product not found in the inventory.")
        self.products[product_name].update_quantity(amount)

    def get_product_info(self, product_name: str) -> str:
        """
        Retrieves information about a specified product.

        Args:
            product_name (str): The name of the product to retrieve.

        Returns:
            str: Information about the product.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if product_name not in self.products:
            raise KeyError("Product not found in the inventory.")
        return str(self.products[product_name])

    def list_products(self):
        """Lists all products in the inventory."""
        return [str(product) for product in self.products.values()]


# Example usage
if __name__ == "__main__":
    try:
        # Create an inventory instance
        inventory = Inventory()

        # Create some refractory products
        brick = RefractoryProduct("Fire Brick", 100, 1600.0)
        mortar = RefractoryProduct("Refractory Mortar", 50, 1400.0)
        fiber = RefractoryProduct("Ceramic Fiber", 200, 1200.0)

        # Add products to the inventory
        inventory.add_product(brick)
        inventory.add_product(mortar)
        inventory.add_product(fiber)

        # Update product quantities
        inventory.update_product_quantity("Fire Brick", -10)
        inventory.update_product_quantity("Refractory Mortar", 5)

        # Print product information
        print(inventory.get_product_info("Fire Brick"))
        print(inventory.get_product_info("Refractory Mortar"))

        # List all products
        print("All products in inventory:")
        print(inventory.list_products())

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
