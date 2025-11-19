"""
Generated Code Metadata:
========================
Original URL: https://tecelagembordartes.com.br
Prompt: Design a RESTful API for managing products, catalogs, and customer information for a home textile company like Tecelagem Bordartes.
Generated: DETERMINISTIC_e62d26621a3582dc
Batch ID: 20250622_210703
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
from typing import Annotated

# Initialize FastAPI app
app = FastAPI(
    title="Bordartes Textile API",
    description="RESTful API for managing products, catalogs, and customer information",
    version="1.0.0"
)

# Security configurations
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (would be replaced with actual database in production)
fake_db = {
    "users": {},
    "products": {},
    "catalogs": {},
    "customers": {}
}

# Pydantic models
class UserBase(BaseModel):
    username: str
    email: str
    full_name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    disabled: bool = False

class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    category: str
    stock_quantity: int
    created_at: datetime
    updated_at: datetime

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category: str
    stock_quantity: int

class Catalog(BaseModel):
    id: str
    name: str
    description: str
    products: List[str]
    created_at: datetime
    updated_at: datetime

class CatalogCreate(BaseModel):
    name: str
    description: str
    products: List[str]

class Customer(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    address: str
    created_at: datetime
    updated_at: datetime

class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

# Helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str):
    if username in fake_db["users"]:
        user_dict = fake_db["users"][username]
        return User(**user_dict)
    return None

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
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
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Authentication endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
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

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    if user.username in fake_db["users"]:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["id"] = str(uuid.uuid4())
    user_dict["password"] = hashed_password
    user_dict["disabled"] = False
    fake_db["users"][user.username] = user_dict
    return user_dict

# Product endpoints
@app.post("/products/", response_model=Product)
async def create_product(
    product: ProductCreate,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    product_id = str(uuid.uuid4())
    now = datetime.utcnow()
    product_dict = product.dict()
    product_dict["id"] = product_id
    product_dict["created_at"] = now
    product_dict["updated_at"] = now
    fake_db["products"][product_id] = product_dict
    return product_dict

@app.get("/products/", response_model=List[Product])
async def read_products(skip: int = 0, limit: int = 10):
    products = list(fake_db["products"].values())[skip : skip + limit]
    return products

@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: str):
    if product_id not in fake_db["products"]:
        raise HTTPException(status_code=404, detail="Product not found")
    return fake_db["products"][product_id]

@app.put("/products/{product_id}", response_model=Product)
async def update_product(
    product_id: str,
    product: ProductCreate,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    if product_id not in fake_db["products"]:
        raise HTTPException(status_code=404, detail="Product not found")
    product_dict = product.dict()
    product_dict["id"] = product_id
    product_dict["updated_at"] = datetime.utcnow()
    product_dict["created_at"] = fake_db["products"][product_id]["created_at"]
    fake_db["products"][product_id] = product_dict
    return product_dict

@app.delete("/products/{product_id}")
async def delete_product(
    product_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    if product_id not in fake_db["products"]:
        raise HTTPException(status_code=404, detail="Product not found")
    del fake_db["products"][product_id]
    return {"message": "Product deleted successfully"}

# Catalog endpoints
@app.post("/catalogs/", response_model=Catalog)
async def create_catalog(
    catalog: CatalogCreate,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    catalog_id = str(uuid.uuid4())
    now = datetime.utcnow()
    catalog_dict = catalog.dict()
    catalog_dict["id"] = catalog_id
    catalog_dict["created_at"] = now
    catalog_dict["updated_at"] = now
    fake_db["catalogs"][catalog_id] = catalog_dict
    return catalog_dict

@app.get("/catalogs/", response_model=List[Catalog])
async def read_catalogs(skip: int = 0, limit: int = 10):
    catalogs = list(fake_db["catalogs"].values())[skip : skip + limit]
    return catalogs

@app.get("/catalogs/{catalog_id}", response_model=Catalog)
async def read_catalog(catalog_id: str):
    if catalog_id not in fake_db["catalogs"]:
        raise HTTPException(status_code=404, detail="Catalog not found")
    return fake_db["catalogs"][catalog_id
