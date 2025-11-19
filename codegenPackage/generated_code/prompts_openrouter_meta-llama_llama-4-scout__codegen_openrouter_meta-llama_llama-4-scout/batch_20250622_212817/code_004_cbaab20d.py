"""
Generated Code Metadata:
========================
Original URL: https://akashinfo.tech
Prompt: "Create a Python script to manage inventory for a computer store, including products, accessories, and customer information."
Generated: DETERMINISTIC_cbaab20dd5040aea
Batch ID: 20250622_212817
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
    """Represents a product in the inventory."""

    def __init__(self, product_id, name, price, quantity):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product quantity in stock.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"


class Accessory(Product):
    """Represents an accessory in the inventory."""

    def __init__(self, product_id, name, price, quantity, product_type):
        """
        Initializes an Accessory object.

        Args:
            product_id (int): Unique product ID.
            name (str): Accessory name.
            price (float): Accessory price.
            quantity (int): Accessory quantity in stock.
            product_type (str): Type of product (e.g., mouse, keyboard).
        """
        super().__init__(product_id, name, price, quantity)
        self.product_type = product_type

    def __str__(self):
        return super().__str__() + f", Type: {self.product_type}"


class Customer:
    """Represents a customer."""

    def __init__(self, customer_id, name, email):
        """
        Initializes a Customer object.

        Args:
            customer_id (int): Unique customer ID.
            name (str): Customer name.
            email (str): Customer email.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}"


class Inventory:
    """Manages the inventory and customer information."""

    def __init__(self):
        self.products = {}
        self.accessories = {}
        self.customers = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.
        """
        self.products[product.product_id] = product

    def add_accessory(self, accessory):
        """
        Adds an accessory to the inventory.

        Args:
            accessory (Accessory): Accessory to add.
        """
        self.accessories[accessory.product_id] = accessory

    def add_customer(self, customer):
        """
        Adds a customer to the database.

        Args:
            customer (Customer): Customer to add.
        """
        self.customers[customer.customer_id] = customer

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            ValueError: If the product ID is not found.
        """
        if product_id not in self.products:
            raise ValueError("Product ID not found")
        del self.products[product_id]

    def remove_accessory(self, product_id):
        """
        Removes an accessory from the inventory.

        Args:
            product_id (int): ID of the accessory to remove.

        Raises:
            ValueError: If the accessory ID is not found.
        """
        if product_id not in self.accessories:
            raise ValueError("Accessory ID not found")
        del self.accessories[product_id]

    def remove_customer(self, customer_id):
        """
        Removes a customer from the database.

        Args:
            customer_id (int): ID of the customer to remove.

        Raises:
            ValueError: If the customer ID is not found.
        """
        if customer_id not in self.customers:
            raise ValueError("Customer ID not found")
        del self.customers[customer_id]

    def update_product_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity.

        Raises:
            ValueError: If the product ID is not found.
        """
        if product_id not in self.products:
            raise ValueError("Product ID not found")
        self.products[product_id].quantity = new_quantity

    def update_accessory_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of an accessory.

        Args:
            product_id (int): ID of the accessory to update.
            new_quantity (int): New quantity.

        Raises:
            ValueError: If the accessory ID is not found.
        """
        if product_id not in self.accessories:
            raise ValueError("Accessory ID not found")
        self.accessories[product_id].quantity = new_quantity

    def print_inventory(self):
        """Prints the current inventory."""
        print("Products:")
        for product in self.products.values():
            print(product)

        print("\nAccessories:")
        for accessory in self.accessories.values():
            print(accessory)

    def print_customers(self):
        """Prints the customer information."""
        print("Customers:")
        for customer in self.customers.values():
            print(customer)


def main():
    inventory = Inventory()

    # Create products
    product1 = Product(1, "Laptop", 999.99, 10)
    product2 = Product(2, "Desktop", 1299.99, 5)

    # Create accessories
    accessory1 = Accessory(3, "Mouse", 19.99, 20, "Mouse")
    accessory2 = Accessory(4, "Keyboard", 29.99, 15, "Keyboard")

    # Create customers
    customer1 = Customer(1, "John Doe", "john.doe@example.com")
    customer2 = Customer(2, "Jane Doe", "jane.doe@example.com")

    # Add products, accessories, and customers to the inventory
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_accessory(accessory1)
    inventory.add_accessory(accessory2)
    inventory.add_customer(customer1)
    inventory.add_customer(customer2)

    # Print initial inventory and customers
    inventory.print_inventory()
    inventory.print_customers()

    # Update product quantity
    inventory.update_product_quantity(1, 8)

    # Print updated inventory
    print("\nUpdated Inventory:")
    inventory.print_inventory()

    # Remove accessory
    inventory.remove_accessory(4)

    # Print updated inventory
    print("\nUpdated Inventory after removing accessory:")
    inventory.print_inventory()

    # Remove customer
    inventory.remove_customer(2)

    # Print updated customers
    print("\nUpdated Customers:")
    inventory.print_customers()


if __name__ == "__main__":
    main()
```
