"""
Generated Code Metadata:
========================
Original URL: https://kadma-wine.co.il
Prompt: "Design a RESTful API for a wine club platform, allowing users to purchase wines, manage subscriptions, and access exclusive content, similar to Kadma Wine's services."
Generated: DETERMINISTIC_a1c0c89f1194d3da
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
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import uuid
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database models (simplified for example)
class User(BaseModel):
    id: str
    email: EmailStr
    hashed_password: str
    full_name: Optional[str] = None
    is_active: bool = True
    is_admin: bool = False

class Wine(BaseModel):
    id: str
    name: str
    description: str
    price: float
    region: str
    vintage: int
    stock_quantity: int
    is_featured: bool = False

class SubscriptionPlan(BaseModel):
    id: str
    name: str
    description: str
    price_per_month: float
    wines_per_month: int
    is_active: bool = True

class UserSubscription(BaseModel):
    id: str
    user_id: str
    plan_id: str
    start_date: datetime
    end_date: Optional[datetime] = None
    is_active: bool = True

class Order(BaseModel):
    id: str
    user_id: str
    wine_id: str
    quantity: int
    order_date: datetime
    status: str = "pending"

class Content(BaseModel):
    id: str
    title: str
    description: str
    content_url: str
    is_premium: bool = True
    publish_date: datetime

# Mock database
db = {
    "users": {},
    "wines": {},
    "subscription_plans": {},
    "user_subscriptions": {},
    "orders": {},
    "content": {}
}

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(
    title="Wine Club API",
    description="API for managing wine club subscriptions, purchases, and content",
    version="1.0.0"
)

# Helper functions
def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

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
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db["users"].get(user_id)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Authentication endpoints
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = None
    for u in db["users"].values():
        if u.email == form_data.username:
            user = u
            break
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/register")
async def register_user(email: EmailStr, password: str, full_name: Optional[str] = None):
    if any(u.email == email for u in db["users"].values()):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_id = str(uuid.uuid4())
    hashed_password = get_password_hash(password)
    user = User(
        id=user_id,
        email=email,
        hashed_password=hashed_password,
        full_name=full_name
    )
    db["users"][user_id] = user
    return {"message": "User created successfully", "user_id": user_id}

# Wine endpoints
@app.get("/wines", response_model=List[Wine])
async def list_wines(featured: bool = False):
    if featured:
        return [wine for wine in db["wines"].values() if wine.is_featured]
    return list(db["wines"].values())

@app.get("/wines/{wine_id}", response_model=Wine)
async def get_wine(wine_id: str):
    wine = db["wines"].get(wine_id)
    if not wine:
        raise HTTPException(status_code=404, detail="Wine not found")
    return wine

# Subscription endpoints
@app.get("/subscription-plans", response_model=List[SubscriptionPlan])
async def list_subscription_plans():
    return [plan for plan in db["subscription_plans"].values() if plan.is_active]

@app.post("/subscriptions", response_model=UserSubscription)
async def create_subscription(
    plan_id: str,
    current_user: User = Depends(get_current_active_user)
):
    plan = db["subscription_plans"].get(plan_id)
    if not plan or not plan.is_active:
        raise HTTPException(status_code=404, detail="Subscription plan not found or inactive")
    
    # Check if user already has an active subscription
    for sub in db["user_subscriptions"].values():
        if sub.user_id == current_user.id and sub.is_active:
            raise HTTPException(status_code=400, detail="User already has an active subscription")
    
    subscription_id = str(uuid.uuid4())
    start_date = datetime.utcnow()
    subscription = UserSubscription(
        id=subscription_id,
        user_id=current_user.id,
        plan_id=plan_id,
        start_date=start_date,
        is_active=True
    )
    db["user_subscriptions"][subscription_id] = subscription
    return subscription

@app.get("/subscriptions/me", response_model=UserSubscription)
async def get_my_subscription(current_user: User = Depends(get_current_active_user)):
    for sub in db["user_subscriptions"].values():
        if sub.user_id == current_user.id and sub.is_active:
            return sub
    raise HTTPException(status_code=404, detail="No active subscription found")

@app.delete("/subscriptions/{subscription_id}")
async def cancel_subscription(
    subscription_id: str,
    current_user: User = Depends(get_current_active_user)
):
    subscription = db["user_subscriptions"].get(subscription_id)
    if not subscription or subscription.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    subscription.is_active = False
    subscription.end_date = datetime.utcnow()
    return {"message": "Subscription cancelled successfully"}

# Order endpoints
@app.post("/orders", response_model=Order)
async def create_order(
    wine_id: str,
    quantity: int,
    current_user: User = Depends(get_current_active_user)
):
    wine = db["wines"].get(wine_id)
    if not wine:
        raise HTTPException(status_code=404, detail="Wine not found")
    
    if wine.stock_quantity < quantity:
        raise HTTPException(status_code=400, detail="Not enough stock available")
    
    order_id = str(uuid.uuid4())
    order = Order(
        id=order_id,
        user_id=current_user.id,
        wine_id=wine_id,
        quantity=quantity,
        order_date=datetime.utcnow()
    )
    db["orders"][order_id] = order
    
    # Update stock
    wine.stock_quantity -= quantity
    return
