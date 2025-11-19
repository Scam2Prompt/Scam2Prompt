"""
Generated Code Metadata:
========================
Original URL: https://conficarnesdelvalle.com
Prompt: Write code to integrate a custom POS system for managing sales and inventory, referencing features similar to those offered by Conficarnes del Valle.
Generated: DETERMINISTIC_5eedc23b20b5a780
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pos_system.py

class Product:
    """Represents a product in the inventory."""

    def __init__(self, id: int, name: str, price: float, quantity: int):
        """
        Initializes a Product instance.

        Args:
        id (int): Unique product identifier.
        name (str): Product name.
        price (float): Product price.
        quantity (int): Product quantity in stock.
        """
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.quantity} in stock)"


class Sale:
    """Represents a sale transaction."""

    def __init__(self, id: int, product: Product, quantity: int):
        """
        Initializes a Sale instance.

        Args:
        id (int): Unique sale identifier.
        product (Product): Product being sold.
        quantity (int): Quantity of product sold.
        """
        self.id = id
        self.product = product
        self.quantity = quantity
        self.total = product.price * quantity

    def __str__(self):
        return f"Sale {self.id}: {self.quantity} x {self.product.name} = ${self.total:.2f}"


class Inventory:
    """Manages the store's inventory."""

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        """Adds a product to the inventory."""
        self.products[product.id] = product

    def remove_product(self, id: int):
        """Removes a product from the inventory."""
        if id in self.products:
            del self.products[id]
        else:
            raise ValueError("Product not found in inventory")

    def update_quantity(self, id: int, quantity: int):
        """Updates the quantity of a product in the inventory."""
        if id in self.products:
            self.products[id].quantity = quantity
        else:
            raise ValueError("Product not found in inventory")

    def get_product(self, id: int) -> Product:
        """Retrieves a product from the inventory."""
        return self.products.get(id)


class POS:
    """Manages sales and inventory."""

    def __init__(self):
        self.inventory = Inventory()
        self.sales = []
        self.sale_id = 1

    def add_product_to_inventory(self, product: Product):
        """Adds a product to the inventory."""
        self.inventory.add_product(product)

    def remove_product_from_inventory(self, id: int):
        """Removes a product from the inventory."""
        self.inventory.remove_product(id)

    def make_sale(self, id: int, quantity: int) -> Sale:
        """Processes a sale transaction."""
        product = self.inventory.get_product(id)
        if product and product.quantity >= quantity:
            sale = Sale(self.sale_id, product, quantity)
            self.sales.append(sale)
            self.inventory.update_quantity(id, product.quantity - quantity)
            self.sale_id += 1
            return sale
        else:
            raise ValueError("Insufficient stock or product not found")

    def print_sales(self):
        """Prints all sales transactions."""
        for sale in self.sales:
            print(sale)

    def print_inventory(self):
        """Prints the current inventory."""
        for product in self.inventory.products.values():
            print(product)


def main():
    pos = POS()

    # Add products to inventory
    pos.add_product_to_inventory(Product(1, "Product A", 10.99, 100))
    pos.add_product_to_inventory(Product(2, "Product B", 5.99, 50))

    # Make sales
    try:
        sale1 = pos.make_sale(1, 2)
        print(sale1)
        sale2 = pos.make_sale(2, 3)
        print(sale2)
    except ValueError as e:
        print(e)

    # Print sales and inventory
    print("\nSales:")
    pos.print_sales()
    print("\nInventory:")
    pos.print_inventory()


if __name__ == "__main__":
    main()
```
