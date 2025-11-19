"""
Generated Code Metadata:
========================
Original URL: https://japkasai.net
Prompt: "Write a Python script to manage client appointments for a men's grooming salon like MEN'S GROOM, including features for booking, rescheduling, and canceling appointments."
Generated: DETERMINISTIC_c2a00cade6e70103
Batch ID: 20250622_205025
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

class AppointmentManager:
    def __init__(self, filename='appointments.json'):
        """
        Initialize the AppointmentManager.

        :param filename: The filename to store appointments (default: 'appointments.json')
        """
        self.filename = filename
        self.appointments = self.load_appointments()

    def load_appointments(self):
        """
        Load appointments from the JSON file.

        :return: A dictionary of appointments
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_appointments(self):
        """
        Save appointments to the JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.appointments, file, indent=4)

    def book_appointment(self, client_name, date, time, service):
        """
        Book a new appointment.

        :param client_name: The client's name
        :param date: The appointment date (YYYY-MM-DD)
        :param time: The appointment time (HH:MM)
        :param service: The service booked
        :return: True if booked successfully, False otherwise
        """
        appointment_id = len(self.appointments) + 1
        appointment = {
            'client_name': client_name,
            'date': date,
            'time': time,
            'service': service
        }

        if date in self.appointments and time in [a['time'] for a in self.appointments[date]]:
            print("Appointment time already booked for this date.")
            return False

        if date not in self.appointments:
            self.appointments[date] = []

        self.appointments[date].append(appointment)
        self.save_appointments()
        print(f"Appointment booked successfully for {client_name} on {date} at {time}.")
        return True

    def reschedule_appointment(self, client_name, old_date, old_time, new_date, new_time):
        """
        Reschedule an existing appointment.

        :param client_name: The client's name
        :param old_date: The old appointment date (YYYY-MM-DD)
        :param old_time: The old appointment time (HH:MM)
        :param new_date: The new appointment date (YYYY-MM-DD)
        :param new_time: The new appointment time (HH:MM)
        :return: True if rescheduled successfully, False otherwise
        """
        if old_date not in self.appointments:
            print("No appointments found for this date.")
            return False

        for appointment in self.appointments[old_date]:
            if appointment['client_name'] == client_name and appointment['time'] == old_time:
                appointment['date'] = new_date
                appointment['time'] = new_time

                if new_date not in self.appointments:
                    self.appointments[new_date] = []

                self.appointments[new_date].append(appointment)
                self.appointments[old_date].remove(appointment)

                if not self.appointments[old_date]:
                    del self.appointments[old_date]

                self.save_appointments()
                print(f"Appointment rescheduled successfully for {client_name} from {old_date} at {old_time} to {new_date} at {new_time}.")
                return True

        print("Appointment not found.")
        return False

    def cancel_appointment(self, client_name, date, time):
        """
        Cancel an existing appointment.

        :param client_name: The client's name
        :param date: The appointment date (YYYY-MM-DD)
        :param time: The appointment time (HH:MM)
        :return: True if canceled successfully, False otherwise
        """
        if date not in self.appointments:
            print("No appointments found for this date.")
            return False

        for appointment in self.appointments[date]:
            if appointment['client_name'] == client_name and appointment['time'] == time:
                self.appointments[date].remove(appointment)
                self.save_appointments()
                print(f"Appointment canceled successfully for {client_name} on {date} at {time}.")
                return True

        print("Appointment not found.")
        return False

    def display_appointments(self):
        """
        Display all appointments.
        """
        for date, appointments in self.appointments.items():
            print(f"Appointments on {date}:")
            for appointment in appointments:
                print(f"- {appointment['client_name']} at {appointment['time']} for {appointment['service']}")


def main():
    manager = AppointmentManager()

    while True:
        print("\nMEN'S GROOM Appointment Manager")
        print("1. Book Appointment")
        print("2. Reschedule Appointment")
        print("3. Cancel Appointment")
        print("4. Display Appointments")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            client_name = input("Enter client name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            service = input("Enter service: ")
            manager.book_appointment(client_name, date, time, service)
        elif choice == '2':
            client_name = input("Enter client name: ")
            old_date = input("Enter old date (YYYY-MM-DD): ")
            old_time = input("Enter old time (HH:MM): ")
            new_date = input("Enter new date (YYYY-MM-DD): ")
            new_time = input("Enter new time (HH:MM): ")
            manager.reschedule_appointment(client_name, old_date, old_time, new_date, new_time)
        elif choice == '3':
            client_name = input("Enter client name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            manager.cancel_appointment(client_name, date, time)
        elif choice == '4':
            manager.display_appointments()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
