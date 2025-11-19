"""
Generated Code Metadata:
========================
Original URL: https://blueseanice.com
Prompt: Write a Python script to manage a simple product catalog for a K-Beauty online store.
Generated: DETERMINISTIC_55bb5c72adcfee50
Batch ID: 20250622_210017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

class Product:
    """Represents a product in the catalog."""

    def __init__(self, product_id, name, description, price, stock_quantity):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            stock_quantity (int): Quantity of the product in stock.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}, Stock Quantity: {self.stock_quantity}"


class ProductCatalog:
    """Manages a catalog of products."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the catalog.

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
        Removes a product from the catalog.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            ValueError: If the product ID does not exist in the catalog.
        """
        if product_id not in self.products:
            raise ValueError("Product ID does not exist in the catalog.")
        del self.products[product_id]

    def update_product(self, product_id, name=None, description=None, price=None, stock_quantity=None):
        """
        Updates a product in the catalog.

        Args:
            product_id (int): ID of the product to update.
            name (str, optional): New product name. Defaults to None.
            description (str, optional): New product description. Defaults to None.
            price (float, optional): New product price. Defaults to None.
            stock_quantity (int, optional): New stock quantity. Defaults to None.

        Raises:
            ValueError: If the product ID does not exist in the catalog.
        """
        if product_id not in self.products:
            raise ValueError("Product ID does not exist in the catalog.")
        product = self.products[product_id]
        if name:
            product.name = name
        if description:
            product.description = description
        if price:
            product.price = price
        if stock_quantity:
            product.stock_quantity = stock_quantity

    def get_product(self, product_id):
        """
        Retrieves a product from the catalog.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product object, or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the catalog."""
        return list(self.products.values())


def main():
    catalog = ProductCatalog()

    while True:
        print("\nProduct Catalog Management")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product")
        print("4. Get Product")
        print("5. List Products")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                product_id = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                description = input("Enter product description: ")
                price = float(input("Enter product price: "))
                stock_quantity = int(input("Enter stock quantity: "))
                product = Product(product_id, name, description, price, stock_quantity)
                catalog.add_product(product)
                print("Product added successfully.")
            elif choice == "2":
                product_id = int(input("Enter product ID to remove: "))
                catalog.remove_product(product_id)
                print("Product removed successfully.")
            elif choice == "3":
                product_id = int(input("Enter product ID to update: "))
                name = input("Enter new product name (press Enter to skip): ")
                description = input("Enter new product description (press Enter to skip): ")
                price = input("Enter new product price (press Enter to skip): ")
                stock_quantity = input("Enter new stock quantity (press Enter to skip): ")
                catalog.update_product(
                    product_id,
                    name or None,
                    description or None,
                    float(price) if price else None,
                    int(stock_quantity) if stock_quantity else None,
                )
                print("Product updated successfully.")
            elif choice == "4":
                product_id = int(input("Enter product ID to retrieve: "))
                product = catalog.get_product(product_id)
                if product:
                    print(product)
                else:
                    print("Product not found.")
            elif choice == "5":
                products = catalog.list_products()
                for product in products:
                    print(product)
            elif choice == "6":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
