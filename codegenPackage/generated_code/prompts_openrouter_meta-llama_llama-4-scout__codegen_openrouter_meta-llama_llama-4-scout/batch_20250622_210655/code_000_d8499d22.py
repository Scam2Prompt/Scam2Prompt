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
# client_information_management_system.py

class Client:
    """Represents a client of the audit firm."""

    def __init__(self, client_id, name, email, phone, services=None):
        """
        Initializes a Client object.

        Args:
            client_id (int): Unique identifier for the client.
            name (str): Client name.
            email (str): Client email.
            phone (str): Client phone number.
            services (list[str], optional): Services provided to the client. Defaults to None.
        """
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone
        self.services = services if services else []

    def add_service(self, service):
        """Adds a service provided to the client."""
        self.services.append(service)

    def remove_service(self, service):
        """Removes a service provided to the client."""
        if service in self.services:
            self.services.remove(service)

    def __str__(self):
        return f"Client ID: {self.client_id}\nName: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nServices: {', '.join(self.services)}"


class ClientInformationManagementSystem:
    """Manages client information for the audit firm."""

    def __init__(self):
        """Initializes the client information management system."""
        self.clients = {}
        self.client_id_counter = 1

    def create_client(self, name, email, phone, services=None):
        """
        Creates a new client.

        Args:
            name (str): Client name.
            email (str): Client email.
            phone (str): Client phone number.
            services (list[str], optional): Services provided to the client. Defaults to None.

        Returns:
            Client: The created client.
        """
        client = Client(self.client_id_counter, name, email, phone, services)
        self.clients[self.client_id_counter] = client
        self.client_id_counter += 1
        return client

    def get_client(self, client_id):
        """
        Retrieves a client by their ID.

        Args:
            client_id (int): The ID of the client to retrieve.

        Returns:
            Client: The client with the specified ID, or None if not found.
        """
        return self.clients.get(client_id)

    def update_client(self, client_id, name=None, email=None, phone=None, services=None):
        """
        Updates a client's information.

        Args:
            client_id (int): The ID of the client to update.
            name (str, optional): New client name. Defaults to None.
            email (str, optional): New client email. Defaults to None.
            phone (str, optional): New client phone number. Defaults to None.
            services (list[str], optional): New services provided to the client. Defaults to None.

        Raises:
            ValueError: If the client ID is not found.
        """
        client = self.get_client(client_id)
        if client:
            if name:
                client.name = name
            if email:
                client.email = email
            if phone:
                client.phone = phone
            if services:
                client.services = services
        else:
            raise ValueError("Client ID not found")

    def delete_client(self, client_id):
        """
        Deletes a client.

        Args:
            client_id (int): The ID of the client to delete.

        Raises:
            ValueError: If the client ID is not found.
        """
        if client_id in self.clients:
            del self.clients[client_id]
        else:
            raise ValueError("Client ID not found")


def main():
    # Example usage
    system = ClientInformationManagementSystem()

    client1 = system.create_client("John Doe", "john.doe@example.com", "1234567890", ["Audit", "Consulting"])
    client2 = system.create_client("Jane Smith", "jane.smith@example.com", "0987654321", ["Tax", "Accounting"])

    print("Client 1:")
    print(client1)

    print("\nClient 2:")
    print(client2)

    system.update_client(client1.client_id, services=["Audit", "Consulting", "Financial Planning"])

    print("\nUpdated Client 1:")
    print(system.get_client(client1.client_id))

    system.delete_client(client2.client_id)

    try:
        system.get_client(client2.client_id)
    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
