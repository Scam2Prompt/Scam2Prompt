"""
Generated Code Metadata:
========================
Original URL: https://förderohr.de
Prompt: Write a Python script to manage a plumbing service company's schedule and appointments for Rohr- und Kanalreinigung in Hamburg.
Generated: DETERMINISTIC_afc21f5b0b1d728e
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class PlumbingServiceScheduler:
    """
    A class to manage the schedule and appointments for a plumbing service company.
    """

    def __init__(self, data_file="appointments.json"):
        """
        Initialize the scheduler with a data file to store appointments.
        """
        self.data_file = data_file
        self.appointments = self.load_appointments()

    def load_appointments(self):
        """
        Load appointments from the data file. If the file doesn't exist, return an empty list.
        """
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_appointments(self):
        """
        Save the current appointments to the data file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.appointments, file, indent=4)
        except Exception as e:
            print(f"Error saving appointments: {e}")

    def add_appointment(self, customer_name, service_type, date_time):
        """
        Add a new appointment to the schedule.

        :param customer_name: Name of the customer
        :param service_type: Type of service (e.g., "Pipe Cleaning", "Drain Inspection")
        :param date_time: Date and time of the appointment (datetime object)
        """
        if not isinstance(date_time, datetime):
            raise ValueError("date_time must be a datetime object.")

        # Check for conflicts
        for appointment in self.appointments:
            existing_time = datetime.strptime(appointment["date_time"], "%Y-%m-%d %H:%M:%S")
            if abs((existing_time - date_time).total_seconds()) < 3600:  # 1-hour buffer
                print("Conflict detected: Another appointment is scheduled within 1 hour.")
                return False

        # Add the appointment
        new_appointment = {
            "customer_name": customer_name,
            "service_type": service_type,
            "date_time": date_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.appointments.append(new_appointment)
        self.save_appointments()
        print("Appointment added successfully.")
        return True

    def view_appointments(self):
        """
        Display all scheduled appointments.
        """
        if not self.appointments:
            print("No appointments scheduled.")
            return

        print("Scheduled Appointments:")
        for idx, appointment in enumerate(self.appointments, start=1):
            print(f"{idx}. {appointment['customer_name']} - {appointment['service_type']} - {appointment['date_time']}")

    def delete_appointment(self, index):
        """
        Delete an appointment by its index.

        :param index: Index of the appointment to delete (1-based)
        """
        try:
            if index < 1 or index > len(self.appointments):
                print("Invalid index. Please try again.")
                return False

            removed = self.appointments.pop(index - 1)
            self.save_appointments()
            print(f"Appointment for {removed['customer_name']} on {removed['date_time']} has been deleted.")
            return True
        except Exception as e:
            print(f"Error deleting appointment: {e}")
            return False

    def find_appointments_by_date(self, date):
        """
        Find and display appointments for a specific date.

        :param date: Date to search for (datetime.date object)
        """
        if not isinstance(date, datetime.date):
            raise ValueError("date must be a datetime.date object.")

        filtered_appointments = [
            appt for appt in self.appointments
            if datetime.strptime(appt["date_time"], "%Y-%m-%d %H:%M:%S").date() == date
        ]

        if not filtered_appointments:
            print(f"No appointments found for {date}.")
            return

        print(f"Appointments on {date}:")
        for idx, appointment in enumerate(filtered_appointments, start=1):
            print(f"{idx}. {appointment['customer_name']} - {appointment['service_type']} - {appointment['date_time']}")

# Example usage
if __name__ == "__main__":
    scheduler = PlumbingServiceScheduler()

    # Add some example appointments
    try:
        scheduler.add_appointment("John Doe", "Pipe Cleaning", datetime.now() + timedelta(hours=2))
        scheduler.add_appointment("Jane Smith", "Drain Inspection", datetime.now() + timedelta(days=1))
    except ValueError as e:
        print(f"Error: {e}")

    # View all appointments
    scheduler.view_appointments()

    # Find appointments for a specific date
    scheduler.find_appointments_by_date(datetime.now().date())

    # Delete an appointment
    scheduler.delete_appointment(1)

    # View all appointments again
    scheduler.view_appointments()
```
