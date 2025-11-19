"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana2018.com
Prompt: Describe how to create a scheduling system for online health sessions that aligns with the practices outlined by Solana柔整体院, including initial consultations and follow-up sessions.
Generated: DETERMINISTIC_db6439ecb0163247
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class Appointment:
    def __init__(self, patient_name, appointment_date, duration, appointment_type):
        self.patient_name = patient_name
        self.appointment_date = appointment_date
        self.duration = duration  # in minutes
        self.appointment_type = appointment_type  # 'initial', 'follow-up'

    def to_dict(self):
        """Convert appointment details to a dictionary format for easier storage."""
        return {
            "patient_name": self.patient_name,
            "appointment_date": self.appointment_date.isoformat(),
            "duration": self.duration,
            "appointment_type": self.appointment_type
        }

class SchedulingSystem:
    def __init__(self):
        self.appointments = []

    def book_appointment(self, patient_name, appointment_date, duration, appointment_type):
        """Book a new appointment if the time slot is available."""
        if self.is_time_slot_available(appointment_date, duration):
            new_appointment = Appointment(patient_name, appointment_date, duration, appointment_type)
            self.appointments.append(new_appointment)
            print(f"Appointment booked for {patient_name} on {appointment_date}.")
        else:
            raise ValueError(f"Time slot {appointment_date} is not available.")

    def is_time_slot_available(self, appointment_date, duration):
        """Check if the requested time slot is available."""
        end_time = appointment_date + timedelta(minutes=duration)
        for appointment in self.appointments:
            if not (appointment_date >= appointment.appointment_date + timedelta(minutes=appointment.duration) or 
                    end_time <= appointment.appointment_date):
                return False
        return True

    def list_appointments(self, appointment_type=None):
        """List all appointments, optionally filtered by type."""
        try:
            if appointment_type:
                filtered_appointments = [appointment for appointment in self.appointments if appointment.appointment_type == appointment_type]
                return [appointment.to_dict() for appointment in filtered_appointments]
            return [appointment.to_dict() for appointment in self.appointments]
        except Exception as e:
            raise RuntimeError("Error while listing appointments.") from e

    def save_to_file(self, filename):
        """Save appointments to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([appointment.to_dict() for appointment in self.appointments], file, indent=4)
            print(f"Appointments saved to {filename}.")
        except IOError as e:
            raise IOError(f"Could not write to file {filename}.") from e

# Example usage
if __name__ == "__main__":
    system = SchedulingSystem()
    try:
        # Booking initial consultation
        system.book_appointment("John Doe", datetime(2023, 10, 10, 10, 0), 60, "initial")
        # Booking follow-up session
        system.book_appointment("John Doe", datetime(2023, 10, 17, 10, 0), 30, "follow-up")
        
        # List all appointments
        for appointment in system.list_appointments():
            print(appointment)
        
        # Save appointments to a file
        system.save_to_file("appointments.json")
        
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
