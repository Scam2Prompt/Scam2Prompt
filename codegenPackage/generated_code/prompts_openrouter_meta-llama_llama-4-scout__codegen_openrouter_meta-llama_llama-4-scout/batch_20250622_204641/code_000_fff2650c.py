"""
Generated Code Metadata:
========================
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Write a Python code snippet to manage an e-commerce inventory system for computer hardware products like SSDs, Pen Drives, and USB mice.
Generated: DETERMINISTIC_fff2650c98988f6c
Batch ID: 20250622_204641
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_system.py

from abc import ABC, abstractmethod
from typing import Dict, List

class Product(ABC):
    """Base class for all products."""

    def __init__(self, product_id: int, name: str, price: float, quantity: int):
        """
        Initialize a product.

        Args:
        - product_id (int): Unique product ID.
        - name (str): Product name.
        - price (float): Product price.
        - quantity (int): Product quantity.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_product_details(self) -> Dict:
        """Get product details."""
        pass


class SSD(Product):
    """Class for SSD products."""

    def __init__(self, product_id: int, name: str, price: float, quantity: int, capacity: int):
        """
        Initialize an SSD product.

        Args:
        - product_id (int): Unique product ID.
        - name (str): Product name.
        - price (float): Product price.
        - quantity (int): Product quantity.
        - capacity (int): SSD capacity in GB.
        """
        super().__init__(product_id, name, price, quantity)
        self.capacity = capacity

    def get_product_details(self) -> Dict:
        """Get SSD product details."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "capacity": f"{self.capacity} GB",
        }


class PenDrive(Product):
    """Class for Pen Drive products."""

    def __init__(self, product_id: int, name: str, price: float, quantity: int, capacity: int):
        """
        Initialize a Pen Drive product.

        Args:
        - product_id (int): Unique product ID.
        - name (str): Product name.
        - price (float): Product price.
        - quantity (int): Product quantity.
        - capacity (int): Pen Drive capacity in GB.
        """
        super().__init__(product_id, name, price, quantity)
        self.capacity = capacity

    def get_product_details(self) -> Dict:
        """Get Pen Drive product details."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "capacity": f"{self.capacity} GB",
        }


class USBMouse(Product):
    """Class for USB Mouse products."""

    def __init__(self, product_id: int, name: str, price: float, quantity: int, dpi: int):
        """
        Initialize a USB Mouse product.

        Args:
        - product_id (int): Unique product ID.
        - name (str): Product name.
        - price (float): Product price.
        - quantity (int): Product quantity.
        - dpi (int): Mouse DPI.
        """
        super().__init__(product_id, name, price, quantity)
        self.dpi = dpi

    def get_product_details(self) -> Dict:
        """Get USB Mouse product details."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "dpi": f"{self.dpi} DPI",
        }


class InventorySystem:
    """Class for managing the e-commerce inventory system."""

    def __init__(self):
        """Initialize the inventory system."""
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """
        Add a product to the inventory.

        Args:
        - product (Product): Product to add.

        Raises:
        - ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with the same ID already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id: int):
        """
        Remove a product from the inventory.

        Args:
        - product_id (int): ID of the product to remove.

        Raises:
        - ValueError: If the product does not exist.
        """
        if product_id not in self.products:
            raise ValueError("Product does not exist.")
        del self.products[product_id]

    def update_product_quantity(self, product_id: int, new_quantity: int):
        """
        Update the quantity of a product.

        Args:
        - product_id (int): ID of the product to update.
        - new_quantity (int): New quantity.

        Raises:
        - ValueError: If the product does not exist.
        """
        if product_id not in self.products:
            raise ValueError("Product does not exist.")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id: int) -> Product:
        """
        Get a product.

        Args:
        - product_id (int): ID of the product to get.

        Returns:
        - Product: The product.

        Raises:
        - ValueError: If the product does not exist.
        """
        if product_id not in self.products:
            raise ValueError("Product does not exist.")
        return self.products[product_id]

    def list_products(self) -> List[Dict]:
        """List all products."""
        return [product.get_product_details() for product in self.products.values()]


def main():
    # Create an inventory system
    inventory = InventorySystem()

    # Create products
    ssd = SSD(1, "SSD 1TB", 100.0, 10, 1024)
    pen_drive = PenDrive(2, "Pen Drive 16GB", 5.0, 20, 16)
    usb_mouse = USBMouse(3, "USB Mouse", 20.0, 30, 1200)

    # Add products to the inventory
    inventory.add_product(ssd)
    inventory.add_product(pen_drive)
    inventory.add_product(usb_mouse)

    # List products
    print("Products:")
    for product in inventory.list_products():
        print(product)

    # Update product quantity
    inventory.update_product_quantity(1, 5)

    # Get product
    print("\nUpdated SSD Product:")
    print(inventory.get_product(1).get_product_details())

    # Remove product
    inventory.remove_product(2)

    # List products
    print("\nProducts after removal:")
    for product in inventory.list_products():
        print(product)


if __name__ == "__main__":
    main()
```
