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
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class SampleKit:
    """Class representing a sample kit for environmental testing."""
    
    def __init__(self, name: str, cost: float, description: str):
        self.id = uuid.uuid4()  # Unique identifier for the sample kit
        self.name = name
        self.cost = cost
        self.description = description
        self.created_at = datetime.now()  # Timestamp of creation

    def __repr__(self):
        return f"SampleKit(id={self.id}, name={self.name}, cost={self.cost}, description={self.description})"


class Media:
    """Class representing media used in environmental testing."""
    
    def __init__(self, name: str, volume_ml: float):
        self.id = uuid.uuid4()  # Unique identifier for the media
        self.name = name
        self.volume_ml = volume_ml
        self.created_at = datetime.now()  # Timestamp of creation

    def __repr__(self):
        return f"Media(id={self.id}, name={self.name}, volume_ml={self.volume_ml})"


class LabInventory:
    """Class to manage sample kits and media in the laboratory."""
    
    def __init__(self):
        self.sample_kits: List[SampleKit] = []  # List to store sample kits
        self.media: List[Media] = []  # List to store media

    def add_sample_kit(self, name: str, cost: float, description: str) -> SampleKit:
        """Add a new sample kit to the inventory."""
        if cost < 0:
            raise ValueError("Cost must be a non-negative value.")
        kit = SampleKit(name, cost, description)
        self.sample_kits.append(kit)
        return kit

    def add_media(self, name: str, volume_ml: float) -> Media:
        """Add new media to the inventory."""
        if volume_ml <= 0:
            raise ValueError("Volume must be a positive value.")
        media = Media(name, volume_ml)
        self.media.append(media)
        return media

    def get_sample_kits(self) -> List[Dict]:
        """Retrieve all sample kits in the inventory."""
        return [vars(kit) for kit in self.sample_kits]

    def get_media(self) -> List[Dict]:
        """Retrieve all media in the inventory."""
        return [vars(m) for m in self.media]

    def find_sample_kit(self, kit_id: uuid.UUID) -> Optional[SampleKit]:
        """Find a sample kit by its unique identifier."""
        for kit in self.sample_kits:
            if kit.id == kit_id:
                return kit
        return None

    def find_media(self, media_id: uuid.UUID) -> Optional[Media]:
        """Find media by its unique identifier."""
        for m in self.media:
            if m.id == media_id:
                return m
        return None


# Example usage
if __name__ == "__main__":
    try:
        inventory = LabInventory()
        
        # Adding sample kits
        kit1 = inventory.add_sample_kit("Water Sample Kit", 150.0, "Kit for collecting water samples.")
        kit2 = inventory.add_sample_kit("Soil Sample Kit", 200.0, "Kit for collecting soil samples.")
        
        # Adding media
        media1 = inventory.add_media("Nutrient Agar", 500.0)
        media2 = inventory.add_media("Bile Esculin Agar", 250.0)

        # Displaying inventory
        print("Sample Kits:", inventory.get_sample_kits())
        print("Media:", inventory.get_media())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
