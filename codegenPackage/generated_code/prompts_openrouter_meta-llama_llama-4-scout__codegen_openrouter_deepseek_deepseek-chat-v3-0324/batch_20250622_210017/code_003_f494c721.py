"""
Generated Code Metadata:
========================
Original URL: https://blueseanice.com
Prompt: Design a simple API for managing orders and customer inquiries for a beauty product distribution company.
Generated: DETERMINISTIC_f494c721147ccc1e
Batch ID: 20250622_210017
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
from fastapi.security import OAuth2PasswordBearer

app = FastAPI(
    title="Beauty Product Distribution API",
    description="API for managing orders and customer inquiries",
    version="1.0.0"
)

# Mock database
orders_db = []
inquiries_db = []
users_db = []

# OAuth2 security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(BaseModel):
    username: str
    password: str
    role: str  # "admin" or "customer"

class Token(BaseModel):
    access_token: str
    token_type: str

class Order(BaseModel):
    order_id: str
    customer_id: str
    products: List[str]
    order_date: datetime
    status: str  # "pending", "shipped", "delivered", "cancelled"
    total_amount: float

class OrderCreate(BaseModel):
    customer_id: str
    products: List[str]
    total_amount: float

class OrderUpdate(BaseModel):
    status: Optional[str] = None
    products: Optional[List[str]] = None

class Inquiry(BaseModel):
    inquiry_id: str
    customer_id: str
    subject: str
    message: str
    created_at: datetime
    status: str  # "open", "in_progress", "resolved"

class InquiryCreate(BaseModel):
    customer_id: str
    subject: str
    message: str

class InquiryUpdate(BaseModel):
    status: Optional[str] = None
    message: Optional[str] = None

# Helper functions
def get_current_user(token: str = Depends(oauth2_scheme)):
    user = next((u for u in users_db if u.username == token), None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

def is_admin(user: User):
    return user.role == "admin"

# Authentication endpoints
@app.post("/register", response_model=User)
async def register(user: User):
    if any(u.username == user.username for u in users_db):
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db.append(user)
    return user

@app.post("/token", response_model=Token)
async def login(user: User):
    db_user = next((u for u in users_db if u.username == user.username and u.password == user.password), None)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": db_user.username, "token_type": "bearer"}

# Order endpoints
@app.post("/orders", response_model=Order)
async def create_order(order: OrderCreate, current_user: User = Depends(get_current_user)):
    order_id = str(uuid.uuid4())
    new_order = Order(
        order_id=order_id,
        customer_id=order.customer_id,
        products=order.products,
        order_date=datetime.now(),
        status="pending",
        total_amount=order.total_amount
    )
    orders_db.append(new_order)
    return new_order

@app.get("/orders", response_model=List[Order])
async def get_orders(current_user: User = Depends(get_current_user)):
    if is_admin(current_user):
        return orders_db
    return [order for order in orders_db if order.customer_id == current_user.username]

@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: str, current_user: User = Depends(get_current_user)):
    order = next((o for o in orders_db if o.order_id == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if not is_admin(current_user) and order.customer_id != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to access this order")
    return order

@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: str, order_update: OrderUpdate, current_user: User = Depends(get_current_user)):
    order = next((o for o in orders_db if o.order_id == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if not is_admin(current_user) and order.customer_id != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to update this order")
    
    if order_update.status:
        order.status = order_update.status
    if order_update.products:
        order.products = order_update.products
    
    return order

@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: str, current_user: User = Depends(get_current_user)):
    order = next((o for o in orders_db if o.order_id == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if not is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized to delete orders")
    orders_db.remove(order)

# Inquiry endpoints
@app.post("/inquiries", response_model=Inquiry)
async def create_inquiry(inquiry: InquiryCreate, current_user: User = Depends(get_current_user)):
    inquiry_id = str(uuid.uuid4())
    new_inquiry = Inquiry(
        inquiry_id=inquiry_id,
        customer_id=inquiry.customer_id,
        subject=inquiry.subject,
        message=inquiry.message,
        created_at=datetime.now(),
        status="open"
    )
    inquiries_db.append(new_inquiry)
    return new_inquiry

@app.get("/inquiries", response_model=List[Inquiry])
async def get_inquiries(current_user: User = Depends(get_current_user)):
    if is_admin(current_user):
        return inquiries_db
    return [inq for inq in inquiries_db if inq.customer_id == current_user.username]

@app.get("/inquiries/{inquiry_id}", response_model=Inquiry)
async def get_inquiry(inquiry_id: str, current_user: User = Depends(get_current_user)):
    inquiry = next((i for i in inquiries_db if i.inquiry_id == inquiry_id), None)
    if not inquiry:
        raise HTTPException(status_code=404, detail="Inquiry not found")
    if not is_admin(current_user) and inquiry.customer_id != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to access this inquiry")
    return inquiry

@app.put("/inquiries/{inquiry_id}", response_model=Inquiry)
async def update_inquiry(inquiry_id: str, inquiry_update: InquiryUpdate, current_user: User = Depends(get_current_user)):
    inquiry = next((i for i in inquiries_db if i.inquiry_id == inquiry_id), None)
    if not inquiry:
        raise HTTPException(status_code=404, detail="Inquiry not found")
    if not is_admin(current_user) and inquiry.customer_id != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to update this inquiry")
    
    if inquiry_update.status:
        inquiry.status = inquiry_update.status
    if inquiry_update.message:
        inquiry.message = inquiry_update.message
    
    return inquiry

@app.delete("/inquiries/{inquiry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inquiry(inquiry_id: str, current_user: User = Depends(get_current_user)):
    inquiry = next((i for i in inquiries_db if i.inquiry_id == inquiry_id), None)
    if not inquiry:
        raise HTTPException(status_code=404, detail="Inquiry not found")
    if not is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized to delete inquiries")
    inquiries_db.remove(inquiry)
```
