"""
Generated Code Metadata:
========================
Original URL: https://mint-playpixiz.vercel.app
Prompt: "Design a basic backend API to manage NFT presale whitelists, including user wallet address and eligibility status."
Generated: DETERMINISTIC_397c67794404a079
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import UUID
from sqlalchemy import create_engine, Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize FastAPI app
app = FastAPI()

# Initialize database connection
SQLALCHEMY_DATABASE_URL = "sqlite:///nft_presale.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define database model
class Whitelist(Base):
    __tablename__ = "whitelist"

    wallet_address = Column(String, primary_key=True)
    eligible = Column(Boolean, default=False)

Base.metadata.create_all(engine)

# Define Pydantic model
class WhitelistRequest(BaseModel):
    wallet_address: str

class WhitelistResponse(BaseModel):
    wallet_address: str
    eligible: bool

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create whitelist entry
@app.post("/whitelist/", response_model=WhitelistResponse)
async def create_whitelist(whitelist_request: WhitelistRequest, db = next(get_db())):
    try:
        existing_entry = db.query(Whitelist).filter_by(wallet_address=whitelist_request.wallet_address).first()
        if existing_entry:
            raise HTTPException(status_code=400, detail="Wallet address already exists in whitelist")
        
        new_whitelist = Whitelist(wallet_address=whitelist_request.wallet_address)
        db.add(new_whitelist)
        db.commit()
        db.refresh(new_whitelist)
        return WhitelistResponse(wallet_address=new_whitelist.wallet_address, eligible=new_whitelist.eligible)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Get whitelist entry by wallet address
@app.get("/whitelist/{wallet_address}", response_model=WhitelistResponse)
async def get_whitelist(wallet_address: str, db = next(get_db())):
    try:
        whitelist_entry = db.query(Whitelist).filter_by(wallet_address=wallet_address).first()
        if not whitelist_entry:
            raise HTTPException(status_code=404, detail="Wallet address not found in whitelist")
        return WhitelistResponse(wallet_address=whitelist_entry.wallet_address, eligible=whitelist_entry.eligible)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Update whitelist entry eligibility
@app.put("/whitelist/{wallet_address}", response_model=WhitelistResponse)
async def update_whitelist(wallet_address: str, eligible: bool, db = next(get_db())):
    try:
        whitelist_entry = db.query(Whitelist).filter_by(wallet_address=wallet_address).first()
        if not whitelist_entry:
            raise HTTPException(status_code=404, detail="Wallet address not found in whitelist")
        
        whitelist_entry.eligible = eligible
        db.commit()
        db.refresh(whitelist_entry)
        return WhitelistResponse(wallet_address=whitelist_entry.wallet_address, eligible=whitelist_entry.eligible)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Delete whitelist entry
@app.delete("/whitelist/{wallet_address}")
async def delete_whitelist(wallet_address: str, db = next(get_db())):
    try:
        whitelist_entry = db.query(Whitelist).filter_by(wallet_address=wallet_address).first()
        if not whitelist_entry:
            raise HTTPException(status_code=404, detail="Wallet address not found in whitelist")
        
        db.delete(whitelist_entry)
        db.commit()
        return {"message": "Whitelist entry deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Get all whitelist entries
@app.get("/whitelist/", response_model=List[WhitelistResponse])
async def get_all_whitelist(db = next(get_db())):
    try:
        whitelist_entries = db.query(Whitelist).all()
        return [WhitelistResponse(wallet_address=entry.wallet_address, eligible=entry.eligible) for entry in whitelist_entries]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```
