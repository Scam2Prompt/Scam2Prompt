"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: "Write a Python code snippet to manage orders for a UPVC window and door systems company like Dexodoor, including customer details, product selection, and installation dates."
Generated: DETERMINISTIC_2a8ff6a20abcac4a
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from typing import Dict, List, Optional

class Customer:
    """Represents a customer with personal and contact details."""
    
    def __init__(self, name: str, address: str, phone: str, email: str):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
    
    def to_dict(self) -> Dict:
        """Convert customer details to dictionary for serialization."""
        return {
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'email': self.email
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """Create Customer instance from dictionary."""
        return cls(
            name=data['name'],
            address=data['address'],
            phone=data['phone'],
            email=data['email']
        )

class Product:
    """Represents a product with its details."""
    
    def __init__(self, product_id: str, name: str, category: str, price: float):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
    
    def to_dict(self) -> Dict:
        """Convert product details to dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'category': self.category,
            'price': self.price
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """Create Product instance from dictionary."""
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            category=data['category'],
            price=data['price']
        )

class Order:
    """Represents an order with customer, products, and installation details."""
    
    def __init__(self, order_id: str, customer: Customer, products: List[Product], 
                 installation_date: datetime.date, status: str = 'Pending'):
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.installation_date = installation_date
        self.status = status
    
    def calculate_total(self) -> float:
        """Calculate the total price of the order."""
        return sum(product.price for product in self.products)
    
    def to_dict(self) -> Dict:
        """Convert order details to dictionary for serialization."""
        return {
            'order_id': self.order_id,
            'customer': self.customer.to_dict(),
            'products': [product.to_dict() for product in self.products],
            'installation_date': self.installation_date.isoformat(),
            'status': self.status,
            'total': self.calculate_total()
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """Create Order instance from dictionary."""
        return cls(
            order_id=data['order_id'],
            customer=Customer.from_dict(data['customer']),
            products=[Product.from_dict(product) for product in data['products']],
            installation_date=datetime.date.fromisoformat(data['installation_date']),
            status=data.get('status', 'Pending')
        )

class OrderManager:
    """Manages orders with CRUD operations and persistence."""
    
    def __init__(self, file_path: str = 'orders.json'):
        self.file_path = file_path
        self.orders: Dict[str, Order] = {}
        self.load_orders()
    
    def add_order(self, order: Order) -> None:
        """Add a new order to the system."""
        if order.order_id in self.orders:
            raise ValueError(f"Order ID {order.order_id} already exists.")
        self.orders[order.order_id] = order
        self.save_orders()
    
    def get_order(self, order_id: str) -> Optional[Order]:
        """Retrieve an order by its ID."""
        return self.orders.get(order_id)
    
    def update_order_status(self, order_id: str, status: str) -> None:
        """Update the status of an existing order."""
        if order_id not in self.orders:
            raise ValueError(f"Order ID {order_id} not found.")
        self.orders[order_id].status = status
        self.save_orders()
    
    def delete_order(self, order_id: str) -> None:
        """Delete an order from the system."""
        if order_id not in self.orders:
            raise ValueError(f"Order ID {order_id} not found.")
        del self.orders[order_id]
        self.save_orders()
    
    def list_orders(self) -> List[Order]:
        """List all orders in the system."""
        return list(self.orders.values())
    
    def save_orders(self) -> None:
        """Save orders to a JSON file."""
        with open(self.file_path, 'w') as f:
            json.dump(
                {order_id: order.to_dict() for order_id, order in self.orders.items()},
                f,
                indent=4
            )
    
    def load_orders(self) -> None:
        """Load orders from a JSON file."""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.orders = {
                    order_id: Order.from_dict(order_data)
                    for order_id, order_data in data.items()
                }
        except FileNotFoundError:
            self.orders = {}
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in orders file.")

# Example usage
if __name__ == "__main__":
    manager = OrderManager()
    
    # Create sample customer
    customer = Customer(
        name="John Doe",
        address="123 Main St, London",
        phone="+44 1234567890",
        email="john.doe@example.com"
    )
    
    # Create sample products
    products = [
        Product("WD001", "Sliding Window", "Windows", 450.00),
        Product("DR001", "Front Door", "Doors", 750.00)
    ]
    
    # Create and add order
    order = Order(
        order_id="ORD123",
        customer=customer,
        products=products,
        installation_date=datetime.date(2023, 12, 15)
    )
    
    try:
        manager.add_order(order)
        print("Order added successfully.")
        
        # Retrieve and print order
        retrieved_order = manager.get_order("ORD123")
        if retrieved_order:
            print(f"Order Total: £{retrieved_order.calculate_total():.2f}")
        
        # Update order status
        manager.update_order_status("ORD123", "Confirmed")
        print("Order status updated.")
        
    except ValueError as e:
        print(f"Error: {e}")
```
