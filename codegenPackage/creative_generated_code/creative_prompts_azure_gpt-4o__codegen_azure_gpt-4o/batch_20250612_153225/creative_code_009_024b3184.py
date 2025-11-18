"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trindadetelecom.com.br
Prompt: Generate code to implement a system for scheduling internet installation appointments, ensuring rapid installation as emphasized by Trindade Telecom.
Generated: DETERMINISTIC_024b318485565f03
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class Appointment:
    """
    Represents an installation appointment.
    """
    def __init__(self, customer_name: str, date: datetime.date, time: datetime.time):
        self.customer_name = customer_name
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment for {self.customer_name} on {self.date} at {self.time}"


class AppointmentScheduler:
    """
    Manages scheduling of installation appointments.
    Ensures rapid installation by prioritizing earliest available time slots.
    """
    def __init__(self):
        # A list to store appointments
        self.appointments: List[Appointment] = []
        # Define business hours for appointments
        self.business_start_hour = 9
        self.business_end_hour = 17

    def is_time_slot_available(self, date: datetime.date, time: datetime.time) -> bool:
        """
        Checks if a specific time slot is available for scheduling.
        """
        for appointment in self.appointments:
            if appointment.date == date and appointment.time == time:
                return False
        return True

    def schedule_appointment(self, customer_name: str, preferred_date: datetime.date) -> Optional[Appointment]:
        """
        Schedules an appointment for the earliest available time slot on the preferred date.
        If no slots are available, returns None.
        """
        current_time = datetime.datetime.now().time()
        # Generate possible time slots for the day
        for hour in range(self.business_start_hour, self.business_end_hour + 1):
            appointment_time = datetime.time(hour=hour, minute=0)
            # Ensure appointment is in the future
            if preferred_date == datetime.date.today() and appointment_time <= current_time:
                continue
            # Check availability for the time slot
            if self.is_time_slot_available(preferred_date, appointment_time):
                # Create and store appointment
                new_appointment = Appointment(customer_name, preferred_date, appointment_time)
                self.appointments.append(new_appointment)
                return new_appointment
        return None

    def list_appointments(self) -> List[Appointment]:
        """
        Returns a list of all scheduled appointments.
        """
        return self.appointments


# Example usage
def main():
    scheduler = AppointmentScheduler()

    try:
        # Schedule an appointment for a customer
        customer_name = "John Doe"
        preferred_date = datetime.date.today()  # Today's date
        appointment = scheduler.schedule_appointment(customer_name, preferred_date)

        if appointment:
            print(f"Appointment scheduled: {appointment}")
        else:
            print("No available time slots for the preferred date.")

        # List all appointments
        print("\nAll appointments:")
        for appt in scheduler.list_appointments():
            print(appt)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
