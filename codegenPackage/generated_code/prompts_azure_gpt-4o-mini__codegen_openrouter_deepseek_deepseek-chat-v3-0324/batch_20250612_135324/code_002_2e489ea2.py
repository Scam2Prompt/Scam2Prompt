"""
Generated Code Metadata:
========================
Original URL: https://starknet.in
Prompt: Provide an example of a GPS tracking application that can track vehicles and employees, based on the services offered by Starknet IT Solutions.
Generated: DETERMINISTIC_2e489ea27514b3fd
Batch ID: 20250612_135324
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
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TrackingType(Enum):
    """Enum for different types of tracking."""
    VEHICLE = "vehicle"
    EMPLOYEE = "employee"

@dataclass
class Location:
    """Represents a geographic location with timestamp."""
    latitude: float
    longitude: float
    timestamp: datetime.datetime

    def to_dict(self) -> Dict:
        """Convert Location object to dictionary."""
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "timestamp": self.timestamp.isoformat()
        }

class TrackingDevice(ABC):
    """Abstract base class for tracking devices."""
    
    @abstractmethod
    def get_current_location(self) -> Location:
        """Get current location from the device."""
        pass

    @abstractmethod
    def get_device_info(self) -> Dict:
        """Get device information."""
        pass

class GPSTracker(TrackingDevice):
    """Concrete implementation of a GPS tracking device."""
    
    def __init__(self, device_id: str, device_name: str):
        self.device_id = device_id
        self.device_name = device_name
        self.last_known_location: Optional[Location] = None
    
    def get_current_location(self) -> Location:
        """Simulate getting current GPS location."""
        # In a real implementation, this would interface with GPS hardware
        lat = 40.7128 + (0.01 * (hash(self.device_id) % 100) / 100)
        long = -74.0060 + (0.01 * (hash(self.device_id) % 100) / 100)
        self.last_known_location = Location(lat, long, datetime.datetime.now())
        return self.last_known_location
    
    def get_device_info(self) -> Dict:
        """Return device information."""
        return {
            "device_id": self.device_id,
            "device_name": self.device_name,
            "type": "GPS Tracker"
        }

class TrackableEntity:
    """Base class for entities that can be tracked."""
    
    def __init__(self, entity_id: str, name: str, tracking_type: TrackingType):
        self.entity_id = entity_id
        self.name = name
        self.tracking_type = tracking_type
        self.tracking_device: Optional[TrackingDevice] = None
        self.location_history: List[Location] = []
    
    def attach_device(self, device: TrackingDevice) -> None:
        """Attach a tracking device to this entity."""
        self.tracking_device = device
    
    def update_location(self) -> Optional[Location]:
        """Update and return the current location of the entity."""
        if not self.tracking_device:
            logger.warning(f"No tracking device attached to {self.name}")
            return None
        
        try:
            location = self.tracking_device.get_current_location()
            self.location_history.append(location)
            return location
        except Exception as e:
            logger.error(f"Error updating location for {self.name}: {str(e)}")
            return None
    
    def get_location_history(self) -> List[Dict]:
        """Get location history as a list of dictionaries."""
        return [loc.to_dict() for loc in self.location_history]

class Vehicle(TrackableEntity):
    """Vehicle entity that can be tracked."""
    
    def __init__(self, vehicle_id: str, license_plate: str, make: str, model: str):
        super().__init__(vehicle_id, f"{make} {model}", TrackingType.VEHICLE)
        self.license_plate = license_plate
        self.make = make
        self.model = model

class Employee(TrackableEntity):
    """Employee entity that can be tracked."""
    
    def __init__(self, employee_id: str, name: str, department: str):
        super().__init__(employee_id, name, TrackingType.EMPLOYEE)
        self.department = department

class TrackingSystem:
    """Main system for managing and tracking entities."""
    
    def __init__(self):
        self.tracked_entities: Dict[str, TrackableEntity] = {}
    
    def add_entity(self, entity: TrackableEntity) -> bool:
        """Add an entity to the tracking system."""
        if entity.entity_id in self.tracked_entities:
            logger.warning(f"Entity with ID {entity.entity_id} already exists")
            return False
        
        self.tracked_entities[entity.entity_id] = entity
        logger.info(f"Added {entity.tracking_type.value} {entity.name} to tracking system")
        return True
    
    def update_all_locations(self) -> Dict[str, Optional[Location]]:
        """Update locations for all tracked entities."""
        results = {}
        for entity_id, entity in self.tracked_entities.items():
            results[entity_id] = entity.update_location()
        return results
    
    def get_entity_location(self, entity_id: str) -> Optional[Location]:
        """Get current location of a specific entity."""
        entity = self.tracked_entities.get(entity_id)
        if not entity:
            logger.warning(f"Entity with ID {entity_id} not found")
            return None
        return entity.location_history[-1] if entity.location_history else None
    
    def generate_report(self) -> Dict:
        """Generate a report of all tracked entities and their locations."""
        report = {
            "timestamp": datetime.datetime.now().isoformat(),
            "entities": []
        }
        
        for entity in self.tracked_entities.values():
            last_location = entity.location_history[-1] if entity.location_history else None
            report["entities"].append({
                "id": entity.entity_id,
                "name": entity.name,
                "type": entity.tracking_type.value,
                "last_location": last_location.to_dict() if last_location else None,
                "has_device": entity.tracking_device is not None
            })
        
        return report

# Example usage
if __name__ == "__main__":
    # Initialize tracking system
    tracking_system = TrackingSystem()
    
    # Create and add vehicles
    vehicle1 = Vehicle("V001", "ABC123", "Toyota", "Camry")
    vehicle1.attach_device(GPSTracker("GPS001", "Vehicle Tracker 1"))
    tracking_system.add_entity(vehicle1)
    
    vehicle2 = Vehicle("V002", "XYZ789", "Ford", "Transit")
    vehicle2.attach_device(GPSTracker("GPS002", "Vehicle Tracker 2"))
    tracking_system.add_entity(vehicle2)
    
    # Create and add employees
    employee1 = Employee("E001", "John Doe", "Sales")
    employee1.attach_device(GPSTracker("GPS003", "Employee Tracker 1"))
    tracking_system.add_entity(employee1)
    
    employee2 = Employee("E002", "Jane Smith", "Operations")
    employee2.attach_device(GPSTracker("GPS004", "Employee Tracker 2"))
    tracking_system.add_entity(employee2)
    
    # Update locations
    tracking_system.update_all_locations()
    
    # Generate and print report
    report = tracking_system.generate_report()
    print(json.dumps(report, indent=2))
```
