"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Write a Python script to help schedule and manage caregiver appointments for clients receiving hourly or 24/7 care from a home care assistance agency.
Generated: DETERMINISTIC_b3070357b4339a78
Batch ID: 20250622_205634
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
    """
    A class to manage caregiver appointments for clients.
    """

    def __init__(self):
        """
        Initializes the scheduler with empty lists for caregivers, clients, and appointments.
        """
        self.caregivers = []  # List of caregivers
        self.clients = []  # List of clients
        self.appointments = []  # List of scheduled appointments

    def add_caregiver(self, name, contact_info):
        """
        Adds a caregiver to the system.

        :param name: Name of the caregiver
        :param contact_info: Contact information of the caregiver
        """
        self.caregivers.append({"name": name, "contact_info": contact_info})
        print(f"Caregiver '{name}' added successfully.")

    def add_client(self, name, care_type, contact_info):
        """
        Adds a client to the system.

        :param name: Name of the client
        :param care_type: Type of care required (e.g., 'hourly', '24/7')
        :param contact_info: Contact information of the client
        """
        self.clients.append({"name": name, "care_type": care_type, "contact_info": contact_info})
        print(f"Client '{name}' added successfully.")

    def schedule_appointment(self, caregiver_name, client_name, start_time, end_time):
        """
        Schedules an appointment between a caregiver and a client.

        :param caregiver_name: Name of the caregiver
        :param client_name: Name of the client
        :param start_time: Start time of the appointment (datetime object)
        :param end_time: End time of the appointment (datetime object)
        """
        # Validate caregiver and client existence
        caregiver = next((c for c in self.caregivers if c["name"] == caregiver_name), None)
        client = next((c for c in self.clients if c["name"] == client_name), None)

        if not caregiver:
            print(f"Error: Caregiver '{caregiver_name}' not found.")
            return
        if not client:
            print(f"Error: Client '{client_name}' not found.")
            return

        # Validate appointment times
        if start_time >= end_time:
            print("Error: Start time must be earlier than end time.")
            return

        # Schedule the appointment
        appointment = {
            "caregiver": caregiver_name,
            "client": client_name,
            "start_time": start_time,
            "end_time": end_time
        }
        self.appointments.append(appointment)
        print(f"Appointment scheduled successfully between '{caregiver_name}' and '{client_name}'.")

    def view_appointments(self):
        """
        Displays all scheduled appointments.
        """
        if not self.appointments:
            print("No appointments scheduled.")
            return

        print("Scheduled Appointments:")
        for idx, appointment in enumerate(self.appointments, start=1):
            print(f"{idx}. Caregiver: {appointment['caregiver']}, Client: {appointment['client']}, "
                  f"Start: {appointment['start_time']}, End: {appointment['end_time']}")

    def save_data(self, filename):
        """
        Saves caregivers, clients, and appointments data to a JSON file.

        :param filename: Name of the file to save data
        """
        data = {
            "caregivers": self.caregivers,
            "clients": self.clients,
            "appointments": self.appointments
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, default=str, indent=4)
            print(f"Data saved successfully to '{filename}'.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename):
        """
        Loads caregivers, clients, and appointments data from a JSON file.

        :param filename: Name of the file to load data from
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.caregivers = data.get("caregivers", [])
                self.clients = data.get("clients", [])
                self.appointments = data.get("appointments", [])
            print(f"Data loaded successfully from '{filename}'.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error loading data: {e}")


# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()

    # Add caregivers
    scheduler.add_caregiver("Alice Johnson", "alice@example.com")
    scheduler.add_caregiver("Bob Smith", "bob@example.com")

    # Add clients
    scheduler.add_client("John Doe", "hourly", "john@example.com")
    scheduler.add_client("Jane Roe", "24/7", "jane@example.com")

    # Schedule appointments
    scheduler.schedule_appointment("Alice Johnson", "John Doe", datetime.datetime(2023, 10, 1, 9, 0), datetime.datetime(2023, 10, 1, 17, 0))
    scheduler.schedule_appointment("Bob Smith", "Jane Roe", datetime.datetime(2023, 10, 2, 0, 0), datetime.datetime(2023, 10, 2, 23, 59))

    # View appointments
    scheduler.view_appointments()

    # Save data to file
    scheduler.save_data("scheduler_data.json")

    # Load data from file
    scheduler.load_data("scheduler_data.json")
```
