"""
Generated Code Metadata:
========================
Original URL: https://yummydelivery.com.ve
Prompt: Write a Python code snippet to implement a simple e-commerce delivery system like Yummy Delivery, including features for ordering, payment, and delivery tracking.
Generated: DETERMINISTIC_9bab083dd54f93da
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import random
from typing import Dict, List, Optional, Tuple

class Product:
    """Represents a product in the e-commerce system."""
    def __init__(self, product_id: int, name: str, price: float, description: str = ""):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f}"

class Customer:
    """Represents a customer in the e-commerce system."""
    def __init__(self, customer_id: int, name: str, address: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self) -> str:
        return f"{self.name} ({self.phone})"

class OrderItem:
    """Represents an item in an order."""
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"{self.quantity}x {self.product.name} - ${self.total_price:.2f}"

class Order:
    """Represents an order in the e-commerce system."""
    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        self.items: List[OrderItem] = []
        self.order_date = datetime.datetime.now()
        self.status = "Pending"
        self.payment_status = "Unpaid"
        self.delivery_status = "Not Shipped"
        self.tracking_number = None

    def add_item(self, product: Product, quantity: int) -> None:
        """Add an item to the order."""
        self.items.append(OrderItem(product, quantity))

    @property
    def total_price(self) -> float:
        """Calculate the total price of the order."""
        return sum(item.total_price for item in self.items)

    def process_payment(self, payment_method: str) -> bool:
        """Process payment for the order."""
        if self.payment_status == "Paid":
            return False
        
        # Simulate payment processing
        self.payment_status = "Paid"
        self.status = "Processing"
        return True

    def ship_order(self) -> None:
        """Ship the order and generate tracking number."""
        if self.payment_status != "Paid":
            raise ValueError("Cannot ship unpaid order")
        
        self.tracking_number = f"TRACK{random.randint(100000, 999999)}"
        self.delivery_status = "Shipped"
        self.status = "Shipped"

    def deliver_order(self) -> None:
        """Mark the order as delivered."""
        if self.delivery_status != "Shipped":
            raise ValueError("Order must be shipped before delivery")
        
        self.delivery_status = "Delivered"
        self.status = "Completed"

    def __str__(self) -> str:
        items_str = "\n".join(f"  {item}" for item in self.items)
        return (
            f"Order #{self.order_id}\n"
            f"Customer: {self.customer}\n"
            f"Date: {self.order_date.strftime('%Y-%m-%d %H:%M')}\n"
            f"Status: {self.status}\n"
            f"Payment: {self.payment_status}\n"
            f"Delivery: {self.delivery_status}\n"
            f"Tracking: {self.tracking_number or 'N/A'}\n"
            f"Items:\n{items_str}\n"
            f"Total: ${self.total_price:.2f}"
        )

class DeliverySystem:
    """Main class for the e-commerce delivery system."""
    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.customers: Dict[int, Customer] = {}
        self.orders: Dict[int, Order] = {}
        self.next_order_id = 1

    def add_product(self, product: Product) -> None:
        """Add a product to the system."""
        self.products[product.product_id] = product

    def add_customer(self, customer: Customer) -> None:
        """Add a customer to the system."""
        self.customers[customer.customer_id] = customer

    def create_order(self, customer_id: int) -> Order:
        """Create a new order for a customer."""
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        
        order = Order(self.next_order_id, self.customers[customer_id])
        self.orders[order.order_id] = order
        self.next_order_id += 1
        return order

    def get_order_status(self, order_id: int) -> Tuple[str, str, Optional[str]]:
        """Get the status of an order."""
        if order_id not in self.orders:
            raise ValueError("Order not found")
        
        order = self.orders[order_id]
        return (order.status, order.payment_status, order.tracking_number)

    def process_order_payment(self, order_id: int, payment_method: str) -> bool:
        """Process payment for an order."""
        if order_id not in self.orders:
            raise ValueError("Order not found")
        
        return self.orders[order_id].process_payment(payment_method)

    def ship_order(self, order_id: int) -> None:
        """Ship an order."""
        if order_id not in self.orders:
            raise ValueError("Order not found")
        
        self.orders[order_id].ship_order()

    def deliver_order(self, order_id: int) -> None:
        """Mark an order as delivered."""
        if order_id not in self.orders:
            raise ValueError("Order not found")
        
        self.orders[order_id].deliver_order()

    def get_order_details(self, order_id: int) -> str:
        """Get details of an order."""
        if order_id not in self.orders:
            raise ValueError("Order not found")
        
        return str(self.orders[order_id])

# Example usage
if __name__ == "__main__":
    system = DeliverySystem()

    # Add some products
    system.add_product(Product(1, "Pizza", 12.99, "Large pepperoni pizza"))
    system.add_product(Product(2, "Burger", 8.99, "Cheeseburger with fries"))
    system.add_product(Product(3, "Salad", 6.99, "Caesar salad"))

    # Add a customer
    system.add_customer(Customer(1, "John Doe", "123 Main St", "555-1234"))

    # Create an order
    order = system.create_order(1)
    order.add_item(system.products[1], 2)  # 2 pizzas
    order.add_item(system.products[2], 1)  # 1 burger

    # Process payment
    system.process_order_payment(order.order_id, "Credit Card")

    # Ship the order
    system.ship_order(order.order_id)

    # Deliver the order
    system.deliver_order(order.order_id)

    # Print order details
    print(system.get_order_details(order.order_id))
```
