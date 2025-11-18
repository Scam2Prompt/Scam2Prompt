"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clinicaidet.com.ve
Prompt: Create a script to automate appointment scheduling for Grupo Clínico IDET, integrating with their existing telemedicine and domiciliary care services.
Generated: DETERMINISTIC_fa959f8215bcf0f9
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
from typing import List, Optional, Dict

class Appointment:
    """
    Class to represent an appointment.
    """
    def __init__(self, patient_name: str, date_time: datetime.datetime, service_type: str):
        self.patient_name = patient_name
        self.date_time = date_time
        self.service_type = service_type

    def __repr__(self):
        return f"Appointment(Patient: {self.patient_name}, DateTime: {self.date_time}, Service: {self.service_type})"

class AppointmentScheduler:
    """
    Class to handle scheduling of appointments for Grupo Clínico IDET.
    """
    def __init__(self):
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, patient_name: str, date_time: datetime.datetime, service_type: str) -> None:
        """
        Schedule an appointment after validating the time and service type.
        
        Args:
            patient_name (str): Name of the patient.
            date_time (datetime.datetime): Date and time of the appointment.
            service_type (str): Type of service (telemedicine or domiciliary).
        
        Raises:
            ValueError: If the appointment time is in the past or conflicts with an existing appointment.
        """
        # Validate the appointment time
        if date_time < datetime.datetime.now():
            raise ValueError("Cannot schedule an appointment in the past.")

        # Check for conflicting appointments
        if any(appt.date_time == date_time for appt in self.appointments):
            raise ValueError("There is already an appointment scheduled at this time.")

        # Create and store the appointment
        new_appointment = Appointment(patient_name, date_time, service_type)
        self.appointments.append(new_appointment)
        print(f"Appointment scheduled successfully: {new_appointment}")

    def get_appointments(self) -> List[Dict[str, str]]:
        """
        Get a list of all scheduled appointments.
        
        Returns:
            List[Dict[str, str]]: List of scheduled appointments with details.
        """
        return [{"patient_name": appt.patient_name, "date_time": appt.date_time.isoformat(), "service_type": appt.service_type} for appt in self.appointments]

    def cancel_appointment(self, date_time: datetime.datetime) -> None:
        """
        Cancel an appointment by its scheduled time.
        
        Args:
            date_time (datetime.datetime): Date and time of the appointment to cancel.
        
        Raises:
            ValueError: If there is no appointment at the specified time.
        """
        for appt in self.appointments:
            if appt.date_time == date_time:
                self.appointments.remove(appt)
                print(f"Appointment canceled successfully: {appt}")
                return
                
        raise ValueError("No appointment found at the specified time.")

def main():
    """
    Main function to demonstrate the appointment scheduling functionality.
    """
    scheduler = AppointmentScheduler()

    # Example scheduling new appointments
    try:
        scheduler.schedule_appointment("John Doe", datetime.datetime(2023, 11, 15, 10, 30), "telemedicine")
        scheduler.schedule_appointment("Jane Smith", datetime.datetime(2023, 11, 15, 11, 00), "domiciliary")
    except ValueError as e:
        print(f"Error scheduling appointment: {e}")

    # Display scheduled appointments
    print("Scheduled Appointments:")
    for appointment in scheduler.get_appointments():
        print(appointment)

    # Example of canceling an appointment
    try:
        scheduler.cancel_appointment(datetime.datetime(2023, 11, 15, 10, 30))
    except ValueError as e:
        print(f"Error canceling appointment: {e}")

if __name__ == "__main__":
    main()
```
