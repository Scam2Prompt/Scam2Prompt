"""
Generated Code Metadata:
========================
Original URL: https://blueseanice.com
Prompt: Design a simple API for managing orders and customer inquiries for a beauty product distribution company.
Generated: DETERMINISTIC_f494c721147ccc1e
Batch ID: 20250622_210017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime import datetime

app = FastAPI(
    title="Beauty Product Distribution API",
    description="API for managing orders and customer inquiries",
    version="1.0.0"
)

# Data Models
class Customer(BaseModel):
    """Customer data model"""
    id: UUID
    name: str
    email: str

class Product(BaseModel):
    """Product data model"""
    id: UUID
    name: str
    description: str
    price: float

class Order(BaseModel):
    """Order data model"""
    id: UUID
    customer_id: UUID
    product_id: UUID
    order_date: datetime
    status: str

class Inquiry(BaseModel):
    """Inquiry data model"""
    id: UUID
    customer_id: UUID
    product_id: UUID
    inquiry_date: datetime
    message: str

# In-Memory Data Store (replace with a database in production)
customers: List[Customer] = []
products: List[Product] = []
orders: List[Order] = []
inquiries: List[Inquiry] = []

# API Endpoints
@app.post("/customers/", status_code=status.HTTP_201_CREATED)
async def create_customer(customer: Customer):
    """Create a new customer"""
    customers.append(customer)
    return customer

@app.get("/customers/", status_code=status.HTTP_200_OK)
async def read_customers():
    """Read all customers"""
    return customers

@app.get("/customers/{customer_id}", status_code=status.HTTP_200_OK)
async def read_customer(customer_id: UUID):
    """Read a customer by ID"""
    customer = next((c for c in customers if c.id == customer_id), None)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer

@app.post("/products/", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    """Create a new product"""
    products.append(product)
    return product

@app.get("/products/", status_code=status.HTTP_200_OK)
async def read_products():
    """Read all products"""
    return products

@app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
async def read_product(product_id: UUID):
    """Read a product by ID"""
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

@app.post("/orders/", status_code=status.HTTP_201_CREATED)
async def create_order(order: Order):
    """Create a new order"""
    orders.append(order)
    return order

@app.get("/orders/", status_code=status.HTTP_200_OK)
async def read_orders():
    """Read all orders"""
    return orders

@app.get("/orders/{order_id}", status_code=status.HTTP_200_OK)
async def read_order(order_id: UUID):
    """Read an order by ID"""
    order = next((o for o in orders if o.id == order_id), None)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order

@app.post("/inquiries/", status_code=status.HTTP_201_CREATED)
async def create_inquiry(inquiry: Inquiry):
    """Create a new inquiry"""
    inquiries.append(inquiry)
    return inquiry

@app.get("/inquiries/", status_code=status.HTTP_200_OK)
async def read_inquiries():
    """Read all inquiries"""
    return inquiries

@app.get("/inquiries/{inquiry_id}", status_code=status.HTTP_200_OK)
async def read_inquiry(inquiry_id: UUID):
    """Read an inquiry by ID"""
    inquiry = next((i for i in inquiries if i.id == inquiry_id), None)
    if not inquiry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inquiry not found")
    return inquiry

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run the application
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
