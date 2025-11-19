"""
Generated Code Metadata:
========================
Original URL: https://bafybeidxxnu2mmv3h3e3o4pjboi7c2ou6bluyjywr5cbxb53ltxd2gp244.ipfs.dweb.link
Prompt: Create a data model to represent the portfolio of a multi-stage web3 investment firm like DWF Labs, including fields for investment amount, pledge percentage, and asset type.
Generated: DETERMINISTIC_5e2da9b38eb75db4
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator
from decimal import Decimal

class AssetType(str, Enum):
    """Enum representing different types of assets in the portfolio."""
    TOKEN = "token"
    NFT = "nft"
    EQUITY = "equity"
    OTHER = "other"

class InvestmentStage(str, Enum):
    """Enum representing different investment stages."""
    SEED = "seed"
    SERIES_A = "series_a"
    SERIES_B = "series_b"
    SERIES_C = "series_c"
    LATE_STAGE = "late_stage"
    GROWTH = "growth"

class PortfolioItem(BaseModel):
    """Represents a single investment in the portfolio."""
    id: str = Field(..., description="Unique identifier for the investment")
    project_name: str = Field(..., description="Name of the invested project")
    asset_type: AssetType = Field(..., description="Type of asset invested in")
    stage: InvestmentStage = Field(..., description="Investment stage")
    investment_amount: Decimal = Field(..., description="Amount invested in USD", gt=0)
    pledge_percentage: Decimal = Field(
        default=Decimal("0"),
        description="Percentage of tokens pledged (0-100)",
        ge=0,
        le=100
    )
    investment_date: datetime = Field(..., description="Date when investment was made")
    expected_exit_date: Optional[datetime] = Field(None, description="Expected exit date")
    notes: Optional[str] = Field(None, description="Additional notes about the investment")

    @validator('investment_amount', 'pledge_percentage')
    def round_decimal(cls, v):
        """Round decimal fields to 2 decimal places."""
        return round(v, 2)

class Portfolio(BaseModel):
    """Represents the complete investment portfolio."""
    items: list[PortfolioItem] = Field(default_factory=list, description="List of investments")
    total_investment: Decimal = Field(..., description="Total investment amount in USD")
    last_updated: datetime = Field(default_factory=datetime.now, description="Last update timestamp")

    def update_totals(self) -> None:
        """Recalculate total investment amount."""
        self.total_investment = sum(item.investment_amount for item in self.items)
        self.last_updated = datetime.now()

    def add_item(self, item: PortfolioItem) -> None:
        """Add a new investment item to the portfolio."""
        self.items.append(item)
        self.update_totals()

    def remove_item(self, item_id: str) -> None:
        """Remove an investment item from the portfolio."""
        self.items = [item for item in self.items if item.id != item_id]
        self.update_totals()
```
