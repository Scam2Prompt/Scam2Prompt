"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Create a data model for storing and managing Oticon hearing aid product information, including product types (e.g., Oticon Real, Oticon Own), features, and technical specifications.
Generated: DETERMINISTIC_6700ab276dd8b6bb
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Optional, Dict
from enum import Enum
from pydantic import BaseModel, Field, validator
from datetime import datetime

class ProductType(str, Enum):
    REAL = "Oticon Real"
    OWN = "Oticon Own"
    MORE = "Oticon More"
    OPNS = "Oticon Opn"
    OTHER = "Other"

class ConnectivityFeature(str, Enum):
    BLUETOOTH = "Bluetooth"
    WIFI = "Wi-Fi"
    NFC = "NFC"
    TCOIL = "Telecoil"
    STREAMING = "Audio Streaming"

class PowerType(str, Enum):
    RECHARGEABLE = "Rechargeable"
    DISPOSABLE = "Disposable Battery"

class HearingAidProduct(BaseModel):
    """
    Represents an Oticon hearing aid product with all relevant specifications.
    """
    product_id: str = Field(..., min_length=3, max_length=20, description="Unique product identifier")
    name: str = Field(..., min_length=3, max_length=100, description="Product name")
    product_type: ProductType = Field(..., description="Product line/category")
    model_number: str = Field(..., min_length=2, max_length=20, description="Model number")
    release_date: datetime = Field(..., description="Product release date")
    description: Optional[str] = Field(None, max_length=500, description="Product description")
    features: List[ConnectivityFeature] = Field(default_factory=list, description="Connectivity features")
    power_type: PowerType = Field(..., description="Power source type")
    battery_life_hours: Optional[float] = Field(None, ge=0, description="Battery life in hours")
    weight_grams: Optional[float] = Field(None, ge=0, description="Weight in grams")
    water_resistance_rating: Optional[str] = Field(None, description="IP water resistance rating")
    compatible_accessories: List[str] = Field(default_factory=list, description="List of compatible accessory IDs")
    technical_specs: Dict[str, str] = Field(default_factory=dict, description="Additional technical specifications")
    is_current_model: bool = Field(default=True, description="Is this a current production model?")
    
    @validator('product_id')
    def validate_product_id(cls, v):
        if not v.isalnum():
            raise ValueError("Product ID must be alphanumeric")
        return v.upper()
    
    @validator('model_number')
    def validate_model_number(cls, v):
        if not v.replace("-", "").isalnum():
            raise ValueError("Model number must be alphanumeric (hyphens allowed)")
        return v.upper()

class ProductUpdate(BaseModel):
    """
    Schema for updating hearing aid product information (all fields optional).
    """
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    features: Optional[List[ConnectivityFeature]] = None
    battery_life_hours: Optional[float] = Field(None, ge=0)
    weight_grams: Optional[float] = Field(None, ge=0)
    water_resistance_rating: Optional[str] = None
    compatible_accessories: Optional[List[str]] = None
    technical_specs: Optional[Dict[str, str]] = None
    is_current_model: Optional[bool] = None

class ProductResponse(BaseModel):
    """
    Response model for product information with additional calculated fields.
    """
    product_id: str
    name: str
    product_type: ProductType
    model_number: str
    release_date: datetime
    description: Optional[str]
    features: List[ConnectivityFeature]
    power_type: PowerType
    battery_life_hours: Optional[float]
    weight_grams: Optional[float]
    water_resistance_rating: Optional[str]
    compatible_accessories: List[str]
    technical_specs: Dict[str, str]
    is_current_model: bool
    years_since_release: float
    
    @classmethod
    def from_product(cls, product: HearingAidProduct):
        years_since_release = (datetime.now() - product.release_date).days / 365.25
        return cls(
            **product.dict(),
            years_since_release=round(years_since_release, 1)
        )
```
