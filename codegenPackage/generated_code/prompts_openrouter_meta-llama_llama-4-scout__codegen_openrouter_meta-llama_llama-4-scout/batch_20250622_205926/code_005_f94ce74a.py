"""
Generated Code Metadata:
========================
Original URL: https://rascalsnft.web.app
Prompt: "Design an API for managing Rascals NFT utilities and rarity, including endpoints for Jelly staking and trading."
Generated: DETERMINISTIC_f94ce74a045442d2
Batch ID: 20250622_205926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from rascal_nft import RascalsNFT

# Initialize FastAPI app
app = FastAPI(
    title="Rascals NFT API",
    description="API for managing Rascals NFT utilities and rarity",
    version="1.0.0"
)

# OAuth2 scheme for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic model for NFT data
class NFT(BaseModel):
    id: int
    name: str
    rarity: str
    utility: str

# Pydantic model for Jelly staking data
class JellyStaking(BaseModel):
    nft_id: int
    amount: float

# Initialize RascalsNFT instance
rascal_nft = RascalsNFT()

# Authentication endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Authenticate user
    if form_data.username != "admin" or form_data.password != "password":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": "fake_access_token", "token_type": "bearer"}

# Endpoint to get all NFTs
@app.get("/nfts")
async def get_nfts(token: str = Depends(oauth2_scheme)):
    try:
        nfts = rascal_nft.get_all_nfts()
        return JSONResponse(content=[NFT(**nft) for nft in nfts], media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get NFT by ID
@app.get("/nfts/{nft_id}")
async def get_nft(nft_id: int, token: str = Depends(oauth2_scheme)):
    try:
        nft = rascal_nft.get_nft_by_id(nft_id)
        if not nft:
            raise HTTPException(status_code=404, detail="NFT not found")
        return JSONResponse(content=NFT(**nft), media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to create new NFT
@app.post("/nfts")
async def create_nft(nft: NFT, token: str = Depends(oauth2_scheme)):
    try:
        new_nft = rascal_nft.create_nft(nft.dict())
        return JSONResponse(content=NFT(**new_nft), media_type="application/json", status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to stake Jelly
@app.post("/jelly-staking")
async def stake_jelly(jelly_staking: JellyStaking, token: str = Depends(oauth2_scheme)):
    try:
        result = rascal_nft.stake_jelly(jelly_staking.dict())
        return JSONResponse(content={"message": "Jelly staked successfully"}, media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to trade NFT
@app.post("/trade-nft")
async def trade_nft(nft_id: int, buyer_address: str, token: str = Depends(oauth2_scheme)):
    try:
        result = rascal_nft.trade_nft(nft_id, buyer_address)
        return JSONResponse(content={"message": "NFT traded successfully"}, media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Error handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# rascal_nft.py
import random

class RascalsNFT:
    def __init__(self):
        self.nfts = [
            {"id": 1, "name": "Rascal 1", "rarity": "Rare", "utility": "Jelly"},
            {"id": 2, "name": "Rascal 2", "rarity": "Common", "utility": "None"},
        ]
        self.jelly_staking = []

    def get_all_nfts(self):
        return self.nfts

    def get_nft_by_id(self, nft_id):
        for nft in self.nfts:
            if nft["id"] == nft_id:
                return nft
        return None

    def create_nft(self, nft_data):
        new_nft = {
            "id": len(self.nfts) + 1,
            "name": nft_data["name"],
            "rarity": nft_data["rarity"],
            "utility": nft_data["utility"],
        }
        self.nfts.append(new_nft)
        return new_nft

    def stake_jelly(self, jelly_staking_data):
        self.jelly_staking.append(jelly_staking_data)
        return True

    def trade_nft(self, nft_id, buyer_address):
        nft = self.get_nft_by_id(nft_id)
        if not nft:
            raise Exception("NFT not found")
        # Simulate trading
        print(f"NFT {nft_id} traded to {buyer_address}")
        return True
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```
