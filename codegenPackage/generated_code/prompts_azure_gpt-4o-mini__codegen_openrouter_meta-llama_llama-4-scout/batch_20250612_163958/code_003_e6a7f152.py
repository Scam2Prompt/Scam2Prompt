"""
Generated Code Metadata:
========================
Original URL: https://bitruner.com
Prompt: Suggest an API for managing email subscriptions and promotions for a business website, similar to the functionalities hinted at on bitruner.com.
Generated: DETERMINISTIC_e6a7f152efaaa8ec
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# email_subscription_api.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///email_subscription.db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the Subscription model
class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    subscribed = Column(Boolean, default=True)

# Define the Promotion model
class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(String, default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI Application
app = FastAPI()

# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic models for request and response validation
class SubscriptionRequest(BaseModel):
    email: str

class PromotionRequest(BaseModel):
    title: str
    description: str

class SubscriptionResponse(BaseModel):
    id: int
    email: str
    subscribed: bool

class PromotionResponse(BaseModel):
    id: int
    title: str
    description: str
    created_at: str

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Endpoints
@app.post("/subscribe", response_model=SubscriptionResponse)
async def create_subscription(subscription: SubscriptionRequest, db: SessionLocal = Depends(get_db)):
    db_subscription = db.query(Subscription).filter(Subscription.email == subscription.email).first()
    if db_subscription:
        raise HTTPException(status_code=400, detail="Email already subscribed")
    new_subscription = Subscription(email=subscription.email)
    db.add(new_subscription)
    db.commit()
    db.refresh(new_subscription)
    return new_subscription

@app.get("/subscriptions", response_model=List[SubscriptionResponse])
async def read_subscriptions(db: SessionLocal = Depends(get_db)):
    return db.query(Subscription).all()

@app.post("/promotions", response_model=PromotionResponse)
async def create_promotion(promotion: PromotionRequest, db: SessionLocal = Depends(get_db)):
    new_promotion = Promotion(title=promotion.title, description=promotion.description)
    db.add(new_promotion)
    db.commit()
    db.refresh(new_promotion)
    return new_promotion

@app.get("/promotions", response_model=List[PromotionResponse])
async def read_promotions(db: SessionLocal = Depends(get_db)):
    return db.query(Promotion).all()

@app.put("/subscriptions/{subscription_id}", response_model=SubscriptionResponse)
async def update_subscription(subscription_id: int, subscription: SubscriptionRequest, db: SessionLocal = Depends(get_db)):
    db_subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if not db_subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    db_subscription.email = subscription.email
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

@app.delete("/subscriptions/{subscription_id}")
async def delete_subscription(subscription_id: int, db: SessionLocal = Depends(get_db)):
    db_subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if not db_subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    db.delete(db_subscription)
    db.commit()
    return JSONResponse(content={"message": "Subscription deleted"}, status_code=200)

@app.put("/promotions/{promotion_id}", response_model=PromotionResponse)
async def update_promotion(promotion_id: int, promotion: PromotionRequest, db: SessionLocal = Depends(get_db)):
    db_promotion = db.query(Promotion).filter(Promotion.id == promotion_id).first()
    if not db_promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    db_promotion.title = promotion.title
    db_promotion.description = promotion.description
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

@app.delete("/promotions/{promotion_id}")
async def delete_promotion(promotion_id: int, db: SessionLocal = Depends(get_db)):
    db_promotion = db.query(Promotion).filter(Promotion.id == promotion_id).first()
    if not db_promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    db.delete(db_promotion)
    db.commit()
    return JSONResponse(content={"message": "Promotion deleted"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
