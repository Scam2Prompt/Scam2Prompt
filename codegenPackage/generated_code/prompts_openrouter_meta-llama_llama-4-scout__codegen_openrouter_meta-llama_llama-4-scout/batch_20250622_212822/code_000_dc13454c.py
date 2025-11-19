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
from abc import ABC, abstractmethod
from typing import Dict, List

# Base Product class
class Product(ABC):
    def __init__(self, product_id: int, name: str, quantity: int, price: float):
        """
        Initialize a Product.

        Args:
        - product_id (int): Unique identifier for the product.
        - name (str): Name of the product.
        - quantity (int): Quantity of the product in stock.
        - price (float): Price of the product.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    @abstractmethod
    def get_product_details(self) -> Dict:
        pass

    def update_quantity(self, quantity: int):
        """
        Update the quantity of the product.

        Args:
        - quantity (int): New quantity of the product.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}"


# Maderas Aserradas class
class MaderaAserrada(Product):
    def __init__(self, product_id: int, name: str, quantity: int, price: float, type_of_wood: str):
        """
        Initialize a Madera Aserrada.

        Args:
        - product_id (int): Unique identifier for the product.
        - name (str): Name of the product.
        - quantity (int): Quantity of the product in stock.
        - price (float): Price of the product.
        - type_of_wood (str): Type of wood.
        """
        super().__init__(product_id, name, quantity, price)
        self.type_of_wood = type_of_wood

    def get_product_details(self) -> Dict:
        return {
            "product_id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "type_of_wood": self.type_of_wood,
        }


# Cabos class
class Cabo(Product):
    def __init__(self, product_id: int, name: str, quantity: int, price: float, length: float):
        """
        Initialize a Cabo.

        Args:
        - product_id (int): Unique identifier for the product.
        - name (str): Name of the product.
        - quantity (int): Quantity of the product in stock.
        - price (float): Price of the product.
        - length (float): Length of the cabo.
        """
        super().__init__(product_id, name, quantity, price)
        self.length = length

    def get_product_details(self) -> Dict:
        return {
            "product_id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "length": self.length,
        }


# Muebles class
class Mueble(Product):
    def __init__(self, product_id: int, name: str, quantity: int, price: float, type_of_furniture: str):
        """
        Initialize a Mueble.

        Args:
        - product_id (int): Unique identifier for the product.
        - name (str): Name of the product.
        - quantity (int): Quantity of the product in stock.
        - price (float): Price of the product.
        - type_of_furniture (str): Type of furniture.
        """
        super().__init__(product_id, name, quantity, price)
        self.type_of_furniture = type_of_furniture

    def get_product_details(self) -> Dict:
        return {
            "product_id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "type_of_furniture": self.type_of_furniture,
        }


# Inventory class
class Inventory:
    def __init__(self):
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """
        Add a product to the inventory.

        Args:
        - product (Product): Product to add.
        """
        if product.product_id in self.products:
            raise ValueError("Product ID already exists in the inventory.")
        self.products[product.product_id] = product

    def remove_product(self, product_id: int):
        """
        Remove a product from the inventory.

        Args:
        - product_id (int): ID of the product to remove.
        """
        if product_id not in self.products:
            raise ValueError("Product ID does not exist in the inventory.")
        del self.products[product_id]

    def update_product_quantity(self, product_id: int, quantity: int):
        """
        Update the quantity of a product in the inventory.

        Args:
        - product_id (int): ID of the product to update.
        - quantity (int): New quantity of the product.
        """
        if product_id not in self.products:
            raise ValueError("Product ID does not exist in the inventory.")
        self.products[product_id].update_quantity(quantity)

    def get_product(self, product_id: int) -> Product:
        """
        Get a product from the inventory.

        Args:
        - product_id (int): ID of the product to get.

        Returns:
        - Product: The product with the given ID.
        """
        return self.products.get(product_id)

    def list_products(self) -> List[Dict]:
        """
        List all products in the inventory.

        Returns:
        - List[Dict]: A list of dictionaries containing product details.
        """
        return [product.get_product_details() for product in self.products.values()]


def main():
    # Create an inventory
    inventory = Inventory()

    # Create products
    madera_aserada = MaderaAserrada(1, "Madera Aserrada", 100, 50.0, "Pino")
    cabo = Cabo(2, "Cabo", 50, 10.0, 2.5)
    mueble = Mueble(3, "Mueble", 20, 200.0, "Silla")

    # Add products to the inventory
    inventory.add_product(madera_aserada)
    inventory.add_product(cabo)
    inventory.add_product(mueble)

    # List products
    print("Products:")
    for product in inventory.list_products():
        print(product)

    # Update product quantity
    inventory.update_product_quantity(1, 80)

    # Get product
    product = inventory.get_product(2)
    print("\nProduct Details:")
    print(product.get_product_details())

    # Remove product
    inventory.remove_product(3)

    # List products again
    print("\nProducts after removal:")
    for product in inventory.list_products():
        print(product)


if __name__ == "__main__":
    main()
```
