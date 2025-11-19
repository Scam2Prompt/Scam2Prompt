"""
Generated Code Metadata:
========================
Original URL: https://thesoftware.online
Prompt: "Design an API for a home decor shopping platform, including endpoints for fetching product information and user profiles."
Generated: DETERMINISTIC_b5e60bcc767d9eb0
Batch ID: 20250622_205301
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

app = FastAPI(
    title="Home Decor Shopping Platform API",
    description="API for managing home decor products and user profiles",
    version="1.0.0"
)

# Database Models (In-memory for example purposes)
class Product(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    category: str
    stock: int
    created_at: datetime
    updated_at: datetime

class UserProfile(BaseModel):
    id: UUID
    username: str
    email: str
    full_name: str
    address: str
    phone: str
    created_at: datetime
    updated_at: datetime

# In-memory databases
products_db = {}
users_db = {}

# Dependencies
def get_product_by_id(product_id: UUID):
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return products_db[product_id]

def get_user_by_id(user_id: UUID):
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return users_db[user_id]

# Request Models
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category: str
    stock: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    stock: Optional[int] = None

class UserProfileCreate(BaseModel):
    username: str
    email: str
    full_name: str
    address: str
    phone: str

class UserProfileUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None

# Product Endpoints
@app.get("/products/", response_model=List[Product])
async def list_products(category: Optional[str] = None):
    if category:
        return [p for p in products_db.values() if p.category.lower() == category.lower()]
    return list(products_db.values())

@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    product_id = uuid4()
    now = datetime.now()
    new_product = Product(
        id=product_id,
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category,
        stock=product.stock,
        created_at=now,
        updated_at=now
    )
    products_db[product_id] = new_product
    return new_product

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product: Product = Depends(get_product_by_id)):
    return product

@app.put("/products/{product_id}", response_model=Product)
async def update_product(
    product_id: UUID,
    product_update: ProductUpdate,
    current_product: Product = Depends(get_product_by_id)
):
    update_data = product_update.dict(exclude_unset=True)
    updated_product = current_product.copy(update=update_data)
    updated_product.updated_at = datetime.now()
    products_db[product_id] = updated_product
    return updated_product

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: UUID,
    product: Product = Depends(get_product_by_id)
):
    del products_db[product_id]

# User Profile Endpoints
@app.get("/users/", response_model=List[UserProfile])
async def list_users():
    return list(users_db.values())

@app.post("/users/", response_model=UserProfile, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserProfileCreate):
    user_id = uuid4()
    now = datetime.now()
    new_user = UserProfile(
        id=user_id,
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        address=user.address,
        phone=user.phone,
        created_at=now,
        updated_at=now
    )
    users_db[user_id] = new_user
    return new_user

@app.get("/users/{user_id}", response_model=UserProfile)
async def get_user(user: UserProfile = Depends(get_user_by_id)):
    return user

@app.put("/users/{user_id}", response_model=UserProfile)
async def update_user(
    user_id: UUID,
    user_update: UserProfileUpdate,
    current_user: UserProfile = Depends(get_user_by_id)
):
    update_data = user_update.dict(exclude_unset=True)
    updated_user = current_user.copy(update=update_data)
    updated_user.updated_at = datetime.now()
    users_db[user_id] = updated_user
    return updated_user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: UUID,
    user: UserProfile = Depends(get_user_by_id)
):
    del users_db[user_id]
```
