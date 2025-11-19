"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Generate a Python function to calculate maintenance schedules for a fleet of RIBs based on usage frequency and maritime safety standards, as described by OpenSea's services.
Generated: DETERMINISTIC_f71602ce3dab33ec
Batch ID: 20250612_150323
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

class MaintenanceType(Enum):
    """Enumeration of maintenance types."""
    ENGINE_SERVICE = "Engine Service"
    HULL_INSPECTION = "Hull Inspection"
    SAFETY_EQUIPMENT_CHECK = "Safety Equipment Check"
    FULL_SERVICE = "Full Service"

class RIB:
    """Class representing a Rigid Inflatable Boat (RIB)."""
    
    def __init__(self, id: str, last_maintenance_date: datetime.date, usage_hours: float):
        """
        Initialize a RIB instance.
        
        Args:
            id: Unique identifier for the RIB.
            last_maintenance_date: Date of the last maintenance.
            usage_hours: Total hours the RIB has been used since last maintenance.
        """
        self.id = id
        self.last_maintenance_date = last_maintenance_date
        self.usage_hours = usage_hours

class MaintenanceSchedule:
    """Class to calculate and manage maintenance schedules for a fleet of RIBs."""
    
    # Maintenance intervals in hours based on maritime safety standards
    MAINTENANCE_INTERVALS = {
        MaintenanceType.ENGINE_SERVICE: 100,
        MaintenanceType.HULL_INSPECTION: 200,
        MaintenanceType.SAFETY_EQUIPMENT_CHECK: 50,
        MaintenanceType.FULL_SERVICE: 500
    }
    
    # Minimum time intervals in days between maintenance types
    MIN_TIME_INTERVALS = {
        MaintenanceType.ENGINE_SERVICE: 30,
        MaintenanceType.HULL_INSPECTION: 90,
        MaintenanceType.SAFETY_EQUIPMENT_CHECK: 15,
        MaintenanceType.FULL_SERVICE: 180
    }
    
    def __init__(self, ribs: List[RIB]):
        """
        Initialize the MaintenanceSchedule with a list of RIBs.
        
        Args:
            ribs: List of RIB objects to manage.
        """
        self.ribs = ribs
    
    def calculate_next_maintenance(self, rib: RIB) -> Dict[MaintenanceType, datetime.date]:
        """
        Calculate the next maintenance dates for each maintenance type for a given RIB.
        
        Args:
            rib: The RIB to calculate maintenance for.
            
        Returns:
            Dictionary mapping maintenance types to their next due dates.
        """
        next_maintenance = {}
        today = datetime.date.today()
        
        for maint_type, interval_hours in self.MAINTENANCE_INTERVALS.items():
            # Calculate based on usage hours
            hours_remaining = interval_hours - rib.usage_hours
            estimated_days_from_usage = (hours_remaining / 24)  # Assuming 24h usage per day
            
            # Calculate based on time interval
            days_since_last = (today - rib.last_maintenance_date).days
            days_remaining = self.MIN_TIME_INTERVALS[maint_type] - days_since_last
            
            # Next maintenance is the earlier of the two criteria
            days_until_maintenance = min(estimated_days_from_usage, days_remaining)
            
            if days_until_maintenance <= 0:
                next_maintenance[maint_type] = today
            else:
                next_maintenance[maint_type] = today + datetime.timedelta(days=days_until_maintenance)
        
        return next_maintenance
    
    def get_priority_maintenance(self, rib: RIB) -> Optional[MaintenanceType]:
        """
        Get the highest priority maintenance type needed for a RIB.
        
        Args:
            rib: The RIB to check.
            
        Returns:
            The highest priority maintenance type needed, or None if no maintenance is due.
        """
        next_maintenance = self.calculate_next_maintenance(rib)
        today = datetime.date.today()
        
        # Check for overdue maintenance first
        for maint_type, due_date in next_maintenance.items():
            if due_date <= today:
                return maint_type
        
        # If nothing is overdue, return the soonest upcoming maintenance
        soonest_type = None
        soonest_date = None
        
        for maint_type, due_date in next_maintenance.items():
            if soonest_date is None or due_date < soonest_date:
                soonest_date = due_date
                soonest_type = maint_type
        
        return soonest_type
    
    def generate_fleet_schedule(self) -> Dict[str, Dict[MaintenanceType, datetime.date]]:
        """
        Generate maintenance schedules for all RIBs in the fleet.
        
        Returns:
            Dictionary mapping RIB IDs to their maintenance schedules.
        """
        fleet_schedule = {}
        for rib in self.ribs:
            fleet_schedule[rib.id] = self.calculate_next_maintenance(rib)
        return fleet_schedule

# Example usage
if __name__ == "__main__":
    # Create some RIBs
    rib1 = RIB(
        id="RIB001",
        last_maintenance_date=datetime.date(2023, 1, 15),
        usage_hours=80
    )
    
    rib2 = RIB(
        id="RIB002",
        last_maintenance_date=datetime.date(2023, 2, 20),
        usage_hours=120
    )
    
    # Create maintenance schedule
    schedule = MaintenanceSchedule([rib1, rib2])
    
    # Get fleet schedule
    fleet_schedule = schedule.generate_fleet_schedule()
    print("Fleet Maintenance Schedule:")
    for rib_id, maintenance in fleet_schedule.items():
        print(f"\nRIB {rib_id}:")
        for maint_type, due_date in maintenance.items():
            print(f"  {maint_type.value}: {due_date}")
    
    # Get priority maintenance for a specific RIB
    priority = schedule.get_priority_maintenance(rib1)
    if priority:
        print(f"\nPriority maintenance for RIB001: {priority.value}")
    else:
        print("\nNo priority maintenance needed for RIB001")
```
