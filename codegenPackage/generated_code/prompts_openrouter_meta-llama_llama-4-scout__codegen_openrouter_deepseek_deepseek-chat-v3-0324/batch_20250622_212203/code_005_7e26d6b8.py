"""
Generated Code Metadata:
========================
Original URL: https://rarecrew-app.com
Prompt: "Design a RESTful API for a service like Rarecrew that might involve managing inventory and sales through an online shop."
Generated: DETERMINISTIC_7e26d6b8a8994c99
Batch ID: 20250622_212203
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
from datetime import datetime
import uuid
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database models (in-memory for this example)
class User(BaseModel):
    id: str
    username: str
    email: str
    hashed_password: str
    disabled: bool = False

class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    quantity: int
    category: str
    created_at: datetime
    updated_at: datetime

class Order(BaseModel):
    id: str
    user_id: str
    products: List[dict]  # List of {product_id: str, quantity: int}
    total_amount: float
    status: str  # "pending", "completed", "cancelled"
    created_at: datetime
    updated_at: datetime

# Pydantic models for request/response
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: str
    username: str
    email: str

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    category: str

class ProductOut(BaseModel):
    id: str
    name: str
    description: str
    price: float
    quantity: int
    category: str
    created_at: datetime
    updated_at: datetime

class OrderCreate(BaseModel):
    products: List[dict]

class OrderOut(BaseModel):
    id: str
    user_id: str
    products: List[dict]
    total_amount: float
    status: str
    created_at: datetime
    updated_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# In-memory database
db_users = {}
db_products = {}
db_orders = {}

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# Helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str):
    for user_id, user in db_users.items():
        if user.username == username:
            return user
    return None

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Authentication routes
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=UserOut)
async def create_user(user: UserCreate):
    if get_user(user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    user_id = str(uuid.uuid4())
    hashed_password = get_password_hash(user.password)
    db_user = User(
        id=user_id,
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db_users[user_id] = db_user
    return db_user

@app.get("/users/me/", response_model=UserOut)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# Product routes
@app.post("/products/", response_model=ProductOut)
async def create_product(
    product: ProductCreate,
    current_user: User = Depends(get_current_active_user)
):
    product_id = str(uuid.uuid4())
    now = datetime.utcnow()
    db_product = Product(
        id=product_id,
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity,
        category=product.category,
        created_at=now,
        updated_at=now
    )
    db_products[product_id] = db_product
    return db_product

@app.get("/products/", response_model=List[ProductOut])
async def read_products(skip: int = 0, limit: int = 10):
    return list(db_products.values())[skip : skip + limit]

@app.get("/products/{product_id}", response_model=ProductOut)
async def read_product(product_id: str):
    if product_id not in db_products:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_products[product_id]

@app.put("/products/{product_id}", response_model=ProductOut)
async def update_product(
    product_id: str,
    product: ProductCreate,
    current_user: User = Depends(get_current_active_user)
):
    if product_id not in db_products:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product = db_products[product_id]
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity
    db_product.category = product.category
    db_product.updated_at = datetime.utcnow()
    return db_product

@app.delete("/products/{product_id}")
async def delete_product(
    product_id: str,
    current_user: User = Depends(get_current_active_user)
):
    if product_id not in db_products:
        raise HTTPException(status_code=404, detail="Product not found")
    del db_products[product_id]
    return {"message": "Product deleted successfully"}

# Order routes
@app.post("/orders/", response_model=OrderOut)
async def create_order(
    order: OrderCreate,
    current_user: User = Depends(get_current_active_user)
):
    order_id = str(uuid.uuid4())
    now = datetime.utcnow()
    
    # Calculate total amount and validate products
    total_amount = 0.0
    for item in order.products:
        product_id = item.get("product_id")
        quantity = item.get("quantity")
        
        if product_id not in db_products:
            raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
        
        product = db_products[product_id]
        if product.quantity < quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Not enough stock for product {product_id}"
            )
        
        total_amount += product.price * quantity
    
    db_order = Order(
        id=order_id,
        user_id=current_user.id,
        products=order.products,
        total_amount=total_amount,
        status="
