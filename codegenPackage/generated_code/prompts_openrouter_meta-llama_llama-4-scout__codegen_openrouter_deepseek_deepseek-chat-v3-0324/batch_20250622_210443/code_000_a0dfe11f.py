"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Write a Python script to manage event planning tasks such as scheduling, vendor management, and timeline creation for a corporate event.
Generated: DETERMINISTIC_a0dfe11fb5346529
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import List, Dict, Optional

class EventTask:
    """Represents a single task in the event planning process."""
    
    def __init__(self, name: str, description: str, deadline: str, assigned_to: str, status: str = "Pending"):
        """
        Initialize an event task.
        
        Args:
            name: Name of the task
            description: Description of the task
            deadline: Deadline in YYYY-MM-DD format
            assigned_to: Person assigned to the task
            status: Current status of the task (default: "Pending")
        """
        self.name = name
        self.description = description
        self.deadline = deadline
        self.assigned_to = assigned_to
        self.status = status
        
    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "deadline": self.deadline,
            "assigned_to": self.assigned_to,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'EventTask':
        """Create task from dictionary."""
        return cls(
            name=data["name"],
            description=data["description"],
            deadline=data["deadline"],
            assigned_to=data["assigned_to"],
            status=data.get("status", "Pending")
        )

class Vendor:
    """Represents a vendor for the event."""
    
    def __init__(self, name: str, service: str, contact: str, cost: float, contract_signed: bool = False):
        """
        Initialize a vendor.
        
        Args:
            name: Vendor name
            service: Service provided
            contact: Contact information
            cost: Cost of service
            contract_signed: Whether contract is signed (default: False)
        """
        self.name = name
        self.service = service
        self.contact = contact
        self.cost = cost
        self.contract_signed = contract_signed
        
    def to_dict(self) -> Dict:
        """Convert vendor to dictionary for serialization."""
        return {
            "name": self.name,
            "service": self.service,
            "contact": self.contact,
            "cost": self.cost,
            "contract_signed": self.contract_signed
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Vendor':
        """Create vendor from dictionary."""
        return cls(
            name=data["name"],
            service=data["service"],
            contact=data["contact"],
            cost=data["cost"],
            contract_signed=data.get("contract_signed", False)
        )

class EventTimeline:
    """Manages the timeline of events."""
    
    def __init__(self, start_date: str, end_date: str):
        """
        Initialize event timeline.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
        """
        self.start_date = start_date
        self.end_date = end_date
        self.milestones: List[Dict] = []
        
    def add_milestone(self, name: str, date: str, description: str):
        """Add a milestone to the timeline."""
        self.milestones.append({
            "name": name,
            "date": date,
            "description": description
        })
        
    def to_dict(self) -> Dict:
        """Convert timeline to dictionary for serialization."""
        return {
            "start_date": self.start_date,
            "end_date": self.end_date,
            "milestones": self.milestones
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'EventTimeline':
        """Create timeline from dictionary."""
        timeline = cls(
            start_date=data["start_date"],
            end_date=data["end_date"]
        )
        timeline.milestones = data.get("milestones", [])
        return timeline

class EventManager:
    """Main class to manage all aspects of event planning."""
    
    def __init__(self, event_name: str):
        """
        Initialize event manager.
        
        Args:
            event_name: Name of the event
        """
        self.event_name = event_name
        self.tasks: List[EventTask] = []
        self.vendors: List[Vendor] = []
        self.timeline: Optional[EventTimeline] = None
        
    def add_task(self, task: EventTask):
        """Add a task to the event."""
        self.tasks.append(task)
        
    def remove_task(self, task_name: str) -> bool:
        """Remove a task by name."""
        for i, task in enumerate(self.tasks):
            if task.name == task_name:
                del self.tasks[i]
                return True
        return False
        
    def update_task_status(self, task_name: str, new_status: str) -> bool:
        """Update task status."""
        for task in self.tasks:
            if task.name == task_name:
                task.status = new_status
                return True
        return False
        
    def add_vendor(self, vendor: Vendor):
        """Add a vendor to the event."""
        self.vendors.append(vendor)
        
    def remove_vendor(self, vendor_name: str) -> bool:
        """Remove a vendor by name."""
        for i, vendor in enumerate(self.vendors):
            if vendor.name == vendor_name:
                del self.vendors[i]
                return True
        return False
        
    def sign_vendor_contract(self, vendor_name: str) -> bool:
        """Mark vendor contract as signed."""
        for vendor in self.vendors:
            if vendor.name == vendor_name:
                vendor.contract_signed = True
                return True
        return False
        
    def set_timeline(self, timeline: EventTimeline):
        """Set the event timeline."""
        self.timeline = timeline
        
    def get_overdue_tasks(self) -> List[EventTask]:
        """Get all tasks that are overdue."""
        today = datetime.date.today().strftime("%Y-%m-%d")
        return [task for task in self.tasks if task.deadline < today and task.status != "Completed"]
        
    def to_dict(self) -> Dict:
        """Convert event manager to dictionary for serialization."""
        return {
            "event_name": self.event_name,
            "tasks": [task.to_dict() for task in self.tasks],
            "vendors": [vendor.to_dict() for vendor in self.vendors],
            "timeline": self.timeline.to_dict() if self.timeline else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'EventManager':
        """Create event manager from dictionary."""
        manager = cls(event_name=data["event_name"])
        manager.tasks = [EventTask.from_dict(task) for task in data.get("tasks", [])]
        manager.vendors = [Vendor.from_dict(vendor) for vendor in data.get("vendors", [])]
        if data.get("timeline"):
            manager.timeline = EventTimeline.from_dict(data["timeline"])
        return manager
        
    def save_to_file(self, filename: str):
        """Save event data to JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)
            
    @classmethod
    def load_from_file(cls, filename: str) -> 'EventManager':
        """Load event data from JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)

def main():
    """Example usage of the EventManager."""
    try:
        # Create a new event
        manager = EventManager("Annual Conference 2023")
        
        # Add tasks
        manager.add_task(EventTask(
            name="Venue Booking",
            description="Book the conference venue",
            deadline="2023-05-15",
            assigned_to="John Doe"
        ))
        
        manager.add_task(EventTask(
            name="Catering Arrangement",
            description="Arrange catering services",
            deadline="2023-06-01",
            assigned_to="Jane Smith"
        ))
        
        # Add vendors
        manager.add_vendor(Vendor(
            name="ABC Catering",
            service="Food and Beverage",
            contact="contact@abccatering.com",
            cost=5000.00
        ))
        
        manager.add_vendor(Vendor(
            name="XYZ AV",
            service="Audio Visual Equipment",
            contact="sales@xyzav.com",
            cost=3000.00
        ))
        
        # Sign a contract
        manager.sign_vendor_contract("ABC Catering")
        
        # Create timeline
        timeline = EventTimeline("2023-09-10", "2023-09-12")
        timeline.add_milestone("Setup", "2023-09-09", "Venue setup and equipment testing")
        timeline.add_milestone("Main Event", "2023-09-10", "First day of conference")
        manager.set_timeline(timeline)
        
        # Save to file
        manager.save_to_file("annual_conference_2023.json")
