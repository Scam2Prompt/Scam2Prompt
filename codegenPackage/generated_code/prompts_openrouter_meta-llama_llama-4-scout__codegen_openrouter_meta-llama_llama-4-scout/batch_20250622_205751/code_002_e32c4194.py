"""
Generated Code Metadata:
========================
Original URL: https://juridiskklinik.se
Prompt: Generate a code snippet in Python for creating a simple appointment booking system, similar to the one used by Juridisk Klinik, which takes into account working hours and provides a confirmation message.
Generated: DETERMINISTIC_e32c4194f4c103d7
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class AppointmentBookingSystem:
    def __init__(self):
        # Initialize working hours
        self.working_hours_start = 9  # 9:00 AM
        self.working_hours_end = 17   # 5:00 PM
        self.appointments = {}

    def book_appointment(self, name, date, time):
        """
        Book an appointment.

        Args:
            name (str): Client's name
            date (str): Date of appointment (YYYY-MM-DD)
            time (str): Time of appointment (HH:MM)

        Returns:
            str: Confirmation message
        """
        try:
            # Validate date and time
            appointment_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            if appointment_datetime.weekday() >= 5:  # Check if weekend
                return "Sorry, we are not open on weekends."

            # Validate working hours
            if appointment_datetime.hour < self.working_hours_start or appointment_datetime.hour >= self.working_hours_end:
                return f"Sorry, we are not open at {time}. Our working hours are between {self.working_hours_start}:00 and {self.working_hours_end}:00."

            # Check for existing appointments
            if appointment_datetime in self.appointments:
                return "Sorry, this time slot is already taken."

            # Book appointment
            self.appointments[appointment_datetime] = name
            return f"Appointment booked successfully for {name} on {date} at {time}."
        except ValueError:
            return "Invalid date or time format. Please use YYYY-MM-DD and HH:MM."

    def cancel_appointment(self, date, time):
        """
        Cancel an appointment.

        Args:
            date (str): Date of appointment (YYYY-MM-DD)
            time (str): Time of appointment (HH:MM)

        Returns:
            str: Confirmation message
        """
        try:
            appointment_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            if appointment_datetime not in self.appointments:
                return "No appointment found at this time."

            del self.appointments[appointment_datetime]
            return f"Appointment on {date} at {time} cancelled successfully."
        except ValueError:
            return "Invalid date or time format. Please use YYYY-MM-DD and HH:MM."

    def display_appointments(self):
        """
        Display all booked appointments.

        Returns:
            str: List of appointments
        """
        appointments_list = ""
        for appointment_datetime, name in self.appointments.items():
            appointments_list += f"{name} - {appointment_datetime.strftime('%Y-%m-%d %H:%M')}\n"
        return appointments_list


def main():
    booking_system = AppointmentBookingSystem()

    while True:
        print("\n1. Book Appointment")
        print("2. Cancel Appointment")
        print("3. Display Appointments")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter your name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            print(booking_system.book_appointment(name, date, time))
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            print(booking_system.cancel_appointment(date, time))
        elif choice == "3":
            print(booking_system.display_appointments())
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
