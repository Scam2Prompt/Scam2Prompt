"""
Generated Code Metadata:
========================
Original URL: https://getupenergy.co.uk
Prompt: Write a Python code snippet to manage client appointments for a massage therapy clinic, including features to track client information and appointment scheduling.
Generated: DETERMINISTIC_bcfc9f4a35bd8f4e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Client:
    """
    Represents a client in the massage therapy clinic.
    """
    def __init__(self, client_id, name, phone, email):
        self.client_id = client_id
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class Appointment:
    """
    Represents an appointment for a client.
    """
    def __init__(self, appointment_id, client, date_time, service_type):
        self.appointment_id = appointment_id
        self.client = client
        self.date_time = date_time
        self.service_type = service_type

    def __str__(self):
        return (f"Appointment ID: {self.appointment_id}, Client: {self.client.name}, "
                f"Date & Time: {self.date_time}, Service: {self.service_type}")


class MassageTherapyClinic:
    """
    Manages clients and appointments for the massage therapy clinic.
    """
    def __init__(self):
        self.clients = {}  # Dictionary to store clients by client_id
        self.appointments = {}  # Dictionary to store appointments by appointment_id

    def add_client(self, client_id, name, phone, email):
        """
        Adds a new client to the clinic.
        """
        if client_id in self.clients:
            raise ValueError(f"Client ID {client_id} already exists.")
        self.clients[client_id] = Client(client_id, name, phone, email)

    def schedule_appointment(self, appointment_id, client_id, date_time, service_type):
        """
        Schedules a new appointment for a client.
        """
        if appointment_id in self.appointments:
            raise ValueError(f"Appointment ID {appointment_id} already exists.")
        if client_id not in self.clients:
            raise ValueError(f"Client ID {client_id} does not exist.")
        if not isinstance(date_time, datetime.datetime):
            raise ValueError("date_time must be a datetime object.")
        self.appointments[appointment_id] = Appointment(
            appointment_id, self.clients[client_id], date_time, service_type
        )

    def get_client_info(self, client_id):
        """
        Retrieves information about a client.
        """
        if client_id not in self.clients:
            raise ValueError(f"Client ID {client_id} does not exist.")
        return str(self.clients[client_id])

    def get_appointment_info(self, appointment_id):
        """
        Retrieves information about an appointment.
        """
        if appointment_id not in self.appointments:
            raise ValueError(f"Appointment ID {appointment_id} does not exist.")
        return str(self.appointments[appointment_id])

    def list_appointments(self):
        """
        Lists all scheduled appointments.
        """
        return [str(appointment) for appointment in self.appointments.values()]


# Example usage:
if __name__ == "__main__":
    clinic = MassageTherapyClinic()

    # Add clients
    clinic.add_client(1, "John Doe", "123-456-7890", "john.doe@example.com")
    clinic.add_client(2, "Jane Smith", "987-654-3210", "jane.smith@example.com")

    # Schedule appointments
    clinic.schedule_appointment(101, 1, datetime.datetime(2023, 11, 1, 10, 0), "Deep Tissue Massage")
    clinic.schedule_appointment(102, 2, datetime.datetime(2023, 11, 2, 14, 0), "Swedish Massage")

    # Retrieve client info
    print(clinic.get_client_info(1))

    # Retrieve appointment info
    print(clinic.get_appointment_info(101))

    # List all appointments
    print("\nAll Appointments:")
    for appointment in clinic.list_appointments():
        print(appointment)
```
