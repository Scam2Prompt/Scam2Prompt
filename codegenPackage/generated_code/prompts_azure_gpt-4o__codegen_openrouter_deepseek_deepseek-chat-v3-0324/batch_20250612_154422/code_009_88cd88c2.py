"""
Generated Code Metadata:
========================
Original URL: https://jieyasoft.com
Prompt: Develop a backend system for handling "百万数据读秒查阅" (millions of data instant lookup) and "庞大数据精确结算" (large-scale data precise calculation) for a direct selling software, as specified on JieyaSoft.
Generated: DETERMINISTIC_88cd88c22875a5f7
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
import time
from typing import Dict, List, Any, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import redis
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
import hashlib

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('app.log', maxBytes=1024*1024*5, backupCount=5),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="JieyaSoft Direct Selling Backend",
    description="Backend system for handling millions of data instant lookup and large-scale data precise calculation",
    version="1.0.0"
)

# Database configuration
DATABASE_URL = "postgresql://user:password@localhost:5432/jieyasoft_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Redis configuration for caching
redis_client = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

# Database models
class Member(Base):
    __tablename__ = "members"
    
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(String(50), unique=True, index=True)
    name = Column(String(100))
    level = Column(Integer)
    parent_id = Column(String(50), index=True)
    join_date = Column(DateTime)
    balance = Column(Float, default=0.0)

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String(50), unique=True, index=True)
    member_id = Column(String(50), index=True)
    amount = Column(Float)
    transaction_type = Column(String(50))
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20), default="completed")

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String(50), unique=True, index=True)
    name = Column(String(100))
    price = Column(Float)
    commission_rate = Column(Float)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Pydantic models for request/response validation
class MemberCreate(BaseModel):
    member_id: str
    name: str
    level: int
    parent_id: Optional[str] = None

class TransactionCreate(BaseModel):
    member_id: str
    amount: float
    transaction_type: str

class ProductCreate(BaseModel):
    product_id: str
    name: str
    price: float
    commission_rate: float

class CommissionCalculationRequest(BaseModel):
    member_id: str
    start_date: datetime
    end_date: datetime

class CommissionCalculationResponse(BaseModel):
    member_id: str
    total_commission: float
    breakdown: Dict[str, float]

# Helper functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_cache_key(params: Dict[str, Any]) -> str:
    """Generate a unique cache key from parameters"""
    param_str = json.dumps(params, sort_keys=True)
    return hashlib.md5(param_str.encode()).hexdigest()

# API endpoints
@app.post("/members/", response_model=MemberCreate)
def create_member(member: MemberCreate):
    """Create a new member"""
    db = SessionLocal()
    try:
        db_member = Member(
            member_id=member.member_id,
            name=member.name,
            level=member.level,
            parent_id=member.parent_id,
            join_date=datetime.utcnow()
        )
        db.add(db_member)
        db.commit()
        db.refresh(db_member)
        return db_member
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating member: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

@app.get("/members/{member_id}", response_model=MemberCreate)
def get_member(member_id: str):
    """Get member details with instant lookup using Redis cache"""
    cache_key = f"member:{member_id}"
    cached_data = redis_client.get(cache_key)
    
    if cached_data:
        return json.loads(cached_data)
    
    db = SessionLocal()
    try:
        member = db.query(Member).filter(Member.member_id == member_id).first()
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")
        
        # Cache the result for 1 hour
        redis_client.setex(cache_key, 3600, json.dumps({
            "member_id": member.member_id,
            "name": member.name,
            "level": member.level,
            "parent_id": member.parent_id
        }))
        
        return {
            "member_id": member.member_id,
            "name": member.name,
            "level": member.level,
            "parent_id": member.parent_id
        }
    except Exception as e:
        logger.error(f"Error retrieving member: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        db.close()

@app.post("/transactions/", response_model=TransactionCreate)
def create_transaction(transaction: TransactionCreate):
    """Create a new transaction"""
    db = SessionLocal()
    try:
        # Verify member exists
        member = db.query(Member).filter(Member.member_id == transaction.member_id).first()
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")
        
        # Create transaction
        transaction_id = f"txn_{int(time.time())}_{hashlib.md5(transaction.member_id.encode()).hexdigest()[:6]}"
        db_transaction = Transaction(
            transaction_id=transaction_id,
            member_id=transaction.member_id,
            amount=transaction.amount,
            transaction_type=transaction.transaction_type
        )
        db.add(db_transaction)
        
        # Update member balance if needed
        if transaction.transaction_type == "deposit":
            member.balance += transaction.amount
        elif transaction.transaction_type == "withdrawal":
            if member.balance < transaction.amount:
                raise HTTPException(status_code=400, detail="Insufficient balance")
            member.balance -= transaction.amount
        
        db.commit()
        return {
            "member_id": transaction.member_id,
            "amount": transaction.amount,
            "transaction_type": transaction.transaction_type
        }
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating transaction: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

@app.post("/calculate_commission/", response_model=CommissionCalculationResponse)
def calculate_commission(request: CommissionCalculationRequest):
    """Calculate commission for a member with large-scale data processing"""
    cache_key = generate_cache_key(request.dict())
    cached_result = redis_client.get(cache_key)
    
    if cached_result:
        return json.loads(cached_result)
    
    db = SessionLocal()
    try:
        # Verify member exists
        member = db.query(Member).filter(Member.member_id == request.member_id).first()
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")
        
        # Use pandas for efficient large-scale data processing
        query = f"""
        SELECT t.member_id, t.amount, p.commission_rate, t.timestamp 
        FROM transactions t
        JOIN products p ON t.transaction_type = p.product_id
        WHERE t.member_id = '{request.member_id}' 
        AND t.timestamp BETWEEN '{request.start_date}' AND '{request.end_date}'
        AND t.status = 'completed'
        """
        
        df = pd.read_sql_query(query, engine)
        
        if df.empty:
            return {
                "member_id": request.member_id,
                "total_commission": 0.0,
                "breakdown": {}
            }
        
        # Calculate commission
        df['commission'] = df['amount'] * df['commission_rate']
        total_commission = df['commission'].sum()
        breakdown = df.groupby('transaction_type')['commission'].sum().to_dict()
        
        result = {
            "member_id": request.member_id,
            "total_commission": float(total_commission),
            "breakdown": breakdown
        }
        
        # Cache the result for 15
