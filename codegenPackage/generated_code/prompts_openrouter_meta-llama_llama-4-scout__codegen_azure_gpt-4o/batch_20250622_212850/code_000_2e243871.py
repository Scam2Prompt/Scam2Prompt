"""
Generated Code Metadata:
========================
Original URL: https://rahelesadeghi.ir
Prompt: Write a Python script to manage client information for a family counseling service, including client contact details and appointment scheduling.
Generated: DETERMINISTIC_2e24387147ac49e6
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class FamilyCounselingService:
    def __init__(self, data_file="clients.json"):
        """
        Initialize the FamilyCounselingService with a data file to store client information.
        """
        self.data_file = data_file
        self.clients = self.load_data()

    def load_data(self):
        """
        Load client data from the JSON file. If the file doesn't exist, initialize an empty dictionary.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        """
        Save client data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.clients, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_client(self, client_id, name, contact_details):
        """
        Add a new client to the system.
        :param client_id: Unique identifier for the client
        :param name: Name of the client
        :param contact_details: Contact details (e.g., phone, email) of the client
        """
        if client_id in self.clients:
            print("Client ID already exists. Please use a unique ID.")
            return

        self.clients[client_id] = {
            "name": name,
            "contact_details": contact_details,
            "appointments": []
        }
        self.save_data()
        print(f"Client {name} added successfully.")

    def schedule_appointment(self, client_id, date, time, counselor_name):
        """
        Schedule an appointment for a client.
        :param client_id: Unique identifier for the client
        :param date: Appointment date (YYYY-MM-DD)
        :param time: Appointment time (HH:MM)
        :param counselor_name: Name of the counselor
        """
        if client_id not in self.clients:
            print("Client ID not found. Please add the client first.")
            return

        try:
            # Validate date and time format
            appointment_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
            return

        appointment = {
            "date": date,
            "time": time,
            "counselor_name": counselor_name
        }
        self.clients[client_id]["appointments"].append(appointment)
        self.save_data()
        print(f"Appointment scheduled for {self.clients[client_id]['name']} on {date} at {time} with {counselor_name}.")

    def view_client_info(self, client_id):
        """
        View information for a specific client.
        :param client_id: Unique identifier for the client
        """
        if client_id not in self.clients:
            print("Client ID not found.")
            return

        client_info = self.clients[client_id]
        print(f"Client ID: {client_id}")
        print(f"Name: {client_info['name']}")
        print(f"Contact Details: {client_info['contact_details']}")
        print("Appointments:")
        for appointment in client_info["appointments"]:
            print(f"  - Date: {appointment['date']}, Time: {appointment['time']}, Counselor: {appointment['counselor_name']}")

    def delete_client(self, client_id):
        """
        Delete a client from the system.
        :param client_id: Unique identifier for the client
        """
        if client_id not in self.clients:
            print("Client ID not found.")
            return

        del self.clients[client_id]
        self.save_data()
        print(f"Client {client_id} deleted successfully.")

# Example usage
if __name__ == "__main__":
    service = FamilyCounselingService()

    # Add a new client
    service.add_client("001", "John Doe", {"phone": "123-456-7890", "email": "john.doe@example.com"})

    # Schedule an appointment
    service.schedule_appointment("001", "2023-10-15", "14:00", "Dr. Smith")

    # View client information
    service.view_client_info("001")

    # Delete a client
    service.delete_client("001")
```
