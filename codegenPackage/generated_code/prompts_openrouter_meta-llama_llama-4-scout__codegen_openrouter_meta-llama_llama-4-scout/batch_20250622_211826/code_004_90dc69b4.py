"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: "Implement a simple point of sale system with electronic invoicing and inventory control using a programming language of your choice, inspired by TICOM SOFTWARE's solutions."
Generated: DETERMINISTIC_90dc69b49808c5a5
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# point_of_sale.py

class Product:
    """Represents a product in the inventory."""

    def __init__(self, id: int, name: str, price: float, quantity: int):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            quantity (int): Initial product quantity.
        """
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (ID: {self.id}, Price: ${self.price:.2f}, Quantity: {self.quantity})"


class Inventory:
    """Manages the store's inventory."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product: Product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.
        """
        self.products[product.id] = product

    def remove_product(self, product_id: int):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            ValueError: If the product ID is not found in the inventory.
        """
        if product_id not in self.products:
            raise ValueError(f"Product ID {product_id} not found in inventory")
        del self.products[product_id]

    def update_quantity(self, product_id: int, new_quantity: int):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity of the product.

        Raises:
            ValueError: If the product ID is not found in the inventory.
        """
        if product_id not in self.products:
            raise ValueError(f"Product ID {product_id} not found in inventory")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product from the inventory.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product instance, or None if not found.
        """
        return self.products.get(product_id)


class Invoice:
    """Represents an electronic invoice."""

    def __init__(self, invoice_id: int, date: str):
        """
        Initializes an Invoice instance.

        Args:
            invoice_id (int): Unique invoice ID.
            date (str): Invoice date (YYYY-MM-DD).
        """
        self.invoice_id = invoice_id
        self.date = date
        self.items = []

    def add_item(self, product: Product, quantity: int):
        """
        Adds an item to the invoice.

        Args:
            product (Product): Product instance.
            quantity (int): Quantity of the product.
        """
        self.items.append((product, quantity))

    def calculate_total(self) -> float:
        """
        Calculates the total cost of the invoice.

        Returns:
            float: Total cost.
        """
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

    def __str__(self):
        invoice_str = f"Invoice ID: {self.invoice_id}, Date: {self.date}\n"
        for product, quantity in self.items:
            invoice_str += f"- {product.name} x {quantity} = ${product.price * quantity:.2f}\n"
        invoice_str += f"Total: ${self.calculate_total():.2f}"
        return invoice_str


class PointOfSale:
    """Manages the point of sale system."""

    def __init__(self):
        """Initializes the point of sale system."""
        self.inventory = Inventory()
        self.invoices = {}

    def create_invoice(self, invoice_id: int, date: str) -> Invoice:
        """
        Creates a new invoice.

        Args:
            invoice_id (int): Unique invoice ID.
            date (str): Invoice date (YYYY-MM-DD).

        Returns:
            Invoice: The new invoice instance.
        """
        invoice = Invoice(invoice_id, date)
        self.invoices[invoice_id] = invoice
        return invoice

    def add_product_to_invoice(self, invoice_id: int, product_id: int, quantity: int):
        """
        Adds a product to an invoice.

        Args:
            invoice_id (int): ID of the invoice.
            product_id (int): ID of the product.
            quantity (int): Quantity of the product.

        Raises:
            ValueError: If the invoice ID or product ID is not found.
        """
        if invoice_id not in self.invoices:
            raise ValueError(f"Invoice ID {invoice_id} not found")
        product = self.inventory.get_product(product_id)
        if product is None:
            raise ValueError(f"Product ID {product_id} not found in inventory")
        if product.quantity < quantity:
            raise ValueError(f"Insufficient quantity of product {product_id} in inventory")
        self.invoices[invoice_id].add_item(product, quantity)
        self.inventory.update_quantity(product_id, product.quantity - quantity)

    def print_invoice(self, invoice_id: int):
        """
        Prints an invoice.

        Args:
            invoice_id (int): ID of the invoice.

        Raises:
            ValueError: If the invoice ID is not found.
        """
        if invoice_id not in self.invoices:
            raise ValueError(f"Invoice ID {invoice_id} not found")
        print(self.invoices[invoice_id])


def main():
    pos = PointOfSale()

    # Create products
    product1 = Product(1, "Product A", 10.99, 100)
    product2 = Product(2, "Product B", 5.99, 50)

    # Add products to inventory
    pos.inventory.add_product(product1)
    pos.inventory.add_product(product2)

    # Create invoice
    invoice = pos.create_invoice(1, "2024-09-16")

    # Add products to invoice
    pos.add_product_to_invoice(1, 1, 2)
    pos.add_product_to_invoice(1, 2, 3)

    # Print invoice
    pos.print_invoice(1)


if __name__ == "__main__":
    main()
```
