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
import datetime

class EyeClinicBookingSystem:
    def __init__(self):
        # Initialize the system with a dictionary to store appointments
        # Key: date (YYYY-MM-DD), Value: list of time slots booked
        self.appointments = {}

    def check_availability(self, date):
        """
        Check available time slots for a given date.
        :param date: str, date in format 'YYYY-MM-DD'
        :return: list of available time slots
        """
        # Define clinic working hours (9 AM to 5 PM, every hour)
        working_hours = [f"{hour}:00" for hour in range(9, 17)]
        booked_slots = self.appointments.get(date, [])
        available_slots = [slot for slot in working_hours if slot not in booked_slots]
        return available_slots

    def book_appointment(self, date, time):
        """
        Book an appointment for a given date and time.
        :param date: str, date in format 'YYYY-MM-DD'
        :param time: str, time in format 'HH:MM'
        :return: str, confirmation message
        """
        # Validate date format
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return "Invalid date format. Please use 'YYYY-MM-DD'."

        # Validate time format
        if time not in [f"{hour}:00" for hour in range(9, 17)]:
            return "Invalid time. Please select a time between 9:00 and 16:00."

        # Check if the slot is already booked
        if date in self.appointments and time in self.appointments[date]:
            return f"Time slot {time} on {date} is already booked."

        # Book the appointment
        if date not in self.appointments:
            self.appointments[date] = []
        self.appointments[date].append(time)
        return f"Appointment confirmed for {date} at {time}."

    def display_appointments(self):
        """
        Display all booked appointments.
        :return: str, formatted list of appointments
        """
        if not self.appointments:
            return "No appointments booked."
        result = "Booked Appointments:\n"
        for date, times in sorted(self.appointments.items()):
            result += f"{date}: {', '.join(sorted(times))}\n"
        return result


# Main script
if __name__ == "__main__":
    clinic = EyeClinicBookingSystem()

    print("Welcome to the Eye Clinic Booking System!")
    while True:
        print("\nOptions:")
        print("1. Check availability")
        print("2. Book an appointment")
        print("3. View all appointments")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            available_slots = clinic.check_availability(date)
            if available_slots:
                print(f"Available time slots on {date}: {', '.join(available_slots)}")
            else:
                print(f"No available slots on {date}.")
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            time = input("Enter the time (HH:MM): ")
            confirmation = clinic.book_appointment(date, time)
            print(confirmation)
        elif choice == 3:
            print(clinic.display_appointments())
        elif choice == 4:
            print("Thank you for using the Eye Clinic Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
```
