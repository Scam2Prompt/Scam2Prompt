"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Illustrate how to implement a booking system for service appointments at a 3S workshop, inspired by the services provided by Suzuki Capital Motors.
Generated: DETERMINISTIC_57ee35b11325ee5e
Batch ID: 20250612_161520
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
    def __init__(self, customer_name: str, service_type: str, appointment_time: datetime):
        self.customer_name = customer_name
        self.service_type = service_type
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment(customer_name={self.customer_name}, service_type={self.service_type}, " \
               f"appointment_time={self.appointment_time})"


class BookingSystem:
    def __init__(self):
        self.appointments: List[Appointment] = []  # List to store appointments

    def book_appointment(self, customer_name: str, service_type: str, appointment_time: datetime) -> None:
        """Book a new appointment if the slot is available."""
        if self.is_time_slot_available(appointment_time):
            new_appointment = Appointment(customer_name, service_type, appointment_time)
            self.appointments.append(new_appointment)
            print(f"Appointment booked successfully: {new_appointment}")
        else:
            print(f"Error: The time slot {appointment_time} is not available.")

    def is_time_slot_available(self, appointment_time: datetime) -> bool:
        """Check if the requested time slot is available."""
        return not any(appointment.appointment_time == appointment_time for appointment in self.appointments)

    def cancel_appointment(self, customer_name: str, appointment_time: datetime) -> None:
        """Cancel an existing appointment."""
        appointment = self.find_appointment(customer_name, appointment_time)
        if appointment:
            self.appointments.remove(appointment)
            print(f"Appointment canceled successfully: {appointment}")
        else:
            print(f"Error: No appointment found for {customer_name} at {appointment_time}.")

    def find_appointment(self, customer_name: str, appointment_time: datetime) -> Optional[Appointment]:
        """Find an existing appointment by customer name and time."""
        for appointment in self.appointments:
            if appointment.customer_name == customer_name and appointment.appointment_time == appointment_time:
                return appointment
        return None

    def list_appointments(self) -> List[Appointment]:
        """List all scheduled appointments."""
        return self.appointments


def main():
    # Create a booking system instance
    booking_system = BookingSystem()

    # Sample usage
    try:
        # Booking appointments
        booking_system.book_appointment("Alice Johnson", "Oil Change", datetime(2023, 10, 15, 10, 0))
        booking_system.book_appointment("Bob Smith", "Tire Rotation", datetime(2023, 10, 15, 11, 0))
        
        # Attempt to book an already booked slot
        booking_system.book_appointment("Charlie Brown", "Brake Inspection", datetime(2023, 10, 15, 10, 0))
        
        # List all appointments
        print("Current appointments:")
        for appointment in booking_system.list_appointments():
            print(appointment)

        # Cancel an appointment
        booking_system.cancel_appointment("Alice Johnson", datetime(2023, 10, 15, 10, 0))
        
        # Attempt to cancel a non-existing appointment
        booking_system.cancel_appointment("Charlie Brown", datetime(2023, 10, 15, 10, 0))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
