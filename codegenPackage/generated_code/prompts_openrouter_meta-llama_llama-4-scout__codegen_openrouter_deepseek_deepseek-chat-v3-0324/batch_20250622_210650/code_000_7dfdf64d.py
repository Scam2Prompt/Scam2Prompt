"""
Generated Code Metadata:
========================
Original URL: https://aceitescondadoloma.com
Prompt: Write a Python script to manage olive oil export orders, including customer information, order quantities, and international shipping logistics, considering the steps outlined by Aceites Condado Loma for exporting olive oil.
Generated: DETERMINISTIC_7dfdf64ddec5ac86
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class Customer:
    """Represents a customer with their details."""
    
    def __init__(self, customer_id: str, name: str, email: str, address: str, country: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.address = address
        self.country = country
    
    def to_dict(self) -> Dict:
        """Convert customer details to a dictionary."""
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'address': self.address,
            'country': self.country
        }

class OrderItem:
    """Represents an item in an order."""
    
    def __init__(self, product_id: str, quantity: int, price_per_unit: float):
        self.product_id = product_id
        self.quantity = quantity
        self.price_per_unit = price_per_unit
    
    def to_dict(self) -> Dict:
        """Convert order item details to a dictionary."""
        return {
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price_per_unit': self.price_per_unit
        }

class ShippingDetails:
    """Represents shipping details for an order."""
    
    def __init__(self, shipping_method: str, tracking_number: str, estimated_delivery: str):
        self.shipping_method = shipping_method
        self.tracking_number = tracking_number
        self.estimated_delivery = estimated_delivery
    
    def to_dict(self) -> Dict:
        """Convert shipping details to a dictionary."""
        return {
            'shipping_method': self.shipping_method,
            'tracking_number': self.tracking_number,
            'estimated_delivery': self.estimated_delivery
        }

class Order:
    """Represents an order with customer, items, and shipping details."""
    
    def __init__(self, order_id: str, customer: Customer, items: List[OrderItem], 
                 shipping_details: ShippingDetails, order_date: Optional[str] = None):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.shipping_details = shipping_details
        self.order_date = order_date or datetime.now().strftime("%Y-%m-%d")
    
    def total_cost(self) -> float:
        """Calculate the total cost of the order."""
        return sum(item.quantity * item.price_per_unit for item in self.items)
    
    def to_dict(self) -> Dict:
        """Convert order details to a dictionary."""
        return {
            'order_id': self.order_id,
            'customer': self.customer.to_dict(),
            'items': [item.to_dict() for item in self.items],
            'shipping_details': self.shipping_details.to_dict(),
            'order_date': self.order_date,
            'total_cost': self.total_cost()
        }

class OrderManager:
    """Manages olive oil export orders."""
    
    def __init__(self):
        self.orders: Dict[str, Order] = {}
    
    def add_order(self, order: Order) -> bool:
        """Add an order to the manager."""
        if order.order_id in self.orders:
            return False
        self.orders[order.order_id] = order
        return True
    
    def get_order(self, order_id: str) -> Optional[Order]:
        """Retrieve an order by ID."""
        return self.orders.get(order_id)
    
    def remove_order(self, order_id: str) -> bool:
        """Remove an order by ID."""
        if order_id not in self.orders:
            return False
        del self.orders[order_id]
        return True
    
    def export_orders_to_csv(self, filename: str) -> bool:
        """Export all orders to a CSV file."""
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['order_id', 'customer_id', 'customer_name', 'customer_email', 
                             'customer_address', 'customer_country', 'product_id', 
                             'quantity', 'price_per_unit', 'shipping_method', 
                             'tracking_number', 'estimated_delivery', 'order_date', 'total_cost']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for order in self.orders.values():
                    for item in order.items:
                        row = {
                            'order_id': order.order_id,
                            'customer_id': order.customer.customer_id,
                            'customer_name': order.customer.name,
                            'customer_email': order.customer.email,
                            'customer_address': order.customer.address,
                            'customer_country': order.customer.country,
                            'product_id': item.product_id,
                            'quantity': item.quantity,
                            'price_per_unit': item.price_per_unit,
                            'shipping_method': order.shipping_details.shipping_method,
                            'tracking_number': order.shipping_details.tracking_number,
                            'estimated_delivery': order.shipping_details.estimated_delivery,
                            'order_date': order.order_date,
                            'total_cost': order.total_cost()
                        }
                        writer.writerow(row)
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    def import_orders_from_csv(self, filename: str) -> bool:
        """Import orders from a CSV file."""
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    customer = Customer(
                        row['customer_id'],
                        row['customer_name'],
                        row['customer_email'],
                        row['customer_address'],
                        row['customer_country']
                    )
                    item = OrderItem(
                        row['product_id'],
                        int(row['quantity']),
                        float(row['price_per_unit'])
                    )
                    shipping_details = ShippingDetails(
                        row['shipping_method'],
                        row['tracking_number'],
                        row['estimated_delivery']
                    )
                    order = Order(
                        row['order_id'],
                        customer,
                        [item],
                        shipping_details,
                        row['order_date']
                    )
                    self.add_order(order)
            return True
        except Exception as e:
            print(f"Error importing from CSV: {e}")
            return False
    
    def export_orders_to_json(self, filename: str) -> bool:
        """Export all orders to a JSON file."""
        try:
            orders_data = [order.to_dict() for order in self.orders.values()]
            with open(filename, 'w') as jsonfile:
                json.dump(orders_data, jsonfile, indent=4)
            return True
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
            return False
    
    def import_orders_from_json(self, filename: str) -> bool:
        """Import orders from a JSON file."""
        try:
            with open(filename, 'r') as jsonfile:
                orders_data = json.load(jsonfile)
                for order_data in orders_data:
                    customer_data = order_data['customer']
                    customer = Customer(
                        customer_data['customer_id'],
                        customer_data['name'],
                        customer_data['email'],
                        customer_data['address'],
                        customer_data['country']
                    )
                    items = [
                        OrderItem(
                            item['product_id'],
                            item['quantity'],
                            item['price_per_unit']
                        ) for item in order_data['items']
                    ]
                    shipping_data = order_data['shipping_details']
                    shipping_details = ShippingDetails(
                        shipping_data['shipping_method'],
                        shipping_data['tracking_number'],
                        shipping_data['estimated_delivery']
                    )
                    order = Order(
                        order_data['order_id'],
                        customer,
                        items,
                        shipping_details,
                        order_data['order_date']
                    )
                    self.add_order(order)
            return True
        except Exception as e:
            print(f"Error importing from JSON: {e}")
            return False

# Example usage
if __name__ == "__main__":
    manager = OrderManager()
    
    # Create a customer
    customer = Customer(
        "CUST001",
        "John Doe",
        "john.doe@example.com",
        "123 Main St, Anytown",
        "USA"
    )
    
    # Create order items
    items = [
        OrderItem("OLIVE001", 10, 15.99),
        OrderItem("OLIVE002", 5, 12.50)
    ]
    
    # Create shipping details
    shipping_details = ShippingDetails(
        "Express",
        "TRACK123456",
        "2023-12-25"
    )
    
    # Create an order
    order = Order(
        "ORDER001",
        customer,
        items,
        shipping_details
    )
    
    # Add the order to the manager
    manager.add_order(order)
    
    # Export orders to CSV and JSON
    manager.export_orders_to_csv("orders.csv")
    manager.export_orders_to_json("orders.json")
```
