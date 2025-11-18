"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clinicaidet.com.ve
Prompt: Generate code to calculate the availability of medical specialists at Grupo Clínico IDET's locations based on their working hours and appointment schedules.
Generated: DETERMINISTIC_56887e430203341e
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class MedicalSpecialist:
    """
    Represents a medical specialist with their working hours and appointments.
    """
    def __init__(self, name, location, working_hours):
        """
        Initialize the specialist with basic information.

        :param name: Name of the specialist (str)
        :param location: Location of the specialist (str)
        :param working_hours: Dictionary with day-wise working hours.
                              Example: {'Monday': ('09:00', '17:00')}
        """
        self.name = name
        self.location = location
        self.working_hours = working_hours  # Dictionary with day-wise working hours
        self.appointments = []  # List to store appointments

    def add_appointment(self, date, start_time, end_time):
        """
        Adds an appointment to the specialist's schedule.

        :param date: Date of the appointment (str in 'YYYY-MM-DD' format)
        :param start_time: Start time of the appointment (str in 'HH:MM' format)
        :param end_time: End time of the appointment (str in 'HH:MM' format)
        """
        try:
            start = datetime.datetime.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M")
            end = datetime.datetime.strptime(f"{date} {end_time}", "%Y-%m-%d %H:%M")
            if start >= end:
                raise ValueError("Start time must be earlier than end time.")
            self.appointments.append((start, end))
        except ValueError as e:
            print(f"Error adding appointment: {e}")

    def get_availability(self, date):
        """
        Calculate the availability of the specialist for a given date.

        :param date: Date for which availability needs to be calculated (str in 'YYYY-MM-DD' format)
        :return: List of available time slots (tuples with start and end times)
        """
        try:
            day_of_week = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A")
            if day_of_week not in self.working_hours:
                return []  # Specialist does not work on this day
            
            working_start, working_end = self.working_hours[day_of_week]
            working_start_dt = datetime.datetime.strptime(f"{date} {working_start}", "%Y-%m-%d %H:%M")
            working_end_dt = datetime.datetime.strptime(f"{date} {working_end}", "%Y-%m-%d %H:%M")
            
            # Initialize availability with the full working hours
            availability = [(working_start_dt, working_end_dt)]
            
            # Sort appointments and refine availability
            for start, end in sorted(self.appointments):
                if start.date() != working_start_dt.date():
                    continue  # Skip appointments not on the requested day
                
                new_availability = []
                for avail_start, avail_end in availability:
                    if end <= avail_start or start >= avail_end:
                        # No overlap, retain current slot
                        new_availability.append((avail_start, avail_end))
                    else:
                        # Overlap detected, split the slot
                        if avail_start < start:
                            new_availability.append((avail_start, start))
                        if avail_end > end:
                            new_availability.append((end, avail_end))
                
                availability = new_availability
            
            return availability
        except ValueError as e:
            print(f"Error calculating availability: {e}")
            return []


# Example Usage:

# Define specialists
specialist1 = MedicalSpecialist(
    name="Dr. Smith",
    location="IDET - Downtown",
    working_hours={
        'Monday': ('09:00', '17:00'),
        'Tuesday': ('09:00', '17:00'),
        'Wednesday': ('09:00', '17:00')
    }
)

# Add appointments
specialist1.add_appointment(date="2023-10-23", start_time="10:00", end_time="11:00")
specialist1.add_appointment(date="2023-10-23", start_time="13:00", end_time="14:30")

# Check availability
availability = specialist1.get_availability(date="2023-10-23")
print("Availability for Dr. Smith on 2023-10-23:")
for start, end in availability:
    print(f"Available from {start.strftime('%H:%M')} to {end.strftime('%H:%M')}")
```
