"""
Generated Code Metadata:
========================
Original URL: https://maderaselaboradas.com.ar
Prompt: Write a Python code snippet to manage inventory for a wood products company like Maderas Elaboradas, including classes for different types of products (e.g., Maderas Aserradas, Cabos, Muebles).
Generated: DETERMINISTIC_dc13454c73126e80
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

# Import necessary modules
from typing import List

# Base class for all products
class Product:
    """
    Base class representing a generic product in the inventory.
    """
    def __init__(self, name: str, product_id: int, quantity: int, price_per_unit: float):
        """
        Initialize a product with basic attributes.
        :param name: Name of the product
        :param product_id: Unique identifier for the product
        :param quantity: Quantity of the product in stock
        :param price_per_unit: Price per unit of the product
        """
        self.name = name
        self.product_id = product_id
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def update_quantity(self, amount: int):
        """
        Update the quantity of the product in stock.
        :param amount: Amount to add (positive) or remove (negative) from stock
        """
        if self.quantity + amount < 0:
            raise ValueError("Insufficient stock to complete the operation.")
        self.quantity += amount

    def calculate_total_value(self) -> float:
        """
        Calculate the total value of the product in stock.
        :return: Total value of the product
        """
        return self.quantity * self.price_per_unit

    def __str__(self):
        """
        String representation of the product.
        """
        return f"Product(name={self.name}, id={self.product_id}, quantity={self.quantity}, price_per_unit={self.price_per_unit})"


# Subclass for Maderas Aserradas
class MaderasAserradas(Product):
    """
    Represents Maderas Aserradas (Sawn Wood) products.
    """
    def __init__(self, name: str, product_id: int, quantity: int, price_per_unit: float, wood_type: str):
        """
        Initialize a Maderas Aserradas product with additional attributes.
        :param wood_type: Type of wood (e.g., pine, oak)
        """
        super().__init__(name, product_id, quantity, price_per_unit)
        self.wood_type = wood_type

    def __str__(self):
        """
        String representation of the Maderas Aserradas product.
        """
        return f"MaderasAserradas(name={self.name}, id={self.product_id}, quantity={self.quantity}, price_per_unit={self.price_per_unit}, wood_type={self.wood_type})"


# Subclass for Cabos
class Cabos(Product):
    """
    Represents Cabos (Wood Handles) products.
    """
    def __init__(self, name: str, product_id: int, quantity: int, price_per_unit: float, length: float):
        """
        Initialize a Cabos product with additional attributes.
        :param length: Length of the wood handle in centimeters
        """
        super().__init__(name, product_id, quantity, price_per_unit)
        self.length = length

    def __str__(self):
        """
        String representation of the Cabos product.
        """
        return f"Cabos(name={self.name}, id={self.product_id}, quantity={self.quantity}, price_per_unit={self.price_per_unit}, length={self.length} cm)"


# Subclass for Muebles
class Muebles(Product):
    """
    Represents Muebles (Furniture) products.
    """
    def __init__(self, name: str, product_id: int, quantity: int, price_per_unit: float, material: str):
        """
        Initialize a Muebles product with additional attributes.
        :param material: Material used for the furniture (e.g., wood, metal)
        """
        super().__init__(name, product_id, quantity, price_per_unit)
        self.material = material

    def __str__(self):
        """
        String representation of the Muebles product.
        """
        return f"Muebles(name={self.name}, id={self.product_id}, quantity={self.quantity}, price_per_unit={self.price_per_unit}, material={self.material})"


# Inventory class to manage all products
class Inventory:
    """
    Class to manage the inventory of products.
    """
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Add a product to the inventory.
        :param product: Product instance to add
        """
        self.products.append(product)

    def remove_product(self, product_id: int):
        """
        Remove a product from the inventory by its ID.
        :param product_id: ID of the product to remove
        """
        self.products = [product for product in self.products if product.product_id != product_id]

    def get_product(self, product_id: int) -> Product:
        """
        Retrieve a product from the inventory by its ID.
        :param product_id: ID of the product to retrieve
        :return: Product instance
        """
        for product in self.products:
            if product.product_id == product_id:
                return product
        raise ValueError(f"Product with ID {product_id} not found.")

    def calculate_inventory_value(self) -> float:
        """
        Calculate the total value of all products in the inventory.
        :return: Total inventory value
        """
        return sum(product.calculate_total_value() for product in self.products)

    def __str__(self):
        """
        String representation of the inventory.
        """
        return f"Inventory({', '.join(str(product) for product in self.products)})"


# Example usage
if __name__ == "__main__":
    try:
        # Create inventory instance
        inventory = Inventory()

        # Add products to inventory
        inventory.add_product(MaderasAserradas("Pine Plank", 1, 50, 12.5, "Pine"))
        inventory.add_product(Cabos("Wood Handle", 2, 100, 3.0, 120))
        inventory.add_product(Muebles("Wooden Chair", 3, 20, 45.0, "Oak"))

        # Print inventory
        print(inventory)

        # Update product quantity
        product = inventory.get_product(1)
        product.update_quantity(-10)  # Remove 10 units
        print(f"Updated product: {product}")

        # Calculate total inventory value
        print(f"Total inventory value: ${inventory.calculate_inventory_value():.2f}")

    except Exception as e:
        print(f"Error: {e}")
```
