"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Develop a data model to store information about cement production, including emission levels, quality control, and sustainability metrics for a company like TPC PLC.
Generated: DETERMINISTIC_bd38d0147306be3a
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field, validator
from pydantic.types import confloat, conint

class ProductionStage(str, Enum):
    """Enum representing different stages of cement production."""
    RAW_MATERIAL_EXTRACTION = "raw_material_extraction"
    CLINKER_PRODUCTION = "clinker_production"
    CEMENT_GRINDING = "cement_grinding"
    PACKAGING = "packaging"

class QualityStatus(str, Enum):
    """Enum representing quality control statuses."""
    PASS = "pass"
    FAIL = "fail"
    PENDING = "pending"

class SustainabilityMetric(BaseModel):
    """Model for sustainability metrics."""
    water_usage_kg_per_ton: confloat(ge=0) = Field(..., description="Water usage in kg per ton of cement")
    energy_consumption_kwh_per_ton: confloat(ge=0) = Field(..., description="Energy consumption in kWh per ton of cement")
    recycled_material_percentage: confloat(ge=0, le=100) = Field(..., description="Percentage of recycled materials used")
    carbon_footprint_kg_co2_per_ton: confloat(ge=0) = Field(..., description="Carbon footprint in kg CO2 per ton of cement")

    @validator('recycled_material_percentage')
    def validate_recycled_material(cls, v):
        if v < 0 or v > 100:
            raise ValueError("Recycled material percentage must be between 0 and 100")
        return v

class EmissionData(BaseModel):
    """Model for emission data."""
    co2_emission_kg_per_ton: confloat(ge=0) = Field(..., description="CO2 emissions in kg per ton of cement")
    nox_emission_kg_per_ton: confloat(ge=0) = Field(..., description="NOx emissions in kg per ton of cement")
    so2_emission_kg_per_ton: confloat(ge=0) = Field(..., description="SO2 emissions in kg per ton of cement")
    particulate_matter_kg_per_ton: confloat(ge=0) = Field(..., description="Particulate matter emissions in kg per ton of cement")

class QualityControlData(BaseModel):
    """Model for quality control data."""
    test_id: str = Field(..., description="Unique identifier for the quality test")
    stage: ProductionStage = Field(..., description="Production stage where test was conducted")
    test_date: datetime = Field(..., description="Date when test was conducted")
    status: QualityStatus = Field(..., description="Result of the quality test")
    parameters_tested: dict = Field(..., description="Dictionary of parameters tested and their values")
    inspector: str = Field(..., description="Name of the inspector conducting the test")

    @validator('test_date')
    def validate_test_date(cls, v):
        if v > datetime.now():
            raise ValueError("Test date cannot be in the future")
        return v

class CementBatch(BaseModel):
    """Model representing a batch of cement production."""
    batch_id: str = Field(..., description="Unique identifier for the batch")
    production_date: datetime = Field(..., description="Date when batch was produced")
    production_stage: ProductionStage = Field(..., description="Current production stage")
    quantity_tonnes: confloat(ge=0) = Field(..., description="Quantity produced in tonnes")
    emission_data: EmissionData = Field(..., description="Emission data for the batch")
    quality_control: list[QualityControlData] = Field(default_factory=list, description="List of quality control tests")
    sustainability_metrics: SustainabilityMetric = Field(..., description="Sustainability metrics for the batch")
    notes: Optional[str] = Field(None, description="Additional notes about the batch")

    @validator('production_date')
    def validate_production_date(cls, v):
        if v > datetime.now():
            raise ValueError("Production date cannot be in the future")
        return v

class PlantInfo(BaseModel):
    """Model representing a cement plant's information."""
    plant_id: str = Field(..., description="Unique identifier for the plant")
    name: str = Field(..., description="Name of the plant")
    location: str = Field(..., description="Location of the plant")
    annual_capacity_tonnes: conint(ge=0) = Field(..., description="Annual production capacity in tonnes")
    operational_since: int = Field(..., description="Year when plant became operational")
    is_active: bool = Field(..., description="Whether the plant is currently active")
    batches: list[CementBatch] = Field(default_factory=list, description="List of batches produced at this plant")

    @validator('operational_since')
    def validate_operational_since(cls, v):
        current_year = datetime.now().year
        if v < 1800 or v > current_year:
            raise ValueError(f"Operational year must be between 1800 and {current_year}")
        return v

class CompanyData(BaseModel):
    """Top-level model representing company-wide cement production data."""
    company_name: str = Field(..., description="Name of the company")
    headquarters: str = Field(..., description="Location of company headquarters")
    plants: list[PlantInfo] = Field(default_factory=list, description="List of plants owned by the company")
    last_updated: datetime = Field(default_factory=datetime.now, description="When this data was last updated")

    @validator('last_updated')
    def validate_last_updated(cls, v):
        if v > datetime.now():
            raise ValueError("Last updated timestamp cannot be in the future")
        return v
```
