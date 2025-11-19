"""
Generated Code Metadata:
========================
Original URL: https://ecg-eg.net
Prompt: "Write a code for a basic client information management system for an audit firm like Experts Consulting Group in Egypt, including fields for client name, contact information, and services provided."
Generated: DETERMINISTIC_d8499d2230e40955
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# client_management_system.py

import json

class ClientManagementSystem:
    """
    A basic client information management system for an audit firm.
    Allows adding, viewing, and saving client information.
    """

    def __init__(self):
        # Initialize an empty list to store client information
        self.clients = []

    def add_client(self, name, contact_info, services_provided):
        """
        Adds a new client to the system.

        :param name: str - Name of the client
        :param contact_info: dict - Contact information (e.g., phone, email)
        :param services_provided: list - List of services provided to the client
        """
        try:
            # Validate input
            if not name or not isinstance(contact_info, dict) or not isinstance(services_provided, list):
                raise ValueError("Invalid input. Please provide valid client details.")

            # Create a client dictionary
            client = {
                "name": name,
                "contact_info": contact_info,
                "services_provided": services_provided
            }

            # Add the client to the list
            self.clients.append(client)
            print(f"Client '{name}' added successfully.")
        except Exception as e:
            print(f"Error adding client: {e}")

    def view_clients(self):
        """
        Displays all clients in the system.
        """
        if not self.clients:
            print("No clients found.")
            return

        print("Client List:")
        for idx, client in enumerate(self.clients, start=1):
            print(f"{idx}. Name: {client['name']}")
            print(f"   Contact Info: {client['contact_info']}")
            print(f"   Services Provided: {', '.join(client['services_provided'])}")
            print("-" * 40)

    def save_to_file(self, filename="clients.json"):
        """
        Saves the client information to a JSON file.

        :param filename: str - Name of the file to save the data (default: 'clients.json')
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.clients, file, indent=4)
            print(f"Client data saved to '{filename}' successfully.")
        except Exception as e:
            print(f"Error saving client data: {e}")

    def load_from_file(self, filename="clients.json"):
        """
        Loads client information from a JSON file.

        :param filename: str - Name of the file to load the data from (default: 'clients.json')
        """
        try:
            with open(filename, "r") as file:
                self.clients = json.load(file)
            print(f"Client data loaded from '{filename}' successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty client list.")
        except Exception as e:
            print(f"Error loading client data: {e}")


# Example usage
if __name__ == "__main__":
    cms = ClientManagementSystem()

    # Add clients
    cms.add_client(
        name="John Doe",
        contact_info={"phone": "123-456-7890", "email": "john.doe@example.com"},
        services_provided=["Tax Audit", "Financial Consulting"]
    )
    cms.add_client(
        name="Jane Smith",
        contact_info={"phone": "987-654-3210", "email": "jane.smith@example.com"},
        services_provided=["Risk Assessment", "Compliance Audit"]
    )

    # View clients
    cms.view_clients()

    # Save clients to file
    cms.save_to_file()

    # Load clients from file
    cms.load_from_file()
    cms.view_clients()
```
