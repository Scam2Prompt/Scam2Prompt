"""
Generated Code Metadata:
========================
Original URL: https://kevinland.pages.dev
Prompt: Develop an API endpoint that retrieves the minting status and FAQs for the KevinLand NFT project, including ownership rights and rarity listings.
Generated: DETERMINISTIC_d483134d0b28ca3b
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
import uvicorn

app = FastAPI(
    title="KevinLand NFT API",
    description="API for retrieving KevinLand NFT project information",
    version="1.0.0"
)

class MintingStatus(BaseModel):
    is_active: bool
    total_minted: int
    total_supply: int
    mint_price: str
    mint_date: Optional[str] = None

class FAQItem(BaseModel):
    question: str
    answer: str

class OwnershipRights(BaseModel):
    commercial_use: bool
    personal_use: bool
    transferable: bool
    resale_royalty: float

class RarityTier(BaseModel):
    name: str
    percentage: float
    traits: List[str]

class NFTProjectInfo(BaseModel):
    minting_status: MintingStatus
    faqs: List[FAQItem]
    ownership_rights: OwnershipRights
    rarity_tiers: List[RarityTier]

# Mock data - in production, this would come from a database or external service
MOCK_MINTING_STATUS = MintingStatus(
    is_active=True,
    total_minted=4231,
    total_supply=10000,
    mint_price="0.08 ETH",
    mint_date="2023-11-15"
)

MOCK_FAQS = [
    FAQItem(
        question="What is KevinLand NFT?",
        answer="KevinLand is a collection of 10,000 unique NFTs..."
    ),
    FAQItem(
        question="How do I mint a KevinLand NFT?",
        answer="Connect your wallet to our website and click the mint button..."
    ),
    FAQItem(
        question="What blockchain is KevinLand on?",
        answer="KevinLand NFTs are on the Ethereum blockchain..."
    )
]

MOCK_OWNERSHIP_RIGHTS = OwnershipRights(
    commercial_use=True,
    personal_use=True,
    transferable=True,
    resale_royalty=5.0
)

MOCK_RARITY_TIERS = [
    RarityTier(
        name="Common",
        percentage=60.0,
        traits=["Basic background", "Standard clothing"]
    ),
    RarityTier(
        name="Rare",
        percentage=30.0,
        traits=["Special background", "Unique accessories"]
    ),
    RarityTier(
        name="Legendary",
        percentage=10.0,
        traits=["Animated features", "One-of-a-kind traits"]
    )
]

@app.get("/project-info", response_model=NFTProjectInfo)
async def get_project_info():
    """
    Retrieve all KevinLand NFT project information including:
    - Current minting status
    - Frequently asked questions
    - Ownership rights
    - Rarity tiers and distributions
    """
    try:
        return NFTProjectInfo(
            minting_status=MOCK_MINTING_STATUS,
            faqs=MOCK_FAQS,
            ownership_rights=MOCK_OWNERSHIP_RIGHTS,
            rarity_tiers=MOCK_RARITY_TIERS
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while retrieving project info: {str(e)}"
        )

@app.get("/minting-status", response_model=MintingStatus)
async def get_minting_status():
    """Retrieve current minting status of the KevinLand NFT project"""
    try:
        return MOCK_MINTING_STATUS
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while retrieving minting status: {str(e)}"
        )

@app.get("/faqs", response_model=List[FAQItem])
async def get_faqs():
    """Retrieve frequently asked questions about the KevinLand NFT project"""
    try:
        return MOCK_FAQS
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while retrieving FAQs: {str(e)}"
        )

@app.get("/ownership-rights", response_model=OwnershipRights)
async def get_ownership_rights():
    """Retrieve ownership rights information for KevinLand NFT holders"""
    try:
        return MOCK_OWNERSHIP_RIGHTS
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while retrieving ownership rights: {str(e)}"
        )

@app.get("/rarity-tiers", response_model=List[RarityTier])
async def get_rarity_tiers():
    """Retrieve rarity tiers and their distributions for KevinLand NFTs"""
    try:
        return MOCK_RARITY_TIERS
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while retrieving rarity tiers: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
