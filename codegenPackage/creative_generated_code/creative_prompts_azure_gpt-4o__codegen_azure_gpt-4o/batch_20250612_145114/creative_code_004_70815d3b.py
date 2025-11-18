"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Write a script to automate scheduling for roofing inspections, referencing King Roofing's free inspection offer and contact hours.
Generated: DETERMINISTIC_70815d3bb34512df
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import Optional


class KingRoofingScheduler:
    """
    A class to automate scheduling for King Roofing's free roofing inspections.
    """

    def __init__(self):
        # King Roofing's contact hours in 24-hour format
        self.contact_hours = {"start": 8, "end": 17}  # 8:00 AM to 5:00 PM
        self.inspection_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]  # Weekdays only

    def is_within_contact_hours(self) -> bool:
        """
        Check if the current time falls within King Roofing's contact hours.
        :return: bool - True if within contact hours, False otherwise.
        """
        current_hour = datetime.datetime.now().hour
        return self.contact_hours["start"] <= current_hour < self.contact_hours["end"]

    def schedule_inspection(self, preferred_date: str, preferred_time: str) -> Optional[str]:
        """
        Attempt to schedule a roofing inspection.
        :param preferred_date: The preferred date in "YYYY-MM-DD" format.
        :param preferred_time: The preferred time in "HH:MM" format (24-hour time).
        :return: Confirmation message if scheduling is successful, or error message otherwise.
        """
        try:
            # Parse the preferred date and time
            inspection_date = datetime.datetime.strptime(preferred_date, "%Y-%m-%d").date()
            inspection_time = datetime.datetime.strptime(preferred_time, "%H:%M").time()

            # Ensure the chosen day is valid for inspections
            if inspection_date.strftime("%A") not in self.inspection_days:
                return "Error: Inspections can only be scheduled on weekdays (Monday through Friday)."

            # Ensure the chosen time falls within contact hours
            if not (self.contact_hours["start"] <= inspection_time.hour < self.contact_hours["end"]):
                return f"Error: Inspections can only be scheduled between {self.contact_hours['start']}:00 and {self.contact_hours['end']}:00."

            # Ensure the inspection date is not in the past
            if inspection_date < datetime.date.today():
                return "Error: Inspection date cannot be in the past."

            # Confirm the inspection
            return (f"Success: Your free roofing inspection has been scheduled on {inspection_date} "
                    f"at {inspection_time}. Thank you for choosing King Roofing!")

        except ValueError as e:
            # Handle invalid date or time formats
            return f"Error: Invalid date or time format. Please use 'YYYY-MM-DD' for date and 'HH:MM' for time. Details: {str(e)}"


if __name__ == "__main__":
    # Example Usage
    scheduler = KingRoofingScheduler()

    # Check contact hours
    if scheduler.is_within_contact_hours():
        print("King Roofing is available for scheduling inspections.")

        # Schedule a sample inspection
        preferred_date = input("Enter preferred date (YYYY-MM-DD): ")
        preferred_time = input("Enter preferred time (HH:MM): ")
        result = scheduler.schedule_inspection(preferred_date, preferred_time)
        print(result)
    else:
        print("King Roofing is currently unavailable. Please contact us between 8:00 AM and 5:00 PM.")
```
