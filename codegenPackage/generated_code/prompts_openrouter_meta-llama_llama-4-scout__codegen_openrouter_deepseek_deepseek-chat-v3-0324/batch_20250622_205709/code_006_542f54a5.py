"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: "Design an API to manage orders and inventory for a store selling Meat Master products, including endpoints for creating orders, updating inventory, and retrieving product information."
Generated: DETERMINISTIC_542f54a576604026
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Meat Master API",
    description="API for managing orders and inventory for Meat Master products",
    version="1.0.0"
)

# Database simulation
inventory_db = {}
orders_db = {}

# Models
class Product(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    quantity: int
    category: str
    created_at: datetime
    updated_at: datetime

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    category: str

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    category: Optional[str] = None

class OrderItem(BaseModel):
    product_id: UUID
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItem]
    customer_name: str
    customer_email: str

class Order(BaseModel):
    id: UUID
    items: List[OrderItem]
    customer_name: str
    customer_email: str
    total_price: float
    status: str
    created_at: datetime
    updated_at: datetime

# Helper functions
def get_product(product_id: UUID):
    product = inventory_db.get(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

def update_product_quantity(product_id: UUID, quantity_change: int):
    product = get_product(product_id)
    new_quantity = product.quantity + quantity_change
    if new_quantity < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient inventory"
        )
    product.quantity = new_quantity
    product.updated_at = datetime.now()
    inventory_db[product_id] = product
    return product

# Endpoints
@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    """
    Create a new product in inventory.
    """
    product_id = uuid4()
    now = datetime.now()
    new_product = Product(
        id=product_id,
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity,
        category=product.category,
        created_at=now,
        updated_at=now
    )
    inventory_db[product_id] = new_product
    logger.info(f"Created product {product_id}")
    return new_product

@app.get("/products/", response_model=List[Product])
def list_products():
    """
    List all products in inventory.
    """
    return list(inventory_db.values())

@app.get("/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: UUID):
    """
    Get details of a specific product by ID.
    """
    return get_product(product_id)

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: UUID, product_update: ProductUpdate):
    """
    Update product details.
    """
    product = get_product(product_id)
    update_data = product_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(product, field, value)
    
    product.updated_at = datetime.now()
    inventory_db[product_id] = product
    logger.info(f"Updated product {product_id}")
    return product

@app.post("/orders/", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate):
    """
    Create a new order.
    """
    order_id = uuid4()
    now = datetime.now()
    total_price = 0.0
    
    # Validate and process order items
    for item in order.items:
        product = get_product(item.product_id)
        if item.quantity > product.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient inventory for product {item.product_id}"
            )
        total_price += product.price * item.quantity
    
    # Update inventory
    for item in order.items:
        update_product_quantity(item.product_id, -item.quantity)
    
    # Create order
    new_order = Order(
        id=order_id,
        items=order.items,
        customer_name=order.customer_name,
        customer_email=order.customer_email,
        total_price=total_price,
        status="created",
        created_at=now,
        updated_at=now
    )
    orders_db[order_id] = new_order
    logger.info(f"Created order {order_id}")
    return new_order

@app.get("/orders/", response_model=List[Order])
def list_orders():
    """
    List all orders.
    """
    return list(orders_db.values())

@app.get("/orders/{order_id}", response_model=Order)
def get_order_by_id(order_id: UUID):
    """
    Get details of a specific order by ID.
    """
    order = orders_db.get(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order

@app.post("/inventory/{product_id}/restock", response_model=Product)
def restock_product(product_id: UUID, quantity: int):
    """
    Restock a product by adding to its quantity.
    """
    if quantity <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quantity must be positive"
        )
    product = update_product_quantity(product_id, quantity)
    logger.info(f"Restocked product {product_id} with {quantity} units")
    return product

@app.post("/inventory/{product_id}/deduct", response_model=Product)
def deduct_inventory(product_id: UUID, quantity: int):
    """
    Deduct inventory from a product.
    """
    if quantity <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quantity must be positive"
        )
    product = update_product_quantity(product_id, -quantity)
    logger.info(f"Deducted {quantity} units from product {product_id}")
    return product
```
