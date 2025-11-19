"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.institute
Prompt: How can I implement a scheduling system for executive coaching appointments that prioritizes privacy and flexibility for high-level clients?
Generated: DETERMINISTIC_8a7ca41e8a0fb00f
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import uuid

class AppointmentScheduler:
    """
    A scheduling system for executive coaching appointments
    that prioritizes privacy and flexibility for high-level clients.
    """

    def __init__(self):
        # Dictionary holding all appointments. The key is the appointment ID, and the value is appointment details.
        self.appointments = {}

    def create_appointment(self, client_name, start_time, end_time):
        """
        Creates a new appointment.
        :param client_name: Name of the client (string)
        :param start_time: Appointment start time (datetime object)
        :param end_time: Appointment end time (datetime object)
        :return: Appointment ID (string)
        """
        if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
            raise ValueError("start_time and end_time must be datetime objects.")

        if start_time >= end_time:
            raise ValueError("start_time must be earlier than end_time.")

        # Generate a unique appointment ID for privacy
        appointment_id = str(uuid.uuid4())

        # Save appointment details
        self.appointments[appointment_id] = {
            "client_name": client_name,
            "start_time": start_time,
            "end_time": end_time,
        }

        return appointment_id

    def get_appointment(self, appointment_id):
        """
        Retrieves an appointment by ID.
        :param appointment_id: The unique ID of the appointment (string)
        :return: Appointment details (dictionary)
        """
        appointment = self.appointments.get(appointment_id)
        if appointment is None:
            raise ValueError("Appointment not found.")
        return appointment

    def update_appointment(self, appointment_id, start_time=None, end_time=None):
        """
        Updates an existing appointment.
        :param appointment_id: The unique ID of the appointment (string)
        :param start_time: New appointment start time (datetime object, optional)
        :param end_time: New appointment end time (datetime object, optional)
        :return: Updated appointment details (dictionary)
        """
        if appointment_id not in self.appointments:
            raise ValueError("Appointment not found.")

        if start_time and not isinstance(start_time, datetime):
            raise ValueError("start_time must be a datetime object.")

        if end_time and not isinstance(end_time, datetime):
            raise ValueError("end_time must be a datetime object.")

        if start_time and end_time and start_time >= end_time:
            raise ValueError("start_time must be earlier than end_time.")

        # Update appointment details
        appointment = self.appointments[appointment_id]
        if start_time:
            appointment["start_time"] = start_time
        if end_time:
            appointment["end_time"] = end_time

        return appointment

    def delete_appointment(self, appointment_id):
        """
        Deletes an appointment by ID.
        :param appointment_id: The unique ID of the appointment (string)
        :return: None
        """
        if appointment_id not in self.appointments:
            raise ValueError("Appointment not found.")
        del self.appointments[appointment_id]

    def list_appointments(self):
        """
        Lists all scheduled appointments.
        :return: List of all appointments (list of dictionaries)
        """
        return list(self.appointments.values())


# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()

    try:
        # Create an appointment
        appointment_id = scheduler.create_appointment(
            client_name="John Doe",
            start_time=datetime.now() + timedelta(hours=1),
            end_time=datetime.now() + timedelta(hours=2),
        )
        print(f"Appointment created with ID: {appointment_id}")

        # Retrieve appointment details
        appointment = scheduler.get_appointment(appointment_id)
        print("Appointment details:", appointment)

        # Update the appointment
        updated_appointment = scheduler.update_appointment(
            appointment_id, end_time=datetime.now() + timedelta(hours=3)
        )
        print("Updated appointment details:", updated_appointment)

        # List all appointments
        print("All appointments:", scheduler.list_appointments())

        # Delete the appointment
        scheduler.delete_appointment(appointment_id)
        print("Appointment deleted.")

        # List all appointments after deletion
        print("All appointments after deletion:", scheduler.list_appointments())

    except ValueError as e:
        print(f"Error: {e}")
```
