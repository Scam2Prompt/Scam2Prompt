"""
Generated Code Metadata:
========================
Original URL: https://birafurniture.com
Prompt: "Design a RESTful API for a furniture e-commerce platform, including endpoints for retrieving product listings by room type (e.g., bedroom, kitchen) and managing prefab home model inquiries."
Generated: DETERMINISTIC_5e7dba8a5cf9fdc2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
import uuid
from datetime import datetime

app = FastAPI(
    title="Furniture E-Commerce API",
    description="RESTful API for a furniture e-commerce platform",
    version="1.0.0"
)

# Database models (in-memory for demonstration)
class RoomType(str, Enum):
    BEDROOM = "bedroom"
    LIVING_ROOM = "living_room"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    DINING_ROOM = "dining_room"
    OFFICE = "office"

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    price: float
    room_type: RoomType
    stock_quantity: int
    created_at: datetime = Field(default_factory=datetime.now)

class PrefabHomeInquiry(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    model_name: str
    customer_name: str
    email: str
    phone: str
    message: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)

# In-memory database
products_db = []
prefab_inquiries_db = []

# Sample data initialization
sample_products = [
    Product(
        name="Queen Size Bed",
        description="Comfortable queen size bed with oak finish",
        price=899.99,
        room_type=RoomType.BEDROOM,
        stock_quantity=10
    ),
    Product(
        name="Dining Table Set",
        description="6-seater dining table with chairs",
        price=1299.99,
        room_type=RoomType.DINING_ROOM,
        stock_quantity=5
    )
]

products_db.extend(sample_products)

# Helper functions
def get_product_by_id(product_id: str) -> Optional[Product]:
    for product in products_db:
        if product.id == product_id:
            return product
    return None

def get_inquiry_by_id(inquiry_id: str) -> Optional[PrefabHomeInquiry]:
    for inquiry in prefab_inquiries_db:
        if inquiry.id == inquiry_id:
            return inquiry
    return None

# API Endpoints
@app.get("/products", response_model=List[Product], tags=["Products"])
async def get_all_products():
    """Retrieve all available products"""
    return products_db

@app.get("/products/{room_type}", response_model=List[Product], tags=["Products"])
async def get_products_by_room_type(room_type: RoomType):
    """Retrieve products filtered by room type"""
    return [product for product in products_db if product.room_type == room_type]

@app.get("/products/id/{product_id}", response_model=Product, tags=["Products"])
async def get_product(product_id: str):
    """Retrieve a single product by ID"""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED, tags=["Products"])
async def create_product(product: Product):
    """Create a new product"""
    products_db.append(product)
    return product

@app.put("/products/{product_id}", response_model=Product, tags=["Products"])
async def update_product(product_id: str, updated_product: Product):
    """Update an existing product"""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    product.name = updated_product.name
    product.description = updated_product.description
    product.price = updated_product.price
    product.room_type = updated_product.room_type
    product.stock_quantity = updated_product.stock_quantity
    
    return product

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Products"])
async def delete_product(product_id: str):
    """Delete a product"""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    products_db.remove(product)

@app.get("/prefab-inquiries", response_model=List[PrefabHomeInquiry], tags=["Prefab Home Inquiries"])
async def get_all_inquiries():
    """Retrieve all prefab home inquiries"""
    return prefab_inquiries_db

@app.post("/prefab-inquiries", response_model=PrefabHomeInquiry, status_code=status.HTTP_201_CREATED, tags=["Prefab Home Inquiries"])
async def create_inquiry(inquiry: PrefabHomeInquiry):
    """Create a new prefab home inquiry"""
    prefab_inquiries_db.append(inquiry)
    return inquiry

@app.get("/prefab-inquiries/{inquiry_id}", response_model=PrefabHomeInquiry, tags=["Prefab Home Inquiries"])
async def get_inquiry(inquiry_id: str):
    """Retrieve a single inquiry by ID"""
    inquiry = get_inquiry_by_id(inquiry_id)
    if not inquiry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inquiry not found"
        )
    return inquiry

@app.delete("/prefab-inquiries/{inquiry_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Prefab Home Inquiries"])
async def delete_inquiry(inquiry_id: str):
    """Delete an inquiry"""
    inquiry = get_inquiry_by_id(inquiry_id)
    if not inquiry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inquiry not found"
        )
    prefab_inquiries_db.remove(inquiry)
```
