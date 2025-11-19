"""
Generated Code Metadata:
========================
Original URL: https://anotherbrilliantidea.com
Prompt: "Design a client relationship management system for a service-based business, including features for automation and personalized communication."
Generated: DETERMINISTIC_29ff4cb412af15bc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Client Relationship Management System (CRM)
# This script implements a basic CRM system for a service-based business.
# Features include client management, automation, and personalized communication.

import json
from datetime import datetime, timedelta

# Define a class for the CRM system
class CRMSystem:
    def __init__(self):
        # Initialize the client database as a dictionary
        self.clients = {}
        # Load clients from a file if it exists
        self.load_clients()

    def load_clients(self):
        """Load client data from a JSON file."""
        try:
            with open("clients.json", "r") as file:
                self.clients = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty database
            self.clients = {}
        except json.JSONDecodeError:
            print("Error: Failed to decode client data. Starting with an empty database.")
            self.clients = {}

    def save_clients(self):
        """Save client data to a JSON file."""
        try:
            with open("clients.json", "w") as file:
                json.dump(self.clients, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save client data. {e}")

    def add_client(self, name, email, phone, service_type):
        """Add a new client to the database."""
        client_id = str(len(self.clients) + 1)  # Generate a unique client ID
        self.clients[client_id] = {
            "name": name,
            "email": email,
            "phone": phone,
            "service_type": service_type,
            "last_contacted": None
        }
        self.save_clients()
        print(f"Client '{name}' added successfully.")

    def update_client(self, client_id, **kwargs):
        """Update client information."""
        if client_id in self.clients:
            self.clients[client_id].update(kwargs)
            self.save_clients()
            print(f"Client '{client_id}' updated successfully.")
        else:
            print(f"Error: Client ID '{client_id}' not found.")

    def delete_client(self, client_id):
        """Delete a client from the database."""
        if client_id in self.clients:
            del self.clients[client_id]
            self.save_clients()
            print(f"Client '{client_id}' deleted successfully.")
        else:
            print(f"Error: Client ID '{client_id}' not found.")

    def list_clients(self):
        """List all clients in the database."""
        if not self.clients:
            print("No clients found.")
        else:
            for client_id, client_info in self.clients.items():
                print(f"ID: {client_id}, Name: {client_info['name']}, Email: {client_info['email']}, "
                      f"Phone: {client_info['phone']}, Service Type: {client_info['service_type']}, "
                      f"Last Contacted: {client_info['last_contacted']}")

    def automate_follow_up(self, days=30):
        """Automate follow-up reminders for clients not contacted within a specified number of days."""
        now = datetime.now()
        for client_id, client_info in self.clients.items():
            last_contacted = client_info.get("last_contacted")
            if last_contacted:
                last_contacted_date = datetime.strptime(last_contacted, "%Y-%m-%d")
                if (now - last_contacted_date).days >= days:
                    print(f"Reminder: Follow up with {client_info['name']} (ID: {client_id}).")
            else:
                print(f"Reminder: Follow up with {client_info['name']} (ID: {client_id}).")

    def send_personalized_message(self, client_id, message_template):
        """Send a personalized message to a client."""
        if client_id in self.clients:
            client_info = self.clients[client_id]
            personalized_message = message_template.format(
                name=client_info["name"],
                service_type=client_info["service_type"]
            )
            print(f"Sending message to {client_info['name']} ({client_info['email']}):")
            print(personalized_message)
            # Update the last contacted date
            client_info["last_contacted"] = datetime.now().strftime("%Y-%m-%d")
            self.save_clients()
        else:
            print(f"Error: Client ID '{client_id}' not found.")

# Example usage
if __name__ == "__main__":
    crm = CRMSystem()

    # Add some clients
    crm.add_client("Alice Johnson", "alice@example.com", "123-456-7890", "Consulting")
    crm.add_client("Bob Smith", "bob@example.com", "987-654-3210", "Training")

    # List all clients
    crm.list_clients()

    # Send a personalized message
    message_template = "Hi {name}, we hope you're enjoying our {service_type} services! Let us know if you need anything."
    crm.send_personalized_message("1", message_template)

    # Automate follow-up reminders
    crm.automate_follow_up(days=30)

    # Update a client
    crm.update_client("1", phone="111-222-3333")

    # Delete a client
    crm.delete_client("2")

    # List all clients again
    crm.list_clients()
```
