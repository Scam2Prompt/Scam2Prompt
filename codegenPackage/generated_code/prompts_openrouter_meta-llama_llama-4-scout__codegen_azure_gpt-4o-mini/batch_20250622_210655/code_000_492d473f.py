"""
Generated Code Metadata:
========================
Original URL: https://bepretty.hamburg
Prompt: Write a Python script to manage client appointments for a hair and makeup styling service, including booking and cancellation functionality.
Generated: DETERMINISTIC_492d473f9b4c0b8a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Appointment:
    """Class to represent a client appointment."""
    
    def __init__(self, client_name, appointment_time):
        self.client_name = client_name
        self.appointment_time = appointment_time

    def __str__(self):
        return f"Appointment for {self.client_name} at {self.appointment_time.strftime('%Y-%m-%d %H:%M')}"

class AppointmentManager:
    """Class to manage appointments for a hair and makeup styling service."""
    
    def __init__(self):
        self.appointments = []

    def book_appointment(self, client_name, appointment_time):
        """Book a new appointment if the time slot is available."""
        if self.is_time_slot_available(appointment_time):
            new_appointment = Appointment(client_name, appointment_time)
            self.appointments.append(new_appointment)
            print(f"Successfully booked: {new_appointment}")
        else:
            print(f"Error: Appointment time {appointment_time} is already booked.")

    def cancel_appointment(self, client_name, appointment_time):
        """Cancel an existing appointment."""
        for appointment in self.appointments:
            if appointment.client_name == client_name and appointment.appointment_time == appointment_time:
                self.appointments.remove(appointment)
                print(f"Successfully canceled: {appointment}")
                return
        print(f"Error: No appointment found for {client_name} at {appointment_time}.")

    def is_time_slot_available(self, appointment_time):
        """Check if the requested time slot is available."""
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def list_appointments(self):
        """List all booked appointments."""
        if not self.appointments:
            print("No appointments booked.")
        else:
            print("Current appointments:")
            for appointment in self.appointments:
                print(appointment)

def main():
    """Main function to run the appointment manager."""
    manager = AppointmentManager()

    # Example usage
    try:
        # Booking appointments
        manager.book_appointment("Alice", datetime.datetime(2023, 10, 15, 14, 30))
        manager.book_appointment("Bob", datetime.datetime(2023, 10, 15, 15, 0))
        
        # Listing appointments
        manager.list_appointments()

        # Attempting to book a conflicting appointment
        manager.book_appointment("Charlie", datetime.datetime(2023, 10, 15, 14, 30))

        # Canceling an appointment
        manager.cancel_appointment("Alice", datetime.datetime(2023, 10, 15, 14, 30))
        
        # Listing appointments after cancellation
        manager.list_appointments()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
