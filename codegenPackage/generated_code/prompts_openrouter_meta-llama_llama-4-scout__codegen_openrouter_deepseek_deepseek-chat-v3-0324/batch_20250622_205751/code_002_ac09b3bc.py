"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Develop a code snippet to track and control changes to a building's status using the Electronic Identity of Buildings/ Apartments (ΗΤΚ) system.
Generated: DETERMINISTIC_ac09b3bcab07f53b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from enum import Enum
from typing import Dict, List, Optional


class BuildingStatus(Enum):
    """Enum representing possible building statuses."""
    UNDER_CONSTRUCTION = "UNDER_CONSTRUCTION"
    OCCUPIED = "OCCUPIED"
    VACANT = "VACANT"
    DEMOLISHED = "DEMOLISHED"
    RENOVATED = "RENOVATED"


class ChangeType(Enum):
    """Enum representing types of changes."""
    STATUS_UPDATE = "STATUS_UPDATE"
    OWNERSHIP_CHANGE = "OWNERSHIP_CHANGE"
    MAINTENANCE = "MAINTENANCE"


class BuildingChange:
    """Class representing a change to a building's status."""
    
    def __init__(
        self,
        change_type: ChangeType,
        new_status: BuildingStatus,
        timestamp: datetime.datetime,
        description: str,
        initiator: str
    ):
        self.change_type = change_type
        self.new_status = new_status
        self.timestamp = timestamp
        self.description = description
        self.initiator = initiator
    
    def to_dict(self) -> Dict:
        """Convert the change to a dictionary for serialization."""
        return {
            "change_type": self.change_type.value,
            "new_status": self.new_status.value,
            "timestamp": self.timestamp.isoformat(),
            "description": self.description,
            "initiator": self.initiator
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'BuildingChange':
        """Create a BuildingChange from a dictionary."""
        return cls(
            change_type=ChangeType(data["change_type"]),
            new_status=BuildingStatus(data["new_status"]),
            timestamp=datetime.datetime.fromisoformat(data["timestamp"]),
            description=data["description"],
            initiator=data["initiator"]
        )


class HTKBuilding:
    """Class representing a building in the HTK system."""
    
    def __init__(self, building_id: str, initial_status: BuildingStatus):
        self.building_id = building_id
        self.current_status = initial_status
        self.change_history: List[BuildingChange] = []
    
    def update_status(
        self,
        new_status: BuildingStatus,
        change_type: ChangeType,
        description: str,
        initiator: str
    ) -> None:
        """Update the building's status and log the change."""
        if not isinstance(new_status, BuildingStatus):
            raise ValueError("Invalid building status")
        
        change = BuildingChange(
            change_type=change_type,
            new_status=new_status,
            timestamp=datetime.datetime.now(),
            description=description,
            initiator=initiator
        )
        
        self.change_history.append(change)
        self.current_status = new_status
    
    def get_change_history(self) -> List[Dict]:
        """Get the building's change history as a list of dictionaries."""
        return [change.to_dict() for change in self.change_history]
    
    def to_dict(self) -> Dict:
        """Convert the building to a dictionary for serialization."""
        return {
            "building_id": self.building_id,
            "current_status": self.current_status.value,
            "change_history": [change.to_dict() for change in self.change_history]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'HTKBuilding':
        """Create an HTKBuilding from a dictionary."""
        building = cls(
            building_id=data["building_id"],
            initial_status=BuildingStatus(data["current_status"])
        )
        building.change_history = [
            BuildingChange.from_dict(change) for change in data["change_history"]
        ]
        return building


class HTKSystem:
    """Class representing the HTK system managing multiple buildings."""
    
    def __init__(self):
        self.buildings: Dict[str, HTKBuilding] = {}
    
    def add_building(self, building_id: str, initial_status: BuildingStatus) -> None:
        """Add a new building to the system."""
        if building_id in self.buildings:
            raise ValueError("Building ID already exists")
        self.buildings[building_id] = HTKBuilding(building_id, initial_status)
    
    def update_building_status(
        self,
        building_id: str,
        new_status: BuildingStatus,
        change_type: ChangeType,
        description: str,
        initiator: str
    ) -> None:
        """Update the status of a building."""
        if building_id not in self.buildings:
            raise ValueError("Building not found")
        self.buildings[building_id].update_status(
            new_status, change_type, description, initiator
        )
    
    def get_building_history(self, building_id: str) -> Optional[List[Dict]]:
        """Get the change history of a building."""
        if building_id not in self.buildings:
            return None
        return self.buildings[building_id].get_change_history()
    
    def save_to_file(self, file_path: str) -> None:
        """Save the system state to a JSON file."""
        data = {
            "buildings": {
                bid: building.to_dict() for bid, building in self.buildings.items()
            }
        }
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_from_file(cls, file_path: str) -> 'HTKSystem':
        """Load the system state from a JSON file."""
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        system = cls()
        for bid, building_data in data["buildings"].items():
            system.buildings[bid] = HTKBuilding.from_dict(building_data)
        return system
```
