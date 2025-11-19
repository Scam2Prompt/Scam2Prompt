"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write code to simulate a carpet repair service workflow, including tasks like carpet seaming, restretching, and weaving, as outlined in Perfect Melbourne Carpet's services.
Generated: DETERMINISTIC_0e096e9ff0e9d4a0
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import enum
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Dict
import random
import uuid

class RepairType(enum.Enum):
    SEAMING = "Seaming"
    RESTRETCHING = "Restretching"
    WEAVING = "Weaving"
    PATCHING = "Patching"
    CLEANING = "Cleaning"

class RepairStatus(enum.Enum):
    SCHEDULED = "Scheduled"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

@dataclass
class Customer:
    id: str
    name: str
    address: str
    phone: str
    email: str

@dataclass
class CarpetDetails:
    material: str
    color: str
    age: int
    size_sqft: float
    pattern: Optional[str] = None

@dataclass
class RepairTask:
    id: str
    repair_type: RepairType
    description: str
    estimated_hours: float
    materials_needed: List[str]
    status: RepairStatus = RepairStatus.SCHEDULED
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    notes: Optional[str] = None

@dataclass
class ServiceRequest:
    id: str
    customer: Customer
    carpet: CarpetDetails
    tasks: List[RepairTask]
    request_date: datetime
    priority: int = 1
    assigned_technician: Optional[str] = None

class CarpetRepairService:
    def __init__(self):
        self.service_requests: Dict[str, ServiceRequest] = {}
        self.technicians = ["John Smith", "Emma Johnson", "Michael Brown", "Sarah Davis"]

    def create_service_request(self, customer: Customer, carpet: CarpetDetails, repair_types: List[RepairType]) -> ServiceRequest:
        request_id = str(uuid.uuid4())
        tasks = []
        
        for repair_type in repair_types:
            task_id = str(uuid.uuid4())
            description, hours, materials = self._get_repair_details(repair_type, carpet)
            tasks.append(RepairTask(
                id=task_id,
                repair_type=repair_type,
                description=description,
                estimated_hours=hours,
                materials_needed=materials
            ))
        
        request = ServiceRequest(
            id=request_id,
            customer=customer,
            carpet=carpet,
            tasks=tasks,
            request_date=datetime.now()
        )
        
        self.service_requests[request_id] = request
        return request

    def _get_repair_details(self, repair_type: RepairType, carpet: CarpetDetails) -> tuple:
        if repair_type == RepairType.SEAMING:
            return (
                f"Seaming repair for {carpet.material} carpet",
                2.5,
                ["Seaming tape", "Seaming iron", "Carpet adhesive"]
            )
        elif repair_type == RepairType.RESTRETCHING:
            return (
                f"Restretching {carpet.size_sqft} sqft {carpet.material} carpet",
                3.0,
                ["Power stretcher", "Knee kicker", "Staple gun"]
            )
        elif repair_type == RepairType.WEAVING:
            return (
                f"Weaving repair for {carpet.color} {carpet.material} carpet",
                4.0,
                ["Carpet fibers", "Weaving tools", "Adhesive"]
            )
        elif repair_type == RepairType.PATCHING:
            return (
                f"Patching damaged area of {carpet.material} carpet",
                1.5,
                ["Carpet patch", "Adhesive", "Cutting tools"]
            )
        elif repair_type == RepairType.CLEANING:
            return (
                f"Deep cleaning for {carpet.material} carpet",
                2.0,
                ["Cleaning solution", "Extractor", "Brush"]
            )
        else:
            raise ValueError(f"Unknown repair type: {repair_type}")

    def assign_technician(self, request_id: str) -> str:
        if request_id not in self.service_requests:
            raise ValueError("Service request not found")
        
        technician = random.choice(self.technicians)
        self.service_requests[request_id].assigned_technician = technician
        return technician

    def start_repair_task(self, request_id: str, task_id: str) -> RepairTask:
        request = self._get_request(request_id)
        task = self._get_task(request, task_id)
        
        if task.status != RepairStatus.SCHEDULED:
            raise ValueError("Task can only be started from Scheduled status")
        
        task.status = RepairStatus.IN_PROGRESS
        task.start_time = datetime.now()
        return task

    def complete_repair_task(self, request_id: str, task_id: str, notes: str = None) -> RepairTask:
        request = self._get_request(request_id)
        task = self._get_task(request, task_id)
        
        if task.status != RepairStatus.IN_PROGRESS:
            raise ValueError("Task can only be completed from In Progress status")
        
        task.status = RepairStatus.COMPLETED
        task.end_time = datetime.now()
        task.notes = notes
        return task

    def cancel_service_request(self, request_id: str) -> ServiceRequest:
        request = self._get_request(request_id)
        
        for task in request.tasks:
            if task.status == RepairStatus.IN_PROGRESS:
                raise ValueError("Cannot cancel request with tasks in progress")
            task.status = RepairStatus.CANCELLED
        
        return request

    def _get_request(self, request_id: str) -> ServiceRequest:
        if request_id not in self.service_requests:
            raise ValueError("Service request not found")
        return self.service_requests[request_id]

    def _get_task(self, request: ServiceRequest, task_id: str) -> RepairTask:
        for task in request.tasks:
            if task.id == task_id:
                return task
        raise ValueError("Task not found in service request")

    def get_service_request_status(self, request_id: str) -> Dict:
        request = self._get_request(request_id)
        completed_tasks = sum(1 for t in request.tasks if t.status == RepairStatus.COMPLETED)
        
        return {
            "request_id": request_id,
            "customer_name": request.customer.name,
            "total_tasks": len(request.tasks),
            "completed_tasks": completed_tasks,
            "assigned_technician": request.assigned_technician,
            "overall_status": "Completed" if completed_tasks == len(request.tasks) else "In Progress"
        }

# Example usage
if __name__ == "__main__":
    service = CarpetRepairService()
    
    customer = Customer(
        id="cust-123",
        name="Jane Doe",
        address="123 Main St, Melbourne",
        phone="0400123456",
        email="jane@example.com"
    )
    
    carpet = CarpetDetails(
        material="Wool",
        color="Beige",
        age=5,
        size_sqft=200.0,
        pattern="Floral"
    )
    
    repair_types = [RepairType.RESTRETCHING, RepairType.CLEANING]
    request = service.create_service_request(customer, carpet, repair_types)
    
    print(f"Created service request: {request.id}")
    technician = service.assign_technician(request.id)
    print(f"Assigned technician: {technician}")
    
    for task in request.tasks:
        started_task = service.start_repair_task(request.id, task.id)
        print(f"Started task: {started_task.description}")
        
        completed_task = service.complete_repair_task(request.id, task.id, "Completed successfully")
        print(f"Completed task: {completed_task.description}")
    
    status = service.get_service_request_status(request.id)
    print(f"Final status: {status}")
```
