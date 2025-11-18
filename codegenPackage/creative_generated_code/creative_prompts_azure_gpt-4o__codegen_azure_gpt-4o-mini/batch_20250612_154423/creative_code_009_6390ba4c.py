"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.connext.solutions
Prompt: Create a script to facilitate patient scheduling and revenue cycle management for healthcare support teams, leveraging Connext's healthcare-specific solutions.
Generated: DETERMINISTIC_6390ba4c97231c6a
Batch ID: 20250612_154423
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

class Patient:
    def __init__(self, patient_id: str, name: str, phone: str, email: str):
        """
        Initialize a Patient object.
        
        :param patient_id: Unique identifier for the patient
        :param name: Full name of the patient
        :param phone: Patient's contact phone number
        :param email: Patient's email address
        """
        self.patient_id = patient_id
        self.name = name
        self.phone = phone
        self.email = email

class Appointment:
    def __init__(self, appointment_id: str, patient: Patient, date_time: datetime.datetime, reason: str):
        """
        Initialize an Appointment object.
        
        :param appointment_id: Unique identifier for the appointment
        :param patient: Patient object associated with the appointment
        :param date_time: Date and time of the appointment
        :param reason: Reason for the appointment
        """
        self.appointment_id = appointment_id
        self.patient = patient
        self.date_time = date_time
        self.reason = reason

class ScheduleManager:
    def __init__(self):
        """Initialize the ScheduleManager with an empty schedule."""
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, patient: Patient, date_time: datetime.datetime, reason: str) -> Appointment:
        """
        Schedule a new appointment for a patient.
        
        :param patient: Patient object
        :param date_time: Date and time of the appointment
        :param reason: Reason for the appointment
        :return: The scheduled Appointment object
        """
        appointment_id = f"APPT-{len(self.appointments) + 1}"
        appointment = Appointment(appointment_id, patient, date_time, reason)
        self.appointments.append(appointment)
        return appointment

    def cancel_appointment(self, appointment_id: str) -> bool:
        """
        Cancel an existing appointment by its ID.
        
        :param appointment_id: Unique identifier for the appointment
        :return: True if cancellation was successful, False otherwise
        """
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                self.appointments.remove(appointment)
                return True
        return False

    def get_schedule(self) -> List[Dict[str, str]]:
        """
        Retrieve the current schedule of appointments.
        
        :return: List of dictionaries representing the appointments
        """
        schedule = []
        for appointment in self.appointments:
            schedule.append({
                'appointment_id': appointment.appointment_id,
                'patient_name': appointment.patient.name,
                'date_time': appointment.date_time.strftime("%Y-%m-%d %H:%M"),
                'reason': appointment.reason
            })
        return schedule

# Example usage of the classes
if __name__ == "__main__":
    try:
        # Create a schedule manager instance
        schedule_manager = ScheduleManager()

        # Create a patient
        patient1 = Patient("P001", "John Doe", "555-1234", "john@example.com")

        # Schedule an appointment
        appointment = schedule_manager.schedule_appointment(patient1, datetime.datetime(2023, 10, 15, 14, 30), "Annual Checkup")
        print(f"Scheduled Appointment: {appointment.appointment_id} for {appointment.patient.name} on {appointment.date_time}")

        # Get current schedule
        print("Current Schedule:")
        for item in schedule_manager.get_schedule():
            print(item)

        # Cancel the appointment
        if schedule_manager.cancel_appointment(appointment.appointment_id):
            print(f"Cancelled Appointment: {appointment.appointment_id}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
