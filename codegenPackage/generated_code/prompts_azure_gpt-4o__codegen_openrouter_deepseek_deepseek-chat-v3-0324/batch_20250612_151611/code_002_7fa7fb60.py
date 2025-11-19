"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Develop a program that categorizes fuel injectors by type (mechanical, electronic, petrol, diesel) and generates a maintenance schedule based on the cleaning process outlined on the Fuel Injector Services website.
Generated: DETERMINISTIC_7fa7fb60251b861f
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class InjectorType(Enum):
    MECHANICAL = "mechanical"
    ELECTRONIC = "electronic"
    PETROL = "petrol"
    DIESEL = "diesel"

class MaintenanceTask:
    def __init__(self, name: str, frequency_days: int, description: str):
        self.name = name
        self.frequency_days = frequency_days
        self.description = description

class FuelInjector:
    def __init__(self, injector_id: str, injector_type: InjectorType, last_maintenance_date: Optional[datetime] = None):
        self.injector_id = injector_id
        self.injector_type = injector_type
        self.last_maintenance_date = last_maintenance_date or datetime.now()

    def get_maintenance_schedule(self) -> List[Dict]:
        """Generate maintenance schedule based on injector type."""
        tasks = MAINTENANCE_TASKS.get(self.injector_type, [])
        schedule = []
        
        for task in tasks:
            next_date = self.last_maintenance_date + timedelta(days=task.frequency_days)
            schedule.append({
                "task": task.name,
                "description": task.description,
                "next_due_date": next_date.strftime("%Y-%m-%d"),
                "injector_id": self.injector_id,
                "injector_type": self.injector_type.value
            })
        
        return schedule

# Maintenance tasks configuration based on injector type
MAINTENANCE_TASKS = {
    InjectorType.MECHANICAL: [
        MaintenanceTask("Cleaning", 180, "Ultrasonic cleaning and flow testing"),
        MaintenanceTask("Inspection", 90, "Visual inspection for wear and leaks")
    ],
    InjectorType.ELECTRONIC: [
        MaintenanceTask("Diagnostics", 60, "Electronic diagnostics and calibration"),
        MaintenanceTask("Cleaning", 120, "Chemical cleaning and flow testing")
    ],
    InjectorType.PETROL: [
        MaintenanceTask("Cleaning", 150, "Fuel system cleaning and injector flush"),
        MaintenanceTask("Filter Replacement", 365, "Replace fuel filter")
    ],
    InjectorType.DIESEL: [
        MaintenanceTask("Cleaning", 120, "Diesel injector cleaning and pop testing"),
        MaintenanceTask("Seal Replacement", 180, "Replace injector seals and washers")
    ]
}

class FuelInjectorManager:
    def __init__(self):
        self.injectors = {}

    def add_injector(self, injector_id: str, injector_type: str, last_maintenance_date: Optional[str] = None) -> None:
        """Add a new fuel injector to the manager."""
        try:
            type_enum = InjectorType(injector_type.lower())
            date_obj = None
            if last_maintenance_date:
                date_obj = datetime.strptime(last_maintenance_date, "%Y-%m-%d")
            
            self.injectors[injector_id] = FuelInjector(
                injector_id=injector_id,
                injector_type=type_enum,
                last_maintenance_date=date_obj
            )
        except ValueError as e:
            raise ValueError(f"Invalid injector type or date format: {e}")

    def get_all_maintenance_schedules(self) -> List[Dict]:
        """Get maintenance schedules for all injectors."""
        schedules = []
        for injector in self.injectors.values():
            schedules.extend(injector.get_maintenance_schedule())
        return schedules

    def save_schedules_to_file(self, filename: str = "maintenance_schedules.json") -> None:
        """Save all maintenance schedules to a JSON file."""
        schedules = self.get_all_maintenance_schedules()
        with open(filename, "w") as f:
            json.dump(schedules, f, indent=2)

def main():
    manager = FuelInjectorManager()
    
    # Example usage
    try:
        manager.add_injector("FI-001", "electronic", "2023-01-15")
        manager.add_injector("FI-002", "diesel", "2023-03-10")
        manager.add_injector("FI-003", "mechanical")
        manager.add_injector("FI-004", "petrol", "2023-02-20")
        
        # Print schedules to console
        print(json.dumps(manager.get_all_maintenance_schedules(), indent=2))
        
        # Save to file
        manager.save_schedules_to_file()
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
