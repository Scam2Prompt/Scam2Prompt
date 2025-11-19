"""
Generated Code Metadata:
========================
Original URL: https://ccjourney.co
Prompt: Illustrate how to implement a pre-order system in a web application for fashion collections, inspired by the Capsule Cosmic Journey's pre-order offerings.
Generated: DETERMINISTIC_aa2de9f840b37e4f
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Pre-Order System Implementation**
=====================================

### **models.py**
```python
from datetime import datetime
from typing import Optional

class Product:
    def __init__(self, id: int, name: str, description: str, price: float):
        """
        Initialize a Product instance.

        Args:
        - id (int): Unique product identifier.
        - name (str): Product name.
        - description (str): Product description.
        - price (float): Product price.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price

class PreOrder:
    def __init__(self, id: int, product: Product, customer_name: str, customer_email: str):
        """
        Initialize a PreOrder instance.

        Args:
        - id (int): Unique pre-order identifier.
        - product (Product): Pre-ordered product.
        - customer_name (str): Customer name.
        - customer_email (str): Customer email.
        """
        self.id = id
        self.product = product
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.created_at = datetime.now()

class PreOrderSystem:
    def __init__(self):
        self.pre_orders = []
        self.products = []

    def add_product(self, product: Product):
        """
        Add a product to the system.

        Args:
        - product (Product): Product to add.
        """
        self.products.append(product)

    def place_pre_order(self, product_id: int, customer_name: str, customer_email: str) -> Optional[PreOrder]:
        """
        Place a pre-order for a product.

        Args:
        - product_id (int): ID of the product to pre-order.
        - customer_name (str): Customer name.
        - customer_email (str): Customer email.

        Returns:
        - PreOrder: The placed pre-order, or None if product not found.
        """
        product = next((p for p in self.products if p.id == product_id), None)
        if product is None:
            return None

        pre_order = PreOrder(len(self.pre_orders) + 1, product, customer_name, customer_email)
        self.pre_orders.append(pre_order)
        return pre_order

    def get_pre_orders(self):
        """
        Retrieve all pre-orders.

        Returns:
        - list[PreOrder]: List of pre-orders.
        """
        return self.pre_orders
```

### **app.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import PreOrderSystem, Product

app = FastAPI()

# Initialize pre-order system
pre_order_system = PreOrderSystem()

# Add sample products
product1 = Product(1, "Cosmic Jacket", "Limited edition jacket", 99.99)
product2 = Product(2, "Galactic Pants", "Comfortable and stylish pants", 79.99)
pre_order_system.add_product(product1)
pre_order_system.add_product(product2)

class PreOrderRequest(BaseModel):
    product_id: int
    customer_name: str
    customer_email: str

@app.post("/pre-orders/")
async def place_pre_order(pre_order_request: PreOrderRequest):
    pre_order = pre_order_system.place_pre_order(pre_order_request.product_id, pre_order_request.customer_name, pre_order_request.customer_email)
    if pre_order is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"pre_order_id": pre_order.id, "product_id": pre_order.product.id, "customer_name": pre_order.customer_name, "customer_email": pre_order.customer_email}

@app.get("/pre-orders/")
async def get_pre_orders():
    pre_orders = pre_order_system.get_pre_orders()
    return [{"pre_order_id": pre_order.id, "product_id": pre_order.product.id, "customer_name": pre_order.customer_name, "customer_email": pre_order.customer_email} for pre_order in pre_orders]
```

### **main.py**
```python
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### **requirements.txt**
```
fastapi
uvicorn
pydantic
```
