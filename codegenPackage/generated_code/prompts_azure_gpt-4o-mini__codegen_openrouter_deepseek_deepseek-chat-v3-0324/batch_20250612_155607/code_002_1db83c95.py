"""
Generated Code Metadata:
========================
Original URL: https://wisemonky-allocation.pages.dev
Prompt: Create a simple API that provides information on cryptocurrency trading risks, similar to the disclaimers found on the Wise Monky page.
Generated: DETERMINISTIC_1db83c95f9613b20
Batch ID: 20250612_155607
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
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Cryptocurrency Trading Risk API",
    description="API providing information about cryptocurrency trading risks",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@cryptoriskapi.com"
    },
    license_info={
        "name": "MIT",
    },
)

class RiskItem(BaseModel):
    id: int
    title: str
    description: str
    severity: str  # low, medium, high
    mitigation: Optional[str] = None

# In-memory database of risk items
RISK_ITEMS = [
    RiskItem(
        id=1,
        title="Market Volatility",
        description="Cryptocurrency prices can be extremely volatile and may fluctuate widely.",
        severity="high",
        mitigation="Only invest what you can afford to lose."
    ),
    RiskItem(
        id=2,
        title="Regulatory Risk",
        description="Cryptocurrencies face regulatory uncertainty in many jurisdictions.",
        severity="medium",
        mitigation="Stay informed about regulations in your country."
    ),
    RiskItem(
        id=3,
        title="Security Risks",
        description="Exchanges and wallets can be hacked, leading to loss of funds.",
        severity="high",
        mitigation="Use hardware wallets and enable 2FA."
    ),
    RiskItem(
        id=4,
        title="Liquidity Risk",
        description="Some cryptocurrencies may have low liquidity, making it hard to sell.",
        severity="medium",
        mitigation="Stick to major cryptocurrencies with high trading volumes."
    ),
    RiskItem(
        id=5,
        title="Technical Risks",
        description="Blockchain networks can experience bugs, forks, or downtime.",
        severity="medium",
        mitigation="Diversify across different blockchain networks."
    )
]

@app.get("/risks", response_model=List[RiskItem], summary="Get all risk items")
async def get_all_risks():
    """Returns all cryptocurrency trading risk items"""
    return RISK_ITEMS

@app.get("/risks/{risk_id}", response_model=RiskItem, summary="Get a specific risk item")
async def get_risk(risk_id: int):
    """Returns a specific cryptocurrency trading risk item by ID"""
    for item in RISK_ITEMS:
        if item.id == risk_id:
            return item
    raise HTTPException(status_code=404, detail="Risk item not found")

@app.get("/risks/severity/{severity}", response_model=List[RiskItem], summary="Get risks by severity")
async def get_risks_by_severity(severity: str):
    """Returns cryptocurrency trading risks filtered by severity (low, medium, high)"""
    severity = severity.lower()
    if severity not in ["low", "medium", "high"]:
        raise HTTPException(status_code=400, detail="Invalid severity level. Use low, medium, or high.")
    
    filtered_items = [item for item in RISK_ITEMS if item.severity == severity]
    return filtered_items

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
