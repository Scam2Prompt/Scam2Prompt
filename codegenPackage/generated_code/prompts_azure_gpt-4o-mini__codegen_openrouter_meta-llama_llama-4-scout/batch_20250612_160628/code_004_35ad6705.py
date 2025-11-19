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
# maintenance_scheduling_system.py

from datetime import datetime, timedelta
from enum import Enum

class LiftStatus(Enum):
    """Enum for lift status"""
    OPERATIONAL = 1
    UNDER_MAINTENANCE = 2
    OUT_OF_ORDER = 3

class HydraulicLift:
    """Class representing a hydraulic lift"""
    def __init__(self, lift_id, installation_date):
        self.lift_id = lift_id
        self.installation_date = installation_date
        self.status = LiftStatus.OPERATIONAL
        self.maintenance_schedule = []

    def schedule_maintenance(self, maintenance_date):
        """Schedule maintenance for the lift"""
        self.maintenance_schedule.append(maintenance_date)
        self.maintenance_schedule.sort()

    def perform_maintenance(self):
        """Perform maintenance on the lift"""
        if self.status == LiftStatus.UNDER_MAINTENANCE:
            raise Exception("Lift is already under maintenance")
        self.status = LiftStatus.UNDER_MAINTENANCE

    def complete_maintenance(self):
        """Complete maintenance on the lift"""
        if self.status != LiftStatus.UNDER_MAINTENANCE:
            raise Exception("Lift is not under maintenance")
        self.status = LiftStatus.OPERATIONAL

    def check_compliance(self):
        """Check if the lift is compliant with safety standards"""
        # Assuming safety standards require maintenance every 6 months
        last_maintenance_date = self.maintenance_schedule[-1] if self.maintenance_schedule else self.installation_date
        time_since_last_maintenance = (datetime.now() - last_maintenance_date).days
        if time_since_last_maintenance > 183:  # 6 months in days
            return False
        return True

class MaintenanceSchedulingSystem:
    """Class representing the maintenance scheduling system"""
    def __init__(self):
        self.lifts = {}

    def add_lift(self, lift_id, installation_date):
        """Add a lift to the system"""
        self.lifts[lift_id] = HydraulicLift(lift_id, installation_date)

    def schedule_maintenance(self, lift_id, maintenance_date):
        """Schedule maintenance for a lift"""
        if lift_id not in self.lifts:
            raise Exception("Lift not found")
        self.lifts[lift_id].schedule_maintenance(maintenance_date)

    def perform_maintenance(self, lift_id):
        """Perform maintenance on a lift"""
        if lift_id not in self.lifts:
            raise Exception("Lift not found")
        self.lifts[lift_id].perform_maintenance()

    def complete_maintenance(self, lift_id):
        """Complete maintenance on a lift"""
        if lift_id not in self.lifts:
            raise Exception("Lift not found")
        self.lifts[lift_id].complete_maintenance()

    def check_compliance(self, lift_id):
        """Check if a lift is compliant with safety standards"""
        if lift_id not in self.lifts:
            raise Exception("Lift not found")
        return self.lifts[lift_id].check_compliance()

def main():
    system = MaintenanceSchedulingSystem()
    system.add_lift("LIFT-1", datetime(2022, 1, 1))

    # Schedule maintenance
    maintenance_date = datetime.now() + timedelta(days=30)
    system.schedule_maintenance("LIFT-1", maintenance_date)

    # Perform maintenance
    system.perform_maintenance("LIFT-1")

    # Complete maintenance
    system.complete_maintenance("LIFT-1")

    # Check compliance
    compliant = system.check_compliance("LIFT-1")
    print(f"Lift LIFT-1 is compliant: {compliant}")

if __name__ == "__main__":
    main()
```
