"""
Generated Code Metadata:
========================
Original URL: https://rapala.tc
Prompt: Generate a code snippet for a travel booking system that includes features for customizing travel packages based on client preferences, similar to the offerings of Rapala Travel Concierge.
Generated: DETERMINISTIC_9280a69edd9260e1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from enum import Enum, auto
from typing import List, Optional, Dict, Any


class TravelType(Enum):
    """Enum representing different types of travel packages."""
    ADVENTURE = auto()
    LUXURY = auto()
    FAMILY = auto()
    BUSINESS = auto()
    SOLO = auto()


class AccommodationType(Enum):
    """Enum representing different types of accommodations."""
    HOTEL = auto()
    RESORT = auto()
    VILLA = auto()
    APARTMENT = auto()
    HOSTEL = auto()


class TransportationType(Enum):
    """Enum representing different types of transportation."""
    FLIGHT = auto()
    TRAIN = auto()
    CAR_RENTAL = auto()
    CRUISE = auto()
    BUS = auto()


@dataclass
class Activity:
    """Class representing a travel activity."""
    name: str
    description: str
    duration_hours: float
    cost: float


@dataclass
class Accommodation:
    """Class representing accommodation details."""
    type: AccommodationType
    name: str
    location: str
    cost_per_night: float
    amenities: List[str]


@dataclass
class Transportation:
    """Class representing transportation details."""
    type: TransportationType
    provider: str
    departure: str
    arrival: str
    cost: float


@dataclass
class TravelPackage:
    """Class representing a customizable travel package."""
    package_id: str
    name: str
    description: str
    travel_type: TravelType
    destination: str
    duration_days: int
    base_cost: float
    accommodations: List[Accommodation]
    transportation: List[Transportation]
    activities: List[Activity]
    customizations: Dict[str, Any] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert the travel package to a dictionary."""
        return asdict(self)

    def to_json(self) -> str:
        """Serialize the travel package to JSON."""
        return json.dumps(self.to_dict(), indent=2, default=str)


class TravelPackageBuilder:
    """Builder class for creating customized travel packages."""
    
    def __init__(self, package_id: str, name: str, description: str, travel_type: TravelType, destination: str):
        """Initialize the builder with basic package information."""
        self.package_id = package_id
        self.name = name
        self.description = description
        self.travel_type = travel_type
        self.destination = destination
        self.duration_days = 0
        self.base_cost = 0.0
        self.accommodations = []
        self.transportation = []
        self.activities = []
        self.customizations = {}

    def set_duration(self, duration_days: int) -> 'TravelPackageBuilder':
        """Set the duration of the travel package."""
        if duration_days <= 0:
            raise ValueError("Duration must be a positive integer")
        self.duration_days = duration_days
        return self

    def set_base_cost(self, cost: float) -> 'TravelPackageBuilder':
        """Set the base cost of the travel package."""
        if cost < 0:
            raise ValueError("Cost cannot be negative")
        self.base_cost = cost
        return self

    def add_accommodation(self, accommodation: Accommodation) -> 'TravelPackageBuilder':
        """Add an accommodation to the travel package."""
        self.accommodations.append(accommodation)
        return self

    def add_transportation(self, transportation: Transportation) -> 'TravelPackageBuilder':
        """Add a transportation option to the travel package."""
        self.transportation.append(transportation)
        return self

    def add_activity(self, activity: Activity) -> 'TravelPackageBuilder':
        """Add an activity to the travel package."""
        self.activities.append(activity)
        return self

    def add_customization(self, key: str, value: Any) -> 'TravelPackageBuilder':
        """Add a customization option to the travel package."""
        self.customizations[key] = value
        return self

    def build(self) -> TravelPackage:
        """Build the final travel package."""
        if not self.accommodations:
            raise ValueError("At least one accommodation is required")
        if not self.transportation:
            raise ValueError("At least one transportation option is required")
        if self.duration_days <= 0:
            raise ValueError("Duration must be set to a positive value")
        
        return TravelPackage(
            package_id=self.package_id,
            name=self.name,
            description=self.description,
            travel_type=self.travel_type,
            destination=self.destination,
            duration_days=self.duration_days,
            base_cost=self.base_cost,
            accommodations=self.accommodations,
            transportation=self.transportation,
            activities=self.activities,
            customizations=self.customizations
        )


class TravelPackageManager:
    """Manager class for handling travel package operations."""
    
    def __init__(self):
        """Initialize the package manager."""
        self.packages = {}

    def add_package(self, package: TravelPackage) -> None:
        """Add a travel package to the manager."""
        if package.package_id in self.packages:
            raise ValueError(f"Package with ID {package.package_id} already exists")
        self.packages[package.package_id] = package

    def get_package(self, package_id: str) -> Optional[TravelPackage]:
        """Retrieve a travel package by its ID."""
        return self.packages.get(package_id)

    def remove_package(self, package_id: str) -> bool:
        """Remove a travel package by its ID."""
        if package_id in self.packages:
            del self.packages[package_id]
            return True
        return False

    def list_packages(self) -> List[TravelPackage]:
        """List all available travel packages."""
        return list(self.packages.values())

    def filter_packages(self, travel_type: Optional[TravelType] = None, 
                        destination: Optional[str] = None) -> List[TravelPackage]:
        """Filter travel packages based on type and/or destination."""
        filtered = []
        for package in self.packages.values():
            if travel_type and package.travel_type != travel_type:
                continue
            if destination and package.destination.lower() != destination.lower():
                continue
            filtered.append(package)
        return filtered


# Example usage
if __name__ == "__main__":
    try:
        # Create a package builder
        builder = TravelPackageBuilder(
            package_id="PKG001",
            name="Luxury Maldives Getaway",
            description="A luxurious escape to the Maldives with premium accommodations",
            travel_type=TravelType.LUXURY,
            destination="Maldives"
        )

        # Set package details
        builder.set_duration(7).set_base_cost(5000.0)

        # Add accommodations
        builder.add_accommodation(Accommodation(
            type=AccommodationType.RESORT,
            name="Paradise Island Resort",
            location="North Male Atoll",
            cost_per_night=800.0,
            amenities=["Private Beach", "Infinity Pool", "Spa", "Gym"]
        ))

        # Add transportation
        builder.add_transportation(Transportation(
            type=TransportationType.FLIGHT,
            provider="Emirates",
            departure="New York (JFK)",
            arrival="Male (MLE)",
            cost=1200.0
        ))

        # Add activities
        builder.add_activity(Activity(
            name="Private Sunset Cruise",
            description="A romantic sunset cruise with champagne",
            duration_hours=2.5,
            cost=300.0
        ))

        # Add customizations
        builder.add_customization("meal_plan", "All Inclusive")
        builder.add_customization("spa_treatments", ["Massage", "Facial"])

        # Build the package
        package = builder.build()

        # Create package manager and add package
        manager = TravelPackageManager()
        manager.add_package(package)

        # Print package details
        print(package.to_json())

    except ValueError as e:
        print(f"Error creating travel package: {e}")
```
