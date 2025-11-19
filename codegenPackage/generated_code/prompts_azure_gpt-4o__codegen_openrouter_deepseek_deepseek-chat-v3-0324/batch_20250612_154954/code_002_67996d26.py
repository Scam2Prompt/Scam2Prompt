"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: Generate code for monitoring and maintaining rice mill equipment, including fabricated valves, pulleys, and soaking tanks, based on the maintenance services offered by Mechano Solutions.
Generated: DETERMINISTIC_67996d26968ccd03
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class EquipmentType(Enum):
    """Enum representing different types of rice mill equipment."""
    FABRICATED_VALVE = "Fabricated Valve"
    PULLEY = "Pulley"
    SOAKING_TANK = "Soaking Tank"


class MaintenanceStatus(Enum):
    """Enum representing maintenance statuses."""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    OVERDUE = "Overdue"


class Equipment:
    """Class representing rice mill equipment."""
    
    def __init__(
        self,
        equipment_id: str,
        equipment_type: EquipmentType,
        installation_date: datetime,
        last_maintenance_date: Optional[datetime] = None,
        maintenance_interval_days: int = 30
    ):
        """
        Initialize equipment with basic information.
        
        Args:
            equipment_id: Unique identifier for the equipment
            equipment_type: Type of equipment (from EquipmentType enum)
            installation_date: Date when equipment was installed
            last_maintenance_date: Date of last maintenance (optional)
            maintenance_interval_days: Days between required maintenance (default 30)
        """
        self.equipment_id = equipment_id
        self.equipment_type = equipment_type
        self.installation_date = installation_date
        self.last_maintenance_date = last_maintenance_date
        self.maintenance_interval_days = maintenance_interval_days
        self.maintenance_history: List[Dict] = []
        
    def add_maintenance_record(
        self,
        maintenance_date: datetime,
        description: str,
        technician: str,
        status: MaintenanceStatus = MaintenanceStatus.COMPLETED
    ) -> None:
        """Add a maintenance record to the equipment's history."""
        record = {
            "date": maintenance_date,
            "description": description,
            "technician": technician,
            "status": status
        }
        self.maintenance_history.append(record)
        self.last_maintenance_date = maintenance_date
        logger.info(f"Added maintenance record for equipment {self.equipment_id}")
        
    def needs_maintenance(self) -> bool:
        """Check if equipment is due for maintenance."""
        if not self.last_maintenance_date:
            return True
            
        next_maintenance_date = self.last_maintenance_date + timedelta(
            days=self.maintenance_interval_days
        )
        return datetime.now() >= next_maintenance_date
        
    def get_maintenance_status(self) -> MaintenanceStatus:
        """Get current maintenance status of the equipment."""
        if not self.needs_maintenance():
            return MaintenanceStatus.COMPLETED
            
        if not self.last_maintenance_date:
            return MaintenanceStatus.OVERDUE
            
        overdue_days = (datetime.now() - (
            self.last_maintenance_date + timedelta(days=self.maintenance_interval_days)
        )).days
        
        if overdue_days > 7:
            return MaintenanceStatus.OVERDUE
        return MaintenanceStatus.PENDING
        
    def __str__(self) -> str:
        """String representation of the equipment."""
        return (
            f"Equipment(ID: {self.equipment_id}, Type: {self.equipment_type.value}, "
            f"Last Maintenance: {self.last_maintenance_date})"
        )


class RiceMillMonitoringSystem:
    """Class representing the rice mill equipment monitoring system."""
    
    def __init__(self):
        """Initialize the monitoring system with empty equipment list."""
        self.equipment_list: Dict[str, Equipment] = {}
        
    def add_equipment(self, equipment: Equipment) -> None:
        """Add equipment to the monitoring system."""
        if equipment.equipment_id in self.equipment_list:
            raise ValueError(f"Equipment with ID {equipment.equipment_id} already exists")
        self.equipment_list[equipment.equipment_id] = equipment
        logger.info(f"Added equipment {equipment.equipment_id} to monitoring system")
        
    def remove_equipment(self, equipment_id: str) -> None:
        """Remove equipment from the monitoring system."""
        if equipment_id not in self.equipment_list:
            raise ValueError(f"Equipment with ID {equipment_id} not found")
        del self.equipment_list[equipment_id]
        logger.info(f"Removed equipment {equipment_id} from monitoring system")
        
    def get_equipment(self, equipment_id: str) -> Equipment:
        """Get equipment by ID."""
        if equipment_id not in self.equipment_list:
            raise ValueError(f"Equipment with ID {equipment_id} not found")
        return self.equipment_list[equipment_id]
        
    def get_maintenance_schedule(self) -> Dict[MaintenanceStatus, List[Equipment]]:
        """Get all equipment categorized by maintenance status."""
        schedule = {
            status: [] for status in MaintenanceStatus
        }
        
        for equipment in self.equipment_list.values():
            status = equipment.get_maintenance_status()
            schedule[status].append(equipment)
            
        return schedule
        
    def generate_maintenance_report(self) -> str:
        """Generate a maintenance report for all equipment."""
        report = []
        schedule = self.get_maintenance_schedule()
        
        for status, equipment_list in schedule.items():
            report.append(f"\n{status.value} Maintenance ({len(equipment_list)}):")
            for equipment in equipment_list:
                report.append(f" - {equipment.equipment_id}: {equipment.equipment_type.value}")
                
        return "\n".join(report)
        
    def perform_maintenance(
        self,
        equipment_id: str,
        description: str,
        technician: str,
        maintenance_date: Optional[datetime] = None
    ) -> None:
        """Perform maintenance on specified equipment."""
        equipment = self.get_equipment(equipment_id)
        maintenance_date = maintenance_date or datetime.now()
        
        equipment.add_maintenance_record(
            maintenance_date=maintenance_date,
            description=description,
            technician=technician
        )
        logger.info(f"Performed maintenance on equipment {equipment_id}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize monitoring system
        monitoring_system = RiceMillMonitoringSystem()
        
        # Add some equipment
        valve1 = Equipment(
            equipment_id="VALVE-001",
            equipment_type=EquipmentType.FABRICATED_VALVE,
            installation_date=datetime(2023, 1, 1),
            maintenance_interval_days=45
        )
        monitoring_system.add_equipment(valve1)
        
        pulley1 = Equipment(
            equipment_id="PULLEY-001",
            equipment_type=EquipmentType.PULLEY,
            installation_date=datetime(2023, 2, 15),
            last_maintenance_date=datetime(2023, 5, 1),
            maintenance_interval_days=60
        )
        monitoring_system.add_equipment(pulley1)
        
        tank1 = Equipment(
            equipment_id="TANK-001",
            equipment_type=EquipmentType.SOAKING_TANK,
            installation_date=datetime(2022, 12, 1),
            last_maintenance_date=datetime(2023, 4, 1),
            maintenance_interval_days=90
        )
        monitoring_system.add_equipment(tank1)
        
        # Perform some maintenance
        monitoring_system.perform_maintenance(
            equipment_id="VALVE-001",
            description="Routine lubrication and inspection",
            technician="John Doe"
        )
        
        # Generate report
        print(monitoring_system.generate_maintenance_report())
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
```
