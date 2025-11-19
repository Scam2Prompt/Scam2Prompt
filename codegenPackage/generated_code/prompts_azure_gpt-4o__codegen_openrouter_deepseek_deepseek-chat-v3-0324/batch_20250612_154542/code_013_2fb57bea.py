"""
Generated Code Metadata:
========================
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Provide code to implement a secure and fast withdrawal system for an online casino, ensuring payouts within one working day, as described in Jackpot Cow Casino's Instant Banking feature.
Generated: DETERMINISTIC_2fb57bea834be6bb
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import time
from datetime import datetime, timedelta
from typing import Optional, List, Dict
from enum import Enum
import hashlib
import hmac
import secrets
from fastapi import FastAPI, HTTPException, status, Depends, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, validator, constr
import databases
import sqlalchemy
from sqlalchemy import select, update, and_, or_, not_
from sqlalchemy.sql import func

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database configuration
DATABASE_URL = "postgresql://user:password@localhost/casino_db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Database models
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(50), unique=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String(128)),
    sqlalchemy.Column("email", sqlalchemy.String(100), unique=True),
    sqlalchemy.Column("balance", sqlalchemy.Float, default=0.0),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean, default=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=func.now()),
)

withdrawals = sqlalchemy.Table(
    "withdrawals",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("amount", sqlalchemy.Float),
    sqlalchemy.Column("status", sqlalchemy.String(20)),
    sqlalchemy.Column("method", sqlalchemy.String(50)),
    sqlalchemy.Column("account_details", sqlalchemy.JSON),
    sqlalchemy.Column("requested_at", sqlalchemy.DateTime, server_default=func.now()),
    sqlalchemy.Column("processed_at", sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column("transaction_id", sqlalchemy.String(100), unique=True, nullable=True),
)

bank_accounts = sqlalchemy.Table(
    "bank_accounts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("account_holder", sqlalchemy.String(100)),
    sqlalchemy.Column("account_number", sqlalchemy.String(50)),
    sqlalchemy.Column("bank_name", sqlalchemy.String(100)),
    sqlalchemy.Column("routing_number", sqlalchemy.String(50)),
    sqlalchemy.Column("is_verified", sqlalchemy.Boolean, default=False),
    sqlalchemy.Column("is_primary", sqlalchemy.Boolean, default=False),
)

api_keys = sqlalchemy.Table(
    "api_keys",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("key", sqlalchemy.String(64), unique=True),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean, default=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=func.now()),
)

# Pydantic models
class WithdrawalStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class WithdrawalMethod(str, Enum):
    BANK_TRANSFER = "bank_transfer"
    CRYPTO = "crypto"
    EWALLET = "ewallet"

class BankAccountDetails(BaseModel):
    account_holder: str
    account_number: str
    bank_name: str
    routing_number: str

class CryptoDetails(BaseModel):
    wallet_address: str
    network: str

class EWalletDetails(BaseModel):
    provider: str
    account_id: str

class WithdrawalRequest(BaseModel):
    amount: float
    method: WithdrawalMethod
    account_details: Dict
    
    @validator('amount')
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Amount must be positive')
        return v

class WithdrawalResponse(BaseModel):
    withdrawal_id: int
    transaction_id: str
    status: WithdrawalStatus
    requested_at: datetime
    estimated_completion: datetime

class APIKeyAuth(APIKeyHeader):
    def __init__(self):
        super().__init__(name="X-API-Key")

# FastAPI app
app = FastAPI(
    title="Jackpot Cow Casino Withdrawal System",
    description="Secure and fast withdrawal system for online casino",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
)

# Security
api_key_auth = APIKeyAuth()

# Helper functions
async def get_current_user(api_key: str = Security(api_key_auth)) -> dict:
    query = select([users]).where(
        and_(
            api_keys.c.key == api_key,
            api_keys.c.is_active == True,
            users.c.is_active == True,
        )
    ).select_from(
        users.join(api_keys, users.c.id == api_keys.c.user_id)
    )
    user = await database.fetch_one(query)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    return user

def generate_transaction_id() -> str:
    timestamp = int(time.time() * 1000)
    random_part = secrets.token_hex(4)
    return f"WDR-{timestamp}-{random_part}"

def verify_account_details(method: WithdrawalMethod, details: Dict) -> bool:
    try:
        if method == WithdrawalMethod.BANK_TRANSFER:
            BankAccountDetails(**details)
        elif method == WithdrawalMethod.CRYPTO:
            CryptoDetails(**details)
        elif method == WithdrawalMethod.EWALLET:
            EWalletDetails(**details)
        return True
    except Exception:
        return False

async def process_withdrawal_in_background(withdrawal_id: int):
    try:
        # Simulate processing delay
        await asyncio.sleep(5)
        
        # Update withdrawal status to completed
        query = update(withdrawals).where(
            withdrawals.c.id == withdrawal_id
        ).values(
            status=WithdrawalStatus.COMPLETED,
            processed_at=func.now(),
        )
        await database.execute(query)
        
        logger.info(f"Withdrawal {withdrawal_id} processed successfully")
    except Exception as e:
        logger.error(f"Error processing withdrawal {withdrawal_id}: {str(e)}")
        # Mark as failed if error occurs
        query = update(withdrawals).where(
            withdrawals.c.id == withdrawal_id
        ).values(
            status=WithdrawalStatus.FAILED,
        )
        await database.execute(query)

# API endpoints
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/withdrawals", response_model=WithdrawalResponse)
async def create_withdrawal(
    withdrawal_request: WithdrawalRequest,
    user: dict = Depends(get_current_user),
):
    # Verify user has sufficient balance
    if user["balance"] < withdrawal_request.amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient balance",
        )
    
    # Verify account details
    if not verify_account_details(withdrawal_request.method, withdrawal_request.account_details):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid account details",
        )
    
    # Generate transaction ID
    transaction_id = generate_transaction_id()
    
    # Create withdrawal record
    query = withdrawals.insert().values(
        user_id=user["id"],
        amount=withdrawal_request.amount,
        status=WithdrawalStatus.PENDING,
        method=withdrawal_request.method,
        account_details=withdrawal_request.account_details,
        transaction_id=transaction_id,
    )
    withdrawal_id = await database.execute(query)
    
    # Deduct from user balance
    query = update(users).where(
        users.c.id == user["id"]
    ).values(
        balance=users.c.balance - withdrawal_request.amount
    )
    await database.execute(query)
    
    # Schedule background processing
    asyncio.create_task(process_withdrawal_in_background(withdrawal_id))
    
    # Calculate estimated completion (next business day)
    now = datetime.utcnow()
    if now.weekday() >= 5:  # Saturday or Sunday
        days
