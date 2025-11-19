"""
Generated Code Metadata:
========================
Original URL: https://globalhospitalitysolution.com
Prompt: Create a program to manage customized holiday packages, incorporating domestic and international destinations like Thailand, Maldives, and Sri Lanka, as described by Global Hospitality Solution.
Generated: DETERMINISTIC_733717776fc79a55
Batch ID: 20250612_153246
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/resort.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/maldives.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/srilanka.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/thailand.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from enum import Enum
from typing import List, Optional, Dict
import uuid
from datetime import date, datetime
import sys

class DestinationType(Enum):
    DOMESTIC = "domestic"
    INTERNATIONAL = "international"

class PackageStatus(Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"

@dataclass
class Destination:
    id: str
    name: str
    type: DestinationType
    description: str
    popular_attractions: List[str]
    best_time_to_visit: str
    image_url: Optional[str] = None

@dataclass
class Activity:
    id: str
    name: str
    description: str
    duration_hours: float
    cost: float

@dataclass
class Accommodation:
    id: str
    name: str
    type: str  # e.g., hotel, resort, villa
    description: str
    cost_per_night: float
    amenities: List[str]
    image_url: Optional[str] = None

@dataclass
class Transportation:
    id: str
    mode: str  # e.g., flight, train, bus
    provider: str
    cost: float
    departure_time: datetime
    arrival_time: datetime

@dataclass
class HolidayPackage:
    id: str
    name: str
    destination_id: str
    duration_days: int
    status: PackageStatus
    activities: List[Activity]
    accommodations: List[Accommodation]
    transportations: List[Transportation]
    total_cost: float
    discount: float = 0.0
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

class HolidayPackageManager:
    def __init__(self):
        self.destinations: Dict[str, Destination] = {}
        self.packages: Dict[str, HolidayPackage] = {}
        self._load_initial_data()

    def _load_initial_data(self):
        """Load initial sample data for destinations."""
        thailand = Destination(
            id=str(uuid.uuid4()),
            name="Thailand",
            type=DestinationType.INTERNATIONAL,
            description="Land of smiles with beautiful beaches and rich culture.",
            popular_attractions=["Bangkok", "Phuket", "Chiang Mai"],
            best_time_to_visit="November to February",
            image_url="https://example.com/thailand.jpg"
        )
        
        maldives = Destination(
            id=str(uuid.uuid4()),
            name="Maldives",
            type=DestinationType.INTERNATIONAL,
            description="Tropical paradise with overwater bungalows and crystal clear waters.",
            popular_attractions=["Male", "Maafushi", "Ari Atoll"],
            best_time_to_visit="November to April",
            image_url="https://example.com/maldives.jpg"
        )
        
        sri_lanka = Destination(
            id=str(uuid.uuid4()),
            name="Sri Lanka",
            type=DestinationType.INTERNATIONAL,
            description="Pearl of the Indian Ocean with diverse landscapes and heritage sites.",
            popular_attractions=["Colombo", "Kandy", "Galle"],
            best_time_to_visit="December to March",
            image_url="https://example.com/srilanka.jpg"
        )
        
        self.destinations[thailand.id] = thailand
        self.destinations[maldives.id] = maldives
        self.destinations[sri_lanka.id] = sri_lanka

    def create_package(
        self,
        name: str,
        destination_id: str,
        duration_days: int,
        activities: List[Activity],
        accommodations: List[Accommodation],
        transportations: List[Transportation],
        discount: float = 0.0
    ) -> HolidayPackage:
        """Create a new holiday package."""
        if destination_id not in self.destinations:
            raise ValueError("Destination not found")
        
        total_cost = self._calculate_total_cost(activities, accommodations, transportations, discount)
        
        package = HolidayPackage(
            id=str(uuid.uuid4()),
            name=name,
            destination_id=destination_id,
            duration_days=duration_days,
            status=PackageStatus.DRAFT,
            activities=activities,
            accommodations=accommodations,
            transportations=transportations,
            total_cost=total_cost,
            discount=discount
        )
        
        self.packages[package.id] = package
        return package

    def _calculate_total_cost(
        self,
        activities: List[Activity],
        accommodations: List[Accommodation],
        transportations: List[Transportation],
        discount: float
    ) -> float:
        """Calculate the total cost of the package with discount."""
        activity_cost = sum(activity.cost for activity in activities)
        accommodation_cost = sum(acc.cost_per_night for acc in accommodations)
        transportation_cost = sum(t.cost for t in transportations)
        
        total = activity_cost + accommodation_cost + transportation_cost
        return total * (1 - discount / 100)

    def update_package_status(self, package_id: str, status: PackageStatus) -> HolidayPackage:
        """Update the status of a package."""
        if package_id not in self.packages:
            raise ValueError("Package not found")
        
        package = self.packages[package_id]
        package.status = status
        package.updated_at = datetime.now()
        return package

    def get_package(self, package_id: str) -> HolidayPackage:
        """Retrieve a package by ID."""
        if package_id not in self.packages:
            raise ValueError("Package not found")
        return self.packages[package_id]

    def get_all_packages(self, status: Optional[PackageStatus] = None) -> List[HolidayPackage]:
        """Retrieve all packages, optionally filtered by status."""
        if status:
            return [p for p in self.packages.values() if p.status == status]
        return list(self.packages.values())

    def delete_package(self, package_id: str) -> None:
        """Delete a package by ID."""
        if package_id not in self.packages:
            raise ValueError("Package not found")
        del self.packages[package_id]

    def search_packages_by_destination(self, destination_name: str) -> List[HolidayPackage]:
        """Search packages by destination name."""
        destination_ids = [
            dest.id for dest in self.destinations.values() 
            if destination_name.lower() in dest.name.lower()
        ]
        
        return [
            package for package in self.packages.values()
            if package.destination_id in destination_ids
        ]

    def to_json(self, obj) -> str:
        """Convert an object to JSON string."""
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Enum):
            return obj.value
        return json.dumps(asdict(obj), default=self.to_json)

def main():
    manager = HolidayPackageManager()
    
    # Sample activity
    snorkeling = Activity(
        id=str(uuid.uuid4()),
        name="Snorkeling Adventure",
        description="Explore coral reefs with expert guides",
        duration_hours=3.5,
        cost=75.0
    )
    
    # Sample accommodation
    resort = Accommodation(
        id=str(uuid.uuid4()),
        name="Luxury Beach Resort",
        type="resort",
        description="5-star resort with private beach access",
        cost_per_night=350.0,
        amenities=["Pool", "Spa", "Restaurant"],
        image_url="https://example.com/resort.jpg"
    )
    
    # Sample transportation
    flight = Transportation(
        id=str(uuid.uuid4()),
        mode="flight",
        provider="Global Airways",
        cost=1200.0,
        departure_time=datetime(2023, 12, 15, 8, 0),
        arrival_time=datetime(2023, 12, 15, 14, 30)
    )
    
    # Create a package
    try:
        package = manager.create_package(
            name="Maldives Luxury Getaway",
            destination_id=next(iter(manager.destinations.values())).id,
            duration_days=7,
            activities=[snorkeling],
            accommodations=[resort],
            transportations=[flight],
            discount=10.0
        )
        
        print(f"Created package: {manager.to_json(package)}")
        
        # Update status
        updated_package = manager.update_package_status(package.id, PackageStatus.PUBLISHED)
        print(f"Updated package status: {updated_package.status.value}")
        
        # Search packages
        maldives_packages = manager.search_packages_by_destination("Maldives")
        print(f"Found {len(maldives_packages)} packages for Maldives")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
