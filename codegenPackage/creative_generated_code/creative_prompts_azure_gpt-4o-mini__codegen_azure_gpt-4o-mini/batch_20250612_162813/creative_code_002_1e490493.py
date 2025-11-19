"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinendtbd.com
Prompt: Write a code snippet that simulates the process of scheduling NDT inspections for marine equipment, considering the customer-focused approach of Marine NDT & Engineering Works.
Generated: DETERMINISTIC_1e490493f18be6e3
Batch ID: 20250612_162813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class Inspection:
    """Class to represent an NDT inspection schedule."""
    
    def __init__(self, equipment_id: str, inspection_date: datetime.date, customer_name: str):
        self.equipment_id = equipment_id
        self.inspection_date = inspection_date
        self.customer_name = customer_name

    def __repr__(self):
        return f"Inspection(equipment_id={self.equipment_id}, inspection_date={self.inspection_date}, customer_name={self.customer_name})"


class NDTInspectionScheduler:
    """Class to manage the scheduling of NDT inspections for marine equipment."""

    def __init__(self):
        self.schedule: List[Inspection] = []

    def schedule_inspection(self, equipment_id: str, inspection_date: datetime.date, customer_name: str) -> None:
        """
        Schedule an inspection for the given equipment.

        Args:
            equipment_id (str): The ID of the equipment to be inspected.
            inspection_date (datetime.date): The date of the inspection.
            customer_name (str): The name of the customer requesting the inspection.

        Raises:
            ValueError: If the inspection date is in the past or if the equipment ID is empty.
        """
        # Validate input
        if inspection_date < datetime.date.today():
            raise ValueError("Inspection date cannot be in the past.")
        if not equipment_id:
            raise ValueError("Equipment ID cannot be empty.")
        
        # Create and add the inspection to the schedule
        new_inspection = Inspection(equipment_id, inspection_date, customer_name)
        self.schedule.append(new_inspection)

    def get_schedule(self) -> List[Dict[str, Optional[str]]]:
        """
        Retrieve the current inspection schedule.

        Returns:
            List[Dict[str, Optional[str]]]: A list of dictionaries containing inspection details.
        """
        return [{"equipment_id": ins.equipment_id, 
                 "inspection_date": ins.inspection_date.isoformat(), 
                 "customer_name": ins.customer_name} for ins in self.schedule]

    def remove_inspection(self, equipment_id: str, inspection_date: datetime.date) -> None:
        """
        Remove an inspection from the schedule.

        Args:
            equipment_id (str): The ID of the equipment whose inspection is to be removed.
            inspection_date (datetime.date): The date of the inspection to be removed.

        Raises:
            ValueError: If the inspection does not exist in the schedule.
        """
        # Find the inspection to remove
        for ins in self.schedule:
            if ins.equipment_id == equipment_id and ins.inspection_date == inspection_date:
                self.schedule.remove(ins)
                return
        raise ValueError("Inspection not found in the schedule.")


# Example usage
if __name__ == "__main__":
    scheduler = NDTInspectionScheduler()
    
    try:
        scheduler.schedule_inspection("EQUIP123", datetime.date(2023, 11, 25), "Marine Corp")
        scheduler.schedule_inspection("EQUIP456", datetime.date(2023, 12, 15), "Oceanic Ltd")
        
        print("Current Inspection Schedule:")
        print(scheduler.get_schedule())
        
        # Removing an inspection
        scheduler.remove_inspection("EQUIP123", datetime.date(2023, 11, 25))
        print("Updated Inspection Schedule after removal:")
        print(scheduler.get_schedule())
        
    except ValueError as e:
        print(f"Error: {e}")
```
