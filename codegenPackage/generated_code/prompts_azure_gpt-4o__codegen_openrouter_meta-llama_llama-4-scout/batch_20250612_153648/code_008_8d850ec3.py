"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Write code to automate the scheduling and resource allocation for managing large-scale residential complexes, inspired by the project management capabilities of Remas Engineering Consultants.
Generated: DETERMINISTIC_8d850ec3971d7a3d
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# complex_manager.py

from datetime import datetime, timedelta
from typing import Dict, List

class Resident:
    """Represents a resident in the complex."""
    
    def __init__(self, resident_id: int, name: str, contact_info: str):
        """
        Initializes a Resident object.

        Args:
        - resident_id (int): Unique identifier for the resident.
        - name (str): Name of the resident.
        - contact_info (str): Contact information of the resident.
        """
        self.resident_id = resident_id
        self.name = name
        self.contact_info = contact_info

class Resource:
    """Represents a resource in the complex."""
    
    def __init__(self, resource_id: int, resource_type: str, capacity: int):
        """
        Initializes a Resource object.

        Args:
        - resource_id (int): Unique identifier for the resource.
        - resource_type (str): Type of the resource (e.g., pool, gym, parking).
        - capacity (int): Capacity of the resource.
        """
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.capacity = capacity
        self.allocated = 0

class Schedule:
    """Represents a schedule for a resource."""
    
    def __init__(self, schedule_id: int, resource: Resource, start_time: datetime, end_time: datetime):
        """
        Initializes a Schedule object.

        Args:
        - schedule_id (int): Unique identifier for the schedule.
        - resource (Resource): Resource being scheduled.
        - start_time (datetime): Start time of the schedule.
        - end_time (datetime): End time of the schedule.
        """
        self.schedule_id = schedule_id
        self.resource = resource
        self.start_time = start_time
        self.end_time = end_time

class ComplexManager:
    """Manages large-scale residential complexes."""
    
    def __init__(self):
        """
        Initializes a ComplexManager object.
        """
        self.residents: Dict[int, Resident] = {}
        self.resources: Dict[int, Resource] = {}
        self.schedules: Dict[int, Schedule] = {}

    def add_resident(self, resident: Resident):
        """
        Adds a resident to the complex.

        Args:
        - resident (Resident): Resident to be added.
        """
        self.residents[resident.resident_id] = resident

    def add_resource(self, resource: Resource):
        """
        Adds a resource to the complex.

        Args:
        - resource (Resource): Resource to be added.
        """
        self.resources[resource.resource_id] = resource

    def schedule_resource(self, schedule: Schedule):
        """
        Schedules a resource.

        Args:
        - schedule (Schedule): Schedule to be added.

        Raises:
        - ValueError: If the resource is not available at the scheduled time.
        """
        resource = self.resources.get(schedule.resource.resource_id)
        if not resource:
            raise ValueError("Resource not found")

        overlapping_schedules = [s for s in self.schedules.values() 
                                 if s.resource.resource_id == schedule.resource.resource_id 
                                 and not (schedule.end_time <= s.start_time or schedule.start_time >= s.end_time)]

        if overlapping_schedules:
            raise ValueError("Resource is not available at the scheduled time")

        self.schedules[schedule.schedule_id] = schedule
        resource.allocated += 1

    def cancel_schedule(self, schedule_id: int):
        """
        Cancels a scheduled resource.

        Args:
        - schedule_id (int): ID of the schedule to be canceled.

        Raises:
        - ValueError: If the schedule is not found.
        """
        schedule = self.schedules.get(schedule_id)
        if not schedule:
            raise ValueError("Schedule not found")

        del self.schedules[schedule_id]
        schedule.resource.allocated -= 1

def main():
    # Example usage
    manager = ComplexManager()

    resident1 = Resident(1, "John Doe", "123-456-7890")
    manager.add_resident(resident1)

    resource1 = Resource(1, "Pool", 10)
    manager.add_resource(resource1)

    schedule1 = Schedule(1, resource1, datetime.now(), datetime.now() + timedelta(hours=2))
    manager.schedule_resource(schedule1)

    print("Schedules:")
    for schedule in manager.schedules.values():
        print(f"Schedule {schedule.schedule_id}: {schedule.resource.resource_type} from {schedule.start_time} to {schedule.end_time}")

if __name__ == "__main__":
    main()
```
