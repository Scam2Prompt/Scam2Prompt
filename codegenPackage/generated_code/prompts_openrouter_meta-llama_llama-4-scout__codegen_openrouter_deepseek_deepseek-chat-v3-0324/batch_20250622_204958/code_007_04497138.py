"""
Generated Code Metadata:
========================
Original URL: https://demoablabs.com
Prompt: "Design a system to manage sample kits and media for environmental testing laboratories, considering the services and costs associated with sample kits provided by A&B Labs."
Generated: DETERMINISTIC_0449713869029a4d
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sample_kit_management.py
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from enum import Enum, auto


class KitStatus(Enum):
    AVAILABLE = auto()
    IN_USE = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    DISCARDED = auto()


class MediaType(Enum):
    WATER = auto()
    SOIL = auto()
    AIR = auto()
    BIOLOGICAL = auto()


@dataclass
class Media:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    type: MediaType
    description: str
    unit_cost: float
    expiration_date: datetime


@dataclass
class Service:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    cost: float
    turnaround_time_days: int


@dataclass
class SampleKit:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    status: KitStatus = KitStatus.AVAILABLE
    media: List[Media] = field(default_factory=list)
    services: List[Service] = field(default_factory=list)
    creation_date: datetime = field(default_factory=datetime.now)
    last_updated: datetime = field(default_factory=datetime.now)

    def add_media(self, media: Media) -> None:
        """Add media to the sample kit."""
        self.media.append(media)
        self.last_updated = datetime.now()

    def add_service(self, service: Service) -> None:
        """Add service to the sample kit."""
        self.services.append(service)
        self.last_updated = datetime.now()

    def update_status(self, new_status: KitStatus) -> None:
        """Update the status of the sample kit."""
        self.status = new_status
        self.last_updated = datetime.now()

    def calculate_total_cost(self) -> float:
        """Calculate the total cost of the sample kit including media and services."""
        media_cost = sum(m.unit_cost for m in self.media)
        service_cost = sum(s.cost for s in self.services)
        return media_cost + service_cost


class SampleKitManager:
    def __init__(self):
        self.kits: List[SampleKit] = []

    def create_kit(self, name: str, description: str) -> SampleKit:
        """Create a new sample kit."""
        kit = SampleKit(name=name, description=description)
        self.kits.append(kit)
        return kit

    def get_kit_by_id(self, kit_id: str) -> Optional[SampleKit]:
        """Retrieve a sample kit by its ID."""
        for kit in self.kits:
            if kit.id == kit_id:
                return kit
        return None

    def update_kit_status(self, kit_id: str, new_status: KitStatus) -> bool:
        """Update the status of a sample kit."""
        kit = self.get_kit_by_id(kit_id)
        if kit:
            kit.update_status(new_status)
            return True
        return False

    def add_media_to_kit(self, kit_id: str, media: Media) -> bool:
        """Add media to a sample kit."""
        kit = self.get_kit_by_id(kit_id)
        if kit:
            kit.add_media(media)
            return True
        return False

    def add_service_to_kit(self, kit_id: str, service: Service) -> bool:
        """Add service to a sample kit."""
        kit = self.get_kit_by_id(kit_id)
        if kit:
            kit.add_service(service)
            return True
        return False

    def get_total_cost_for_kit(self, kit_id: str) -> Optional[float]:
        """Calculate the total cost for a sample kit."""
        kit = self.get_kit_by_id(kit_id)
        if kit:
            return kit.calculate_total_cost()
        return None

    def get_kits_by_status(self, status: KitStatus) -> List[SampleKit]:
        """Retrieve all sample kits with a specific status."""
        return [kit for kit in self.kits if kit.status == status]

    def discard_expired_media(self, kit_id: str) -> bool:
        """Discard expired media from a sample kit."""
        kit = self.get_kit_by_id(kit_id)
        if not kit:
            return False

        current_date = datetime.now()
        expired_media = [m for m in kit.media if m.expiration_date < current_date]
        
        if not expired_media:
            return False

        kit.media = [m for m in kit.media if m.expiration_date >= current_date]
        kit.last_updated = datetime.now()
        return True


# Example usage
if __name__ == "__main__":
    manager = SampleKitManager()
    
    # Create a sample kit
    kit = manager.create_kit("Water Testing Kit", "Kit for testing water quality")
    
    # Add media to the kit
    water_media = Media(
        type=MediaType.WATER,
        description="Sterile water collection bottle",
        unit_cost=5.99,
        expiration_date=datetime(2024, 12, 31)
    )
    manager.add_media_to_kit(kit.id, water_media)
    
    # Add service to the kit
    testing_service = Service(
        name="Heavy Metal Analysis",
        description="Analysis for heavy metals in water samples",
        cost=150.00,
        turnaround_time_days=7
    )
    manager.add_service_to_kit(kit.id, testing_service)
    
    # Update kit status
    manager.update_kit_status(kit.id, KitStatus.IN_USE)
    
    # Calculate total cost
    total_cost = manager.get_total_cost_for_kit(kit.id)
    print(f"Total cost for kit {kit.id}: ${total_cost:.2f}")
```
