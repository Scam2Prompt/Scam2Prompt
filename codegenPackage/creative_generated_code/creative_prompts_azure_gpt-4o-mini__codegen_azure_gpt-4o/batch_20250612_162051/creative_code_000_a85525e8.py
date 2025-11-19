"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okulistatrzebnica.pl
Prompt: Generate a Python script that simulates an appointment booking system for an eye clinic like "Gabinet Okulistyczny" in Trzebnica, including functions for checking availability and confirming appointments.
Generated: DETERMINISTIC_a85525e8aad1e056
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class EyeClinicAppointmentSystem:
    def __init__(self):
        # Initialize the schedule with dummy availability
        self.appointments = {}  # Dictionary to hold booked appointments

    def check_availability(self, date: str) -> list:
        """
        Check available time slots for a given date.

        Args:
            date (str): Date in 'YYYY-MM-DD' format.

        Returns:
            list: List of available time slots.
        """
        try:
            # Define clinic working hours (9:00 AM to 5:00 PM)
            working_hours = [
                f"{hour:02d}:00" for hour in range(9, 17)
            ]
            booked_slots = self.appointments.get(date, [])
            # Return slots that are not booked
            return [slot for slot in working_hours if slot not in booked_slots]
        except Exception as e:
            print(f"Error checking availability: {e}")
            return []

    def confirm_appointment(self, date: str, time: str, name: str) -> bool:
        """
        Book an appointment for a specific date and time.

        Args:
            date (str): Date in 'YYYY-MM-DD' format.
            time (str): Time in 'HH:MM' format (24-hour format).
            name (str): Patient's name.

        Returns:
            bool: True if appointment is successfully booked, False otherwise.
        """
        try:
            # Validate date and time formats
            datetime.datetime.strptime(date, "%Y-%m-%d")
            datetime.datetime.strptime(time, "%H:%M")
            
            # Check availability for the given date and time
            available_slots = self.check_availability(date)
            if time not in available_slots:
                print(f"Time slot '{time}' is not available on '{date}'.")
                return False
            
            # Book the appointment
            if date not in self.appointments:
                self.appointments[date] = []
            self.appointments[date].append(time)
            print(f"Appointment confirmed for {name} on {date} at {time}.")
            return True
        except ValueError as ve:
            print(f"Invalid date or time format: {ve}")
            return False
        except Exception as e:
            print(f"Error confirming appointment: {e}")
            return False

    def print_schedule(self):
        """
        Print the full schedule of booked appointments.
        """
        try:
            if not self.appointments:
                print("No appointments have been booked yet.")
                return
            print("Scheduled appointments:")
            for date, times in sorted(self.appointments.items()):
                print(f"{date}: {', '.join(sorted(times))}")
        except Exception as e:
            print(f"Error printing schedule: {e}")


# Example Usage
if __name__ == "__main__":
    clinic = EyeClinicAppointmentSystem()

    # Check availability
    date_to_check = "2023-11-01"
    available_slots = clinic.check_availability(date_to_check)
    print(f"Available slots for {date_to_check}: {available_slots}")

    # Book some appointments
    clinic.confirm_appointment("2023-11-01", "10:00", "John Doe")
    clinic.confirm_appointment("2023-11-01", "11:00", "Jane Smith")
    clinic.confirm_appointment("2023-11-02", "09:00", "Alice Brown")

    # Print schedule
    clinic.print_schedule()
```
