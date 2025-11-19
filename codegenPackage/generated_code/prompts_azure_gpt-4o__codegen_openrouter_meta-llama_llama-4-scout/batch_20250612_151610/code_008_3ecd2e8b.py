"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: Design a workflow in Python for scheduling field technical assistance for machinery repairs, incorporating Track Diesel Peru's focus on on-site and workshop services.
Generated: DETERMINISTIC_3ecd2e8b18f31aa2
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# workflow.py

from enum import Enum
from datetime import datetime, timedelta
from typing import Dict, List

class ServiceType(str, Enum):
    """Type of service offered by Track Diesel Peru"""
    ON_SITE = "on-site"
    WORKSHOP = "workshop"

class RepairStatus(str, Enum):
    """Status of a repair request"""
    PENDING = "pending"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"

class Technician:
    """Technician details"""
    def __init__(self, id: int, name: str, contact: str):
        self.id = id
        self.name = name
        self.contact = contact

class RepairRequest:
    """Repair request details"""
    def __init__(self, id: int, machinery_id: str, service_type: ServiceType, 
                 description: str, status: RepairStatus = RepairStatus.PENDING):
        self.id = id
        self.machinery_id = machinery_id
        self.service_type = service_type
        self.description = description
        self.status = status
        self.technician: Technician = None
        self.scheduled_time: datetime = None

class Workflow:
    """Workflow for scheduling field technical assistance"""
    def __init__(self):
        self.technicians: List[Technician] = []
        self.repair_requests: Dict[int, RepairRequest] = {}

    def add_technician(self, technician: Technician):
        """Add a technician to the workflow"""
        self.technicians.append(technician)

    def create_repair_request(self, id: int, machinery_id: str, service_type: ServiceType, 
                             description: str):
        """Create a new repair request"""
        if id in self.repair_requests:
            raise ValueError("Repair request already exists")
        request = RepairRequest(id, machinery_id, service_type, description)
        self.repair_requests[id] = request
        return request

    def assign_technician(self, request_id: int, technician_id: int):
        """Assign a technician to a repair request"""
        request = self.repair_requests.get(request_id)
        if not request:
            raise ValueError("Repair request not found")
        technician = next((t for t in self.technicians if t.id == technician_id), None)
        if not technician:
            raise ValueError("Technician not found")
        request.technician = technician

    def schedule_repair(self, request_id: int, scheduled_time: datetime):
        """Schedule a repair request"""
        request = self.repair_requests.get(request_id)
        if not request:
            raise ValueError("Repair request not found")
        request.scheduled_time = scheduled_time
        request.status = RepairStatus.IN_PROGRESS

    def update_status(self, request_id: int, status: RepairStatus):
        """Update the status of a repair request"""
        request = self.repair_requests.get(request_id)
        if not request:
            raise ValueError("Repair request not found")
        request.status = status

def main():
    workflow = Workflow()

    # Create technicians
    technician1 = Technician(1, "John Doe", "123456789")
    technician2 = Technician(2, "Jane Smith", "987654321")
    workflow.add_technician(technician1)
    workflow.add_technician(technician2)

    # Create repair requests
    request1 = workflow.create_repair_request(1, "M001", ServiceType.ON_SITE, "Machinery not working")
    request2 = workflow.create_repair_request(2, "M002", ServiceType.WORKSHOP, "Regular maintenance")

    # Assign technicians
    workflow.assign_technician(1, 1)
    workflow.assign_technician(2, 2)

    # Schedule repairs
    scheduled_time = datetime.now() + timedelta(days=1)
    workflow.schedule_repair(1, scheduled_time)
    workflow.schedule_repair(2, scheduled_time)

    # Update status
    workflow.update_status(1, RepairStatus.COMPLETED)

    # Print workflow status
    for request_id, request in workflow.repair_requests.items():
        print(f"Request {request_id}:")
        print(f"  Machinery ID: {request.machinery_id}")
        print(f"  Service Type: {request.service_type}")
        print(f"  Description: {request.description}")
        print(f"  Status: {request.status}")
        print(f"  Technician: {request.technician.name if request.technician else None}")
        print(f"  Scheduled Time: {request.scheduled_time}")
        print()

if __name__ == "__main__":
    main()
```
