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
# environmental_testing_labs.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class KitStatus(str, Enum):
    """Status of a sample kit."""
    AVAILABLE = "available"
    IN_USE = "in_use"
    DISCARDED = "discarded"

@dataclass
class SampleKit:
    """Represents a sample kit."""
    kit_id: int
    kit_name: str
    status: KitStatus = KitStatus.AVAILABLE
    cost: float = 0.0

@dataclass
class Media:
    """Represents a media for environmental testing."""
    media_id: int
    media_name: str
    description: str

class ABLabsService:
    """Simulates A&B Labs services for sample kits."""
    def __init__(self):
        self.kits: Dict[int, SampleKit] = {}
        self.media: Dict[int, Media] = {}

    def add_kit(self, kit: SampleKit):
        """Add a sample kit to the system."""
        self.kits[kit.kit_id] = kit

    def add_media(self, media: Media):
        """Add a media to the system."""
        self.media[media.media_id] = media

    def get_kit(self, kit_id: int) -> SampleKit:
        """Retrieve a sample kit by ID."""
        return self.kits.get(kit_id)

    def get_media(self, media_id: int) -> Media:
        """Retrieve a media by ID."""
        return self.media.get(media_id)

    def update_kit_status(self, kit_id: int, status: KitStatus):
        """Update the status of a sample kit."""
        kit = self.get_kit(kit_id)
        if kit:
            kit.status = status
        else:
            raise ValueError(f"Kit {kit_id} not found")

class EnvironmentalTestingLab:
    """Manages sample kits and media for environmental testing laboratories."""
    def __init__(self, ab_labs_service: ABLabsService):
        self.ab_labs_service = ab_labs_service
        self.kit_costs: Dict[int, float] = {}
        self.media_costs: Dict[int, float] = {}

    def add_kit_cost(self, kit_id: int, cost: float):
        """Add the cost of a sample kit."""
        self.kit_costs[kit_id] = cost
        kit = self.ab_labs_service.get_kit(kit_id)
        if kit:
            kit.cost = cost

    def add_media_cost(self, media_id: int, cost: float):
        """Add the cost of a media."""
        self.media_costs[media_id] = cost

    def calculate_total_cost(self, kit_ids: List[int], media_ids: List[int]) -> float:
        """Calculate the total cost of sample kits and media."""
        total_cost = 0.0
        for kit_id in kit_ids:
            total_cost += self.kit_costs.get(kit_id, 0.0)
        for media_id in media_ids:
            total_cost += self.media_costs.get(media_id, 0.0)
        return total_cost

def main():
    # Create A&B Labs service
    ab_labs_service = ABLabsService()

    # Create sample kits
    kit1 = SampleKit(1, "Kit 1")
    kit2 = SampleKit(2, "Kit 2")
    ab_labs_service.add_kit(kit1)
    ab_labs_service.add_kit(kit2)

    # Create media
    media1 = Media(1, "Media 1", "Description 1")
    media2 = Media(2, "Media 2", "Description 2")
    ab_labs_service.add_media(media1)
    ab_labs_service.add_media(media2)

    # Create environmental testing lab
    lab = EnvironmentalTestingLab(ab_labs_service)

    # Add costs
    lab.add_kit_cost(1, 100.0)
    lab.add_kit_cost(2, 200.0)
    lab.add_media_cost(1, 50.0)
    lab.add_media_cost(2, 75.0)

    # Calculate total cost
    kit_ids = [1, 2]
    media_ids = [1, 2]
    total_cost = lab.calculate_total_cost(kit_ids, media_ids)
    print(f"Total cost: ${total_cost:.2f}")

    # Update kit status
    ab_labs_service.update_kit_status(1, KitStatus.IN_USE)

if __name__ == "__main__":
    main()
```
