"""
Generated Code Metadata:
========================
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Design an API for tracking cryptocurrency token presales, including fields for presale cap, total supply, and token pricing tiers, inspired by the $ALIEN PRE-SALE webpage.
Generated: DETERMINISTIC_311a79892fbf5452
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
from enum import Enum

app = FastAPI(
    title="Cryptocurrency Presale Tracker API",
    description="API for tracking cryptocurrency token presales",
    version="1.0.0"
)

class TokenStandard(str, Enum):
    ERC20 = "ERC20"
    BEP20 = "BEP20"
    TRC20 = "TRC20"
    OTHER = "OTHER"

class PricingTier(BaseModel):
    min_purchase: float = Field(..., description="Minimum purchase amount in USD for this tier")
    max_purchase: float = Field(..., description="Maximum purchase amount in USD for this tier")
    price_per_token: float = Field(..., description="Price per token in USD for this tier")
    bonus_percentage: Optional[float] = Field(0.0, description="Bonus percentage for this tier")

    @validator('min_purchase', 'max_purchase', 'price_per_token')
    def validate_positive_values(cls, v):
        if v <= 0:
            raise ValueError("Value must be positive")
        return v

    @validator('bonus_percentage')
    def validate_bonus_percentage(cls, v):
        if v < 0 or v > 100:
            raise ValueError("Bonus percentage must be between 0 and 100")
        return v

class PresaleCreate(BaseModel):
    token_name: str = Field(..., min_length=1, max_length=100)
    token_symbol: str = Field(..., min_length=1, max_length=10)
    token_standard: TokenStandard
    presale_cap: float = Field(..., description="Total presale cap in USD")
    total_supply: float = Field(..., description="Total token supply")
    presale_start: datetime
    presale_end: datetime
    pricing_tiers: List[PricingTier]
    website_url: Optional[str] = None
    whitepaper_url: Optional[str] = None
    social_links: Optional[dict] = None

    @validator('presale_cap', 'total_supply')
    def validate_positive_values(cls, v):
        if v <= 0:
            raise ValueError("Value must be positive")
        return v

    @validator('presale_end')
    def validate_end_after_start(cls, v, values):
        if 'presale_start' in values and v <= values['presale_start']:
            raise ValueError("Presale end must be after presale start")
        return v

class Presale(PresaleCreate):
    id: str
    created_at: datetime
    updated_at: datetime

# In-memory database simulation
presales_db = {}

@app.post("/presales/", response_model=Presale, status_code=status.HTTP_201_CREATED)
async def create_presale(presale: PresaleCreate):
    """Create a new presale entry"""
    presale_id = f"presale_{len(presales_db) + 1}"
    now = datetime.now()
    db_presale = Presale(
        **presale.dict(),
        id=presale_id,
        created_at=now,
        updated_at=now
    )
    presales_db[presale_id] = db_presale
    return db_presale

@app.get("/presales/", response_model=List[Presale])
async def get_presales(skip: int = 0, limit: int = 100):
    """Get list of all presales with pagination"""
    return list(presales_db.values())[skip:skip + limit]

@app.get("/presales/{presale_id}", response_model=Presale)
async def get_presale(presale_id: str):
    """Get a specific presale by ID"""
    if presale_id not in presales_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Presale not found"
        )
    return presales_db[presale_id]

@app.put("/presales/{presale_id}", response_model=Presale)
async def update_presale(presale_id: str, presale: PresaleCreate):
    """Update an existing presale"""
    if presale_id not in presales_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Presale not found"
        )
    
    updated_presale = Presale(
        **presale.dict(),
        id=presale_id,
        created_at=presales_db[presale_id].created_at,
        updated_at=datetime.now()
    )
    presales_db[presale_id] = updated_presale
    return updated_presale

@app.delete("/presales/{presale_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_presale(presale_id: str):
    """Delete a presale"""
    if presale_id not in presales_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Presale not found"
        )
    del presales_db[presale_id]
    return None
```
