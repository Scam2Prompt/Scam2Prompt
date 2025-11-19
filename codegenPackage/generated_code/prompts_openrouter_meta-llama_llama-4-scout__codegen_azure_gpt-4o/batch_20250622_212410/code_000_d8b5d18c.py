"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.com
Prompt: Write a Python script to manage appointment scheduling for a multidisciplinary clinic offering chiropractic care, osteopathy, and massage therapy.
Generated: DETERMINISTIC_d8b5d18c3fdb7e7e
Batch ID: 20250622_212410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class AppointmentScheduler:
    """
    A class to manage appointment scheduling for a multidisciplinary clinic.
    The clinic offers chiropractic care, osteopathy, and massage therapy.
    """

    def __init__(self):
        # Initialize an empty list to store appointments
        self.appointments = []

    def add_appointment(self, patient_name, service_type, date, time):
        """
        Adds a new appointment to the schedule.

        Args:
            patient_name (str): Name of the patient.
            service_type (str): Type of service (chiropractic, osteopathy, massage therapy).
            date (str): Appointment date in YYYY-MM-DD format.
            time (str): Appointment time in HH:MM format.

        Returns:
            str: Confirmation message or error message.
        """
        try:
            # Validate service type
            if service_type.lower() not in ['chiropractic', 'osteopathy', 'massage therapy']:
                return "Error: Invalid service type. Please choose chiropractic, osteopathy, or massage therapy."

            # Validate date and time format
            appointment_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

            # Check for conflicts
            for appointment in self.appointments:
                if appointment['datetime'] == appointment_datetime:
                    return "Error: Appointment slot is already booked."

            # Add the appointment
            self.appointments.append({
                'patient_name': patient_name,
                'service_type': service_type.lower(),
                'datetime': appointment_datetime
            })
            return f"Appointment successfully scheduled for {patient_name} on {date} at {time} for {service_type}."
        except ValueError:
            return "Error: Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."

    def view_appointments(self):
        """
        Displays all scheduled appointments.

        Returns:
            str: A formatted list of all appointments or a message if no appointments exist.
        """
        if not self.appointments:
            return "No appointments scheduled."

        # Sort appointments by date and time
        self.appointments.sort(key=lambda x: x['datetime'])

        # Format and display appointments
        result = "Scheduled Appointments:\n"
        for appointment in self.appointments:
            result += (f"Patient: {appointment['patient_name']}, "
                       f"Service: {appointment['service_type'].capitalize()}, "
                       f"Date: {appointment['datetime'].strftime('%Y-%m-%d')}, "
                       f"Time: {appointment['datetime'].strftime('%H:%M')}\n")
        return result

    def cancel_appointment(self, patient_name, date, time):
        """
        Cancels an existing appointment.

        Args:
            patient_name (str): Name of the patient.
            date (str): Appointment date in YYYY-MM-DD format.
            time (str): Appointment time in HH:MM format.

        Returns:
            str: Confirmation message or error message.
        """
        try:
            # Validate date and time format
            appointment_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

            # Find and remove the appointment
            for appointment in self.appointments:
                if appointment['patient_name'] == patient_name and appointment['datetime'] == appointment_datetime:
                    self.appointments.remove(appointment)
                    return f"Appointment for {patient_name} on {date} at {time} has been canceled."

            return "Error: Appointment not found."
        except ValueError:
            return "Error: Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."


# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()

    # Add appointments
    print(scheduler.add_appointment("John Doe", "chiropractic", "2023-10-15", "10:00"))
    print(scheduler.add_appointment("Jane Smith", "massage therapy", "2023-10-15", "11:00"))

    # View appointments
    print(scheduler.view_appointments())

    # Cancel an appointment
    print(scheduler.cancel_appointment("John Doe", "2023-10-15", "10:00"))

    # View appointments after cancellation
    print(scheduler.view_appointments())
```
