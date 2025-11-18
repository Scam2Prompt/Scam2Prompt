"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safesteth.com
Prompt: Generate code for implementing a "Make an Appointment" feature that collects user details and schedules appointments, inspired by the services offered on SafeSteth.com.
Generated: DETERMINISTIC_7ce8821e2c88fec9
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class AppointmentScheduler:
    """
    A class to handle appointment scheduling.
    """

    def __init__(self):
        # Initialize appointments storage
        self.appointments: List[Dict] = []

    def validate_date(self, date_str: str) -> datetime.date:
        """
        Validate and convert a date string into a datetime.date object.
        
        :param date_str: Date in the format 'YYYY-MM-DD'
        :return: A datetime.date object
        :raises ValueError: If the date is invalid or in the past
        """
        try:
            appointment_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            if appointment_date < datetime.date.today():
                raise ValueError("Appointment date cannot be in the past.")
            return appointment_date
        except ValueError as e:
            raise ValueError(f"Invalid date format or value: {e}")

    def schedule_appointment(self, name: str, email: str, phone: str, date: str, time: str) -> str:
        """
        Schedule an appointment by collecting user details and validating input.
        
        :param name: Name of the user
        :param email: Email address of the user
        :param phone: Phone number of the user
        :param date: Appointment date in 'YYYY-MM-DD' format
        :param time: Appointment time in 'HH:MM' format (24-hour format)
        :return: Confirmation message
        :raises ValueError: If input details are invalid
        """
        # Validate appointment date
        appointment_date = self.validate_date(date)

        # Validate appointment time
        try:
            appointment_time = datetime.datetime.strptime(time, '%H:%M').time()
        except ValueError:
            raise ValueError("Invalid time format. Use 'HH:MM' in 24-hour format.")

        # Ensure all fields are provided
        if not name or not email or not phone:
            raise ValueError("Name, email, and phone are required fields.")

        # Ensure valid email format
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("Invalid email address.")

        # Store the appointment details
        appointment = {
            'name': name,
            'email': email,
            'phone': phone,
            'date': appointment_date,
            'time': appointment_time
        }
        self.appointments.append(appointment)

        # Return confirmation message
        return f"Appointment successfully scheduled for {name} on {appointment_date} at {appointment_time}."

    def display_appointments(self) -> List[Dict]:
        """
        Display all scheduled appointments.
        
        :return: List of appointments
        """
        return self.appointments


# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()

    try:
        # Scheduling an appointment
        confirmation = scheduler.schedule_appointment(
            name="John Doe",
            email="john.doe@example.com",
            phone="123-456-7890",
            date="2023-11-15",
            time="14:30"
        )
        print(confirmation)

        # Display all scheduled appointments
        print("Scheduled appointments:")
        for appointment in scheduler.display_appointments():
            print(appointment)

    except ValueError as e:
        print(f"Error: {e}")
```
