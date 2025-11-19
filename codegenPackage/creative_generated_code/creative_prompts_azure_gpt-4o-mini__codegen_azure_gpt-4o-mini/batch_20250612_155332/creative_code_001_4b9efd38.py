"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedsoftwareservices.com
Prompt: How can I implement custom ERP and CRM solutions in Python based on the services provided by United Software Services?
Generated: DETERMINISTIC_4b9efd386f707934
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Customer:
    """Represents a customer in the CRM system."""
    
    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Customer(id={self.customer_id}, name='{self.name}', email='{self.email}')"

class Product:
    """Represents a product in the ERP system."""
    
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price})"

class Order:
    """Represents an order in the ERP system."""
    
    def __init__(self, order_id: int, customer: Customer, products: List[Product]):
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.total = sum(product.price for product in products)

    def __repr__(self):
        return f"Order(id={self.order_id}, customer={self.customer}, total={self.total})"

class CRM:
    """Simple CRM implementation for managing customers."""
    
    def __init__(self):
        self.customers: Dict[int, Customer] = {}

    def add_customer(self, customer: Customer):
        """Add a new customer to the CRM."""
        if customer.customer_id in self.customers:
            logging.error("Customer with this ID already exists.")
            raise ValueError("Customer ID already exists.")
        self.customers[customer.customer_id] = customer
        logging.info(f"Added customer: {customer}")

    def get_customer(self, customer_id: int) -> Optional[Customer]:
        """Retrieve a customer by their ID."""
        return self.customers.get(customer_id)

class ERP:
    """Simple ERP implementation for managing products and orders."""
    
    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.orders: Dict[int, Order] = {}

    def add_product(self, product: Product):
        """Add a new product to the ERP."""
        if product.product_id in self.products:
            logging.error("Product with this ID already exists.")
            raise ValueError("Product ID already exists.")
        self.products[product.product_id] = product
        logging.info(f"Added product: {product}")

    def create_order(self, order_id: int, customer: Customer, product_ids: List[int]) -> Order:
        """Create a new order for a customer."""
        products = [self.products[prod_id] for prod_id in product_ids if prod_id in self.products]
        
        if not products:
            logging.error("No valid products found for the order.")
            raise ValueError("No valid products found.")
        
        order = Order(order_id, customer, products)
        self.orders[order_id] = order
        logging.info(f"Created order: {order}")
        return order

# Example usage
if __name__ == "__main__":
    # Initialize CRM and ERP systems
    crm = CRM()
    erp = ERP()

    try:
        # Add some customers and products
        crm.add_customer(Customer(1, "Alice Smith", "alice@example.com"))
        crm.add_customer(Customer(2, "Bob Johnson", "bob@example.com"))
        
        erp.add_product(Product(101, "Product A", 19.99))
        erp.add_product(Product(102, "Product B", 29.99))
        
        # Create an order for a customer
        customer = crm.get_customer(1)
        order = erp.create_order(201, customer, [101, 102])
        
        logging.info(f"Order created successfully: {order}")

    except ValueError as e:
        logging.error(f"An error occurred: {e}")
```
