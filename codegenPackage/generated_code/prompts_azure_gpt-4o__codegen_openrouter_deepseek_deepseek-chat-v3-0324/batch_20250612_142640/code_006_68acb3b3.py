"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Design an API endpoint that retrieves financing options for specific asset categories (e.g., amusement coin-op rides or commercial mortgages) and supports filtering by industry sector, as described on Rhino Asset Finance.
Generated: DETERMINISTIC_68acb3b37f22e561
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

app = FastAPI(
    title="Rhino Asset Finance API",
    description="API for retrieving financing options for specific asset categories",
    version="1.0.0"
)

class IndustrySector(str, Enum):
    ENTERTAINMENT = "entertainment"
    REAL_ESTATE = "real_estate"
    MANUFACTURING = "manufacturing"
    TRANSPORTATION = "transportation"
    HOSPITALITY = "hospitality"
    RETAIL = "retail"
    HEALTHCARE = "healthcare"
    CONSTRUCTION = "construction"

class AssetCategory(str, Enum):
    AMUSEMENT_RIDES = "amusement_coin_op_rides"
    COMMERCIAL_MORTGAGES = "commercial_mortgages"
    INDUSTRIAL_EQUIPMENT = "industrial_equipment"
    VEHICLES = "vehicles"
    MEDICAL_EQUIPMENT = "medical_equipment"

class FinancingOption(BaseModel):
    id: str
    name: str
    asset_category: AssetCategory
    industry_sectors: List[IndustrySector]
    min_amount: float
    max_amount: float
    term_months: int
    interest_rate: float
    description: str

# Mock database
FINANCING_OPTIONS = [
    FinancingOption(
        id="opt1",
        name="Amusement Ride Lease",
        asset_category=AssetCategory.AMUSEMENT_RIDES,
        industry_sectors=[IndustrySector.ENTERTAINMENT, IndustrySector.HOSPITALITY],
        min_amount=5000,
        max_amount=500000,
        term_months=60,
        interest_rate=6.5,
        description="Flexible leasing for coin-operated amusement rides"
    ),
    FinancingOption(
        id="opt2",
        name="Commercial Property Loan",
        asset_category=AssetCategory.COMMERCIAL_MORTGAGES,
        industry_sectors=[IndustrySector.REAL_ESTATE, IndustrySector.RETAIL],
        min_amount=100000,
        max_amount=10000000,
        term_months=240,
        interest_rate=4.5,
        description="Long-term financing for commercial properties"
    ),
    # Add more options as needed
]

@app.get("/financing-options", response_model=List[FinancingOption])
async def get_financing_options(
    asset_category: Optional[AssetCategory] = Query(None, description="Filter by asset category"),
    industry_sector: Optional[IndustrySector] = Query(None, description="Filter by industry sector"),
    min_amount: Optional[float] = Query(None, description="Minimum financing amount"),
    max_amount: Optional[float] = Query(None, description="Maximum financing amount")
):
    """
    Retrieve financing options with optional filters.
    
    Args:
        asset_category: Filter by specific asset category
        industry_sector: Filter by industry sector
        min_amount: Minimum financing amount
        max_amount: Maximum financing amount
    
    Returns:
        List of matching financing options
    """
    filtered_options = FINANCING_OPTIONS
    
    if asset_category:
        filtered_options = [opt for opt in filtered_options if opt.asset_category == asset_category]
    
    if industry_sector:
        filtered_options = [opt for opt in filtered_options if industry_sector in opt.industry_sectors]
    
    if min_amount is not None:
        filtered_options = [opt for opt in filtered_options if opt.max_amount >= min_amount]
    
    if max_amount is not None:
        filtered_options = [opt for opt in filtered_options if opt.min_amount <= max_amount]
    
    if not filtered_options:
        raise HTTPException(
            status_code=404,
            detail="No financing options found matching the criteria"
        )
    
    return filtered_options
```
