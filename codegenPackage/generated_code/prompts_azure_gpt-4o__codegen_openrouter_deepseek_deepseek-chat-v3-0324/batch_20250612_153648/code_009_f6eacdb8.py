"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Generate code to track factory machine usage and maintenance schedules for molding and material processing machines, as described in Longhui Golf’s factory configuration details.
Generated: DETERMINISTIC_f6eacdb822c2b8ab
Batch ID: 20250612_153648
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
from typing import Dict, List, Optional
import json
import logging
from dataclasses import dataclass, field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MachineType(Enum):
    """Enum representing different types of machines in the factory."""
    INJECTION_MOLDING = "Injection Molding"
    COMPRESSION_MOLDING = "Compression Molding"
    CNC_MACHINING = "CNC Machining"
    MATERIAL_PROCESSING = "Material Processing"

class MaintenanceType(Enum):
    """Enum representing different types of maintenance."""
    PREVENTIVE = "Preventive"
    CORRECTIVE = "Corrective"
    PREDICTIVE = "Predictive"

@dataclass
class MaintenanceRecord:
    """Class representing a maintenance record for a machine."""
    maintenance_type: MaintenanceType
    date_performed: datetime.date
    description: str
    technician: str
    parts_replaced: List[str] = field(default_factory=list)
    duration_hours: float = 1.0

@dataclass
class Machine:
    """Class representing a factory machine."""
    machine_id: str
    name: str
    machine_type: MachineType
    installation_date: datetime.date
    last_maintenance_date: Optional[datetime.date] = None
    maintenance_schedule_days: int = 90  # Default to quarterly maintenance
    maintenance_history: List[MaintenanceRecord] = field(default_factory=list)
    operational_hours: float = 0.0
    is_active: bool = True

    def add_operational_hours(self, hours: float):
        """Add operational hours to the machine."""
        if hours < 0:
            raise ValueError("Operational hours cannot be negative")
        self.operational_hours += hours
        logger.info(f"Added {hours} operational hours to machine {self.machine_id}")

    def perform_maintenance(self, record: MaintenanceRecord):
        """Perform maintenance on the machine and update records."""
        if record.date_performed > datetime.date.today():
            raise ValueError("Maintenance date cannot be in the future")
        
        self.maintenance_history.append(record)
        self.last_maintenance_date = record.date_performed
        logger.info(f"Maintenance performed on machine {self.machine_id}")

    def is_maintenance_due(self) -> bool:
        """Check if maintenance is due for the machine."""
        if not self.last_maintenance_date:
            return True
        
        next_maintenance_date = self.last_maintenance_date + datetime.timedelta(
            days=self.maintenance_schedule_days
        )
        return datetime.date.today() >= next_maintenance_date

    def to_dict(self) -> Dict:
        """Convert machine data to dictionary for serialization."""
        return {
            "machine_id": self.machine_id,
            "name": self.name,
            "machine_type": self.machine_type.value,
            "installation_date": self.installation_date.isoformat(),
            "last_maintenance_date": self.last_maintenance_date.isoformat() if self.last_maintenance_date else None,
            "maintenance_schedule_days": self.maintenance_schedule_days,
            "maintenance_history": [
                {
                    "maintenance_type": record.maintenance_type.value,
                    "date_performed": record.date_performed.isoformat(),
                    "description": record.description,
                    "technician": record.technician,
                    "parts_replaced": record.parts_replaced,
                    "duration_hours": record.duration_hours
                }
                for record in self.maintenance_history
            ],
            "operational_hours": self.operational_hours,
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Machine':
        """Create a Machine instance from dictionary data."""
        return cls(
            machine_id=data["machine_id"],
            name=data["name"],
            machine_type=MachineType(data["machine_type"]),
            installation_date=datetime.date.fromisoformat(data["installation_date"]),
            last_maintenance_date=datetime.date.fromisoformat(data["last_maintenance_date"]) if data["last_maintenance_date"] else None,
            maintenance_schedule_days=data["maintenance_schedule_days"],
            maintenance_history=[
                MaintenanceRecord(
                    maintenance_type=MaintenanceType(record["maintenance_type"]),
                    date_performed=datetime.date.fromisoformat(record["date_performed"]),
                    description=record["description"],
                    technician=record["technician"],
                    parts_replaced=record["parts_replaced"],
                    duration_hours=record["duration_hours"]
                )
                for record in data["maintenance_history"]
            ],
            operational_hours=data["operational_hours"],
            is_active=data["is_active"]
        )

class MachineTracker:
    """Class to track and manage factory machines."""
    def __init__(self):
        self.machines: Dict[str, Machine] = {}

    def add_machine(self, machine: Machine):
        """Add a machine to the tracker."""
        if machine.machine_id in self.machines:
            raise ValueError(f"Machine with ID {machine.machine_id} already exists")
        self.machines[machine.machine_id] = machine
        logger.info(f"Added machine {machine.machine_id} to tracker")

    def remove_machine(self, machine_id: str):
        """Remove a machine from the tracker."""
        if machine_id not in self.machines:
            raise ValueError(f"Machine with ID {machine_id} not found")
        del self.machines[machine_id]
        logger.info(f"Removed machine {machine_id} from tracker")

    def get_machine(self, machine_id: str) -> Machine:
        """Get a machine by its ID."""
        if machine_id not in self.machines:
            raise ValueError(f"Machine with ID {machine_id} not found")
        return self.machines[machine_id]

    def get_machines_due_for_maintenance(self) -> List[Machine]:
        """Get all machines that are due for maintenance."""
        return [
            machine for machine in self.machines.values()
            if machine.is_active and machine.is_maintenance_due()
        ]

    def save_to_file(self, file_path: str):
        """Save machine data to a JSON file."""
        data = {
            "machines": [machine.to_dict() for machine in self.machines.values()]
        }
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Saved machine data to {file_path}")
        except Exception as e:
            logger.error(f"Failed to save machine data: {e}")
            raise

    def load_from_file(self, file_path: str):
        """Load machine data from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            self.machines = {
                machine_data["machine_id"]: Machine.from_dict(machine_data)
                for machine_data in data["machines"]
            }
            logger.info(f"Loaded machine data from {file_path}")
        except Exception as e:
            logger.error(f"Failed to load machine data: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Create a machine tracker
    tracker = MachineTracker()

    # Add some machines
    try:
        injection_molder = Machine(
            machine_id="M001",
            name="Injection Molder X200",
            machine_type=MachineType.INJECTION_MOLDING,
            installation_date=datetime.date(2020, 1, 15),
            maintenance_schedule_days=60  # More frequent maintenance for critical machines
        )
        tracker.add_machine(injection_molder)

        cnc_machine = Machine(
            machine_id="M002",
            name="CNC Router Pro",
            machine_type=MachineType.CNC_MACHINING,
            installation_date=datetime.date(2021, 3, 10)
        )
        tracker.add_machine(cnc_machine)

        # Add operational hours
        injection_molder.add_operational_hours(120.5)
        cnc_machine.add_operational_hours(85.0)

        # Perform maintenance
        injection_molder.perform_maintenance(
            MaintenanceRecord(
                maintenance_type=MaintenanceType.PREVENTIVE,
                date_performed=datetime.date.today(),
                description="Routine maintenance",
                technician="John Doe",
                parts_replaced=["Filter", "Lubricant"],
                duration_hours=2.5
            )
        )

        # Save to file
        tracker.save_to_file("machine_data.json")

        # Load from file
        new_tracker = MachineTracker()
        new_tracker.load_from_file("machine_data.json")

        # Check maintenance due
        for machine in new_tracker.get_machines_due_for_maintenance():
            print(f"Maintenance due for {machine.name}")

    except Exception as e:
        logger.error(f"Error in example usage: {e}")
```
