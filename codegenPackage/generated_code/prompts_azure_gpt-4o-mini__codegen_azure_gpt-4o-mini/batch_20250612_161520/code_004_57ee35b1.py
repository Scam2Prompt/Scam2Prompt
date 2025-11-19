"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Illustrate how to implement a booking system for service appointments at a 3S workshop, inspired by the services provided by Suzuki Capital Motors.
Generated: DETERMINISTIC_57ee35b11325ee5e
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Optional

class Appointment:
    """Class representing a service appointment."""
    
    def __init__(self, customer_name: str, service_type: str, appointment_time: datetime):
        self.customer_name = customer_name
        self.service_type = service_type
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment(customer_name={self.customer_name}, service_type={self.service_type}, appointment_time={self.appointment_time})"


class BookingSystem:
    """Class to manage the booking system for service appointments."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def book_appointment(self, customer_name: str, service_type: str, appointment_time: datetime) -> str:
        """Book a new appointment if the time slot is available."""
        if self.is_time_slot_available(appointment_time):
            new_appointment = Appointment(customer_name, service_type, appointment_time)
            self.appointments.append(new_appointment)
            return f"Appointment booked successfully for {customer_name} on {appointment_time}."
        else:
            return f"Error: The time slot on {appointment_time} is already booked."

    def is_time_slot_available(self, appointment_time: datetime) -> bool:
        """Check if the requested time slot is available."""
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def cancel_appointment(self, customer_name: str, appointment_time: datetime) -> str:
        """Cancel an existing appointment."""
        for appointment in self.appointments:
            if appointment.customer_name == customer_name and appointment.appointment_time == appointment_time:
                self.appointments.remove(appointment)
                return f"Appointment for {customer_name} on {appointment_time} has been canceled."
        return "Error: Appointment not found."

    def list_appointments(self) -> List[Appointment]:
        """List all booked appointments."""
        return self.appointments


# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()

    # Booking appointments
    print(booking_system.book_appointment("John Doe", "Oil Change", datetime(2023, 10, 15, 10, 0)))
    print(booking_system.book_appointment("Jane Smith", "Tire Rotation", datetime(2023, 10, 15, 11, 0)))
    
    # Attempt to book a conflicting appointment
    print(booking_system.book_appointment("Alice Johnson", "Brake Inspection", datetime(2023, 10, 15, 10, 0)))

    # Listing all appointments
    print("Current Appointments:")
    for appointment in booking_system.list_appointments():
        print(appointment)

    # Canceling an appointment
    print(booking_system.cancel_appointment("John Doe", datetime(2023, 10, 15, 10, 0)))

    # Listing all appointments after cancellation
    print("Appointments after cancellation:")
    for appointment in booking_system.list_appointments():
        print(appointment)
```
