"""
Generated Code Metadata:
========================
Original URL: https://okulistatrzebnica.pl
Prompt: Generate a Python script that simulates an appointment booking system for an eye clinic like "Gabinet Okulistyczny" in Trzebnica, including functions for checking availability and confirming appointments.
Generated: DETERMINISTIC_a85525e8aad1e056
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Appointment:
    def __init__(self, patient_name, date, time):
        """
        Initialize an Appointment object.

        Args:
            patient_name (str): Name of the patient.
            date (str): Date of the appointment in YYYY-MM-DD format.
            time (str): Time of the appointment in HH:MM format.
        """
        self.patient_name = patient_name
        self.date = date
        self.time = time

class EyeClinic:
    def __init__(self):
        """
        Initialize an EyeClinic object with an empty schedule.
        """
        self.schedule = {}

    def add_appointment(self, appointment):
        """
        Add an appointment to the schedule.

        Args:
            appointment (Appointment): Appointment object to add.

        Returns:
            bool: True if the appointment was added successfully, False otherwise.
        """
        date = appointment.date
        time = appointment.time
        if date not in self.schedule:
            self.schedule[date] = {}
        if time in self.schedule[date]:
            print(f"Appointment at {date} {time} is already booked.")
            return False
        self.schedule[date][time] = appointment.patient_name
        print(f"Appointment at {date} {time} booked for {appointment.patient_name}.")
        return True

    def check_availability(self, date, time):
        """
        Check if an appointment is available at a given date and time.

        Args:
            date (str): Date to check in YYYY-MM-DD format.
            time (str): Time to check in HH:MM format.

        Returns:
            bool: True if the appointment is available, False otherwise.
        """
        if date not in self.schedule or time not in self.schedule[date]:
            return True
        print(f"Appointment at {date} {time} is not available.")
        return False

    def confirm_appointment(self, date, time):
        """
        Confirm an appointment at a given date and time.

        Args:
            date (str): Date of the appointment in YYYY-MM-DD format.
            time (str): Time of the appointment in HH:MM format.

        Returns:
            str: Patient name if the appointment is confirmed, None otherwise.
        """
        if date in self.schedule and time in self.schedule[date]:
            return self.schedule[date][time]
        print(f"Appointment at {date} {time} does not exist.")
        return None

    def cancel_appointment(self, date, time):
        """
        Cancel an appointment at a given date and time.

        Args:
            date (str): Date of the appointment in YYYY-MM-DD format.
            time (str): Time of the appointment in HH:MM format.

        Returns:
            bool: True if the appointment was canceled successfully, False otherwise.
        """
        if date in self.schedule and time in self.schedule[date]:
            del self.schedule[date][time]
            if not self.schedule[date]:
                del self.schedule[date]
            print(f"Appointment at {date} {time} canceled.")
            return True
        print(f"Appointment at {date} {time} does not exist.")
        return False

def main():
    clinic = EyeClinic()

    while True:
        print("\n1. Book an appointment")
        print("2. Check availability")
        print("3. Confirm appointment")
        print("4. Cancel appointment")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            patient_name = input("Enter patient name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            appointment = Appointment(patient_name, date, time)
            clinic.add_appointment(appointment)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            clinic.check_availability(date, time)
        elif choice == "3":
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            patient_name = clinic.confirm_appointment(date, time)
            if patient_name:
                print(f"Appointment confirmed for {patient_name}.")
        elif choice == "4":
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            clinic.cancel_appointment(date, time)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
