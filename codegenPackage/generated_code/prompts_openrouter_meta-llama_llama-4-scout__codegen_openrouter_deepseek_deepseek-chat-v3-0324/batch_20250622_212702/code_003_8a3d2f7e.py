"""
Generated Code Metadata:
========================
Original URL: https://perucotiza.com
Prompt: Design a system for managing supplier relationships and product offerings in an online automotive parts marketplace, ensuring that products are original, OEM, or alternative.
Generated: DETERMINISTIC_8a3d2f7eca94e4ac
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import uuid
from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing_extensions import Annotated

# Constants
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Enums
class ProductType(str, Enum):
    ORIGINAL = "original"
    OEM = "oem"
    ALTERNATIVE = "alternative"

class SupplierStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

# Models
class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool = False

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    price: float
    stock: int
    product_type: ProductType
    supplier_id: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @validator('price')
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Price must be positive')
        return v

    @validator('stock')
    def stock_must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError('Stock cannot be negative')
        return v

class Supplier(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    contact_email: str
    phone: str
    address: str
    status: SupplierStatus = SupplierStatus.ACTIVE
    products: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

# Database (simulated)
db_users = {
    "admin": {
        "username": "admin",
        "email": "admin@example.com",
        "full_name": "Admin User",
        "disabled": False,
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGgaXNlK"  # password: secret
    }
}

db_suppliers: Dict[str, Supplier] = {}
db_products: Dict[str, Product] = {}

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
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
    user = get_user(db_users, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Routes
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db_users, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

@app.post("/suppliers/", response_model=Supplier)
async def create_supplier(
    supplier: Supplier,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    if supplier.id in db_suppliers:
        raise HTTPException(status_code=400, detail="Supplier already exists")
    db_suppliers[supplier.id] = supplier
    return supplier

@app.get("/suppliers/", response_model=List[Supplier])
async def list_suppliers(
    current_user: Annotated[User, Depends(get_current_active_user)],
    status: Optional[SupplierStatus] = None
):
    if status:
        return [s for s in db_suppliers.values() if s.status == status]
    return list(db_suppliers.values())

@app.get("/suppliers/{supplier_id}", response_model=Supplier)
async def get_supplier(
    supplier_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    if supplier_id not in db_suppliers:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_suppliers[supplier_id]

@app.put("/suppliers/{supplier_id}", response_model=Supplier)
async def update_supplier(
    supplier_id: str,
    supplier: Supplier,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    if supplier_id not in db_suppliers:
        raise HTTPException(status_code=404, detail="Supplier not found")
    db_suppliers[supplier_id] = supplier
    return supplier

@app.post("/products/", response_model=Product)
async def create_product(
    product: Product,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    if product.supplier_id not in db_suppliers:
        raise HTTPException(status_code=400, detail="Supplier does not exist")
    if product.id in db_products:
        raise HTTPException(status_code=400, detail="Product already exists")
    db_products[product.id] = product
    db_suppliers[product.supplier_id].products.append(product.id)
    return product

@app.get("/products/", response_model=List[Product])
async def list_products(
    current_user: Annotated[User, Depends(get_current_active_user)],
    product_type: Optional[ProductType] = None,
    supplier_id: Optional[str] = None
):
    products = list(db_products.values())
    if product_type:
        products = [p for p in products if p.product_type == product_type]
    if supplier_id:
        products = [p for p in products if p.supplier_id == supplier_id]
    return products

@app.get("/products/{product_id}", response_model=Product)
async def get_product(
    product_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    if product_id not in db_products:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_products[product_id]

@app.put("/products/{product_id}", response_model=Product)
async def update_product(
    product_id: str,
    product: Product,
    current_user: Annotated[User, Depends
