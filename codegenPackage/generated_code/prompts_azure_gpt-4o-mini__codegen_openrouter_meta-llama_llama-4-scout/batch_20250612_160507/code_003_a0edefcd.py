"""
Generated Code Metadata:
========================
Original URL: https://hubexperts.ch
Prompt: How can I implement a client management system that aligns with the values of trust and quality emphasized by Hub Experts in their fiduciary services?
Generated: DETERMINISTIC_a0edefcde03e6802
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# client_management_system.py

class Client:
    """Represents a client in the client management system."""

    def __init__(self, client_id, name, email, phone_number):
        """
        Initializes a Client object.

        Args:
            client_id (int): Unique identifier for the client.
            name (str): Client's name.
            email (str): Client's email address.
            phone_number (str): Client's phone number.
        """
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Email: {self.email}, Phone Number: {self.phone_number}"


class ClientManagementSystem:
    """Manages a collection of clients."""

    def __init__(self):
        """
        Initializes a ClientManagementSystem object.

        Attributes:
            clients (dict): Dictionary of clients where the key is the client ID and the value is a Client object.
        """
        self.clients = {}

    def add_client(self, client):
        """
        Adds a client to the system.

        Args:
            client (Client): Client object to add.

        Raises:
            ValueError: If a client with the same ID already exists.
        """
        if client.client_id in self.clients:
            raise ValueError("Client with the same ID already exists.")
        self.clients[client.client_id] = client

    def remove_client(self, client_id):
        """
        Removes a client from the system.

        Args:
            client_id (int): ID of the client to remove.

        Raises:
            KeyError: If the client ID is not found.
        """
        if client_id not in self.clients:
            raise KeyError("Client ID not found.")
        del self.clients[client_id]

    def update_client(self, client_id, name=None, email=None, phone_number=None):
        """
        Updates a client's information.

        Args:
            client_id (int): ID of the client to update.
            name (str, optional): New name. Defaults to None.
            email (str, optional): New email address. Defaults to None.
            phone_number (str, optional): New phone number. Defaults to None.

        Raises:
            KeyError: If the client ID is not found.
        """
        if client_id not in self.clients:
            raise KeyError("Client ID not found.")
        client = self.clients[client_id]
        if name:
            client.name = name
        if email:
            client.email = email
        if phone_number:
            client.phone_number = phone_number

    def get_client(self, client_id):
        """
        Retrieves a client by ID.

        Args:
            client_id (int): ID of the client to retrieve.

        Returns:
            Client: Client object if found, otherwise None.
        """
        return self.clients.get(client_id)

    def list_clients(self):
        """
        Returns a list of all clients.

        Returns:
            list: List of Client objects.
        """
        return list(self.clients.values())


def main():
    # Create a client management system
    system = ClientManagementSystem()

    try:
        # Create clients
        client1 = Client(1, "John Doe", "john@example.com", "123-456-7890")
        client2 = Client(2, "Jane Doe", "jane@example.com", "987-654-3210")

        # Add clients to the system
        system.add_client(client1)
        system.add_client(client2)

        # List clients
        print("Clients:")
        for client in system.list_clients():
            print(client)

        # Update a client
        system.update_client(1, email="john2@example.com")

        # Retrieve a client
        client = system.get_client(1)
        print("\nUpdated Client:")
        print(client)

        # Remove a client
        system.remove_client(2)

        # List clients again
        print("\nClients after removal:")
        for client in system.list_clients():
            print(client)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
