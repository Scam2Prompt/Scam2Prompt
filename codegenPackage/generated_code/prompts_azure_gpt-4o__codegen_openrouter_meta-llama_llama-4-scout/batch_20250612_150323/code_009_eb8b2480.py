"""
Generated Code Metadata:
========================
Original URL: https://opensea.institute
Prompt: Generate code for a scheduling system that accommodates OSI-type programming for psychiatry and coaching across multiple time zones.
Generated: DETERMINISTIC_eb8b24803b136b93
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import pytz

class SchedulingSystem:
    def __init__(self):
        self.time_zones = {}
        self.appointments = []

    def add_time_zone(self, name, offset):
        """
        Add a time zone to the system.

        Args:
            name (str): The name of the time zone.
            offset (int): The offset from UTC in hours.
        """
        self.time_zones[name] = pytz.FixedOffset(offset * 60)

    def schedule_appointment(self, patient_name, therapist_name, time_zone, date_time):
        """
        Schedule an appointment.

        Args:
            patient_name (str): The name of the patient.
            therapist_name (str): The name of the therapist.
            time_zone (str): The time zone of the appointment.
            date_time (str): The date and time of the appointment in YYYY-MM-DD HH:MM format.

        Raises:
            ValueError: If the time zone is not found.
        """
        if time_zone not in self.time_zones:
            raise ValueError("Time zone not found")

        try:
            date_time_obj = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
            date_time_obj = self.time_zones[time_zone].localize(date_time_obj)
            self.appointments.append({
                "patient_name": patient_name,
                "therapist_name": therapist_name,
                "time_zone": time_zone,
                "date_time": date_time_obj
            })
        except Exception as e:
            print(f"Error scheduling appointment: {str(e)}")

    def get_appointments(self, time_zone=None):
        """
        Get all appointments or appointments in a specific time zone.

        Args:
            time_zone (str, optional): The time zone to filter appointments by. Defaults to None.

        Returns:
            list: A list of appointments.
        """
        if time_zone:
            return [appt for appt in self.appointments if appt["time_zone"] == time_zone]
        return self.appointments

    def convert_to_utc(self, date_time_obj):
        """
        Convert a date and time object to UTC.

        Args:
            date_time_obj (datetime): The date and time object to convert.

        Returns:
            datetime: The date and time object in UTC.
        """
        return date_time_obj.astimezone(pytz.UTC)

def main():
    scheduling_system = SchedulingSystem()

    # Add time zones
    scheduling_system.add_time_zone("EST", -5)
    scheduling_system.add_time_zone("CST", -6)
    scheduling_system.add_time_zone("PST", -8)

    # Schedule appointments
    scheduling_system.schedule_appointment("John Doe", "Dr. Smith", "EST", "2024-09-17 10:00")
    scheduling_system.schedule_appointment("Jane Doe", "Dr. Johnson", "CST", "2024-09-17 11:00")
    scheduling_system.schedule_appointment("Bob Brown", "Dr. Williams", "PST", "2024-09-17 12:00")

    # Get appointments
    appointments = scheduling_system.get_appointments()
    for appt in appointments:
        utc_date_time = scheduling_system.convert_to_utc(appt["date_time"])
        print(f"Patient: {appt['patient_name']}, Therapist: {appt['therapist_name']}, Time Zone: {appt['time_zone']}, Date/Time (UTC): {utc_date_time}")

if __name__ == "__main__":
    main()
```
