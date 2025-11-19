"""
Generated Code Metadata:
========================
Original URL: https://azuharu.net
Prompt: Write a script to manage laptop rental inventory and customer orders, inspired by the "Sewa Laptop Surabaya" article on Azuharu.net.
Generated: DETERMINISTIC_b9128a4b9d00b31e
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# laptop_rental.py

class Laptop:
    """Represents a laptop in the rental inventory."""

    def __init__(self, laptop_id, brand, model, rental_price):
        """
        Initializes a Laptop object.

        Args:
            laptop_id (int): Unique identifier for the laptop.
            brand (str): Laptop brand.
            model (str): Laptop model.
            rental_price (float): Daily rental price.
        """
        self.laptop_id = laptop_id
        self.brand = brand
        self.model = model
        self.rental_price = rental_price
        self.is_available = True

    def __str__(self):
        return f"Laptop {self.laptop_id}: {self.brand} {self.model}, Rental Price: ${self.rental_price:.2f}, Available: {self.is_available}"


class Customer:
    """Represents a customer with an order."""

    def __init__(self, customer_id, name):
        """
        Initializes a Customer object.

        Args:
            customer_id (int): Unique identifier for the customer.
            name (str): Customer name.
        """
        self.customer_id = customer_id
        self.name = name
        self.order = None

    def __str__(self):
        return f"Customer {self.customer_id}: {self.name}"


class Order:
    """Represents a laptop rental order."""

    def __init__(self, order_id, customer, laptop, rental_duration):
        """
        Initializes an Order object.

        Args:
            order_id (int): Unique identifier for the order.
            customer (Customer): Customer who made the order.
            laptop (Laptop): Laptop being rented.
            rental_duration (int): Number of days for the rental.
        """
        self.order_id = order_id
        self.customer = customer
        self.laptop = laptop
        self.rental_duration = rental_duration

    def calculate_total(self):
        """Calculates the total rental cost."""
        return self.laptop.rental_price * self.rental_duration

    def __str__(self):
        return f"Order {self.order_id}: {self.customer.name} rented {self.laptop.brand} {self.laptop.model} for {self.rental_duration} days, Total: ${self.calculate_total():.2f}"


class LaptopRentalSystem:
    """Manages laptop rental inventory and customer orders."""

    def __init__(self):
        self.laptops = []
        self.customers = []
        self.orders = []
        self.laptop_id_counter = 1
        self.customer_id_counter = 1
        self.order_id_counter = 1

    def add_laptop(self, brand, model, rental_price):
        """
        Adds a laptop to the inventory.

        Args:
            brand (str): Laptop brand.
            model (str): Laptop model.
            rental_price (float): Daily rental price.
        """
        laptop = Laptop(self.laptop_id_counter, brand, model, rental_price)
        self.laptops.append(laptop)
        self.laptop_id_counter += 1
        print(f"Laptop added: {laptop}")

    def add_customer(self, name):
        """
        Adds a customer.

        Args:
            name (str): Customer name.
        """
        customer = Customer(self.customer_id_counter, name)
        self.customers.append(customer)
        self.customer_id_counter += 1
        print(f"Customer added: {customer}")

    def place_order(self, customer_name, laptop_brand, laptop_model, rental_duration):
        """
        Places a laptop rental order.

        Args:
            customer_name (str): Name of the customer.
            laptop_brand (str): Brand of the laptop.
            laptop_model (str): Model of the laptop.
            rental_duration (int): Number of days for the rental.
        """
        customer = next((c for c in self.customers if c.name == customer_name), None)
        if customer is None:
            print("Customer not found.")
            return

        laptop = next((l for l in self.laptops if l.brand == laptop_brand and l.model == laptop_model and l.is_available), None)
        if laptop is None:
            print("Laptop not available.")
            return

        order = Order(self.order_id_counter, customer, laptop, rental_duration)
        self.orders.append(order)
        laptop.is_available = False
        customer.order = order
        self.order_id_counter += 1
        print(f"Order placed: {order}")

    def return_laptop(self, order_id):
        """
        Returns a laptop and marks the order as completed.

        Args:
            order_id (int): ID of the order.
        """
        order = next((o for o in self.orders if o.order_id == order_id), None)
        if order is None:
            print("Order not found.")
            return

        order.laptop.is_available = True
        order.customer.order = None
        print(f"Laptop returned for order {order_id}")

    def print_inventory(self):
        """Prints the current laptop inventory."""
        print("Laptop Inventory:")
        for laptop in self.laptops:
            print(laptop)

    def print_orders(self):
        """Prints all orders."""
        print("Orders:")
        for order in self.orders:
            print(order)


def main():
    system = LaptopRentalSystem()

    while True:
        print("\nLaptop Rental System Menu:")
        print("1. Add Laptop")
        print("2. Add Customer")
        print("3. Place Order")
        print("4. Return Laptop")
        print("5. Print Inventory")
        print("6. Print Orders")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            brand = input("Enter laptop brand: ")
            model = input("Enter laptop model: ")
            rental_price = float(input("Enter rental price: "))
            system.add_laptop(brand, model, rental_price)
        elif choice == "2":
            name = input("Enter customer name: ")
            system.add_customer(name)
        elif choice == "3":
            customer_name = input("Enter customer name: ")
            laptop_brand = input("Enter laptop brand: ")
            laptop_model = input("Enter laptop model: ")
            rental_duration = int(input("Enter rental duration (days): "))
            system.place_order(customer_name, laptop_brand, laptop_model, rental_duration)
        elif choice == "4":
            order_id = int(input("Enter order ID: "))
            system.return_laptop(order_id)
        elif choice == "5":
            system.print_inventory()
        elif choice == "6":
            system.print_orders()
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
