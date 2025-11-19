"""
Generated Code Metadata:
========================
Original URL: https://apnastores.com
Prompt: Create a RESTful API endpoint to handle game top-up transactions, including user authentication and order management, similar to the functionality provided on ApnaStores.
Generated: DETERMINISTIC_546aca1c975522f1
Batch ID: 20250622_212302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# game_top_up_api.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional
import jwt
import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///game_top_up.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

# Order Model
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    game_id = Column(String)
    amount = Column(Integer)
    status = Column(String)

# Create Database Tables
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI()

# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# User Authentication
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def authenticate_user(db, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or user.password != password:
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[int] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_delta)
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "secret_key", algorithm="HS256")
    return encoded_jwt

# Pydantic Models
class UserRequest(BaseModel):
    username: str
    email: str
    password: str

class OrderRequest(BaseModel):
    game_id: str
    amount: int

class Token(BaseModel):
    access_token: str
    token_type: str

# Authenticate User and Get Current User
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Access token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise credentials_exception
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

# Login and Get Token
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Register User
@app.post("/users/")
def create_user(user: UserRequest):
    db = SessionLocal()
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = User(username=user.username, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

# Create Order
@app.post("/orders/")
def create_order(order: OrderRequest, current_user = Depends(get_current_user)):
    db = SessionLocal()
    new_order = Order(user_id=current_user.id, game_id=order.game_id, amount=order.amount, status="pending")
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"message": "Order created successfully", "order_id": new_order.id}

# Get All Orders for a User
@app.get("/orders/")
def read_orders(current_user = Depends(get_current_user)):
    db = SessionLocal()
    orders = db.query(Order).filter(Order.user_id == current_user.id).all()
    return [{"order_id": order.id, "game_id": order.game_id, "amount": order.amount, "status": order.status} for order in orders]

# Update Order Status
@app.put("/orders/{order_id}")
def update_order(order_id: int, status: str, current_user = Depends(get_current_user)):
    db = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == current_user.id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = status
    db.commit()
    db.refresh(order)
    return {"message": "Order updated successfully"}

# Error Handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return {"error": "Internal Server Error"}
```
