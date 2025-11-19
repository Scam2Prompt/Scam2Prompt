"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: "Develop a basic inventory management system for tracking Lando Parafusos products, including Parafuso Cabeça de Martelo and Porcas."
Generated: DETERMINISTIC_8cefa2f904a7c05d
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management_system.py

class Product:
    """Base class for all products."""

    def __init__(self, product_id, name, quantity):
        """
        Initialize a Product.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            quantity (int): Initial quantity of the product.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Quantity: {self.quantity}"


class ParafusoCabeçaDeMartelo(Product):
    """Parafuso Cabeça de Martelo product."""

    def __init__(self, product_id, quantity, size):
        """
        Initialize a Parafuso Cabeça de Martelo product.

        Args:
            product_id (int): Unique identifier for the product.
            quantity (int): Initial quantity of the product.
            size (str): Size of the parafuso.
        """
        super().__init__(product_id, "Parafuso Cabeça de Martelo", quantity)
        self.size = size

    def __str__(self):
        return super().__str__() + f", Size: {self.size}"


class Porca(Product):
    """Porca product."""

    def __init__(self, product_id, quantity, material):
        """
        Initialize a Porca product.

        Args:
            product_id (int): Unique identifier for the product.
            quantity (int): Initial quantity of the product.
            material (str): Material of the porca.
        """
        super().__init__(product_id, "Porca", quantity)
        self.material = material

    def __str__(self):
        return super().__str__() + f", Material: {self.material}"


class Inventory:
    """Inventory management system."""

    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with the same ID already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Remove a product from the inventory.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product does not exist.")
        del self.products[product_id]

    def update_quantity(self, product_id, new_quantity):
        """
        Update the quantity of a product.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If the product does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product does not exist.")
        self.products[product_id].quantity = new_quantity

    def __str__(self):
        inventory_str = "Inventory:\n"
        for product in self.products.values():
            inventory_str += str(product) + "\n"
        return inventory_str


def main():
    # Create an inventory
    inventory = Inventory()

    try:
        # Create products
        parafuso = ParafusoCabeçaDeMartelo(1, 100, "M10")
        porca = Porca(2, 50, "Steel")

        # Add products to the inventory
        inventory.add_product(parafuso)
        inventory.add_product(porca)

        # Print the inventory
        print(inventory)

        # Update quantity
        inventory.update_quantity(1, 80)

        # Print the updated inventory
        print("\nUpdated Inventory:")
        print(inventory)

        # Remove a product
        inventory.remove_product(2)

        # Print the updated inventory
        print("\nUpdated Inventory after removal:")
        print(inventory)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
