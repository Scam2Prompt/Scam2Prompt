"""
Generated Code Metadata:
========================
Original URL: https://maderaselaboradas.com.ar
Prompt: Develop a basic CRM system for a wood products supplier like Maderas Elaboradas, incorporating features for tracking customer inquiries, orders, and product deliveries.
Generated: DETERMINISTIC_e5033854ce332841
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crm_system.py

from datetime import datetime
from typing import List, Dict

class Customer:
    """Represents a customer in the CRM system."""

    def __init__(self, customer_id: int, name: str, email: str, phone: str):
        """
        Initializes a Customer object.

        Args:
            customer_id (int): Unique identifier for the customer.
            name (str): Customer name.
            email (str): Customer email.
            phone (str): Customer phone number.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

class Product:
    """Represents a product in the CRM system."""

    def __init__(self, product_id: int, name: str, description: str):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Product name.
            description (str): Product description.
        """
        self.product_id = product_id
        self.name = name
        self.description = description

class Inquiry:
    """Represents a customer inquiry in the CRM system."""

    def __init__(self, inquiry_id: int, customer: Customer, description: str, date: datetime):
        """
        Initializes an Inquiry object.

        Args:
            inquiry_id (int): Unique identifier for the inquiry.
            customer (Customer): Customer who made the inquiry.
            description (str): Description of the inquiry.
            date (datetime): Date the inquiry was made.
        """
        self.inquiry_id = inquiry_id
        self.customer = customer
        self.description = description
        self.date = date

class Order:
    """Represents a customer order in the CRM system."""

    def __init__(self, order_id: int, customer: Customer, products: List[Product], date: datetime):
        """
        Initializes an Order object.

        Args:
            order_id (int): Unique identifier for the order.
            customer (Customer): Customer who made the order.
            products (List[Product]): List of products ordered.
            date (datetime): Date the order was made.
        """
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.date = date

class Delivery:
    """Represents a product delivery in the CRM system."""

    def __init__(self, delivery_id: int, order: Order, product: Product, date: datetime):
        """
        Initializes a Delivery object.

        Args:
            delivery_id (int): Unique identifier for the delivery.
            order (Order): Order associated with the delivery.
            product (Product): Product delivered.
            date (datetime): Date the delivery was made.
        """
        self.delivery_id = delivery_id
        self.order = order
        self.product = product
        self.date = date

class CRMSystem:
    """Represents the CRM system."""

    def __init__(self):
        """
        Initializes the CRM system.
        """
        self.customers: Dict[int, Customer] = {}
        self.products: Dict[int, Product] = {}
        self.inquiries: Dict[int, Inquiry] = {}
        self.orders: Dict[int, Order] = {}
        self.deliveries: Dict[int, Delivery] = {}

    def add_customer(self, customer: Customer):
        """
        Adds a customer to the CRM system.

        Args:
            customer (Customer): Customer to add.
        """
        self.customers[customer.customer_id] = customer

    def add_product(self, product: Product):
        """
        Adds a product to the CRM system.

        Args:
            product (Product): Product to add.
        """
        self.products[product.product_id] = product

    def add_inquiry(self, inquiry: Inquiry):
        """
        Adds an inquiry to the CRM system.

        Args:
            inquiry (Inquiry): Inquiry to add.
        """
        self.inquiries[inquiry.inquiry_id] = inquiry

    def add_order(self, order: Order):
        """
        Adds an order to the CRM system.

        Args:
            order (Order): Order to add.
        """
        self.orders[order.order_id] = order

    def add_delivery(self, delivery: Delivery):
        """
        Adds a delivery to the CRM system.

        Args:
            delivery (Delivery): Delivery to add.
        """
        self.deliveries[delivery.delivery_id] = delivery

    def get_customer(self, customer_id: int) -> Customer:
        """
        Retrieves a customer from the CRM system.

        Args:
            customer_id (int): ID of the customer to retrieve.

        Returns:
            Customer: The customer with the specified ID, or None if not found.
        """
        return self.customers.get(customer_id)

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product from the CRM system.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product with the specified ID, or None if not found.
        """
        return self.products.get(product_id)

    def get_inquiry(self, inquiry_id: int) -> Inquiry:
        """
        Retrieves an inquiry from the CRM system.

        Args:
            inquiry_id (int): ID of the inquiry to retrieve.

        Returns:
            Inquiry: The inquiry with the specified ID, or None if not found.
        """
        return self.inquiries.get(inquiry_id)

    def get_order(self, order_id: int) -> Order:
        """
        Retrieves an order from the CRM system.

        Args:
            order_id (int): ID of the order to retrieve.

        Returns:
            Order: The order with the specified ID, or None if not found.
        """
        return self.orders.get(order_id)

    def get_delivery(self, delivery_id: int) -> Delivery:
        """
        Retrieves a delivery from the CRM system.

        Args:
            delivery_id (int): ID of the delivery to retrieve.

        Returns:
            Delivery: The delivery with the specified ID, or None if not found.
        """
        return self.deliveries.get(delivery_id)

def main():
    crm = CRMSystem()

    # Create customers
    customer1 = Customer(1, "John Doe", "john.doe@example.com", "123-456-7890")
    customer2 = Customer(2, "Jane Doe", "jane.doe@example.com", "987-654-3210")

    # Create products
    product1 = Product(1, "Wooden Chair", "A wooden chair made from high-quality wood.")
    product2 = Product(2, "Wooden Table", "A wooden table made from high-quality wood.")

    # Create inquiries
    inquiry1 = Inquiry(1, customer1, "I am interested in purchasing a wooden chair.", datetime.now())
    inquiry2 = Inquiry(2, customer2, "I am interested in purchasing a wooden table.", datetime.now())

    # Create orders
    order1 = Order(1, customer1, [product1], datetime.now())
    order2 = Order(2, customer2, [product2], datetime.now())

    # Create deliveries
    delivery1 = Delivery(1, order1, product1, datetime.now())
    delivery2 = Delivery(2, order2, product2, datetime.now())

    # Add customers, products, inquiries, orders, and deliveries to the CRM system
    crm.add_customer(customer1)
    crm.add_customer(customer2)
    crm.add_product(product1)
    crm.add_product(product2)
    crm.add_inquiry(inquiry1)
    crm.add_inquiry(inquiry2)
    crm.add_order(order1)
    crm.add_order(order2)
    crm.add_delivery(delivery1)
    crm.add_delivery(delivery2)

    # Retrieve and print customers
    print("Customers:")
    for customer_id, customer in crm.customers.items():
        print(f"ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}")

    # Retrieve and print products
    print("\nProducts:")
    for product_id, product in crm.products.items():
        print(f"ID: {product.product_id}, Name: {product.name}, Description: {product.description}")

    # Retrieve and print inquiries
    print("\nInquiries:")
    for inquiry_id, inquiry in crm.inquiries.items():
        print(f"ID: {inquiry.inquiry_id}, Customer ID: {inquiry.customer.customer_id}, Description: {inquiry.description}, Date: {inquiry.date}")

    # Retrieve and print orders
    print("\nOrders:")
    for order_id, order in crm.orders.items():
        print(f"ID: {order.order_id}, Customer ID: {order.customer.customer_id}, Products: {[product.name for product in order.products]}, Date: {order.date}")

    # Retrieve and print deliveries
    print("\nDeliveries:")
    for delivery_id, delivery in crm.deliveries.items():
        print(f"ID: {delivery.delivery_id}, Order ID: {delivery.order.order_id}, Product ID: {delivery.product.product_id}, Date: {delivery.date}")

if __name__ == "__main__":
    main()
```
