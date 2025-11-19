"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Write a Python script to create a simple text-based appointment booking system for a counseling service, including features for sending messages and storing client information.
Generated: DETERMINISTIC_f302cecfc87fdb46
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class Appointment:
    """Class to represent an appointment."""
    
    def __init__(self, client_name, appointment_time, message):
        self.client_name = client_name
        self.appointment_time = appointment_time
        self.message = message

    def to_dict(self):
        """Convert appointment details to a dictionary."""
        return {
            'client_name': self.client_name,
            'appointment_time': self.appointment_time.isoformat(),
            'message': self.message
        }

class AppointmentSystem:
    """Class to manage appointments."""
    
    def __init__(self, storage_file='appointments.json'):
        self.storage_file = storage_file
        self.appointments = self.load_appointments()

    def load_appointments(self):
        """Load appointments from a JSON file."""
        try:
            with open(self.storage_file, 'r') as file:
                return [Appointment(**data) for data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_appointments(self):
        """Save appointments to a JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump([appt.to_dict() for appt in self.appointments], file)

    def book_appointment(self, client_name, appointment_time, message):
        """Book a new appointment."""
        appointment = Appointment(client_name, appointment_time, message)
        self.appointments.append(appointment)
        self.save_appointments()
        print(f"Appointment booked for {client_name} on {appointment_time}.")

    def list_appointments(self):
        """List all booked appointments."""
        if not self.appointments:
            print("No appointments booked.")
            return
        for appt in self.appointments:
            print(f"{appt.client_name} - {appt.appointment_time} - {appt.message}")

def main():
    """Main function to run the appointment booking system."""
    system = AppointmentSystem()
    
    while True:
        print("\n--- Appointment Booking System ---")
        print("1. Book an appointment")
        print("2. List appointments")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            client_name = input("Enter client name: ")
            appointment_time_str = input("Enter appointment time (YYYY-MM-DD HH:MM): ")
            message = input("Enter a message: ")
            try:
                appointment_time = datetime.strptime(appointment_time_str, '%Y-%m-%d %H:%M')
                system.book_appointment(client_name, appointment_time, message)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
        
        elif choice == '2':
            system.list_appointments()
        
        elif choice == '3':
            print("Exiting the appointment booking system.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```
