"""
Generated Code Metadata:
========================
Original URL: https://npaautocare.zouxiaodong.workers.dev
Prompt: Create a data model for storing information about NAPA Auto Care services, including service categories, prices, and descriptions, and suggest a database schema for managing this data.
Generated: DETERMINISTIC_48054f2c3f94d29b
Batch ID: 20250622_205031
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
from pydantic import BaseModel, Field, validator
from enum import Enum

class ServiceCategory(str, Enum):
    OIL_CHANGE = "Oil Change"
    TIRE_ROTATION = "Tire Rotation"
    BRAKE_SERVICE = "Brake Service"
    BATTERY_SERVICE = "Battery Service"
    ALIGNMENT = "Alignment"
    DIAGNOSTICS = "Diagnostics"
    FLUID_SERVICE = "Fluid Service"
    FILTER_REPLACEMENT = "Filter Replacement"
    OTHER = "Other"

class Service(BaseModel):
    """
    Represents an auto care service offered by NAPA.
    """
    id: str = Field(..., description="Unique identifier for the service")
    name: str = Field(..., min_length=3, max_length=100, description="Name of the service")
    category: ServiceCategory = Field(..., description="Category of the service")
    description: str = Field(..., min_length=10, max_length=500, description="Detailed description of the service")
    base_price: float = Field(..., gt=0, description="Base price of the service in USD")
    estimated_duration_minutes: int = Field(..., gt=0, description="Estimated duration in minutes")
    is_active: bool = Field(default=True, description="Whether the service is currently offered")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="When the service was added")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")

    @validator('name')
    def name_must_contain_letters(cls, v):
        if not any(c.isalpha() for c in v):
            raise ValueError('Name must contain at least one letter')
        return v

class ServiceUpdate(BaseModel):
    """
    Model for updating service information (all fields optional).
    """
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    category: Optional[ServiceCategory]
    description: Optional[str] = Field(None, min_length=10, max_length=500)
    base_price: Optional[float] = Field(None, gt=0)
    estimated_duration_minutes: Optional[int] = Field(None, gt=0)
    is_active: Optional[bool]

class ServiceResponse(BaseModel):
    """
    Response model for service data including metadata.
    """
    success: bool
    message: str
    data: Optional[Service]
    errors: Optional[List[str]]

# Database schema (SQL)
SQL_SCHEMA = """
CREATE TABLE service_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE services (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    category_id INTEGER REFERENCES service_categories(id) ON DELETE RESTRICT,
    description TEXT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL CHECK (base_price > 0),
    estimated_duration_minutes INTEGER NOT NULL CHECK (estimated_duration_minutes > 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_name CHECK (name ~ '[A-Za-z]')
);

CREATE INDEX idx_services_category ON services(category_id);
CREATE INDEX idx_services_active ON services(is_active) WHERE is_active = TRUE;

CREATE OR REPLACE FUNCTION update_modified_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_service_timestamp
BEFORE UPDATE ON services
FOR EACH ROW EXECUTE FUNCTION update_modified_timestamp();
"""
```
