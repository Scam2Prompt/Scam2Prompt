"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: "Create a data model for storing and retrieving information about various metal products, including Nickel 200 Forged Fittings and Alloy Steel Pipes."
Generated: DETERMINISTIC_65b0d941f9b3a15e
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from enum import Enum

class MaterialType(str, Enum):
    NICKEL_200 = "Nickel 200"
    ALLOY_STEEL = "Alloy Steel"
    STAINLESS_STEEL = "Stainless Steel"
    CARBON_STEEL = "Carbon Steel"
    OTHER = "Other"

class ProductType(str, Enum):
    FORGED_FITTINGS = "Forged Fittings"
    PIPES = "Pipes"
    VALVES = "Valves"
    FLANGES = "Flanges"
    OTHER = "Other"

class MetalProduct(BaseModel):
    """
    Data model for storing metal product information.
    """
    id: str = Field(..., description="Unique identifier for the product")
    name: str = Field(..., description="Product name (e.g., Nickel 200 Forged Fittings)")
    material_type: MaterialType = Field(..., description="Type of material")
    product_type: ProductType = Field(..., description="Type of product")
    description: Optional[str] = Field(None, description="Detailed product description")
    specifications: dict = Field(default_factory=dict, description="Technical specifications")
    price: Optional[float] = Field(None, description="Price per unit")
    available_quantity: int = Field(0, description="Current stock quantity")
    weight: Optional[float] = Field(None, description="Weight per unit in kg")
    dimensions: Optional[dict] = Field(None, description="Product dimensions")
    manufacturer: Optional[str] = Field(None, description="Manufacturer name")
    certifications: List[str] = Field(default_factory=list, description="List of certifications")

    @validator('price')
    def validate_price(cls, v):
        if v is not None and v < 0:
            raise ValueError("Price cannot be negative")
        return v

    @validator('available_quantity')
    def validate_quantity(cls, v):
        if v < 0:
            raise ValueError("Quantity cannot be negative")
        return v

class MetalProductUpdate(BaseModel):
    """
    Model for updating metal product information (all fields optional).
    """
    name: Optional[str] = None
    material_type: Optional[MaterialType] = None
    product_type: Optional[ProductType] = None
    description: Optional[str] = None
    specifications: Optional[dict] = None
    price: Optional[float] = None
    available_quantity: Optional[int] = None
    weight: Optional[float] = None
    dimensions: Optional[dict] = None
    manufacturer: Optional[str] = None
    certifications: Optional[List[str]] = None

    @validator('price')
    def validate_price(cls, v):
        if v is not None and v < 0:
            raise ValueError("Price cannot be negative")
        return v

    @validator('available_quantity')
    def validate_quantity(cls, v):
        if v is not None and v < 0:
            raise ValueError("Quantity cannot be negative")
        return v

class MetalProductResponse(BaseModel):
    """
    Response model for metal product operations.
    """
    success: bool
    message: str
    data: Optional[MetalProduct] = None
    error: Optional[str] = None
```
