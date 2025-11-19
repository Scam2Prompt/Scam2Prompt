"""
Generated Code Metadata:
========================
Original URL: https://jellydrop.web.app
Prompt: Develop a feature for tracking and displaying unique 1/1 NFTs, similar to the "Jelly 1/1" concept mentioned on the JellyDrop site.
Generated: DETERMINISTIC_8bd1fa08883556ba
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import uuid
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator
import motor.motor_asyncio
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

# Database configuration
MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.nft_tracker
nft_collection = db.get_collection("unique_nfts")

# Pydantic models for data validation
class NFTBase(BaseModel):
    name: str
    creator: str
    description: Optional[str] = None
    image_url: str
    external_url: Optional[str] = None
    attributes: Optional[List[Dict[str, str]]] = None
    blockchain: str
    contract_address: str
    token_id: str

    @validator('token_id')
    def validate_token_id(cls, v):
        if not v.strip():
            raise ValueError("Token ID cannot be empty")
        return v

class NFTCreate(NFTBase):
    pass

class NFTDB(NFTBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {ObjectId: str}

# Helper functions
async def get_nft(id: str) -> Optional[Dict]:
    nft = await nft_collection.find_one({"_id": ObjectId(id)})
    if nft:
        return nft
    return None

async def get_nft_by_token_details(contract_address: str, token_id: str) -> Optional[Dict]:
    nft = await nft_collection.find_one({
        "contract_address": contract_address,
        "token_id": token_id
    })
    if nft:
        return nft
    return None

async def get_all_nfts(skip: int = 0, limit: int = 100) -> List[Dict]:
    nfts = []
    cursor = nft_collection.find().skip(skip).limit(limit)
    async for nft in cursor:
        nfts.append(nft)
    return nfts

# FastAPI app setup
app = FastAPI(
    title="1/1 NFT Tracker API",
    description="API for tracking and displaying unique 1/1 NFTs",
    version="0.1.0"
)

# API endpoints
@app.post("/nfts/", response_model=NFTDB, status_code=status.HTTP_201_CREATED)
async def create_nft(nft: NFTCreate):
    # Check if NFT already exists
    existing_nft = await get_nft_by_token_details(nft.contract_address, nft.token_id)
    if existing_nft:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="NFT with this contract address and token ID already exists"
        )
    
    # Create new NFT
    now = datetime.utcnow()
    nft_dict = nft.dict()
    nft_dict["created_at"] = now
    nft_dict["updated_at"] = now
    
    try:
        result = await nft_collection.insert_one(nft_dict)
        created_nft = await get_nft(str(result.inserted_id))
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_nft)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the NFT: {str(e)}"
        )

@app.get("/nfts/", response_model=List[NFTDB])
async def read_nfts(skip: int = 0, limit: int = 100):
    nfts = await get_all_nfts(skip, limit)
    return nfts

@app.get("/nfts/{nft_id}", response_model=NFTDB)
async def read_nft(nft_id: str):
    nft = await get_nft(nft_id)
    if not nft:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="NFT not found"
        )
    return nft

@app.get("/nfts/by_token/{contract_address}/{token_id}", response_model=NFTDB)
async def read_nft_by_token(contract_address: str, token_id: str):
    nft = await get_nft_by_token_details(contract_address, token_id)
    if not nft:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="NFT not found"
        )
    return nft

@app.put("/nfts/{nft_id}", response_model=NFTDB)
async def update_nft(nft_id: str, nft: NFTCreate):
    existing_nft = await get_nft(nft_id)
    if not existing_nft:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="NFT not found"
        )
    
    # Check if the update would create a duplicate
    if (existing_nft["contract_address"] != nft.contract_address or 
        existing_nft["token_id"] != nft.token_id):
        duplicate_check = await get_nft_by_token_details(nft.contract_address, nft.token_id)
        if duplicate_check:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="NFT with this contract address and token ID already exists"
            )
    
    update_data = nft.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.utcnow()
    
    try:
        await nft_collection.update_one(
            {"_id": ObjectId(nft_id)},
            {"$set": update_data}
        )
        updated_nft = await get_nft(nft_id)
        return updated_nft
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while updating the NFT: {str(e)}"
        )

@app.delete("/nfts/{nft_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_nft(nft_id: str):
    delete_result = await nft_collection.delete_one({"_id": ObjectId(nft_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="NFT not found"
        )
    return None

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
