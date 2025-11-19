"""
Generated Code Metadata:
========================
Original URL: https://analos-meme.web.app
Prompt: Suggest an API for retrieving information about NFT holders, specifically for Tensorians, SMB, Mad Lads, Claynosaurz, Okay Bears, and FFF NFT holders.
Generated: DETERMINISTIC_c42fe0e518917ce3
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_holders_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="NFT Holders API",
    description="API for retrieving information about NFT holders",
    version="1.0.0"
)

# Define a model for NFT holder information
class NFTHolder(BaseModel):
    nft_name: str
    holder_address: str
    token_id: int

# Define a model for NFT collection information
class NFTCollection(BaseModel):
    name: str
    holders: List[NFTHolder]

# Mock data for demonstration purposes
# In a real application, this data would come from a database or external API
nft_collections = {
    "Tensorians": [
        NFTHolder(nft_name="Tensorians", holder_address="0x123", token_id=1),
        NFTHolder(nft_name="Tensorians", holder_address="0x456", token_id=2),
    ],
    "SMB": [
        NFTHolder(nft_name="SMB", holder_address="0x789", token_id=3),
        NFTHolder(nft_name="SMB", holder_address="0x012", token_id=4),
    ],
    "Mad Lads": [
        NFTHolder(nft_name="Mad Lads", holder_address="0x345", token_id=5),
        NFTHolder(nft_name="Mad Lads", holder_address="0x678", token_id=6),
    ],
    "Claynosaurz": [
        NFTHolder(nft_name="Claynosaurz", holder_address="0x901", token_id=7),
        NFTHolder(nft_name="Claynosaurz", holder_address="0x234", token_id=8),
    ],
    "Okay Bears": [
        NFTHolder(nft_name="Okay Bears", holder_address="0x567", token_id=9),
        NFTHolder(nft_name="Okay Bears", holder_address="0x890", token_id=10),
    ],
    "FFF": [
        NFTHolder(nft_name="FFF", holder_address="0x111", token_id=11),
        NFTHolder(nft_name="FFF", holder_address="0x222", token_id=12),
    ],
}

# Define a route for retrieving NFT holders by collection
@app.get("/nft-holders/{collection_name}")
async def get_nft_holders(collection_name: str):
    """
    Retrieve a list of NFT holders for a specific collection.

    Args:
    - collection_name (str): The name of the NFT collection.

    Returns:
    - A list of NFT holders for the specified collection.

    Raises:
    - HTTPException: If the collection is not found.
    """
    if collection_name not in nft_collections:
        raise HTTPException(status_code=404, detail="Collection not found")

    return {"name": collection_name, "holders": nft_collections[collection_name]}

# Define a route for retrieving NFT holders by collection and address
@app.get("/nft-holders/{collection_name}/{address}")
async def get_nft_holder(collection_name: str, address: str):
    """
    Retrieve a list of NFT holders for a specific collection and address.

    Args:
    - collection_name (str): The name of the NFT collection.
    - address (str): The address of the NFT holder.

    Returns:
    - A list of NFT holders for the specified collection and address.

    Raises:
    - HTTPException: If the collection or address is not found.
    """
    if collection_name not in nft_collections:
        raise HTTPException(status_code=404, detail="Collection not found")

    holders = [holder for holder in nft_collections[collection_name] if holder.holder_address == address]
    if not holders:
        raise HTTPException(status_code=404, detail="No holders found for the specified address")

    return {"name": collection_name, "holders": holders}

# Define a route for retrieving all NFT holders
@app.get("/nft-holders")
async def get_all_nft_holders():
    """
    Retrieve a list of all NFT holders.

    Returns:
    - A dictionary of NFT collections with their respective holders.
    """
    return {name: holders for name, holders in nft_collections.items()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
