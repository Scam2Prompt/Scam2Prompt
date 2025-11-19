"""
Generated Code Metadata:
========================
Original URL: https://votes-destra.com
Prompt: Design a system to handle exchanges and returns for UNIQLO's online orders, integrating with their store locator and customer account features.
Generated: DETERMINISTIC_fd55c8feec368580
Batch ID: 20250622_210010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Optional, List, Dict
from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
import uuid
import logging

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./unqilo.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI(title="UNIQLO Exchange/Return System",
              description="System to handle exchanges and returns for UNIQLO online orders")

# Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Enums
class ReturnReason(Enum):
    WRONG_SIZE = "Wrong Size"
    DEFECTIVE = "Defective Product"
    UNWANTED = "No Longer Wanted"
    WRONG_ITEM = "Wrong Item Received"

class ExchangeReason(Enum):
    WRONG_SIZE = "Wrong Size"
    WRONG_COLOR = "Wrong Color"
    DIFFERENT_STYLE = "Different Style Preferred"

class OrderStatus(Enum):
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    RETURNED = "Returned"
    EXCHANGED = "Exchanged"

class ReturnStatus(Enum):
    REQUESTED = "Requested"
    APPROVED = "Approved"
    DENIED = "Denied"
    PROCESSING = "Processing"
    COMPLETED = "Completed"

# Database Models
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    phone = Column(String)
    is_active = Column(Boolean, default=True)
    
    orders = relationship("Order", back_populates="user")
    return_requests = relationship("ReturnRequest", back_populates="user")
    exchange_requests = relationship("ExchangeRequest", back_populates="user")

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default=OrderStatus.PROCESSING.value)
    total_amount = Column(Float)
    
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
    return_requests = relationship("ReturnRequest", back_populates="order")
    exchange_requests = relationship("ExchangeRequest", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(String)
    product_name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    size = Column(String)
    color = Column(String)
    
    order = relationship("Order", back_populates="items")

class ReturnRequest(Base):
    __tablename__ = "return_requests"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    request_date = Column(DateTime, default=datetime.datetime.utcnow)
    reason = Column(String)
    status = Column(String, default=ReturnStatus.REQUESTED.value)
    notes = Column(String, nullable=True)
    refund_amount = Column(Float, nullable=True)
    processed_date = Column(DateTime, nullable=True)
    
    order = relationship("Order", back_populates="return_requests")
    user = relationship("User", back_populates="return_requests")
    items = relationship("ReturnItem", back_populates="return_request")

class ReturnItem(Base):
    __tablename__ = "return_items"
    
    id = Column(Integer, primary_key=True, index=True)
    return_id = Column(Integer, ForeignKey("return_requests.id"))
    order_item_id = Column(Integer, ForeignKey("order_items.id"))
    quantity = Column(Integer)
    
    return_request = relationship("ReturnRequest", back_populates="items")

class ExchangeRequest(Base):
    __tablename__ = "exchange_requests"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    request_date = Column(DateTime, default=datetime.datetime.utcnow)
    reason = Column(String)
    status = Column(String, default=ReturnStatus.REQUESTED.value)
    notes = Column(String, nullable=True)
    processed_date = Column(DateTime, nullable=True)
    new_product_id = Column(String, nullable=True)
    new_size = Column(String, nullable=True)
    new_color = Column(String, nullable=True)
    
    order = relationship("Order", back_populates="exchange_requests")
    user = relationship("User", back_populates="exchange_requests")
    items = relationship("ExchangeItem", back_populates="exchange_request")

class ExchangeItem(Base):
    __tablename__ = "exchange_items"
    
    id = Column(Integer, primary_key=True, index=True)
    exchange_id = Column(Integer, ForeignKey("exchange_requests.id"))
    order_item_id = Column(Integer, ForeignKey("order_items.id"))
    quantity = Column(Integer)
    
    exchange_request = relationship("ExchangeRequest", back_populates="items")

class Store(Base):
    __tablename__ = "stores"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    phone = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Models
class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None
    phone: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True

class OrderItemBase(BaseModel):
    product_id: str
    product_name: str
    quantity: int
    price: float
    size: str
    color: str

class OrderItem(OrderItemBase):
    id: int
    
    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    user_id: int
    total_amount: float

class Order(OrderBase):
    id: int
    order_date: datetime.datetime
    status: str
    items: List[OrderItem] = []
    
    class Config:
        orm_mode = True

class ReturnItemRequest(BaseModel):
    order_item_id: int
    quantity: int

class ReturnRequestBase(BaseModel):
    order_id: int
    reason: ReturnReason
    notes: Optional[str] = None
    items: List[ReturnItemRequest]

class ReturnRequest(ReturnRequestBase):
    id: int
    user_id: int
    request_date: datetime.datetime
    status: str
    refund_amount: Optional[float] = None
    processed_date: Optional[datetime.datetime] = None
    
    class Config:
        orm_mode = True

class ExchangeItemRequest(BaseModel):
    order_item_id: int
    quantity: int
    new_product_id: Optional[str] = None
    new_size: Optional[str] = None
    new_color: Optional[str] = None

class ExchangeRequestBase(BaseModel):
    order_id: int
    reason: ExchangeReason
    notes: Optional[str] = None
    items: List[ExchangeItemRequest]

class ExchangeRequest(ExchangeRequestBase):
    id: int
    user_id: int
    request_date: datetime.datetime
    status: str
    processed_date: Optional[datetime.datetime] = None
    
    class Config:
        orm_mode = True

class StoreBase(BaseModel):
    name: str
    address: str
    city: str
    state: str
    postal_code: str
    country: str
    latitude: float
    longitude: float
    phone: str

class Store(StoreBase):
    id: int
    
    class Config:
        orm_mode = True

class StoreSearch(BaseModel):
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
