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
from typing import List, Dict

class InspectionScheduler:
    """
    A class to schedule NDT inspections for marine equipment.
    """

    def __init__(self):
        """
        Initializes the scheduler with an empty schedule.
        """
        self.schedule = []  # List to store scheduled inspections

    def add_inspection(self, equipment_id: str, customer_name: str, preferred_date: str) -> Dict:
        """
        Adds an inspection to the schedule.

        Args:
            equipment_id (str): Unique identifier for the marine equipment.
            customer_name (str): Name of the customer requesting the inspection.
            preferred_date (str): Preferred date for the inspection in 'YYYY-MM-DD' format.

        Returns:
            Dict: Details of the scheduled inspection or an error message.
        """
        try:
            # Validate the preferred date format
            inspection_date = datetime.datetime.strptime(preferred_date, '%Y-%m-%d').date()
            
            # Check if the preferred date is in the future
            if inspection_date < datetime.date.today():
                return {"error": "Preferred date must be in the future."}

            # Create inspection record
            inspection = {
                "equipment_id": equipment_id,
                "customer_name": customer_name,
                "inspection_date": inspection_date,
                "status": "Scheduled"
            }

            # Add inspection to the schedule
            self.schedule.append(inspection)
            return {"success": "Inspection scheduled successfully.", "inspection": inspection}

        except ValueError:
            return {"error": "Invalid date format. Use 'YYYY-MM-DD'."}

    def view_schedule(self) -> List[Dict]:
        """
        Returns the current inspection schedule.

        Returns:
            List[Dict]: List of scheduled inspections.
        """
        return self.schedule

    def cancel_inspection(self, equipment_id: str) -> Dict:
        """
        Cancels an inspection for the given equipment ID.

        Args:
            equipment_id (str): Unique identifier for the marine equipment.

        Returns:
            Dict: Success or error message.
        """
        for inspection in self.schedule:
            if inspection["equipment_id"] == equipment_id:
                self.schedule.remove(inspection)
                return {"success": f"Inspection for equipment ID {equipment_id} has been canceled."}
        
        return {"error": f"No inspection found for equipment ID {equipment_id}."}


# Example usage
if __name__ == "__main__":
    scheduler = InspectionScheduler()

    # Schedule inspections
    print(scheduler.add_inspection("EQ123", "John Doe", "2023-11-15"))
    print(scheduler.add_inspection("EQ124", "Jane Smith", "2023-10-10"))

    # View schedule
    print("Current Schedule:", scheduler.view_schedule())

    # Cancel an inspection
    print(scheduler.cancel_inspection("EQ123"))

    # View updated schedule
    print("Updated Schedule:", scheduler.view_schedule())
```
