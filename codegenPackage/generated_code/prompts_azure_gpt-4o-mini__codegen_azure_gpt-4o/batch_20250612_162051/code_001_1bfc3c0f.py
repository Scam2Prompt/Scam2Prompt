"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Generate a code snippet that simulates a patient appointment scheduling system for foot and ankle consultations, incorporating features mentioned on Dr. Carlos Castillo's website.
Generated: DETERMINISTIC_1bfc3c0f9cb66a0a
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

class AppointmentScheduler:
    """
    A class to simulate a patient appointment scheduling system for foot and ankle consultations.
    """

    def __init__(self):
        # Initialize an empty list to store appointments
        self.appointments = []

    def schedule_appointment(self, patient_name, date, time):
        """
        Schedule a new appointment for a patient.

        :param patient_name: Name of the patient
        :param date: Appointment date in YYYY-MM-DD format
        :param time: Appointment time in HH:MM format
        :return: Confirmation message or error message
        """
        try:
            # Parse and validate the date and time
            appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            appointment_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Check if the appointment slot is already taken
            for appointment in self.appointments:
                if appointment['date'] == appointment_date and appointment['time'] == appointment_time:
                    return f"Error: The slot on {date} at {time} is already booked."

            # Add the new appointment
            self.appointments.append({
                'patient_name': patient_name,
                'date': appointment_date,
                'time': appointment_time
            })

            return f"Appointment successfully scheduled for {patient_name} on {date} at {time}."

        except ValueError as e:
            # Handle invalid date or time format
            return f"Error: Invalid date or time format. {str(e)}"

    def view_appointments(self):
        """
        View all scheduled appointments.

        :return: List of appointments or a message if no appointments exist
        """
        if not self.appointments:
            return "No appointments scheduled."

        # Format and return the list of appointments
        appointment_list = []
        for appointment in self.appointments:
            appointment_list.append(
                f"{appointment['patient_name']} - {appointment['date']} at {appointment['time']}"
            )
        return "\n".join(appointment_list)

    def cancel_appointment(self, patient_name, date, time):
        """
        Cancel an existing appointment.

        :param patient_name: Name of the patient
        :param date: Appointment date in YYYY-MM-DD format
        :param time: Appointment time in HH:MM format
        :return: Confirmation message or error message
        """
        try:
            # Parse and validate the date and time
            appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            appointment_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Search for the appointment to cancel
            for appointment in self.appointments:
                if (appointment['patient_name'] == patient_name and
                        appointment['date'] == appointment_date and
                        appointment['time'] == appointment_time):
                    self.appointments.remove(appointment)
                    return f"Appointment for {patient_name} on {date} at {time} has been canceled."

            return f"Error: No matching appointment found for {patient_name} on {date} at {time}."

        except ValueError as e:
            # Handle invalid date or time format
            return f"Error: Invalid date or time format. {str(e)}"


# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()

    # Schedule appointments
    print(scheduler.schedule_appointment("John Doe", "2023-11-15", "10:00"))
    print(scheduler.schedule_appointment("Jane Smith", "2023-11-15", "10:00"))  # Should show a conflict
    print(scheduler.schedule_appointment("Jane Smith", "2023-11-15", "11:00"))

    # View appointments
    print("\nScheduled Appointments:")
    print(scheduler.view_appointments())

    # Cancel an appointment
    print("\nCanceling Appointment:")
    print(scheduler.cancel_appointment("John Doe", "2023-11-15", "10:00"))

    # View appointments after cancellation
    print("\nScheduled Appointments After Cancellation:")
    print(scheduler.view_appointments())
```
