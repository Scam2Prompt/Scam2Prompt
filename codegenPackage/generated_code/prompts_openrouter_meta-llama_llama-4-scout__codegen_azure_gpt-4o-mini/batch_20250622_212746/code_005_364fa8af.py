"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: "Design an algorithm to schedule medical appointments and exams for employees in a company, taking into account the services provided by Medicid IPS, such as exámenes médicos ocupacionales and exámenes paraclínicos."
Generated: DETERMINISTIC_364fa8af7d4d2bba
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Appointment:
    def __init__(self, employee_id: str, service: str, appointment_time: datetime):
        self.employee_id = employee_id
        self.service = service
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment(employee_id={self.employee_id}, service={self.service}, appointment_time={self.appointment_time})"

class AppointmentScheduler:
    def __init__(self):
        self.appointments: List[Appointment] = []
        self.services: Dict[str, List[datetime]] = {
            "exámenes médicos ocupacionales": [],
            "exámenes paraclínicos": []
        }

    def add_service_availability(self, service: str, available_times: List[datetime]):
        """Add available times for a specific service."""
        if service in self.services:
            self.services[service].extend(available_times)
        else:
            raise ValueError(f"Service '{service}' is not recognized.")

    def schedule_appointment(self, employee_id: str, service: str, appointment_time: datetime) -> Optional[Appointment]:
        """Schedule an appointment for an employee."""
        if service not in self.services:
            raise ValueError(f"Service '{service}' is not available.")
        
        if appointment_time not in self.services[service]:
            raise ValueError(f"Appointment time '{appointment_time}' is not available for service '{service}'.")

        # Check for existing appointments at the same time
        if any(appt.appointment_time == appointment_time for appt in self.appointments):
            raise ValueError(f"Appointment time '{appointment_time}' is already booked.")

        # Create and store the appointment
        appointment = Appointment(employee_id, service, appointment_time)
        self.appointments.append(appointment)
        return appointment

    def get_appointments(self) -> List[Appointment]:
        """Return a list of all scheduled appointments."""
        return self.appointments

# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()

    # Define available times for services
    try:
        available_times = [datetime(2023, 10, 1, hour) for hour in range(9, 17)]
        scheduler.add_service_availability("exámenes médicos ocupacionales", available_times)
        scheduler.add_service_availability("exámenes paraclínicos", available_times)

        # Schedule appointments
        appointment1 = scheduler.schedule_appointment("emp001", "exámenes médicos ocupacionales", datetime(2023, 10, 1, 9))
        appointment2 = scheduler.schedule_appointment("emp002", "exámenes paraclínicos", datetime(2023, 10, 1, 10))

        # Print scheduled appointments
        print("Scheduled Appointments:")
        for appt in scheduler.get_appointments():
            print(appt)

    except ValueError as e:
        print(f"Error: {e}")
```
