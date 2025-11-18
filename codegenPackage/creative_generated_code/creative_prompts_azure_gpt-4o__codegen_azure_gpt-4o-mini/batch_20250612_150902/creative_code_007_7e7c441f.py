"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Suggest tools or frameworks for implementing a scheduling system for medical examinations, including tests for confined spaces and working at heights, as offered by Medicid IPS.
Generated: DETERMINISTIC_7e7c441fc0f546d6
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# scheduling_system.py

"""
A simple scheduling system for medical examinations.
This system allows users to schedule tests for confined spaces and working at heights.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Appointment:
    """Class representing a medical examination appointment."""

    def __init__(self, patient_name: str, appointment_time: datetime, test_type: str):
        self.patient_name = patient_name
        self.appointment_time = appointment_time
        self.test_type = test_type

    def __repr__(self):
        return f"Appointment(patient_name='{self.patient_name}', appointment_time={self.appointment_time}, test_type='{self.test_type}')"


class SchedulingSystem:
    """Class to manage scheduling of medical examinations."""

    def __init__(self):
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, patient_name: str, appointment_time: datetime, test_type: str) -> None:
        """Schedules a new appointment if the time slot is available."""
        if self.is_time_slot_available(appointment_time):
            self.appointments.append(Appointment(patient_name, appointment_time, test_type))
        else:
            raise ValueError("The selected time slot is already booked.")

    def is_time_slot_available(self, appointment_time: datetime) -> bool:
        """Checks if the given time slot is available for scheduling."""
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def get_appointments(self) -> List[Dict[str, str]]:
        """Returns a list of scheduled appointments."""
        return [{"patient_name": appt.patient_name, "appointment_time": appt.appointment_time.strftime("%Y-%m-%d %H:%M"), "test_type": appt.test_type} for appt in self.appointments]

    def cancel_appointment(self, patient_name: str, appointment_time: datetime) -> None:
        """Cancels an existing appointment."""
        for appointment in self.appointments:
            if appointment.patient_name == patient_name and appointment.appointment_time == appointment_time:
                self.appointments.remove(appointment)
                return
        raise ValueError("Appointment not found.")


# Example usage
if __name__ == "__main__":
    scheduling_system = SchedulingSystem()
    
    try:
        # Schedule an appointment
        appointment_time = datetime.now() + timedelta(days=1)  # Schedule for next day
        scheduling_system.schedule_appointment("John Doe", appointment_time, "Confined Space Test")
        print("Appointment scheduled successfully.")

        # List appointments
        print("Scheduled Appointments:", scheduling_system.get_appointments())

        # Cancel the appointment
        scheduling_system.cancel_appointment("John Doe", appointment_time)
        print("Appointment canceled successfully.")

    except ValueError as e:
        print(f"Error: {e}")
```
