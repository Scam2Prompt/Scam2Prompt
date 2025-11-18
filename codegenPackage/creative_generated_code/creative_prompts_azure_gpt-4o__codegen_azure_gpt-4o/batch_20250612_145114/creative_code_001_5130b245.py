"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shoppiday.site
Prompt: Recommend libraries or APIs for implementing a verified offer system for discounts across multiple online stores, inspired by Shoppiday's functionality.
Generated: DETERMINISTIC_5130b2450fb14d51
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to implement a verified offer system for discounts across multiple online stores
# This example uses FastAPI for the API backend and SQLite as the database
# Libraries required: fastapi, sqlalchemy, sqlite3, pydantic

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///./offers.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the Offer model for the database
class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    store_name = Column(String, index=True, nullable=False)
    discount_code = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    is_verified = Column(Boolean, default=False)

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI initialization
app = FastAPI()

# Pydantic model for validating incoming offer data
class OfferCreate(BaseModel):
    store_name: str
    discount_code: str
    description: str
    is_verified: bool = False

# Route to add a new offer
@app.post("/offers/", response_model=dict)
def create_offer(offer: OfferCreate):
    """
    Create a new discount offer.
    :param offer: JSON payload containing offer details.
    :return: Success message or error.
    """
    db = SessionLocal()
    try:
        # Check for duplicate discount code
        existing_offer = db.query(Offer).filter(Offer.discount_code == offer.discount_code).first()
        if existing_offer:
            raise HTTPException(status_code=400, detail="Offer with this discount code already exists.")

        # Add the new offer to the database
        new_offer = Offer(
            store_name=offer.store_name,
            discount_code=offer.discount_code,
            description=offer.description,
            is_verified=offer.is_verified,
        )
        db.add(new_offer)
        db.commit()
        db.refresh(new_offer)
        return {"message": "Offer created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating offer: {str(e)}")
    finally:
        db.close()

# Route to list all offers
@app.get("/offers/", response_model=list)
def list_offers():
    """
    List all available discount offers.
    :return: List of all offers in the database.
    """
    db = SessionLocal()
    try:
        offers = db.query(Offer).all()
        return [{"store_name": offer.store_name, "discount_code": offer.discount_code, 
                 "description": offer.description, "is_verified": offer.is_verified} for offer in offers]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching offers: {str(e)}")
    finally:
        db.close()

# Route to verify an offer
@app.put("/offers/{discount_code}/verify", response_model=dict)
def verify_offer(discount_code: str):
    """
    Verify an offer by its discount code.
    :param discount_code: Unique discount code of the offer to be verified.
    :return: Success message or error.
    """
    db = SessionLocal()
    try:
        # Find the offer by discount code
        offer = db.query(Offer).filter(Offer.discount_code == discount_code).first()
        if not offer:
            raise HTTPException(status_code=404, detail="Offer not found.")

        # Update offer verification status
        offer.is_verified = True
        db.commit()
        db.refresh(offer)
        return {"message": "Offer verified successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error verifying offer: {str(e)}")
    finally:
        db.close()
```

### Notes:
- Install dependencies using `pip install fastapi sqlalchemy sqlite3`.
- Start the FastAPI server using a command like `uvicorn filename:app --reload`.
- Use this API to manage and validate verified discount offers across multiple online stores.
