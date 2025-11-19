"""
Generated Code Metadata:
========================
Original URL: https://elara-celestia.com
Prompt: Create a data model to represent the L&T Elara Celestia project, including attributes for apartment configurations, pricing, and amenities.
Generated: DETERMINISTIC_0f84a4d514eed6a4
Batch ID: 20250622_212053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto

class ApartmentType(Enum):
    """Enum representing different apartment types."""
    STUDIO = auto()
    ONE_BHK = auto()
    TWO_BHK = auto()
    THREE_BHK = auto()
    FOUR_BHK = auto()

class Amenity(Enum):
    """Enum representing different amenities available."""
    SWIMMING_POOL = auto()
    GYM = auto()
    CLUB_HOUSE = auto()
    PARK = auto()
    PLAY_AREA = auto()
    POWER_BACKUP = auto()
    SECURITY = auto()
    PARKING = auto()
    LIFT = auto()

@dataclass
class ApartmentConfiguration:
    """Represents the configuration of an apartment."""
    type: ApartmentType
    carpet_area: float  # in square feet
    built_up_area: float  # in square feet
    floor_number: int
    total_floors: int
    facing_direction: str  # e.g., "North", "South", etc.
    balcony: bool
    bedrooms: int
    bathrooms: int

@dataclass
class Pricing:
    """Represents pricing details for an apartment."""
    base_price: float
    maintenance_charges: float
    registration_charges: float
    stamp_duty: float
    gst: float
    other_charges: Dict[str, float] = field(default_factory=dict)

    def total_price(self) -> float:
        """Calculate the total price including all charges."""
        return (
            self.base_price +
            self.maintenance_charges +
            self.registration_charges +
            self.stamp_duty +
            self.gst +
            sum(self.other_charges.values())
        )

@dataclass
class ApartmentUnit:
    """Represents a single apartment unit in the project."""
    unit_id: str
    configuration: ApartmentConfiguration
    pricing: Pricing
    amenities: List[Amenity]
    is_sold: bool = False
    booking_status: Optional[str] = None

@dataclass
class Tower:
    """Represents a tower in the project."""
    tower_id: str
    tower_name: str
    apartments: List[ApartmentUnit]
    total_floors: int

@dataclass
class Project:
    """Represents the L&T Elara Celestia project."""
    project_id: str
    project_name: str
    location: str
    towers: List[Tower]
    common_amenities: List[Amenity]
    possession_date: Optional[str] = None
    builder_name: str = "Larsen & Toubro"
    rera_number: Optional[str] = None

    def get_all_apartments(self) -> List[ApartmentUnit]:
        """Get all apartments across all towers."""
        return [apt for tower in self.towers for apt in tower.apartments]

    def get_available_apartments(self) -> List[ApartmentUnit]:
        """Get all available (unsold) apartments."""
        return [apt for apt in self.get_all_apartments() if not apt.is_sold]

    def get_apartments_by_type(self, apartment_type: ApartmentType) -> List[ApartmentUnit]:
        """Get apartments filtered by type."""
        return [apt for apt in self.get_all_apartments() if apt.configuration.type == apartment_type]
```
