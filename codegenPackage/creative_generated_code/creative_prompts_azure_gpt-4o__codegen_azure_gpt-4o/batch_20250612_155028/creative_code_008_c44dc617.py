"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelllar.org
Prompt: Generate a script to simulate e-commerce fulfillment and delivery setup in under 10 days, inspired by Stelllar Logistics' case study.
Generated: DETERMINISTIC_c44dc617590db0c9
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random
import string

class Product:
    """
    Represents a product in the e-commerce store.
    """
    def __init__(self, product_id, name, weight):
        self.product_id = product_id
        self.name = name
        self.weight = weight  # Weight in kg

class Order:
    """
    Represents a customer order.
    """
    def __init__(self, order_id, products, address):
        self.order_id = order_id
        self.products = products
        self.address = address
        self.created_at = datetime.datetime.now()
        self.status = "Pending"

    def calculate_total_weight(self):
        """
        Calculate the total weight of the products in the order.
        """
        return sum(product.weight for product in self.products)

class LogisticsPartner:
    """
    Represents a logistics partner responsible for delivery.
    """
    def __init__(self, name, max_weight_capacity):
        self.name = name
        self.max_weight_capacity = max_weight_capacity  # Maximum weight capacity in kg

    def can_handle_order(self, order):
        """
        Determines if the logistics partner can handle the given order based on weight.
        """
        return order.calculate_total_weight() <= self.max_weight_capacity

class FulfillmentCenter:
    """
    Represents the fulfillment center.
    """
    def __init__(self):
        self.orders = []

    def receive_order(self, order):
        """
        Receives a new order for processing.
        """
        self.orders.append(order)
        print(f"Order {order.order_id} received. Address: {order.address}")

    def assign_to_logistics(self, logistics_partners):
        """
        Assigns orders to available logistics partners for delivery.
        """
        for order in self.orders:
            if order.status == "Pending":
                assigned = False
                for partner in logistics_partners:
                    if partner.can_handle_order(order):
                        order.status = "Assigned to Logistics"
                        print(f"Order {order.order_id} assigned to {partner.name}.")
                        assigned = True
                        break
                if not assigned:
                    print(f"Order {order.order_id} cannot be assigned. No suitable logistics partner available.")

    def process_delivery(self):
        """
        Simulates delivery of orders.
        """
        for order in self.orders:
            if order.status == "Assigned to Logistics":
                delivery_date = order.created_at + datetime.timedelta(days=random.randint(1, 10))
                order.status = "Delivered"
                print(f"Order {order.order_id} delivered successfully on {delivery_date.strftime('%Y-%m-%d')}.")

def generate_random_order_id():
    """
    Generates a random order ID.
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def main():
    """
    Main function to simulate e-commerce fulfillment and delivery setup.
    """
    # Create sample products
    product1 = Product("P001", "Laptop", 2.5)
    product2 = Product("P002", "Smartphone", 0.5)
    product3 = Product("P003", "Tablet", 0.8)

    # Create sample orders
    order1 = Order(generate_random_order_id(), [product1, product2], "123 Main St, Springfield")
    order2 = Order(generate_random_order_id(), [product3], "456 Elm St, Shelbyville")
    
    # Create logistics partners
    logistics1 = LogisticsPartner("Stellar Logistics", max_weight_capacity=5.0)
    logistics2 = LogisticsPartner("Rapid Transit", max_weight_capacity=10.0)
    
    # Fulfillment center setup
    fulfillment_center = FulfillmentCenter()
    fulfillment_center.receive_order(order1)
    fulfillment_center.receive_order(order2)
    
    # Assign orders to logistics partners
    fulfillment_center.assign_to_logistics([logistics1, logistics2])
    
    # Process deliveries
    fulfillment_center.process_delivery()

if __name__ == "__main__":
    main()
```
