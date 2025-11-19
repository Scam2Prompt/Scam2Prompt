"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Generate code to automate the scheduling of domestic services, including spring cleaning and garden maintenance, based on the property management offerings of Alphamor.
Generated: DETERMINISTIC_00bc0f5823860bcf
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
import json
import logging
from dataclasses import dataclass, field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ServiceType(Enum):
    """Enum representing different types of domestic services."""
    SPRING_CLEANING = "spring_cleaning"
    GARDEN_MAINTENANCE = "garden_maintenance"
    GENERAL_CLEANING = "general_cleaning"

@dataclass
class Property:
    """Class representing a property managed by Alphamor."""
    id: str
    address: str
    size_sqft: int
    has_garden: bool
    services_subscribed: List[ServiceType] = field(default_factory=list)

@dataclass
class ServiceSchedule:
    """Class representing a scheduled service."""
    service_id: str
    property_id: str
    service_type: ServiceType
    scheduled_date: datetime.date
    completed: bool = False

class Scheduler:
    """Main class for scheduling domestic services."""
    
    def __init__(self):
        self.properties: Dict[str, Property] = {}
        self.schedules: Dict[str, ServiceSchedule] = {}
    
    def add_property(self, property_data: Dict) -> None:
        """Add a property to the scheduler."""
        try:
            property_obj = Property(
                id=property_data["id"],
                address=property_data["address"],
                size_sqft=property_data["size_sqft"],
                has_garden=property_data["has_garden"],
                services_subscribed=[
                    ServiceType(service) for service in property_data.get("services_subscribed", [])
                ]
            )
            self.properties[property_obj.id] = property_obj
            logger.info(f"Added property: {property_obj.id}")
        except KeyError as e:
            logger.error(f"Missing required property field: {e}")
            raise
        except ValueError as e:
            logger.error(f"Invalid service type: {e}")
            raise
    
    def schedule_service(
        self,
        property_id: str,
        service_type: ServiceType,
        date: datetime.date,
        force_schedule: bool = False
    ) -> Optional[ServiceSchedule]:
        """Schedule a service for a property."""
        if property_id not in self.properties:
            logger.error(f"Property not found: {property_id}")
            return None
        
        property = self.properties[property_id]
        
        # Check if property is subscribed to this service
        if service_type not in property.services_subscribed and not force_schedule:
            logger.error(f"Property {property_id} not subscribed to {service_type.value}")
            return None
        
        # Additional validation for garden maintenance
        if service_type == ServiceType.GARDEN_MAINTENANCE and not property.has_garden:
            logger.error(f"Property {property_id} doesn't have a garden")
            return None
        
        # Generate unique service ID
        service_id = f"{property_id}_{service_type.value}_{date.isoformat()}"
        
        # Check for existing schedule
        if service_id in self.schedules:
            logger.warning(f"Service already scheduled: {service_id}")
            return self.schedules[service_id]
        
        # Create and store the schedule
        schedule = ServiceSchedule(
            service_id=service_id,
            property_id=property_id,
            service_type=service_type,
            scheduled_date=date
        )
        self.schedules[service_id] = schedule
        logger.info(f"Scheduled {service_type.value} for property {property_id} on {date}")
        return schedule
    
    def get_upcoming_schedules(
        self,
        days_ahead: int = 30,
        service_type: Optional[ServiceType] = None
    ) -> List[ServiceSchedule]:
        """Get upcoming schedules within the specified days."""
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)
        
        upcoming = []
        for schedule in self.schedules.values():
            if not schedule.completed and today <= schedule.scheduled_date <= end_date:
                if service_type is None or schedule.service_type == service_type:
                    upcoming.append(schedule)
        
        # Sort by date
        upcoming.sort(key=lambda x: x.scheduled_date)
        return upcoming
    
    def mark_completed(self, service_id: str) -> bool:
        """Mark a service as completed."""
        if service_id not in self.schedules:
            logger.error(f"Service not found: {service_id}")
            return False
        
        self.schedules[service_id].completed = True
        logger.info(f"Marked service {service_id} as completed")
        return True
    
    def save_to_file(self, filename: str) -> bool:
        """Save scheduler data to a JSON file."""
        try:
            data = {
                "properties": [
                    {
                        "id": prop.id,
                        "address": prop.address,
                        "size_sqft": prop.size_sqft,
                        "has_garden": prop.has_garden,
                        "services_subscribed": [s.value for s in prop.services_subscribed]
                    }
                    for prop in self.properties.values()
                ],
                "schedules": [
                    {
                        "service_id": s.service_id,
                        "property_id": s.property_id,
                        "service_type": s.service_type.value,
                        "scheduled_date": s.scheduled_date.isoformat(),
                        "completed": s.completed
                    }
                    for s in self.schedules.values()
                ]
            }
            
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            logger.info(f"Saved data to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save data: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load scheduler data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            # Clear existing data
            self.properties = {}
            self.schedules = {}
            
            # Load properties
            for prop_data in data.get("properties", []):
                self.add_property(prop_data)
            
            # Load schedules
            for sched_data in data.get("schedules", []):
                try:
                    schedule = ServiceSchedule(
                        service_id=sched_data["service_id"],
                        property_id=sched_data["property_id"],
                        service_type=ServiceType(sched_data["service_type"]),
                        scheduled_date=datetime.date.fromisoformat(sched_data["scheduled_date"]),
                        completed=sched_data.get("completed", False)
                    )
                    self.schedules[schedule.service_id] = schedule
                except (KeyError, ValueError) as e:
                    logger.error(f"Invalid schedule data: {e}")
                    continue
            
            logger.info(f"Loaded data from {filename}")
            return True
        except FileNotFoundError:
            logger.error(f"File not found: {filename}")
            return False
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in file: {filename}")
            return False
        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            return False

# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()
    
    # Add sample properties
    properties = [
        {
            "id": "prop1",
            "address": "123 Main St",
            "size_sqft": 1500,
            "has_garden": True,
            "services_subscribed": ["spring_cleaning", "garden_maintenance"]
        },
        {
            "id": "prop2",
            "address": "456 Oak Ave",
            "size_sqft": 2000,
            "has_garden": False,
            "services_subscribed": ["spring_cleaning"]
        }
    ]
    
    for prop in properties:
        scheduler.add_property(prop)
    
    # Schedule services
    today = datetime.date.today()
    scheduler.schedule_service("prop1", ServiceType.SPRING_CLEANING, today + datetime.timedelta(days=7))
    scheduler.schedule_service("prop1", ServiceType.GARDEN_MAINTENANCE, today + datetime.timedelta(days=14))
    scheduler.schedule_service("prop2", ServiceType.SPRING_CLEANING, today + datetime.timedelta(days=10))
    
    # Save to file
    scheduler.save_to_file("scheduler_data.json")
```
