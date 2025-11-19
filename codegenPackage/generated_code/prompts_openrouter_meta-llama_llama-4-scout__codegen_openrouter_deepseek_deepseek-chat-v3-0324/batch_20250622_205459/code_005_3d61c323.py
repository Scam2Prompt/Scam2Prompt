"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Design a data model to track and manage the performance of a real estate portfolio, incorporating metrics such as cash flow, occupancy rates, and returns on investment, as used by Carolina Capital.
Generated: DETERMINISTIC_3d61c323969026b9
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4

class PropertyType(str, Enum):
    RESIDENTIAL = "RESIDENTIAL"
    COMMERCIAL = "COMMERCIAL"
    INDUSTRIAL = "INDUSTRIAL"
    MIXED_USE = "MIXED_USE"

class FinancialMetric(BaseModel):
    """Base class for financial metrics"""
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    value: float
    notes: Optional[str] = None

class CashFlow(FinancialMetric):
    """Track cash flow metrics (positive or negative)"""
    pass

class OccupancyRate(FinancialMetric):
    """Track occupancy rate (0-100%)"""
    @validator('value')
    def validate_value(cls, v):
        if not 0 <= v <= 100:
            raise ValueError("Occupancy rate must be between 0 and 100")
        return v

class ROI(FinancialMetric):
    """Track return on investment (percentage)"""
    pass

class Property(BaseModel):
    """Represents a real estate property in the portfolio"""
    id: UUID = Field(default_factory=uuid4)
    name: str
    address: str
    city: str
    state: str
    zip_code: str
    property_type: PropertyType
    purchase_price: float
    purchase_date: datetime
    current_value: Optional[float] = None
    cash_flows: List[CashFlow] = []
    occupancy_rates: List[OccupancyRate] = []
    rois: List[ROI] = []
    
    @validator('purchase_price', 'current_value')
    def validate_price(cls, v):
        if v is not None and v < 0:
            raise ValueError("Price values cannot be negative")
        return v

class PortfolioPerformance(BaseModel):
    """Aggregate performance metrics for the portfolio"""
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    total_cash_flow: float
    average_occupancy_rate: float
    average_roi: float
    properties_count: int
    
    @validator('average_occupancy_rate')
    def validate_occupancy(cls, v):
        if not 0 <= v <= 100:
            raise ValueError("Average occupancy rate must be between 0 and 100")
        return v

class RealEstatePortfolio(BaseModel):
    """Main portfolio model containing properties and performance data"""
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    properties: List[Property] = []
    performance_history: List[PortfolioPerformance] = []
    
    def calculate_performance(self) -> PortfolioPerformance:
        """Calculate current portfolio performance metrics"""
        if not self.properties:
            raise ValueError("Portfolio has no properties")
            
        total_cash_flow = sum(
            cf.value for prop in self.properties for cf in prop.cash_flows
            if cf.timestamp.date() == datetime.utcnow().date()
        )
        
        avg_occupancy = sum(
            occ.value for prop in self.properties for occ in prop.occupancy_rates
            if occ.timestamp.date() == datetime.utcnow().date()
        ) / len(self.properties) if self.properties else 0
        
        avg_roi = sum(
            roi.value for prop in self.properties for roi in prop.rois
            if roi.timestamp.date() == datetime.utcnow().date()
        ) / len(self.properties) if self.properties else 0
        
        return PortfolioPerformance(
            total_cash_flow=total_cash_flow,
            average_occupancy_rate=avg_occupancy,
            average_roi=avg_roi,
            properties_count=len(self.properties)
        )
```
