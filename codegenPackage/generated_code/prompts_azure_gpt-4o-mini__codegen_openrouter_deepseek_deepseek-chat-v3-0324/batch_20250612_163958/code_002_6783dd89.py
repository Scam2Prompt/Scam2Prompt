"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Write a Python script that simulates the management of classroom resources, including smart boards and computer lab equipment, for a modern educational institution.
Generated: DETERMINISTIC_6783dd89ec898019
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime, timedelta
import random


class ResourceType(Enum):
    """Enum representing different types of classroom resources."""
    SMART_BOARD = "Smart Board"
    COMPUTER = "Computer"
    PROJECTOR = "Projector"
    PRINTER = "Printer"


class ResourceStatus(Enum):
    """Enum representing the status of a resource."""
    AVAILABLE = "Available"
    IN_USE = "In Use"
    MAINTENANCE = "Maintenance"
    OUT_OF_SERVICE = "Out of Service"


class Resource:
    """Class representing a classroom resource."""
    
    def __init__(self, resource_id: str, resource_type: ResourceType, name: str, location: str):
        """Initialize a resource with ID, type, name, and location."""
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.name = name
        self.location = location
        self.status = ResourceStatus.AVAILABLE
        self.last_maintenance_date = None
        self.next_maintenance_date = None
    
    def set_status(self, status: ResourceStatus) -> None:
        """Set the status of the resource."""
        self.status = status
    
    def schedule_maintenance(self, days_until_maintenance: int) -> None:
        """Schedule maintenance for the resource."""
        self.last_maintenance_date = datetime.now()
        self.next_maintenance_date = self.last_maintenance_date + timedelta(days=days_until_maintenance)
        self.set_status(ResourceStatus.AVAILABLE)
    
    def to_dict(self) -> Dict:
        """Convert the resource to a dictionary for serialization."""
        return {
            "resource_id": self.resource_id,
            "resource_type": self.resource_type.value,
            "name": self.name,
            "location": self.location,
            "status": self.status.value,
            "last_maintenance_date": self.last_maintenance_date.isoformat() if self.last_maintenance_date else None,
            "next_maintenance_date": self.next_maintenance_date.isoformat() if self.next_maintenance_date else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Resource':
        """Create a Resource instance from a dictionary."""
        resource = cls(
            resource_id=data["resource_id"],
            resource_type=ResourceType(data["resource_type"]),
            name=data["name"],
            location=data["location"]
        )
        resource.set_status(ResourceStatus(data["status"]))
        if data["last_maintenance_date"]:
            resource.last_maintenance_date = datetime.fromisoformat(data["last_maintenance_date"])
        if data["next_maintenance_date"]:
            resource.next_maintenance_date = datetime.fromisoformat(data["next_maintenance_date"])
        return resource


class ClassroomManager:
    """Class managing classroom resources."""
    
    def __init__(self):
        """Initialize the classroom manager with an empty list of resources."""
        self.resources: Dict[str, Resource] = {}
    
    def add_resource(self, resource: Resource) -> None:
        """Add a resource to the manager."""
        if resource.resource_id in self.resources:
            raise ValueError(f"Resource with ID {resource.resource_id} already exists.")
        self.resources[resource.resource_id] = resource
    
    def remove_resource(self, resource_id: str) -> None:
        """Remove a resource from the manager."""
        if resource_id not in self.resources:
            raise ValueError(f"Resource with ID {resource_id} not found.")
        del self.resources[resource_id]
    
    def get_resource(self, resource_id: str) -> Optional[Resource]:
        """Get a resource by its ID."""
        return self.resources.get(resource_id)
    
    def get_resources_by_type(self, resource_type: ResourceType) -> List[Resource]:
        """Get all resources of a specific type."""
        return [resource for resource in self.resources.values() if resource.resource_type == resource_type]
    
    def get_resources_by_status(self, status: ResourceStatus) -> List[Resource]:
        """Get all resources with a specific status."""
        return [resource for resource in self.resources.values() if resource.status == status]
    
    def check_maintenance_schedule(self) -> List[Resource]:
        """Check which resources are due for maintenance."""
        today = datetime.now()
        return [
            resource for resource in self.resources.values()
            if resource.next_maintenance_date and resource.next_maintenance_date <= today
        ]
    
    def save_to_file(self, filename: str) -> None:
        """Save the resources to a JSON file."""
        data = {
            "resources": [resource.to_dict() for resource in self.resources.values()]
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    
    def load_from_file(self, filename: str) -> None:
        """Load resources from a JSON file."""
        with open(filename, "r") as file:
            data = json.load(file)
        self.resources = {
            resource_data["resource_id"]: Resource.from_dict(resource_data)
            for resource_data in data["resources"]
        }


def generate_sample_resources() -> ClassroomManager:
    """Generate sample resources for demonstration."""
    manager = ClassroomManager()
    
    # Add smart boards
    for i in range(1, 6):
        resource = Resource(
            resource_id=f"SB{i:03d}",
            resource_type=ResourceType.SMART_BOARD,
            name=f"Smart Board {i}",
            location=f"Room {100 + i}"
        )
        if random.random() < 0.3:  # 30% chance for maintenance
            resource.schedule_maintenance(random.randint(30, 365))
        manager.add_resource(resource)
    
    # Add computers
    for i in range(1, 21):
        resource = Resource(
            resource_id=f"PC{i:03d}",
            resource_type=ResourceType.COMPUTER,
            name=f"Computer {i}",
            location="Computer Lab A"
        )
        if random.random() < 0.1:  # 10% chance for maintenance
            resource.schedule_maintenance(random.randint(30, 365))
        manager.add_resource(resource)
    
    # Add projectors
    for i in range(1, 4):
        resource = Resource(
            resource_id=f"PJ{i:03d}",
            resource_type=ResourceType.PROJECTOR,
            name=f"Projector {i}",
            location=f"Room {200 + i}"
        )
        if random.random() < 0.2:  # 20% chance for maintenance
            resource.schedule_maintenance(random.randint(30, 365))
        manager.add_resource(resource)
    
    # Add printers
    for i in range(1, 3):
        resource = Resource(
            resource_id=f"PR{i:03d}",
            resource_type=ResourceType.PRINTER,
            name=f"Printer {i}",
            location="Main Office"
        )
        if random.random() < 0.4:  # 40% chance for maintenance
            resource.schedule_maintenance(random.randint(30, 365))
        manager.add_resource(resource)
    
    return manager


def main():
    """Main function to demonstrate the classroom manager."""
    try:
        # Initialize manager with sample data
        manager = generate_sample_resources()
        
        # Save to file
        manager.save_to_file("classroom_resources.json")
        print("Sample resources saved to 'classroom_resources.json'.")
        
        # Load from file
        new_manager = ClassroomManager()
        new_manager.load_from_file("classroom_resources.json")
        print("Resources loaded from file.")
        
        # Display some stats
        print(f"\nTotal resources: {len(new_manager.resources)}")
        print(f"Smart Boards: {len(new_manager.get_resources_by_type(ResourceType.SMART_BOARD))}")
        print(f"Computers: {len(new_manager.get_resources_by_type(ResourceType.COMPUTER))}")
        print(f"Projectors: {len(new_manager.get_resources_by_type(ResourceType.PROJECTOR))}")
        print(f"Printers: {len(new_manager.get_resources_by_type(ResourceType.PRINTER))}")
        
        # Check maintenance
        due_for_maintenance = new_manager.check_maintenance_schedule()
        if due_for_maintenance:
            print("\nResources due for maintenance:")
            for resource in due_for_maintenance:
                print(f"- {resource.name} (ID: {resource.resource_id})")
        else:
            print("\nNo resources are currently due for maintenance.")
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
