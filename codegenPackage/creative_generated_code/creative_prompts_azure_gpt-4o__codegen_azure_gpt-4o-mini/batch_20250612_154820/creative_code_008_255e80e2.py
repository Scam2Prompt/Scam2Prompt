"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthinsuranceshop.ie
Prompt: Write code to implement a virtual healthcare service booking system, inspired by the "MyClinic" feature mentioned for Irish Life Health members on the Health Insurance Shop website.
Generated: DETERMINISTIC_255e80e26482413f
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Optional

class Appointment:
    """Class representing a healthcare appointment."""
    
    def __init__(self, patient_name: str, doctor_name: str, appointment_time: datetime):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment({self.patient_name}, {self.doctor_name}, {self.appointment_time})"

class Clinic:
    """Class representing a virtual healthcare clinic."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def book_appointment(self, patient_name: str, doctor_name: str, appointment_time: datetime) -> str:
        """
        Books an appointment for a patient with a specified doctor at a given time.
        
        :param patient_name: Name of the patient
        :param doctor_name: Name of the doctor
        :param appointment_time: Date and time for the appointment
        :return: Confirmation message
        """
        if not self.is_time_available(appointment_time):
            return "The selected time is not available. Please choose another time."
        
        new_appointment = Appointment(patient_name, doctor_name, appointment_time)
        self.appointments.append(new_appointment)
        return f"Appointment booked for {patient_name} with {doctor_name} at {appointment_time}."

    def is_time_available(self, appointment_time: datetime) -> bool:
        """
        Checks if the appointment time is available.
        
        :param appointment_time: Date and time for the appointment
        :return: True if the time is available, False otherwise
        """
        return all(appt.appointment_time != appointment_time for appt in self.appointments)

    def get_appointments(self) -> List[Appointment]:
        """Returns a list of all booked appointments."""
        return self.appointments

def main():
    clinic = Clinic()
    
    # Booking appointments
    try:
        appointment1 = clinic.book_appointment("Alice Smith", "Dr. Jones", datetime.now() + timedelta(days=1, hours=10))
        print(appointment1)
        
        appointment2 = clinic.book_appointment("Bob Johnson", "Dr. Smith", datetime.now() + timedelta(days=1, hours=11))
        print(appointment2)

        # Trying to book a conflicting appointment
        appointment3 = clinic.book_appointment("Charlie Brown", "Dr. Jones", datetime.now() + timedelta(days=1, hours=10))
        print(appointment3)  # Should notify that the time is not available

        # Listing all appointments
        print("All appointments:")
        for appointment in clinic.get_appointments():
            print(appointment)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
