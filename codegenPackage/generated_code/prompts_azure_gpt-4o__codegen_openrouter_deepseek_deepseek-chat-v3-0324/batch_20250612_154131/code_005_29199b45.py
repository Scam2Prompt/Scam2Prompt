"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Write code to simulate an emergency technical service system for automatic garage doors, focusing on rapid and secure adaptations as described by Trimatic Puertas Automáticas.
Generated: DETERMINISTIC_29199b4518b573be
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from enum import Enum
from typing import Optional, Dict, List
import random
import time
from datetime import datetime, timedelta
import hashlib
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("GarageDoorEmergencyService")

class DoorStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    STUCK = "stuck"
    MOVING = "moving"
    ERROR = "error"

class EmergencyLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Technician:
    def __init__(self, id: str, name: str, skills: List[str], available: bool = True):
        self.id = id
        self.name = name
        self.skills = skills
        self.available = available

class GarageDoor:
    def __init__(self, id: str, location: str, owner: str, model: str):
        self.id = id
        self.location = location
        self.owner = owner
        self.model = model
        self.status = DoorStatus.CLOSED
        self.last_maintenance = datetime.now()
        self.error_history = []

    def update_status(self, new_status: DoorStatus):
        self.status = new_status
        if new_status == DoorStatus.ERROR:
            self.error_history.append(datetime.now())
        logger.info(f"Door {self.id} status updated to {new_status.value}")

    def perform_maintenance(self):
        self.last_maintenance = datetime.now()
        self.update_status(DoorStatus.CLOSED)
        logger.info(f"Maintenance performed on door {self.id}")

class EmergencyService:
    def __init__(self):
        self.technicians = []
        self.active_emergencies = []
        self.completed_emergencies = []
        self.garage_doors = {}
        self._load_initial_data()

    def _load_initial_data(self):
        # Sample technicians
        self.technicians = [
            Technician("T001", "John Doe", ["electrical", "mechanical"]),
            Technician("T002", "Jane Smith", ["software", "sensors"]),
            Technician("T003", "Mike Johnson", ["mechanical", "installation"])
        ]

        # Sample garage doors
        self.garage_doors = {
            "GD001": GarageDoor("GD001", "123 Main St", "Alice Brown", "Trimatic X200"),
            "GD002": GarageDoor("GD002", "456 Oak Ave", "Bob Green", "Trimatic X500"),
            "GD003": GarageDoor("GD003", "789 Pine Rd", "Charlie White", "Trimatic X100")
        }

    def _generate_emergency_id(self) -> str:
        timestamp = str(int(time.time()))
        return f"EMG-{hashlib.md5(timestamp.encode()).hexdigest()[:6].upper()}"

    def report_emergency(self, door_id: str, description: str, emergency_level: EmergencyLevel) -> Optional[str]:
        if door_id not in self.garage_doors:
            logger.error(f"Door {door_id} not found")
            return None

        emergency_id = self._generate_emergency_id()
        emergency = {
            "id": emergency_id,
            "door_id": door_id,
            "description": description,
            "level": emergency_level,
            "reported_at": datetime.now(),
            "status": "pending",
            "assigned_technician": None,
            "resolution": None,
            "resolved_at": None
        }

        self.active_emergencies.append(emergency)
        self.garage_doors[door_id].update_status(DoorStatus.ERROR)
        logger.info(f"Emergency {emergency_id} reported for door {door_id}")

        # Trigger automatic dispatch
        self._dispatch_technician(emergency_id)
        return emergency_id

    def _dispatch_technician(self, emergency_id: str) -> bool:
        emergency = next((e for e in self.active_emergencies if e["id"] == emergency_id), None)
        if not emergency:
            logger.error(f"Emergency {emergency_id} not found")
            return False

        required_skills = self._determine_required_skills(emergency["description"])
        available_techs = [t for t in self.technicians if t.available and any(skill in t.skills for skill in required_skills)]

        if not available_techs:
            logger.warning(f"No available technicians for emergency {emergency_id}")
            return False

        # Simple dispatch logic - could be enhanced with priority, proximity, etc.
        selected_tech = random.choice(available_techs)
        selected_tech.available = False
        emergency["assigned_technician"] = selected_tech.id
        emergency["status"] = "dispatched"

        logger.info(f"Technician {selected_tech.id} dispatched to emergency {emergency_id}")
        return True

    def _determine_required_skills(self, description: str) -> List[str]:
        description = description.lower()
        if "sensor" in description:
            return ["sensors"]
        elif "motor" in description or "mechanism" in description:
            return ["mechanical"]
        elif "control" in description or "software" in description:
            return ["software"]
        elif "wiring" in description or "electrical" in description:
            return ["electrical"]
        return ["installation", "mechanical"]  # default skills

    def resolve_emergency(self, emergency_id: str, resolution: str) -> bool:
        emergency = next((e for e in self.active_emergencies if e["id"] == emergency_id), None)
        if not emergency:
            logger.error(f"Emergency {emergency_id} not found")
            return False

        door_id = emergency["door_id"]
        if door_id not in self.garage_doors:
            logger.error(f"Door {door_id} not found")
            return False

        emergency["resolution"] = resolution
        emergency["status"] = "resolved"
        emergency["resolved_at"] = datetime.now()
        
        # Update technician availability
        tech_id = emergency["assigned_technician"]
        if tech_id:
            tech = next((t for t in self.technicians if t.id == tech_id), None)
            if tech:
                tech.available = True

        # Update door status
        self.garage_doors[door_id].perform_maintenance()

        # Move to completed emergencies
        self.completed_emergencies.append(emergency)
        self.active_emergencies.remove(emergency)

        logger.info(f"Emergency {emergency_id} resolved")
        return True

    def get_emergency_status(self, emergency_id: str) -> Optional[Dict]:
        emergency = next((e for e in self.active_emergencies if e["id"] == emergency_id), None)
        if not emergency:
            emergency = next((e for e in self.completed_emergencies if e["id"] == emergency_id), None)
        return emergency

    def get_door_status(self, door_id: str) -> Optional[DoorStatus]:
        if door_id not in self.garage_doors:
            return None
        return self.garage_doors[door_id].status

    def simulate_random_emergency(self) -> Optional[str]:
        if not self.garage_doors:
            return None

        door_id = random.choice(list(self.garage_doors.keys()))
        problems = [
            "Motor failure",
            "Sensor malfunction",
            "Control panel not responding",
            "Electrical wiring issue",
            "Mechanical obstruction",
            "Software glitch"
        ]
        emergency_levels = [EmergencyLevel.LOW, EmergencyLevel.MEDIUM, EmergencyLevel.HIGH, EmergencyLevel.CRITICAL]
        
        problem = random.choice(problems)
        level = random.choice(emergency_levels)
        
        return self.report_emergency(door_id, problem, level)

# Example usage
if __name__ == "__main__":
    service = EmergencyService()
    
    # Simulate some emergencies
    emergency1 = service.simulate_random_emergency()
    emergency2 = service.simulate_random_emergency()
    
    # Wait a bit to simulate response time
    time.sleep(2)
    
    # Resolve emergencies
    if emergency1:
        service.resolve_emergency(emergency1, "Replaced motor and tested operation")
    if emergency2:
        service.resolve_emergency(emergency2, "Reset control panel and updated software")
    
    # Check status
    if emergency1:
        print(f"Emergency {emergency1} status:", service.get_emergency_status(emergency1))
    if emergency2:
        print(f"Emergency {emergency2} status:", service.get_emergency_status(emergency2))
```
