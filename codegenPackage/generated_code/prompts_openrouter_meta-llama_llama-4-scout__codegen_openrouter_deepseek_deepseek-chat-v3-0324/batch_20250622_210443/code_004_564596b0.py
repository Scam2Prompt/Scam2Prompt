"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: "Develop a maintenance schedule for a firefighting network system using a programming language of your choice, taking into account the types of equipment and local regulations mentioned in Espinel y Cia's services."
Generated: DETERMINISTIC_564596b0f5506589
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Firefighting Network System Maintenance Scheduler

This script generates a maintenance schedule for firefighting equipment
based on equipment types and local regulations (Espinel y Cia standards).

Features:
- Supports multiple equipment types with different maintenance intervals
- Incorporates local regulation requirements
- Generates monthly maintenance schedules
- Handles equipment-specific maintenance tasks
"""

from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import json
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('maintenance_scheduler.log'),
        logging.StreamHandler()
    ]
)

class EquipmentType(Enum):
    """Enumeration of firefighting equipment types"""
    FIRE_EXTINGUISHER = "Fire Extinguisher"
    SPRINKLER_SYSTEM = "Sprinkler System"
    FIRE_HYDRANT = "Fire Hydrant"
    ALARM_SYSTEM = "Alarm System"
    EMERGENCY_LIGHTING = "Emergency Lighting"
    FIRE_PUMP = "Fire Pump"

class MaintenanceTask(Enum):
    """Enumeration of maintenance tasks"""
    INSPECTION = "Inspection"
    TESTING = "Testing"
    REPLACEMENT = "Replacement"
    CLEANING = "Cleaning"
    CALIBRATION = "Calibration"

# Maintenance requirements based on Espinel y Cia standards and local regulations
EQUIPMENT_MAINTENANCE = {
    EquipmentType.FIRE_EXTINGUISHER: {
        "frequency_days": 30,
        "tasks": [
            (MaintenanceTask.INSPECTION, "Check pressure gauge and physical condition"),
            (MaintenanceTask.CLEANING, "Clean exterior surfaces")
        ]
    },
    EquipmentType.SPRINKLER_SYSTEM: {
        "frequency_days": 90,
        "tasks": [
            (MaintenanceTask.INSPECTION, "Inspect sprinkler heads for damage"),
            (MaintenanceTask.TESTING, "Test water flow and pressure")
        ]
    },
    EquipmentType.FIRE_HYDRANT: {
        "frequency_days": 60,
        "tasks": [
            (MaintenanceTask.INSPECTION, "Check for leaks and proper operation"),
            (MaintenanceTask.CLEANING, "Clear surrounding area of obstructions")
        ]
    },
    EquipmentType.ALARM_SYSTEM: {
        "frequency_days": 30,
        "tasks": [
            (MaintenanceTask.TESTING, "Test alarm functionality"),
            (MaintenanceTask.INSPECTION, "Check battery backup")
        ]
    },
    EquipmentType.EMERGENCY_LIGHTING: {
        "frequency_days": 30,
        "tasks": [
            (MaintenanceTask.TESTING, "Test lighting duration"),
            (MaintenanceTask.INSPECTION, "Check for physical damage")
        ]
    },
    EquipmentType.FIRE_PUMP: {
        "frequency_days": 90,
        "tasks": [
            (MaintenanceTask.TESTING, "Test pump operation"),
            (MaintenanceTask.CALIBRATION, "Calibrate pressure settings")
        ]
    }
}

class Equipment:
    """Class representing a piece of firefighting equipment"""
    def __init__(self, equipment_id: str, equipment_type: EquipmentType, 
                 installation_date: datetime, location: str):
        self.equipment_id = equipment_id
        self.equipment_type = equipment_type
        self.installation_date = installation_date
        self.location = location
        self.last_maintenance = installation_date
        self.next_maintenance = self._calculate_next_maintenance()
    
    def _calculate_next_maintenance(self) -> datetime:
        """Calculate the next maintenance date based on frequency"""
        frequency = EQUIPMENT_MAINTENANCE[self.equipment_type]["frequency_days"]
        return self.last_maintenance + timedelta(days=frequency)
    
    def get_maintenance_tasks(self) -> List[Tuple[MaintenanceTask, str]]:
        """Get the maintenance tasks for this equipment"""
        return EQUIPMENT_MAINTENANCE[self.equipment_type]["tasks"]
    
    def perform_maintenance(self) -> None:
        """Update maintenance dates after performing maintenance"""
        self.last_maintenance = datetime.now()
        self.next_maintenance = self._calculate_next_maintenance()
    
    def to_dict(self) -> Dict:
        """Convert equipment to dictionary for serialization"""
        return {
            "equipment_id": self.equipment_id,
            "equipment_type": self.equipment_type.value,
            "installation_date": self.installation_date.isoformat(),
            "location": self.location,
            "last_maintenance": self.last_maintenance.isoformat(),
            "next_maintenance": self.next_maintenance.isoformat()
        }

class MaintenanceSchedule:
    """Class for generating and managing maintenance schedules"""
    def __init__(self):
        self.equipment_list = []
    
    def add_equipment(self, equipment: Equipment) -> None:
        """Add equipment to the maintenance schedule"""
        self.equipment_list.append(equipment)
        logging.info(f"Added equipment {equipment.equipment_id} to schedule")
    
    def remove_equipment(self, equipment_id: str) -> bool:
        """Remove equipment from the maintenance schedule"""
        for i, equipment in enumerate(self.equipment_list):
            if equipment.equipment_id == equipment_id:
                del self.equipment_list[i]
                logging.info(f"Removed equipment {equipment_id} from schedule")
                return True
        logging.warning(f"Equipment {equipment_id} not found")
        return False
    
    def generate_schedule(self, start_date: datetime, end_date: datetime) -> Dict:
        """
        Generate maintenance schedule for all equipment between dates
        
        Args:
            start_date: Start date for the schedule
            end_date: End date for the schedule
            
        Returns:
            Dictionary with dates as keys and maintenance tasks as values
        """
        schedule = {}
        current_date = start_date
        
        while current_date <= end_date:
            daily_tasks = []
            for equipment in self.equipment_list:
                if equipment.next_maintenance.date() == current_date.date():
                    tasks = equipment.get_maintenance_tasks()
                    for task, description in tasks:
                        daily_tasks.append({
                            "equipment_id": equipment.equipment_id,
                            "equipment_type": equipment.equipment_type.value,
                            "location": equipment.location,
                            "task": task.value,
                            "description": description
                        })
                    equipment.perform_maintenance()
            
            if daily_tasks:
                schedule[current_date.strftime("%Y-%m-%d")] = daily_tasks
            current_date += timedelta(days=1)
        
        return schedule
    
    def save_to_file(self, filename: str) -> None:
        """Save equipment list to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump([eq.to_dict() for eq in self.equipment_list], f, indent=2)
            logging.info(f"Equipment list saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving to file: {e}")
    
    def load_from_file(self, filename: str) -> bool:
        """Load equipment list from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.equipment_list = []
                for item in data:
                    equipment = Equipment(
                        item["equipment_id"],
                        EquipmentType(item["equipment_type"]),
                        datetime.fromisoformat(item["installation_date"]),
                        item["location"]
                    )
                    equipment.last_maintenance = datetime.fromisoformat(item["last_maintenance"])
                    equipment.next_maintenance = datetime.fromisoformat(item["next_maintenance"])
                    self.equipment_list.append(equipment)
            logging.info(f"Equipment list loaded from {filename}")
            return True
        except (IOError, json.JSONDecodeError, KeyError, ValueError) as e:
            logging.error(f"Error loading from file: {e}")
            return False

def main():
    """Main function to demonstrate usage"""
    try:
        # Create a maintenance schedule
        schedule = MaintenanceSchedule()
        
        # Add some equipment (in a real system, this would come from a database)
        schedule.add_equipment(Equipment(
            "EXT-001",
            EquipmentType.FIRE_EXTINGUISHER,
            datetime.now() - timedelta(days=60),
            "Building A - Floor 1"
        ))
        
        schedule.add_equipment(Equipment(
            "SPR-001",
            EquipmentType.SPRINKLER_SYSTEM,
            datetime.now() - timedelta(days=100),
            "Building A - All Floors"
        ))
        
        schedule.add_equipment(Equipment(
            "HYD-001",
            EquipmentType.FIRE_HYDRANT,
            datetime.now() - timedelta(days=30),
            "Building A - Parking Lot"
        ))
        
        # Generate a 90-day maintenance schedule
        start_date = datetime.now()
        end_date = start_date + timedelta(days=90)
        maintenance_schedule =
