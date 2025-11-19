"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Write a Python script to schedule and manage appointments for a mobile fuel injector cleaning service, considering different types of vehicles such as cars, LPG, hybrid, and motorbikes.
Generated: DETERMINISTIC_e78a03cb71497c3c
Batch ID: 20250622_205301
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

class AppointmentScheduler:
    def __init__(self):
        # Initialize the scheduler with an empty list of appointments
        self.appointments = []

    def add_appointment(self, customer_name, vehicle_type, date, time):
        """
        Adds a new appointment to the scheduler.

        Args:
            customer_name (str): Name of the customer.
            vehicle_type (str): Type of vehicle (e.g., car, LPG, hybrid, motorbike).
            date (str): Appointment date in YYYY-MM-DD format.
            time (str): Appointment time in HH:MM format.

        Returns:
            str: Confirmation message or error message.
        """
        try:
            # Validate date and time format
            appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            appointment_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Validate vehicle type
            valid_vehicle_types = ["car", "LPG", "hybrid", "motorbike"]
            if vehicle_type.lower() not in valid_vehicle_types:
                return f"Error: Invalid vehicle type. Valid types are: {', '.join(valid_vehicle_types)}."

            # Check for conflicts
            for appointment in self.appointments:
                if appointment["date"] == date and appointment["time"] == time:
                    return "Error: Appointment slot is already booked."

            # Add the appointment
            new_appointment = {
                "customer_name": customer_name,
                "vehicle_type": vehicle_type.lower(),
                "date": date,
                "time": time
            }
            self.appointments.append(new_appointment)
            return f"Appointment successfully scheduled for {customer_name} on {date} at {time}."
        except ValueError:
            return "Error: Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."

    def view_appointments(self):
        """
        Returns a list of all scheduled appointments.

        Returns:
            str: JSON-formatted string of appointments.
        """
        if not self.appointments:
            return "No appointments scheduled."
        return json.dumps(self.appointments, indent=4)

    def cancel_appointment(self, customer_name, date, time):
        """
        Cancels an existing appointment.

        Args:
            customer_name (str): Name of the customer.
            date (str): Appointment date in YYYY-MM-DD format.
            time (str): Appointment time in HH:MM format.

        Returns:
            str: Confirmation message or error message.
        """
        for appointment in self.appointments:
            if (
                appointment["customer_name"] == customer_name
                and appointment["date"] == date
                and appointment["time"] == time
            ):
                self.appointments.remove(appointment)
                return f"Appointment for {customer_name} on {date} at {time} has been canceled."
        return "Error: Appointment not found."

# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()

    # Add appointments
    print(scheduler.add_appointment("John Doe", "car", "2023-10-15", "10:00"))
    print(scheduler.add_appointment("Jane Smith", "motorbike", "2023-10-15", "11:00"))

    # View appointments
    print("Scheduled Appointments:")
    print(scheduler.view_appointments())

    # Cancel an appointment
    print(scheduler.cancel_appointment("John Doe", "2023-10-15", "10:00"))

    # View appointments after cancellation
    print("Scheduled Appointments After Cancellation:")
    print(scheduler.view_appointments())
```
