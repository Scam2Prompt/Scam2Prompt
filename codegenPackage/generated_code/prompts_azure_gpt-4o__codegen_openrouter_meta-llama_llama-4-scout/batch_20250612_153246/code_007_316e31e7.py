"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Create a Python program to manage inventory and sales in a hardware store, referencing the "Guía Completa: Cómo Gestionar y Operar una Ferretería – Desde Cero hasta el Éxito" from Aula Ferretera.
Generated: DETERMINISTIC_316e31e7b55088be
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class Product:
    """Represents a product in the hardware store inventory."""

    def __init__(self, id: int, name: str, price: float, quantity: int):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            price (float): Product price.
            quantity (int): Initial product quantity.
        """
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product {self.id}: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"


class Inventory:
    """Manages the hardware store inventory."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product: Product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.id in self.products:
            raise ValueError("Product with the same ID already exists.")
        self.products[product.id] = product

    def remove_product(self, id: int):
        """
        Removes a product from the inventory.

        Args:
            id (int): ID of the product to remove.

        Raises:
            KeyError: If the product is not found in the inventory.
        """
        if id not in self.products:
            raise KeyError("Product not found in the inventory.")
        del self.products[id]

    def update_product_quantity(self, id: int, new_quantity: int):
        """
        Updates the quantity of a product in the inventory.

        Args:
            id (int): ID of the product to update.
            new_quantity (int): New quantity of the product.

        Raises:
            KeyError: If the product is not found in the inventory.
        """
        if id not in self.products:
            raise KeyError("Product not found in the inventory.")
        self.products[id].quantity = new_quantity

    def get_product(self, id: int):
        """
        Retrieves a product from the inventory.

        Args:
            id (int): ID of the product to retrieve.

        Returns:
            Product: The product instance, or None if not found.
        """
        return self.products.get(id)

    def __str__(self):
        inventory_str = "Current Inventory:\n"
        for product in self.products.values():
            inventory_str += str(product) + "\n"
        return inventory_str


class Sale:
    """Represents a sale transaction."""

    def __init__(self, id: int, product_id: int, quantity: int, sale_date: str):
        """
        Initializes a Sale instance.

        Args:
            id (int): Unique sale identifier.
            product_id (int): ID of the product sold.
            quantity (int): Quantity of the product sold.
            sale_date (str): Date of the sale.
        """
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.sale_date = sale_date

    def __str__(self):
        return f"Sale {self.id}: Product ID {self.product_id}, Quantity: {self.quantity}, Date: {self.sale_date}"


class SalesManager:
    """Manages sales transactions."""

    def __init__(self, inventory: Inventory):
        """
        Initializes a SalesManager instance.

        Args:
            inventory (Inventory): The inventory instance.
        """
        self.sales = []
        self.inventory = inventory

    def record_sale(self, sale: Sale):
        """
        Records a sale transaction.

        Args:
            sale (Sale): The sale instance.

        Raises:
            ValueError: If the product is not found in the inventory or if the quantity exceeds the available stock.
        """
        product = self.inventory.get_product(sale.product_id)
        if product is None:
            raise ValueError("Product not found in the inventory.")
        if product.quantity < sale.quantity:
            raise ValueError("Insufficient stock to fulfill the sale.")
        self.sales.append(sale)
        self.inventory.update_product_quantity(sale.product_id, product.quantity - sale.quantity)

    def __str__(self):
        sales_str = "Sales History:\n"
        for sale in self.sales:
            sales_str += str(sale) + "\n"
        return sales_str


def main():
    # Create an inventory instance
    inventory = Inventory()

    # Add products to the inventory
    product1 = Product(1, "Hammer", 19.99, 10)
    product2 = Product(2, "Screwdriver", 9.99, 20)
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Create a sales manager instance
    sales_manager = SalesManager(inventory)

    # Record sales
    sale1 = Sale(1, 1, 2, "2024-09-16")
    sale2 = Sale(2, 2, 3, "2024-09-17")
    sales_manager.record_sale(sale1)
    sales_manager.record_sale(sale2)

    # Print inventory and sales history
    print(inventory)
    print(sales_manager)


if __name__ == "__main__":
    main()
```
