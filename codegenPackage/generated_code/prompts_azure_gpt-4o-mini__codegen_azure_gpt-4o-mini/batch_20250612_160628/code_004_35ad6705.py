"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Provide an example of a maintenance scheduling system for hydraulic lifts that ensures compliance with safety standards.
Generated: DETERMINISTIC_35ad6705978d4e92
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class MaintenanceRecord:
    """Class to represent a maintenance record for a hydraulic lift."""
    
    def __init__(self, lift_id: str, maintenance_date: datetime.date, description: str):
        self.lift_id = lift_id
        self.maintenance_date = maintenance_date
        self.description = description

    def __repr__(self):
        return f"MaintenanceRecord(lift_id={self.lift_id}, maintenance_date={self.maintenance_date}, description={self.description})"


class HydraulicLift:
    """Class to represent a hydraulic lift with maintenance scheduling."""
    
    def __init__(self, lift_id: str, last_maintenance: Optional[datetime.date] = None):
        self.lift_id = lift_id
        self.last_maintenance = last_maintenance
        self.maintenance_records: List[MaintenanceRecord] = []

    def schedule_maintenance(self, maintenance_date: datetime.date, description: str):
        """Schedule maintenance for the lift and record it."""
        if maintenance_date <= datetime.date.today():
            raise ValueError("Maintenance date must be in the future.")
        
        self.last_maintenance = maintenance_date
        record = MaintenanceRecord(self.lift_id, maintenance_date, description)
        self.maintenance_records.append(record)

    def get_maintenance_records(self) -> List[MaintenanceRecord]:
        """Return all maintenance records for the lift."""
        return self.maintenance_records

    def is_due_for_maintenance(self, interval_days: int) -> bool:
        """Check if the lift is due for maintenance based on the given interval."""
        if self.last_maintenance is None:
            return True  # If no maintenance has been done, it's due.
        return (datetime.date.today() - self.last_maintenance).days >= interval_days


class MaintenanceScheduler:
    """Class to manage multiple hydraulic lifts and their maintenance schedules."""
    
    def __init__(self):
        self.lifts: Dict[str, HydraulicLift] = {}

    def add_lift(self, lift_id: str):
        """Add a new hydraulic lift to the scheduler."""
        if lift_id in self.lifts:
            raise ValueError(f"Lift with ID {lift_id} already exists.")
        self.lifts[lift_id] = HydraulicLift(lift_id)

    def schedule_maintenance(self, lift_id: str, maintenance_date: datetime.date, description: str):
        """Schedule maintenance for a specific lift."""
        if lift_id not in self.lifts:
            raise ValueError(f"Lift with ID {lift_id} not found.")
        self.lifts[lift_id].schedule_maintenance(maintenance_date, description)

    def check_due_maintenance(self, interval_days: int) -> List[str]:
        """Check which lifts are due for maintenance."""
        due_lifts = []
        for lift in self.lifts.values():
            if lift.is_due_for_maintenance(interval_days):
                due_lifts.append(lift.lift_id)
        return due_lifts

    def get_lift_records(self, lift_id: str) -> List[MaintenanceRecord]:
        """Get maintenance records for a specific lift."""
        if lift_id not in self.lifts:
            raise ValueError(f"Lift with ID {lift_id} not found.")
        return self.lifts[lift_id].get_maintenance_records()


# Example usage
if __name__ == "__main__":
    scheduler = MaintenanceScheduler()
    
    # Adding lifts
    scheduler.add_lift("Lift001")
    scheduler.add_lift("Lift002")

    # Scheduling maintenance
    try:
        scheduler.schedule_maintenance("Lift001", datetime.date(2023, 12, 1), "Annual safety check")
        scheduler.schedule_maintenance("Lift002", datetime.date(2024, 1, 15), "Hydraulic fluid replacement")
    except ValueError as e:
        print(f"Error: {e}")

    # Checking due maintenance
    due_lifts = scheduler.check_due_maintenance(interval_days=30)
    print(f"Lifts due for maintenance: {due_lifts}")

    # Retrieving maintenance records
    records = scheduler.get_lift_records("Lift001")
    print(f"Maintenance records for Lift001: {records}")
```
