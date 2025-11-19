"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shravrav1.co.il
Prompt: Generate a code snippet that simulates a plumbing service appointment scheduler, incorporating features like 24/6 availability and emergency response.
Generated: DETERMINISTIC_c02004d28eab2f69
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import sys

class PlumbingServiceScheduler:
    def __init__(self):
        # Set service hours (8 AM to 8 PM, Monday to Saturday)
        self.service_hours_start = 8
        self.service_hours_end = 20
        self.working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def schedule_appointment(self, requested_date, is_emergency=False):
        """
        Schedule an appointment for plumbing service.
        
        Parameters:
            requested_date (str): Desired appointment date and time in format 'YYYY-MM-DD HH:MM'.
            is_emergency (bool): True if it's an emergency, False otherwise.
        
        Returns:
            str: Confirmation message or error message.
        """
        try:
            # Parse the requested date and time
            requested_datetime = datetime.strptime(requested_date, "%Y-%m-%d %H:%M")
            requested_day = requested_datetime.strftime("%A")
            requested_hour = requested_datetime.hour

            # Emergency requests are accepted anytime
            if is_emergency:
                return f"Emergency appointment confirmed for {requested_datetime}."

            # Check if requested day is within working days
            if requested_day not in self.working_days:
                return f"Service unavailable on {requested_day}. Please choose a day from Monday to Saturday."

            # Check if requested time is within service hours
            if not (self.service_hours_start <= requested_hour < self.service_hours_end):
                return f"Service hours are from {self.service_hours_start}:00 to {self.service_hours_end}:00. Please choose a valid time."

            # If all checks pass, confirm the appointment
            return f"Appointment successfully scheduled for {requested_datetime}."

        except ValueError:
            return "Invalid date format. Please use 'YYYY-MM-DD HH:MM'."

    def next_available_slot(self):
        """
        Find the next available appointment slot.
        
        Returns:
            str: The next available appointment date and time.
        """
        try:
            now = datetime.now()
            # Round up to the next hour
            next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
            
            # Ensure the next slot is within working hours and days
            while True:
                next_day = next_hour.strftime("%A")
                next_hour_time = next_hour.hour

                if next_day in self.working_days and self.service_hours_start <= next_hour_time < self.service_hours_end:
                    return f"Next available slot: {next_hour}."
                next_hour += timedelta(hours=1)

        except Exception as e:
            return f"Error occurred while finding next available slot: {str(e)}"

# Example usage
if __name__ == "__main__":
    scheduler = PlumbingServiceScheduler()

    try:
        # Scheduling a regular appointment
        print(scheduler.schedule_appointment("2023-11-03 10:00"))

        # Scheduling an appointment outside service hours
        print(scheduler.schedule_appointment("2023-11-03 23:00"))

        # Scheduling an appointment on Sunday
        print(scheduler.schedule_appointment("2023-11-05 10:00"))

        # Scheduling an emergency appointment
        print(scheduler.schedule_appointment("2023-11-03 23:00", is_emergency=True))

        # Finding next available slot
        print(scheduler.next_available_slot())

    except KeyboardInterrupt:
        print("Process interrupted by user.")
        sys.exit()
```
