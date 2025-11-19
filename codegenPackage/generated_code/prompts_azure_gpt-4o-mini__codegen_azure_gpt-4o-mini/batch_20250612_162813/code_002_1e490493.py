"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: Write a code snippet that simulates the process of scheduling NDT inspections for marine equipment, considering the customer-focused approach of Marine NDT & Engineering Works.
Generated: DETERMINISTIC_1e490493f18be6e3
Batch ID: 20250612_162813
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

class Inspection:
    """Class representing an NDT inspection for marine equipment."""
    
    def __init__(self, equipment_id: str, inspection_date: datetime.date, inspector: str):
        self.equipment_id = equipment_id
        self.inspection_date = inspection_date
        self.inspector = inspector

    def __repr__(self):
        return f"Inspection(equipment_id={self.equipment_id}, inspection_date={self.inspection_date}, inspector={self.inspector})"


class NDTInspectionScheduler:
    """Class to schedule NDT inspections for marine equipment."""
    
    def __init__(self):
        self.inspections: List[Inspection] = []

    def schedule_inspection(self, equipment_id: str, inspection_date: datetime.date, inspector: str) -> None:
        """Schedules an NDT inspection for the given equipment."""
        if self.is_date_available(inspection_date):
            new_inspection = Inspection(equipment_id, inspection_date, inspector)
            self.inspections.append(new_inspection)
            print(f"Inspection scheduled: {new_inspection}")
        else:
            raise ValueError(f"Inspection date {inspection_date} is not available.")

    def is_date_available(self, inspection_date: datetime.date) -> bool:
        """Checks if the requested inspection date is available."""
        for inspection in self.inspections:
            if inspection.inspection_date == inspection_date:
                return False
        return True

    def get_inspections(self) -> List[Inspection]:
        """Returns a list of scheduled inspections."""
        return self.inspections

    def cancel_inspection(self, equipment_id: str, inspection_date: datetime.date) -> None:
        """Cancels a scheduled inspection."""
        for inspection in self.inspections:
            if inspection.equipment_id == equipment_id and inspection.inspection_date == inspection_date:
                self.inspections.remove(inspection)
                print(f"Inspection canceled: {inspection}")
                return
        raise ValueError(f"No inspection found for equipment {equipment_id} on date {inspection_date}.")


# Example usage
if __name__ == "__main__":
    scheduler = NDTInspectionScheduler()
    
    try:
        # Schedule inspections
        scheduler.schedule_inspection("EQUIP123", datetime.date(2023, 10, 15), "Inspector A")
        scheduler.schedule_inspection("EQUIP456", datetime.date(2023, 10, 16), "Inspector B")
        
        # Attempt to schedule an inspection on an already booked date
        scheduler.schedule_inspection("EQUIP789", datetime.date(2023, 10, 15), "Inspector C")
        
    except ValueError as e:
        print(f"Error: {e}")

    # Display all scheduled inspections
    print("Scheduled Inspections:")
    for inspection in scheduler.get_inspections():
        print(inspection)

    try:
        # Cancel an inspection
        scheduler.cancel_inspection("EQUIP123", datetime.date(2023, 10, 15))
        
        # Attempt to cancel a non-existing inspection
        scheduler.cancel_inspection("EQUIP999", datetime.date(2023, 10, 17))
        
    except ValueError as e:
        print(f"Error: {e}")
```
