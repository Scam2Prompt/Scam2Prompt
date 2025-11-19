"""
Generated Code Metadata:
========================
Original URL: https://maximuslimited.com
Prompt: "Design a data model for a financial services platform, including entities for investment strategies, asset management, and business transformation."
Generated: DETERMINISTIC_4189383afd4462ec
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4

class AssetClass(str, Enum):
    EQUITIES = "EQUITIES"
    FIXED_INCOME = "FIXED_INCOME"
    REAL_ESTATE = "REAL_ESTATE"
    COMMODITIES = "COMMODITIES"
    CRYPTOCURRENCY = "CRYPTOCURRENCY"
    CASH = "CASH"

class InvestmentStrategyType(str, Enum):
    ACTIVE = "ACTIVE"
    PASSIVE = "PASSIVE"
    QUANTITATIVE = "QUANTITATIVE"
    ALTERNATIVE = "ALTERNATIVE"

class RiskProfile(str, Enum):
    CONSERVATIVE = "CONSERVATIVE"
    MODERATE = "MODERATE"
    AGGRESSIVE = "AGGRESSIVE"

class Asset(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    symbol: str
    asset_class: AssetClass
    current_price: float
    currency: str = "USD"
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('current_price')
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError("Price must be positive")
        return v

class Portfolio(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    assets: List[Asset] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class InvestmentStrategy(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    type: InvestmentStrategyType
    risk_profile: RiskProfile
    description: str
    target_return: float
    max_drawdown: float
    portfolios: List[Portfolio] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('target_return')
    def validate_return(cls, v):
        if v < -100:
            raise ValueError("Target return cannot be less than -100%")
        return v

class BusinessUnit(str, Enum):
    WEALTH_MANAGEMENT = "WEALTH_MANAGEMENT"
    INVESTMENT_BANKING = "INVESTMENT_BANKING"
    ASSET_MANAGEMENT = "ASSET_MANAGEMENT"
    RETAIL_BANKING = "RETAIL_BANKING"

class TransformationInitiative(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    business_unit: BusinessUnit
    start_date: datetime
    end_date: datetime
    budget: float
    strategy: InvestmentStrategy
    status: str = "PLANNED"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('end_date')
    def validate_dates(cls, v, values):
        if 'start_date' in values and v < values['start_date']:
            raise ValueError("End date must be after start date")
        return v

class FinancialServicesPlatform(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    strategies: List[InvestmentStrategy] = []
    transformation_initiatives: List[TransformationInitiative] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```
