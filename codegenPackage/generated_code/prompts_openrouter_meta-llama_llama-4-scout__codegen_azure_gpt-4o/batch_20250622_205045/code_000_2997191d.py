"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Write a Python script to manage client information for a small business that offers immigration services, tax preparation, and accounting, including fields for client name, contact information, and services needed.
Generated: DETERMINISTIC_2997191d3704275f
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class ClientManager:
    """
    A class to manage client information for a small business offering immigration services,
    tax preparation, and accounting.
    """

    def __init__(self, data_file="clients.json"):
        """
        Initialize the ClientManager with a data file to store client information.
        :param data_file: Path to the JSON file where client data will be stored.
        """
        self.data_file = data_file
        self.clients = self._load_data()

    def _load_data(self):
        """
        Load client data from the JSON file. If the file does not exist, return an empty list.
        :return: List of client data.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading client data. Starting with an empty list.")
                return []
        return []

    def _save_data(self):
        """
        Save client data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.clients, file, indent=4)
        except IOError as e:
            print(f"Error saving client data: {e}")

    def add_client(self, name, contact_info, services_needed):
        """
        Add a new client to the system.
        :param name: Client's name.
        :param contact_info: Client's contact information (e.g., phone, email).
        :param services_needed: List of services the client needs.
        """
        client = {
            "name": name,
            "contact_info": contact_info,
            "services_needed": services_needed
        }
        self.clients.append(client)
        self._save_data()
        print(f"Client '{name}' added successfully.")

    def list_clients(self):
        """
        List all clients in the system.
        """
        if not self.clients:
            print("No clients found.")
            return
        for idx, client in enumerate(self.clients, start=1):
            print(f"{idx}. Name: {client['name']}, Contact: {client['contact_info']}, Services: {', '.join(client['services_needed'])}")

    def search_client(self, name):
        """
        Search for a client by name.
        :param name: Name of the client to search for.
        """
        results = [client for client in self.clients if client['name'].lower() == name.lower()]
        if results:
            for client in results:
                print(f"Found: Name: {client['name']}, Contact: {client['contact_info']}, Services: {', '.join(client['services_needed'])}")
        else:
            print(f"No client found with the name '{name}'.")

    def delete_client(self, name):
        """
        Delete a client by name.
        :param name: Name of the client to delete.
        """
        initial_count = len(self.clients)
        self.clients = [client for client in self.clients if client['name'].lower() != name.lower()]
        if len(self.clients) < initial_count:
            self._save_data()
            print(f"Client '{name}' deleted successfully.")
        else:
            print(f"No client found with the name '{name}'.")

# Main script
if __name__ == "__main__":
    manager = ClientManager()

    while True:
        print("\nClient Management System")
        print("1. Add Client")
        print("2. List Clients")
        print("3. Search Client")
        print("4. Delete Client")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter client name: ")
            contact_info = input("Enter client contact information: ")
            services_needed = input("Enter services needed (comma-separated): ").split(",")
            services_needed = [service.strip() for service in services_needed]
            manager.add_client(name, contact_info, services_needed)
        elif choice == "2":
            manager.list_clients()
        elif choice == "3":
            name = input("Enter client name to search: ")
            manager.search_client(name)
        elif choice == "4":
            name = input("Enter client name to delete: ")
            manager.delete_client(name)
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
