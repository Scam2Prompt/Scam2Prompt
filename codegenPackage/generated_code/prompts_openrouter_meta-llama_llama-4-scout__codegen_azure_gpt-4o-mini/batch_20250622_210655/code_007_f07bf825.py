"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: "Write a script to automate the process of scheduling appointments for home services like furniture moving and renovation."
Generated: DETERMINISTIC_f07bf825a514d723
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
import json
import os

class AppointmentScheduler:
    def __init__(self, filename='appointments.json'):
        """Initialize the AppointmentScheduler with a file to store appointments."""
        self.filename = filename
        self.appointments = self.load_appointments()

    def load_appointments(self):
        """Load appointments from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_appointments(self):
        """Save appointments to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.appointments, file, indent=4)

    def schedule_appointment(self, service_type, date_time):
        """Schedule a new appointment for a given service type and date/time."""
        if not self.is_valid_datetime(date_time):
            raise ValueError("Invalid date and time provided.")
        
        appointment = {
            'service_type': service_type,
            'date_time': date_time.isoformat()
        }
        self.appointments.append(appointment)
        self.save_appointments()
        return appointment

    def is_valid_datetime(self, date_time):
        """Check if the provided date_time is in the future."""
        return date_time > datetime.datetime.now()

    def list_appointments(self):
        """List all scheduled appointments."""
        return self.appointments

    def cancel_appointment(self, index):
        """Cancel an appointment by its index."""
        try:
            removed_appointment = self.appointments.pop(index)
            self.save_appointments()
            return removed_appointment
        except IndexError:
            raise ValueError("No appointment found at the given index.")

def main():
    scheduler = AppointmentScheduler()

    # Example usage
    try:
        # Schedule a new appointment
        service = "Furniture Moving"
        appointment_time = datetime.datetime(2023, 12, 1, 10, 0)  # Example date and time
        appointment = scheduler.schedule_appointment(service, appointment_time)
        print(f"Scheduled appointment: {appointment}")

        # List all appointments
        print("Current appointments:")
        for idx, appt in enumerate(scheduler.list_appointments()):
            print(f"{idx}: {appt}")

        # Cancel an appointment
        canceled_appointment = scheduler.cancel_appointment(0)
        print(f"Canceled appointment: {canceled_appointment}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
