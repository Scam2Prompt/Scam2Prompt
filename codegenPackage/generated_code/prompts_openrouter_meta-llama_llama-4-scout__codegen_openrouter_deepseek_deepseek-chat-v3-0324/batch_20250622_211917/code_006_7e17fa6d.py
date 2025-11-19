"""
Generated Code Metadata:
========================
Original URL: https://dizneypin.com
Prompt: "Suggest a set of RESTful API endpoints for managing Disney merchandise inventory, including endpoints for retrieving products by category, updating product stock levels, and processing orders."
Generated: DETERMINISTIC_7e17fa6d48d5bbb1
Batch ID: 20250622_211917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI(
    title="Disney Merchandise Inventory API",
    description="RESTful API for managing Disney merchandise inventory",
    version="1.0.0"
)

# Database mock (in production, replace with actual database)
inventory_db = {}
orders_db = {}

class Product(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    stock: int
    category: str
    image_url: Optional[str] = None

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    category: str
    image_url: Optional[str] = None

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category: Optional[str] = None
    image_url: Optional[str] = None

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
    total: float
    status: str = "pending"

@app.get("/products", response_model=List[Product], tags=["Products"])
async def get_all_products():
    """Get all products in inventory"""
    return list(inventory_db.values())

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
async def get_product(product_id: UUID):
    """Get a specific product by ID"""
    if product_id not in inventory_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return inventory_db[product_id]

@app.get("/products/category/{category}", response_model=List[Product], tags=["Products"])
async def get_products_by_category(category: str):
    """Get all products in a specific category"""
    return [product for product in inventory_db.values() if product.category.lower() == category.lower()]

@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED, tags=["Products"])
async def create_product(product: ProductCreate):
    """Create a new product"""
    product_id = uuid4()
    new_product = Product(
        id=product_id,
        **product.dict()
    )
    inventory_db[product_id] = new_product
    return new_product

@app.put("/products/{product_id}", response_model=Product, tags=["Products"])
async def update_product(product_id: UUID, product_update: ProductUpdate):
    """Update an existing product"""
    if product_id not in inventory_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    stored_product = inventory_db[product_id]
    update_data = product_update.dict(exclude_unset=True)
    updated_product = stored_product.copy(update=update_data)
    inventory_db[product_id] = updated_product
    return updated_product

@app.patch("/products/{product_id}/stock", response_model=Product, tags=["Products"])
async def update_product_stock(product_id: UUID, stock_change: int):
    """Update product stock level (increment/decrement)"""
    if product_id not in inventory_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    product = inventory_db[product_id]
    new_stock = product.stock + stock_change
    if new_stock < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient stock"
        )
    
    updated_product = product.copy(update={"stock": new_stock})
    inventory_db[product_id] = updated_product
    return updated_product

@app.post("/orders", response_model=Order, status_code=status.HTTP_201_CREATED, tags=["Orders"])
async def create_order(order: OrderCreate):
    """Create a new order"""
    order_id = uuid4()
    order_items = []
    total = 0.0
    
    # Validate products and calculate total
    for item in order.items:
        if item.product_id not in inventory_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product {item.product_id} not found"
            )
        
        product = inventory_db[item.product_id]
        if product.stock < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient stock for product {product.name}"
            )
        
        total += product.price * item.quantity
        order_items.append(item)
    
    # Create order
    new_order = Order(
        id=order_id,
        items=order_items,
        customer_name=order.customer_name,
        customer_email=order.customer_email,
        total=total
    )
    orders_db[order_id] = new_order
    
    # Update stock levels
    for item in order_items:
        product = inventory_db[item.product_id]
        updated_product = product.copy(update={"stock": product.stock - item.quantity})
        inventory_db[item.product_id] = updated_product
    
    return new_order

@app.get("/orders/{order_id}", response_model=Order, tags=["Orders"])
async def get_order(order_id: UUID):
    """Get order details"""
    if order_id not in orders_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return orders_db[order_id]
```
