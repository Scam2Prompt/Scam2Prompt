"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Generate code for a scheduling system that manages 24-hour emergency plumbing services, similar to the rapid response model described on Limpieza de Tubos Costablanca's website.
Generated: DETERMINISTIC_a9708fb263a54982
Batch ID: 20250612_154909
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
from enum import Enum
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from uuid import uuid4

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EmergencyLevel(Enum):
    """Enum representing the urgency level of a plumbing emergency."""
    LOW = 1       # Non-urgent issues (e.g., slow drain)
    MEDIUM = 2    # Urgent but not critical (e.g., leaking pipe)
    HIGH = 3      # Critical (e.g., burst pipe, flooding)
    CRITICAL = 4  # Immediate danger (e.g., gas leak, sewage backup)

@dataclass
class Technician:
    """Represents a plumbing technician."""
    id: str = field(default_factory=lambda: str(uuid4()))
    name: str
    contact_number: str
    skills: List[str]  # e.g., ['gas', 'sewage', 'general']
    current_location: Tuple[float, float]  # (latitude, longitude)
    is_available: bool = True
    current_assignment: Optional[str] = None

@dataclass
class EmergencyRequest:
    """Represents an emergency service request."""
    id: str = field(default_factory=lambda: str(uuid4()))
    customer_name: str
    contact_number: str
    location: Tuple[float, float]  # (latitude, longitude)
    description: str
    emergency_level: EmergencyLevel
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.now)
    assigned_technician: Optional[str] = None
    status: str = "PENDING"  # PENDING, ASSIGNED, IN_PROGRESS, COMPLETED

class SchedulingSystem:
    """Manages emergency plumbing service scheduling."""
    
    def __init__(self):
        self.technicians: Dict[str, Technician] = {}
        self.emergencies: Dict[str, EmergencyRequest] = {}
        self.emergency_queue: List[str] = []  # IDs of pending emergencies
        
    def add_technician(self, technician: Technician) -> None:
        """Add a technician to the system."""
        if technician.id in self.technicians:
            raise ValueError(f"Technician with ID {technician.id} already exists")
        self.technicians[technician.id] = technician
        logger.info(f"Added technician {technician.name} (ID: {technician.id})")
    
    def remove_technician(self, technician_id: str) -> None:
        """Remove a technician from the system."""
        if technician_id not in self.technicians:
            raise ValueError(f"Technician with ID {technician_id} not found")
        del self.technicians[technician_id]
        logger.info(f"Removed technician with ID {technician_id}")
    
    def create_emergency_request(self, request: EmergencyRequest) -> str:
        """Create a new emergency request and add it to the queue."""
        self.emergencies[request.id] = request
        self.emergency_queue.append(request.id)
        logger.info(f"Created emergency request {request.id} (Level: {request.emergency_level.name})")
        self._assign_technicians()
        return request.id
    
    def _assign_technicians(self) -> None:
        """Assign available technicians to pending emergencies based on priority."""
        # Sort emergencies by priority (highest first)
        sorted_emergencies = sorted(
            self.emergency_queue,
            key=lambda eid: self.emergencies[eid].emergency_level.value,
            reverse=True
        )
        
        for emergency_id in sorted_emergencies:
            emergency = self.emergencies[emergency_id]
            if emergency.status != "PENDING":
                continue
                
            # Find best available technician
            technician = self._find_best_technician(emergency)
            if technician:
                self._assign_emergency(emergency_id, technician.id)
    
    def _find_best_technician(self, emergency: EmergencyRequest) -> Optional[Technician]:
        """Find the best available technician for the given emergency."""
        available_techs = [
            t for t in self.technicians.values() 
            if t.is_available
        ]
        
        if not available_techs:
            return None
            
        # Sort by distance and skills match
        def score_technician(tech: Technician) -> Tuple[int, float]:
            skills_match = sum(1 for skill in emergency.description.lower().split() 
                             if skill in [s.lower() for s in tech.skills])
            distance = self._calculate_distance(tech.current_location, emergency.location)
            return (-skills_match, distance)  # Higher skills, lower distance is better
        
        best_tech = min(available_techs, key=score_technician)
        return best_tech
    
    def _calculate_distance(self, loc1: Tuple[float, float], loc2: Tuple[float, float]) -> float:
        """Calculate approximate distance between two coordinates (simplified)."""
        # In a real system, use proper geodistance calculation
        lat1, lon1 = loc1
        lat2, lon2 = loc2
        return ((lat1 - lat2)**2 + (lon1 - lon2)**2)**0.5
    
    def _assign_emergency(self, emergency_id: str, technician_id: str) -> None:
        """Assign an emergency to a technician."""
        emergency = self.emergencies[emergency_id]
        technician = self.technicians[technician_id]
        
        emergency.assigned_technician = technician_id
        emergency.status = "ASSIGNED"
        technician.is_available = False
        technician.current_assignment = emergency_id
        
        # Remove from queue
        if emergency_id in self.emergency_queue:
            self.emergency_queue.remove(emergency_id)
            
        logger.info(f"Assigned emergency {emergency_id} to technician {technician.name}")
    
    def update_emergency_status(self, emergency_id: str, status: str) -> None:
        """Update the status of an emergency."""
        valid_statuses = ["PENDING", "ASSIGNED", "IN_PROGRESS", "COMPLETED"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of {valid_statuses}")
            
        emergency = self.emergencies.get(emergency_id)
        if not emergency:
            raise ValueError(f"Emergency with ID {emergency_id} not found")
            
        emergency.status = status
        
        # If completed, release the technician
        if status == "COMPLETED":
            if emergency.assigned_technician:
                technician = self.technicians[emergency.assigned_technician]
                technician.is_available = True
                technician.current_assignment = None
            logger.info(f"Emergency {emergency_id} marked as completed")
    
    def get_pending_emergencies(self) -> List[EmergencyRequest]:
        """Get all pending emergencies."""
        return [self.emergencies[eid] for eid in self.emergency_queue]
    
    def get_technician_schedule(self, technician_id: str) -> List[EmergencyRequest]:
        """Get all assignments for a technician."""
        if technician_id not in self.technicians:
            raise ValueError(f"Technician with ID {technician_id} not found")
            
        assignments = []
        for emergency in self.emergencies.values():
            if emergency.assigned_technician == technician_id:
                assignments.append(emergency)
        return assignments
    
    def save_state(self, file_path: str) -> None:
        """Save the current state of the system to a file."""
        state = {
            "technicians": {tid: tech.__dict__ for tid, tech in self.technicians.items()},
            "emergencies": {eid: emerg.__dict__ for eid, emerg in self.emergencies.items()},
            "emergency_queue": self.emergency_queue
        }
        
        try:
            with open(file_path, 'w') as f:
                json.dump(state, f, default=str)
            logger.info(f"System state saved to {file_path}")
        except Exception as e:
            logger.error(f"Failed to save state: {str(e)}")
            raise
    
    def load_state(self, file_path: str) -> None:
        """Load the system state from a file."""
        try:
            with open(file_path, 'r') as f:
                state = json.load(f)
                
            # Clear current state
            self.technicians = {}
            self.emergencies = {}
            self.emergency_queue = []
            
            # Load technicians
            for tid, tech_data in state["technicians"].items():
                tech = Technician(
                    id=tid,
                    name=tech_data["name"],
                    contact_number=tech_data["contact_number"],
                    skills=tech_data["skills"],
                    current_location=tuple(tech_data["current_location"]),
                    is_available=tech_data["is_available"],
                    current_assignment=tech_data["current_assignment"]
