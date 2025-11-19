"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliniquerobinpaul.com
Prompt: Generate a code snippet for a booking system that allows patients to schedule appointments with a chiropractor or osteopath, similar to the services offered at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_072b4278a4a5457e
Batch ID: 20250612_162311
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
    """Class representing a patient's appointment."""
    def __init__(self, patient_name: str, practitioner_type: str, appointment_time: datetime):
        self.patient_name = patient_name
        self.practitioner_type = practitioner_type
        self.appointment_time = appointment_time

    def __str__(self):
        return f"Appointment({self.patient_name}, {self.practitioner_type}, {self.appointment_time})"


class BookingSystem:
    """Class to manage bookings for chiropractors and osteopaths."""
    def __init__(self):
        self.appointments: List[Appointment] = []
        self.available_slots: List[datetime] = self.generate_availability()

    def generate_availability(self) -> List[datetime]:
        """Generate available appointment slots for the next 30 days."""
        now = datetime.now()
        slots = []
        for i in range(30):  # Next 30 days
            for hour in range(9, 17):  # Working hours from 9 AM to 5 PM
                slots.append(now.replace(hour=hour, minute=0) + timedelta(days=i))
        return slots

    def book_appointment(self, patient_name: str, practitioner_type: str, appointment_time: datetime) -> Optional[str]:
        """Book an appointment for a patient.

        Args:
            patient_name (str): Name of the patient.
            practitioner_type (str): Type of practitioner (chiropractor or osteopath).
            appointment_time (datetime): Preferred appointment time.

        Returns:
            Optional[str]: Confirmation message or error message.
        """
        try:
            if practitioner_type not in ["chiropractor", "osteopath"]:
                return "Error: Invalid practitioner type."

            if appointment_time not in self.available_slots:
                return "Error: Selected time is not available."

            # Create and store the appointment
            appointment = Appointment(patient_name, practitioner_type, appointment_time)
            self.appointments.append(appointment)

            # Remove the slot from available slots
            self.available_slots.remove(appointment_time)

            return f"Appointment booked successfully: {appointment}"
        except Exception as e:
            return f"Error: {str(e)}"

    def list_appointments(self) -> List[str]:
        """List all booked appointments.

        Returns:
            List[str]: A list of appointment details.
        """
        return [str(appointment) for appointment in self.appointments]


# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Attempt to book an appointment
    response = booking_system.book_appointment("John Doe", "chiropractor", booking_system.available_slots[0])
    print(response)

    # List all appointments
    appointments = booking_system.list_appointments()
    print("\nBooked Appointments:")
    for appointment in appointments:
        print(appointment)
```
