"""
Generated Code Metadata:
========================
Original URL: https://govindsweets.com
Prompt: Generate a Python script to create an online ordering system for sweets and bakery products similar to those offered by Govind Sweets, including categories like Mava Mithai and Namkeen.
Generated: DETERMINISTIC_6e990229ffc86a61
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# online_ordering_system.py

class Product:
    """Represents a product in the online ordering system."""

    def __init__(self, id, name, category, price, quantity):
        """
        Initializes a Product object.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            category (str): Product category (e.g., Mava Mithai, Namkeen).
            price (float): Product price.
            quantity (int): Available quantity.
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

class Order:
    """Represents a customer's order."""

    def __init__(self, id, customer_name):
        """
        Initializes an Order object.

        Args:
            id (int): Unique order ID.
            customer_name (str): Customer name.
        """
        self.id = id
        self.customer_name = customer_name
        self.items = []

    def add_item(self, product, quantity):
        """
        Adds a product to the order.

        Args:
            product (Product): Product to add.
            quantity (int): Quantity to add.

        Raises:
            ValueError: If quantity exceeds available product quantity.
        """
        if quantity > product.quantity:
            raise ValueError("Insufficient quantity available.")
        self.items.append((product, quantity))

    def calculate_total(self):
        """
        Calculates the total cost of the order.

        Returns:
            float: Total cost.
        """
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

class OnlineOrderingSystem:
    """Represents the online ordering system."""

    def __init__(self):
        """Initializes the online ordering system."""
        self.products = []
        self.orders = []
        self.product_id_counter = 1
        self.order_id_counter = 1

    def add_product(self, name, category, price, quantity):
        """
        Adds a product to the system.

        Args:
            name (str): Product name.
            category (str): Product category.
            price (float): Product price.
            quantity (int): Available quantity.
        """
        product = Product(self.product_id_counter, name, category, price, quantity)
        self.products.append(product)
        self.product_id_counter += 1

    def place_order(self, customer_name):
        """
        Creates a new order.

        Args:
            customer_name (str): Customer name.

        Returns:
            Order: The newly created order.
        """
        order = Order(self.order_id_counter, customer_name)
        self.orders.append(order)
        self.order_id_counter += 1
        return order

    def display_products(self):
        """
        Displays all available products.
        """
        print("Available Products:")
        for product in self.products:
            print(f"ID: {product.id}, Name: {product.name}, Category: {product.category}, Price: {product.price}, Quantity: {product.quantity}")

    def display_orders(self):
        """
        Displays all orders.
        """
        print("Orders:")
        for order in self.orders:
            print(f"Order ID: {order.id}, Customer Name: {order.customer_name}")
            for product, quantity in order.items:
                print(f"  - {product.name} x {quantity}")

def main():
    system = OnlineOrderingSystem()

    # Add products
    system.add_product("Mava Mithai", "Mava Mithai", 10.99, 100)
    system.add_product("Namkeen Mix", "Namkeen", 5.99, 50)
    system.add_product("Gajar Ka Halwa", "Mava Mithai", 7.99, 200)

    while True:
        print("\n1. Display Products")
        print("2. Place Order")
        print("3. Display Orders")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            system.display_products()
        elif choice == "2":
            customer_name = input("Enter customer name: ")
            order = system.place_order(customer_name)
            while True:
                system.display_products()
                product_id = int(input("Enter product ID to add: "))
                product = next((p for p in system.products if p.id == product_id), None)
                if product:
                    quantity = int(input("Enter quantity: "))
                    try:
                        order.add_item(product, quantity)
                    except ValueError as e:
                        print(e)
                else:
                    print("Product not found.")
                cont = input("Add another item? (y/n): ")
                if cont.lower() != "y":
                    break
            print(f"Order total: {order.calculate_total()}")
        elif choice == "3":
            system.display_orders()
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
```
