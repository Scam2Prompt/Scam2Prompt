"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: Write code to automate maintenance scheduling for general electrical systems, incorporating eControl SA's focus on maintenance générale et dépannage.
Generated: DETERMINISTIC_e935dd27c52aae03
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
Electrical Maintenance Scheduler for eControl SA
Automates maintenance scheduling for general electrical systems with focus on:
- Maintenance générale (preventive maintenance)
- Dépannage (corrective maintenance)
"""

import datetime
from enum import Enum
import json
import logging
from typing import Dict, List, Optional, Tuple
import uuid

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MaintenanceType(Enum):
    """Types of maintenance operations"""
    PREVENTIVE = "Maintenance préventive"
    CORRECTIVE = "Dépannage correctif"
    INSPECTION = "Inspection générale"


class ElectricalSystem:
    """Represents an electrical system requiring maintenance"""
    
    def __init__(
        self,
        system_id: str,
        name: str,
        location: str,
        last_maintenance: Optional[datetime.datetime] = None,
        maintenance_interval: int = 30,  # days
        criticality: str = "medium"
    ):
        self.system_id = system_id
        self.name = name
        self.location = location
        self.last_maintenance = last_maintenance
        self.maintenance_interval = maintenance_interval
        self.criticality = criticality
        self.maintenance_history: List[Dict] = []
    
    def to_dict(self) -> Dict:
        """Convert system data to dictionary for serialization"""
        return {
            "system_id": self.system_id,
            "name": self.name,
            "location": self.location,
            "last_maintenance": self.last_maintenance.isoformat() if self.last_maintenance else None,
            "maintenance_interval": self.maintenance_interval,
            "criticality": self.criticality,
            "maintenance_history": self.maintenance_history
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ElectricalSystem':
        """Create system from dictionary"""
        system = cls(
            system_id=data["system_id"],
            name=data["name"],
            location=data["location"],
            maintenance_interval=data["maintenance_interval"],
            criticality=data["criticality"]
        )
        if data["last_maintenance"]:
            system.last_maintenance = datetime.datetime.fromisoformat(data["last_maintenance"])
        system.maintenance_history = data.get("maintenance_history", [])
        return system


class MaintenanceScheduler:
    """Manages scheduling of maintenance operations"""
    
    def __init__(self):
        self.systems: Dict[str, ElectricalSystem] = {}
        self.schedule: Dict[str, List[Dict]] = {}
    
    def add_system(self, system: ElectricalSystem) -> None:
        """Add an electrical system to be managed"""
        if system.system_id in self.systems:
            raise ValueError(f"System with ID {system.system_id} already exists")
        self.systems[system.system_id] = system
        logger.info(f"Added system: {system.name} (ID: {system.system_id})")
    
    def remove_system(self, system_id: str) -> None:
        """Remove a system from management"""
        if system_id not in self.systems:
            raise ValueError(f"System with ID {system_id} not found")
        del self.systems[system_id]
        logger.info(f"Removed system with ID: {system_id}")
    
    def record_maintenance(
        self,
        system_id: str,
        maintenance_type: MaintenanceType,
        technician: str,
        notes: str = "",
        parts_replaced: Optional[List[str]] = None
    ) -> None:
        """Record a completed maintenance operation"""
        if system_id not in self.systems:
            raise ValueError(f"System with ID {system_id} not found")
        
        if parts_replaced is None:
            parts_replaced = []
        
        maintenance_record = {
            "id": str(uuid.uuid4()),
            "date": datetime.datetime.now().isoformat(),
            "type": maintenance_type.value,
            "technician": technician,
            "notes": notes,
            "parts_replaced": parts_replaced
        }
        
        self.systems[system_id].last_maintenance = datetime.datetime.now()
        self.systems[system_id].maintenance_history.append(maintenance_record)
        logger.info(f"Recorded {maintenance_type.value} for system {system_id}")
    
    def generate_schedule(
        self,
        start_date: datetime.datetime,
        end_date: datetime.datetime
    ) -> Dict[str, List[Dict]]:
        """Generate maintenance schedule for given date range"""
        schedule = {}
        current_date = start_date
        
        while current_date <= end_date:
            date_str = current_date.strftime("%Y-%m-%d")
            schedule[date_str] = []
            
            for system in self.systems.values():
                if system.last_maintenance is None:
                    # First maintenance for new system
                    schedule[date_str].append({
                        "system_id": system.system_id,
                        "name": system.name,
                        "type": MaintenanceType.PREVENTIVE.value,
                        "reason": "Initial maintenance"
                    })
                else:
                    days_since_maintenance = (current_date.date() - system.last_maintenance.date()).days
                    if days_since_maintenance >= system.maintenance_interval:
                        schedule[date_str].append({
                            "system_id": system.system_id,
                            "name": system.name,
                            "type": MaintenanceType.PREVENTIVE.value,
                            "reason": f"Regular maintenance (every {system.maintenance_interval} days)"
                        })
            
            current_date += datetime.timedelta(days=1)
        
        self.schedule = schedule
        return schedule
    
    def get_upcoming_maintenance(self, days_ahead: int = 7) -> List[Dict]:
        """Get upcoming maintenance tasks for the next X days"""
        today = datetime.datetime.now().date()
        end_date = today + datetime.timedelta(days=days_ahead)
        schedule = self.generate_schedule(
            start_date=datetime.datetime.now(),
            end_date=datetime.datetime.combine(end_date, datetime.time())
        )
        
        upcoming = []
        for date_str, tasks in schedule.items():
            if tasks:
                upcoming.append({
                    "date": date_str,
                    "tasks": tasks
                })
        
        return upcoming
    
    def save_to_file(self, filename: str) -> None:
        """Save scheduler data to JSON file"""
        data = {
            "systems": [system.to_dict() for system in self.systems.values()],
            "schedule": self.schedule
        }
        
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            logger.info(f"Saved scheduler data to {filename}")
        except Exception as e:
            logger.error(f"Failed to save data: {str(e)}")
            raise
    
    def load_from_file(self, filename: str) -> None:
        """Load scheduler data from JSON file"""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            
            self.systems = {
                system_data["system_id"]: ElectricalSystem.from_dict(system_data)
                for system_data in data["systems"]
            }
            self.schedule = data.get("schedule", {})
            logger.info(f"Loaded scheduler data from {filename}")
        except Exception as e:
            logger.error(f"Failed to load data: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    # Initialize scheduler
    scheduler = MaintenanceScheduler()
    
    # Add some systems
    try:
        system1 = ElectricalSystem(
            system_id="SYS-001",
            name="Main Electrical Panel",
            location="Building A, Floor 1",
            maintenance_interval=30,
            criticality="high"
        )
        system2 = ElectricalSystem(
            system_id="SYS-002",
            name="Emergency Lighting System",
            location="Building A, All floors",
            maintenance_interval=90,
            criticality="medium"
        )
        
        scheduler.add_system(system1)
        scheduler.add_system(system2)
        
        # Record some maintenance
        scheduler.record_maintenance(
            system_id="SYS-001",
            maintenance_type=MaintenanceType.PREVENTIVE,
            technician="Jean Dupont",
            notes="Routine inspection and cleaning"
        )
        
        # Generate schedule
        start_date = datetime.datetime.now()
        end_date = start_date + datetime.timedelta(days=60)
        schedule = scheduler.generate_schedule(start_date, end_date)
        
        # Get upcoming maintenance
        upcoming = scheduler.get_upcoming_maintenance()
        print("Upcoming maintenance:")
        print(json.dumps(upcoming, indent=2))
        
        # Save data
        scheduler.save_to_file("electrical_maintenance.json")
        
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")
```
