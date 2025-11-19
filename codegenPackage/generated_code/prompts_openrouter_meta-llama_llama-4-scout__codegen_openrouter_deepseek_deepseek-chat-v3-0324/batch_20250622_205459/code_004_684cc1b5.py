"""
Generated Code Metadata:
========================
Original URL: https://mfxhk.com
Prompt: Design a referral program similar to MFX-Online Trade's, allowing users to earn commissions from deposits made by referred friends, and describe its benefits and potential drawbacks.
Generated: DETERMINISTIC_684cc1b5aa2408af
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, validator, Field
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import databases
import sqlalchemy
from sqlalchemy import ForeignKey

# Database configuration
DATABASE_URL = "sqlite:///./referral_program.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Security configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

class ReferralStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str
    email: str
    hashed_password: str
    role: UserRole = UserRole.USER
    referral_code: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    balance: float = 0.0
    disabled: bool = False

    @validator('email')
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email format")
        return v

class Referral(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    referrer_id: str
    referee_id: str
    deposit_amount: float
    commission_percentage: float
    commission_earned: float
    status: ReferralStatus = ReferralStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None

class Deposit(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    amount: float
    currency: str = "USD"
    status: ReferralStatus = ReferralStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None

# Database tables
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String, unique=True),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("role", sqlalchemy.String),
    sqlalchemy.Column("referral_code", sqlalchemy.String, unique=True),
    sqlalchemy.Column("balance", sqlalchemy.Float),
    sqlalchemy.Column("disabled", sqlalchemy.Boolean),
)

referrals = sqlalchemy.Table(
    "referrals",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("referrer_id", sqlalchemy.String, ForeignKey("users.id")),
    sqlalchemy.Column("referee_id", sqlalchemy.String, ForeignKey("users.id")),
    sqlalchemy.Column("deposit_amount", sqlalchemy.Float),
    sqlalchemy.Column("commission_percentage", sqlalchemy.Float),
    sqlalchemy.Column("commission_earned", sqlalchemy.Float),
    sqlalchemy.Column("status", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("completed_at", sqlalchemy.DateTime, nullable=True),
)

deposits = sqlalchemy.Table(
    "deposits",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey("users.id")),
    sqlalchemy.Column("amount", sqlalchemy.Float),
    sqlalchemy.Column("currency", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("completed_at", sqlalchemy.DateTime, nullable=True),
)

# Create tables
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

# Dependency to get DB connection
async def get_db():
    async with database.transaction():
        yield database

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def get_user(username: str):
    query = users.select().where(users.c.username == username)
    user = await database.fetch_one(query)
    if user:
        return User(**user)

async def authenticate_user(username: str, password: str):
    user = await get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real app, you would validate the token here
    # For simplicity, we'll just get the user by username
    user = await get_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API Endpoints
@app.post("/register/")
async def register_user(username: str, email: str, password: str, referral_code: Optional[str] = None):
    # Check if user exists
    existing_user = await get_user(username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Create new user
    hashed_password = get_password_hash(password)
    user = User(username=username, email=email, hashed_password=hashed_password)
    
    # Insert user into database
    query = users.insert().values(**user.dict())
    await database.execute(query)
    
    # If referral code was provided, create referral relationship
    if referral_code:
        referrer_query = users.select().where(users.c.referral_code == referral_code)
        referrer = await database.fetch_one(referrer_query)
        if referrer:
            referral = Referral(
                referrer_id=referrer["id"],
                referee_id=user.id,
                deposit_amount=0.0,
                commission_percentage=0.1,  # 10% commission
                commission_earned=0.0
            )
            query = referrals.insert().values(**referral.dict())
            await database.execute(query)
    
    return {"message": "User registered successfully"}

@app.post("/deposit/")
async def create_deposit(
    amount: float,
    current_user: User = Depends(get_current_active_user),
    db: databases.Database = Depends(get_db)
):
    # Create deposit record
    deposit = Deposit(user_id=current_user.id, amount=amount)
    query = deposits.insert().values(**deposit.dict())
    await db.execute(query)
    
    # Check if this user was referred
    referral_query = referrals.select().where(referrals.c.referee_id == current_user.id)
    referral = await db.fetch_one(referral_query)
    
    if referral and referral["status"] == ReferralStatus.PENDING.value:
        # Calculate commission
        commission = amount * referral["commission_percentage"]
        
        # Update referral status
        update_referral_query = (
            referrals.update()
            .where(referrals.c.id == referral["id"])
            .values(
                deposit_amount=amount,
                commission_earned=commission,
                status=ReferralStatus.COMPLETED,
                completed_at=datetime.utcnow()
            )
        )
        await db.execute(update_referral_query)
        
        # Update referrer's balance
        referrer_query = users.select().where(users.c.id == referral["referrer_id"])
        referrer = await db.fetch_one(referrer_query)
        
        if referrer:
            update_user_query = (
                users.update()
                .where(users.c.id == referrer["id"])
                .values(balance=referrer["balance"] + commission)
            )
            await db.execute(update_user_query)
    
    return {"message": "Deposit created successfully"}

@app.get("/user/referrals/")
async def get_user_referrals(
    current_user: User = Depends(get_current_active_user),
    db: databases.Database = Depends(get_db)
):
    query = referrals.select().where(referrals.c.referrer_id == current_user.id
