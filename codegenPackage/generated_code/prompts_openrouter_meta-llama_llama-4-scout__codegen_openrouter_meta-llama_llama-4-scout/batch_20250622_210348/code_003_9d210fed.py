"""
Generated Code Metadata:
========================
Original URL: https://babysamocoin-nft.web.app
Prompt: Design an API for managing NFT whitelist minting, including endpoints for checking eligibility and processing mint requests.
Generated: DETERMINISTIC_9d210fed334564ca
Batch ID: 20250622_210348
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
from typing import Optional

app = FastAPI()

# Define a model for the NFT whitelist
class NFTWhitelist(BaseModel):
    address: str
    max_mints: int

# Define a model for the mint request
class MintRequest(BaseModel):
    address: str
    nft_id: str

# In-memory whitelist storage (replace with a database in production)
whitelist: dict[str, NFTWhitelist] = {}

# Endpoint to add an address to the whitelist
@app.post("/whitelist/")
async def add_to_whitelist(nft_whitelist: NFTWhitelist):
    """Add an address to the whitelist"""
    whitelist[nft_whitelist.address] = nft_whitelist
    return {"message": "Address added to whitelist"}

# Endpoint to check eligibility for minting
@app.get("/eligibility/{address}")
async def check_eligibility(address: str):
    """Check if an address is eligible for minting"""
    if address not in whitelist:
        raise HTTPException(status_code=404, detail="Address not found in whitelist")
    return {"eligible": True, "max_mints": whitelist[address].max_mints}

# Endpoint to process a mint request
@app.post("/mint/")
async def process_mint_request(mint_request: MintRequest):
    """Process a mint request"""
    if mint_request.address not in whitelist:
        raise HTTPException(status_code=404, detail="Address not found in whitelist")
    
    # Simulate minting process (replace with actual minting logic)
    whitelist[mint_request.address].max_mints -= 1
    if whitelist[mint_request.address].max_mints < 0:
        raise HTTPException(status_code=400, detail="Max mints exceeded")
    return {"message": "Mint request processed successfully"}

# Endpoint to get whitelist details
@app.get("/whitelist/{address}")
async def get_whitelist_details(address: str):
    """Get whitelist details for an address"""
    if address not in whitelist:
        raise HTTPException(status_code=404, detail="Address not found in whitelist")
    return whitelist[address]

# Error handler for HTTP exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
