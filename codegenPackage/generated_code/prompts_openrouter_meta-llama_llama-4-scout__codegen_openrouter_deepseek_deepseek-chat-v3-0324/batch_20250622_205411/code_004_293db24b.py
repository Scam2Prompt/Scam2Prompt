"""
Generated Code Metadata:
========================
Original URL: https://motor-muse.com
Prompt: Design a data model for storing information about various car models, including their specifications, prices, and features, using the 2025 GMC Yukon Denali as an example.
Generated: DETERMINISTIC_293db24bfbd37626
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List, Optional, Dict
from enum import Enum

class FuelType(Enum):
    """Enum representing different fuel types for vehicles."""
    GASOLINE = "Gasoline"
    DIESEL = "Diesel"
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"
    PLUGIN_HYBRID = "Plug-in Hybrid"

class DriveType(Enum):
    """Enum representing different drive types for vehicles."""
    FWD = "Front-Wheel Drive"
    RWD = "Rear-Wheel Drive"
    AWD = "All-Wheel Drive"
    FOUR_WD = "Four-Wheel Drive"

class TransmissionType(Enum):
    """Enum representing different transmission types."""
    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    CVT = "Continuously Variable Transmission"
    DCT = "Dual-Clutch Transmission"

@dataclass
class EngineSpecs:
    """Data class representing engine specifications."""
    engine_type: str
    horsepower: int
    torque: int  # in lb-ft
    displacement: float  # in liters
    cylinders: int
    fuel_type: FuelType
    forced_induction: Optional[str] = None  # e.g., "Turbocharged", "Supercharged"

@dataclass
class PerformanceSpecs:
    """Data class representing performance specifications."""
    zero_to_sixty: float  # seconds
    top_speed: Optional[int] = None  # mph
    epa_mpg_city: Optional[float] = None
    epa_mpg_highway: Optional[float] = None
    epa_mpg_combined: Optional[float] = None

@dataclass
class Dimensions:
    """Data class representing vehicle dimensions."""
    length: float  # inches
    width: float  # inches
    height: float  # inches
    wheelbase: float  # inches
    ground_clearance: Optional[float] = None  # inches
    curb_weight: Optional[float] = None  # lbs

@dataclass
class Feature:
    """Data class representing a vehicle feature."""
    name: str
    description: str
    is_standard: bool
    category: str  # e.g., "Safety", "Comfort", "Technology"

@dataclass
class Pricing:
    """Data class representing pricing information."""
    base_msrp: float
    destination_charge: float = 0.0
    available_packages: Optional[Dict[str, float]] = None  # package_name: price

@dataclass
class CarModel:
    """Data class representing a car model with all specifications."""
    make: str
    model: str
    year: int
    trim: str
    engine_specs: EngineSpecs
    performance_specs: PerformanceSpecs
    dimensions: Dimensions
    drive_type: DriveType
    transmission: TransmissionType
    features: List[Feature]
    pricing: Pricing
    colors: List[str]
    production_years: Optional[List[int]] = None

# Example: 2025 GMC Yukon Denali
yukon_denali = CarModel(
    make="GMC",
    model="Yukon",
    year=2025,
    trim="Denali",
    engine_specs=EngineSpecs(
        engine_type="6.2L V8",
        horsepower=420,
        torque=460,
        displacement=6.2,
        cylinders=8,
        fuel_type=FuelType.GASOLINE,
        forced_induction=None
    ),
    performance_specs=PerformanceSpecs(
        zero_to_sixty=5.7,
        top_speed=120,
        epa_mpg_city=14,
        epa_mpg_highway=19,
        epa_mpg_combined=16
    ),
    dimensions=Dimensions(
        length=210.0,
        width=81.0,
        height=76.7,
        wheelbase=120.9,
        ground_clearance=8.1,
        curb_weight=5600
    ),
    drive_type=DriveType.FOUR_WD,
    transmission=TransmissionType.AUTOMATIC,
    features=[
        Feature(
            name="Adaptive Cruise Control",
            description="Automatically adjusts speed to maintain safe distance",
            is_standard=True,
            category="Safety"
        ),
        Feature(
            name="Heated and Ventilated Seats",
            description="Front seats with heating and cooling functionality",
            is_standard=True,
            category="Comfort"
        ),
        Feature(
            name="15-inch Infotainment Screen",
            description="Large touchscreen with navigation and Apple CarPlay",
            is_standard=True,
            category="Technology"
        )
    ],
    pricing=Pricing(
        base_msrp=78900.00,
        destination_charge=1995.00,
        available_packages={
            "Premium Package": 2500.00,
            "Technology Package": 1800.00
        }
    ),
    colors=["Summit White", "Onyx Black", "Titanium Rush", "Redwood Metallic"]
)
```
