"""
Generated Code Metadata:
========================
Original URL: https://www.lattechocolate.com.ar
Prompt: Design a simple API for managing products, orders, and shipping information for an e-commerce platform like Latte Chocolate, including endpoints for product categories and shipping calculations.
Generated: DETERMINISTIC_b969322538c70514
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import uuid

# Initialize FastAPI app
app = FastAPI(
    title="Latte Chocolate E-Commerce API",
    description="API for managing products, orders, and shipping information",
    version="1.0.0"
)

# Database simulation (in-memory for demonstration)
products_db = []
orders_db = []
categories_db = []

# Pydantic models for request/response validation
class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    category_id: str
    stock: int

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: str
    stock: int

class Category(BaseModel):
    id: str
    name: str
    description: str

class CategoryCreate(BaseModel):
    name: str
    description: str

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    id: str
    customer_name: str
    customer_email: str
    items: List[OrderItem]
    shipping_address: str
    status: str = "pending"
    total: float
    shipping_cost: float

class OrderCreate(BaseModel):
    customer_name: str
    customer_email: str
    items: List[OrderItem]
    shipping_address: str

class ShippingCalculation(BaseModel):
    items: List[OrderItem]
    shipping_address: str

# Helper functions
def calculate_shipping_cost(items: List[OrderItem], shipping_address: str) -> float:
    """Calculate shipping cost based on items and address"""
    # Simplified shipping calculation (production would use a real service)
    total_weight = len(items) * 0.5  # Assume each item is 0.5kg
    if "international" in shipping_address.lower():
        return 25.0 + (total_weight * 5.0)
    return 10.0 + (total_weight * 2.0)

def calculate_order_total(items: List[OrderItem]) -> float:
    """Calculate order total by summing product prices"""
    total = 0.0
    for item in items:
        product = next((p for p in products_db if p["id"] == item.product_id), None)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Product with ID {item.product_id} not found"
            )
        total += product["price"] * item.quantity
    return total

# Product endpoints
@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    """Create a new product"""
    product_id = str(uuid.uuid4())
    new_product = {
        "id": product_id,
        **product.dict()
    }
    products_db.append(new_product)
    return new_product

@app.get("/products/", response_model=List[Product])
def list_products():
    """List all available products"""
    return products_db

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    """Get details of a specific product"""
    product = next((p for p in products_db if p["id"] == product_id), None)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

# Category endpoints
@app.post("/categories/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate):
    """Create a new product category"""
    category_id = str(uuid.uuid4())
    new_category = {
        "id": category_id,
        **category.dict()
    }
    categories_db.append(new_category)
    return new_category

@app.get("/categories/", response_model=List[Category])
def list_categories():
    """List all available categories"""
    return categories_db

@app.get("/categories/{category_id}/products", response_model=List[Product])
def get_products_by_category(category_id: str):
    """Get all products in a specific category"""
    return [p for p in products_db if p["category_id"] == category_id]

# Order endpoints
@app.post("/orders/", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate):
    """Create a new order"""
    order_id = str(uuid.uuid4())
    
    # Calculate order total and shipping cost
    try:
        subtotal = calculate_order_total(order.items)
        shipping_cost = calculate_shipping_cost(order.items, order.shipping_address)
        total = subtotal + shipping_cost
    except HTTPException as e:
        raise e
    
    new_order = {
        "id": order_id,
        **order.dict(),
        "status": "pending",
        "total": total,
        "shipping_cost": shipping_cost
    }
    orders_db.append(new_order)
    return new_order

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: str):
    """Get details of a specific order"""
    order = next((o for o in orders_db if o["id"] == order_id), None)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order

@app.post("/shipping/calculate", response_model=dict)
def calculate_shipping(shipping_calc: ShippingCalculation):
    """Calculate shipping cost for potential order"""
    try:
        shipping_cost = calculate_shipping_cost(shipping_calc.items, shipping_calc.shipping_address)
        subtotal = calculate_order_total(shipping_calc.items)
        return {
            "shipping_cost": shipping_cost,
            "subtotal": subtotal,
            "total": subtotal + shipping_cost
        }
    except HTTPException as e:
        raise e
```
