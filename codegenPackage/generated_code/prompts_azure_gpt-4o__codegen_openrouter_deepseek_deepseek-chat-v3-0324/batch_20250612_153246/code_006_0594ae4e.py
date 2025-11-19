"""
Generated Code Metadata:
========================
Original URL: https://iconelevator.in
Prompt: Develop a software solution for managing elevator repairs, focusing on qualitative service delivery as outlined by ICON Elevator.
Generated: DETERMINISTIC_0594ae4e8356a868
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Elevator Repair Management System for ICON Elevator

This system manages elevator repair requests, tracks service quality, and ensures timely resolution.
"""

from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Optional
import uuid
import json
import logging
from dataclasses import dataclass, field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RepairStatus(Enum):
    """Enum representing possible repair statuses"""
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    CANCELLED = auto()

class PriorityLevel(Enum):
    """Enum representing repair priority levels"""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

class ServiceQualityRating(Enum):
    """Enum representing service quality ratings"""
    POOR = 1
    FAIR = 2
    GOOD = 3
    EXCELLENT = 4
    OUTSTANDING = 5

@dataclass
class Technician:
    """Represents a repair technician"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    certification: str
    specialization: str
    contact_number: str

@dataclass
class Elevator:
    """Represents an elevator unit"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    building_name: str
    location: str
    model: str
    serial_number: str
    installation_date: datetime
    last_maintenance_date: Optional[datetime] = None

@dataclass
class RepairRequest:
    """Represents a repair request"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    elevator_id: str
    description: str
    reported_by: str
    reported_at: datetime = field(default_factory=datetime.now)
    status: RepairStatus = RepairStatus.PENDING
    priority: PriorityLevel = PriorityLevel.MEDIUM
    assigned_technician: Optional[str] = None
    estimated_completion: Optional[datetime] = None
    actual_completion: Optional[datetime] = None
    service_quality_rating: Optional[ServiceQualityRating] = None
    notes: List[str] = field(default_factory=list)

    def add_note(self, note: str) -> None:
        """Add a note to the repair request"""
        self.notes.append(f"{datetime.now()}: {note}")

class RepairManagementSystem:
    """Main system for managing elevator repairs"""
    
    def __init__(self):
        self.repair_requests: Dict[str, RepairRequest] = {}
        self.elevators: Dict[str, Elevator] = {}
        self.technicians: Dict[str, Technician] = {}
        
    def add_elevator(self, elevator: Elevator) -> None:
        """Add an elevator to the system"""
        if elevator.id in self.elevators:
            raise ValueError("Elevator with this ID already exists")
        self.elevators[elevator.id] = elevator
        logger.info(f"Added elevator {elevator.id} to system")
        
    def add_technician(self, technician: Technician) -> None:
        """Add a technician to the system"""
        if technician.id in self.technicians:
            raise ValueError("Technician with this ID already exists")
        self.technicians[technician.id] = technician
        logger.info(f"Added technician {technician.id} to system")
        
    def create_repair_request(self, elevator_id: str, description: str, reported_by: str) -> RepairRequest:
        """Create a new repair request"""
        if elevator_id not in self.elevators:
            raise ValueError("Elevator not found in system")
            
        request = RepairRequest(
            elevator_id=elevator_id,
            description=description,
            reported_by=reported_by
        )
        
        self.repair_requests[request.id] = request
        logger.info(f"Created repair request {request.id}")
        return request
        
    def assign_technician(self, request_id: str, technician_id: str) -> None:
        """Assign a technician to a repair request"""
        if request_id not in self.repair_requests:
            raise ValueError("Repair request not found")
        if technician_id not in self.technicians:
            raise ValueError("Technician not found")
            
        request = self.repair_requests[request_id]
        request.assigned_technician = technician_id
        request.status = RepairStatus.IN_PROGRESS
        request.add_note(f"Assigned technician {technician_id}")
        logger.info(f"Assigned technician {technician_id} to request {request_id}")
        
    def update_repair_status(self, request_id: str, status: RepairStatus) -> None:
        """Update the status of a repair request"""
        if request_id not in self.repair_requests:
            raise ValueError("Repair request not found")
            
        request = self.repair_requests[request_id]
        request.status = status
        
        if status == RepairStatus.COMPLETED:
            request.actual_completion = datetime.now()
            
        request.add_note(f"Status changed to {status.name}")
        logger.info(f"Updated status of request {request_id} to {status.name}")
        
    def set_service_quality_rating(self, request_id: str, rating: ServiceQualityRating) -> None:
        """Set the service quality rating for a completed repair"""
        if request_id not in self.repair_requests:
            raise ValueError("Repair request not found")
            
        request = self.repair_requests[request_id]
        if request.status != RepairStatus.COMPLETED:
            raise ValueError("Cannot rate an incomplete repair")
            
        request.service_quality_rating = rating
        request.add_note(f"Service quality rated as {rating.name}")
        logger.info(f"Set service quality rating for request {request_id} to {rating.name}")
        
    def get_repair_requests_by_status(self, status: RepairStatus) -> List[RepairRequest]:
        """Get all repair requests with a specific status"""
        return [req for req in self.repair_requests.values() if req.status == status]
        
    def get_technician_performance(self, technician_id: str) -> Dict:
        """Get performance metrics for a technician"""
        if technician_id not in self.technicians:
            raise ValueError("Technician not found")
            
        completed = [req for req in self.repair_requests.values() 
                    if req.assigned_technician == technician_id 
                    and req.status == RepairStatus.COMPLETED]
        
        avg_rating = None
        if completed:
            ratings = [req.service_quality_rating.value for req in completed if req.service_quality_rating]
            if ratings:
                avg_rating = sum(ratings) / len(ratings)
                
        return {
            "total_completed": len(completed),
            "average_rating": avg_rating,
            "pending_assignments": len([req for req in self.repair_requests.values() 
                                      if req.assigned_technician == technician_id 
                                      and req.status != RepairStatus.COMPLETED])
        }
        
    def save_to_file(self, filename: str) -> None:
        """Save system data to a JSON file"""
        data = {
            "elevators": [vars(e) for e in self.elevators.values()],
            "technicians": [vars(t) for t in self.technicians.values()],
            "repair_requests": [vars(r) for r in self.repair_requests.values()]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, default=str, indent=2)
        logger.info(f"Saved system data to {filename}")
        
    def load_from_file(self, filename: str) -> None:
        """Load system data from a JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
            
        self.elevators = {
            e["id"]: Elevator(**e) for e in data.get("elevators", [])
        }
        
        self.technicians = {
            t["id"]: Technician(**t) for t in data.get("technicians", [])
        }
        
        self.repair_requests = {
            r["id"]: RepairRequest(**r) for r in data.get("repair_requests", [])
        }
        logger.info(f"Loaded system data from {filename}")

# Example usage
if __name__ == "__main__":
    system = RepairManagementSystem()
    
    # Add sample data
    elevator = Elevator(
        building_name="ICON Tower",
        location="Main Lobby",
        model="EL-5000",
        serial_number="EL-2023-001",
        installation_date=datetime(2023, 1, 15)
    )
    system.add_elevator(elevator)
    
    technician = Technician(
        name="John Smith",
        certification="Elevator Repair Master",
        specialization="Hyd
