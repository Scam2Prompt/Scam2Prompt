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
# appointment_manager.py

from datetime import datetime, timedelta
import json
import os

class AppointmentManager:
    def __init__(self, data_file='appointments.json'):
        """
        Initialize the AppointmentManager.

        :param data_file: The file to store appointment data.
        """
        self.data_file = data_file
        self.appointments = self.load_appointments()

    def load_appointments(self):
        """
        Load appointments from the data file.

        :return: A dictionary of appointments.
        """
        if not os.path.exists(self.data_file):
            return {}

        with open(self.data_file, 'r') as f:
            return json.load(f)

    def save_appointments(self):
        """
        Save appointments to the data file.
        """
        with open(self.data_file, 'w') as f:
            json.dump(self.appointments, f, indent=4)

    def book_appointment(self, client_name, date, time, service):
        """
        Book a new appointment.

        :param client_name: The client's name.
        :param date: The appointment date (YYYY-MM-DD).
        :param time: The appointment time (HH:MM).
        :param service: The service(s) booked (e.g., hair, makeup).
        :return: True if the appointment was booked successfully, False otherwise.
        """
        appointment_id = len(self.appointments) + 1
        appointment_date = f"{date} {time}"

        # Check for conflicts
        for appointment in self.appointments.values():
            if appointment['date'] == appointment_date:
                print("Conflict: Appointment time already booked.")
                return False

        # Create the appointment
        self.appointments[appointment_id] = {
            'client_name': client_name,
            'date': appointment_date,
            'service': service
        }

        self.save_appointments()
        print(f"Appointment booked for {client_name} on {appointment_date} for {service}.")
        return True

    def cancel_appointment(self, appointment_id):
        """
        Cancel an existing appointment.

        :param appointment_id: The ID of the appointment to cancel.
        :return: True if the appointment was canceled successfully, False otherwise.
        """
        if appointment_id not in self.appointments:
            print("Error: Appointment not found.")
            return False

        del self.appointments[appointment_id]
        self.save_appointments()
        print(f"Appointment {appointment_id} canceled.")
        return True

    def list_appointments(self):
        """
        List all booked appointments.
        """
        if not self.appointments:
            print("No appointments booked.")
            return

        for appointment in self.appointments.values():
            print(f"Client: {appointment['client_name']}")
            print(f"Date: {appointment['date']}")
            print(f"Service: {appointment['service']}\n")


def main():
    manager = AppointmentManager()

    while True:
        print("\n1. Book Appointment")
        print("2. Cancel Appointment")
        print("3. List Appointments")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            client_name = input("Enter client name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            service = input("Enter service(s): ")
            manager.book_appointment(client_name, date, time, service)
        elif choice == '2':
            appointment_id = int(input("Enter appointment ID to cancel: "))
            manager.cancel_appointment(appointment_id)
        elif choice == '3':
            manager.list_appointments()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
```
