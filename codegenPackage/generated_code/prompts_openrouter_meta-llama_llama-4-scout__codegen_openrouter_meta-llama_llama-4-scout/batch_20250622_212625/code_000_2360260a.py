"""
Generated Code Metadata:
========================
Original URL: https://www.bronzetanning.co
Prompt: Write a Python script to manage appointments for a spa like Bronze Tanning Spa, including features for booking, canceling, and rescheduling appointments.
Generated: DETERMINISTIC_2360260a489c7f2a
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class Appointment:
    def __init__(self, customer_name, service, date_time):
        """
        Initialize an Appointment object.

        Args:
            customer_name (str): Name of the customer.
            service (str): Type of service booked.
            date_time (datetime): Date and time of the appointment.
        """
        self.customer_name = customer_name
        self.service = service
        self.date_time = date_time

class SpaAppointmentManager:
    def __init__(self):
        """
        Initialize the SpaAppointmentManager with an empty list of appointments.
        """
        self.appointments = []

    def book_appointment(self, customer_name, service, date_time):
        """
        Book a new appointment.

        Args:
            customer_name (str): Name of the customer.
            service (str): Type of service booked.
            date_time (datetime): Date and time of the appointment.

        Raises:
            ValueError: If the appointment date/time is in the past.
        """
        if date_time < datetime.now():
            raise ValueError("Appointment date/time cannot be in the past.")

        new_appointment = Appointment(customer_name, service, date_time)
        self.appointments.append(new_appointment)
        self.appointments.sort(key=lambda x: x.date_time)

    def cancel_appointment(self, customer_name, date_time):
        """
        Cancel an existing appointment.

        Args:
            customer_name (str): Name of the customer.
            date_time (datetime): Date and time of the appointment.

        Raises:
            ValueError: If no appointment is found with the given customer name and date/time.
        """
        for appointment in self.appointments:
            if appointment.customer_name == customer_name and appointment.date_time == date_time:
                self.appointments.remove(appointment)
                return
        raise ValueError("No appointment found with the given customer name and date/time.")

    def reschedule_appointment(self, customer_name, old_date_time, new_date_time):
        """
        Reschedule an existing appointment.

        Args:
            customer_name (str): Name of the customer.
            old_date_time (datetime): Old date and time of the appointment.
            new_date_time (datetime): New date and time of the appointment.

        Raises:
            ValueError: If no appointment is found with the given customer name and old date/time.
            ValueError: If the new appointment date/time is in the past.
        """
        if new_date_time < datetime.now():
            raise ValueError("New appointment date/time cannot be in the past.")

        for appointment in self.appointments:
            if appointment.customer_name == customer_name and appointment.date_time == old_date_time:
                appointment.date_time = new_date_time
                self.appointments.sort(key=lambda x: x.date_time)
                return
        raise ValueError("No appointment found with the given customer name and old date/time.")

    def print_appointments(self):
        """
        Print all appointments.
        """
        for appointment in self.appointments:
            print(f"Customer: {appointment.customer_name}, Service: {appointment.service}, Date/Time: {appointment.date_time}")


def main():
    try:
        manager = SpaAppointmentManager()

        while True:
            print("\n1. Book Appointment")
            print("2. Cancel Appointment")
            print("3. Reschedule Appointment")
            print("4. Print Appointments")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                customer_name = input("Enter customer name: ")
                service = input("Enter service: ")
                date_time_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
                date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
                manager.book_appointment(customer_name, service, date_time)
            elif choice == "2":
                customer_name = input("Enter customer name: ")
                date_time_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
                date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
                manager.cancel_appointment(customer_name, date_time)
            elif choice == "3":
                customer_name = input("Enter customer name: ")
                old_date_time_str = input("Enter old date and time (YYYY-MM-DD HH:MM): ")
                old_date_time = datetime.strptime(old_date_time_str, "%Y-%m-%d %H:%M")
                new_date_time_str = input("Enter new date and time (YYYY-MM-DD HH:MM): ")
                new_date_time = datetime.strptime(new_date_time_str, "%Y-%m-%d %H:%M")
                manager.reschedule_appointment(customer_name, old_date_time, new_date_time)
            elif choice == "4":
                manager.print_appointments()
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose a valid option.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
