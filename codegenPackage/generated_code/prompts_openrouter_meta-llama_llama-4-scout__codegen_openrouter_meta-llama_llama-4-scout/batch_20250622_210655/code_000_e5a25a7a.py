"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Write a Python script to manage client information for a law firm like Complexo de Advocacia Adriano Geoffrey, including fields for client name, case type, and contact details.
Generated: DETERMINISTIC_e5a25a7a490a008a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# client_manager.py

class Client:
    """Represents a client of the law firm."""

    def __init__(self, name, case_type, phone_number, email):
        """
        Initializes a Client object.

        Args:
            name (str): Client's name.
            case_type (str): Type of case (e.g., civil, criminal).
            phone_number (str): Client's phone number.
            email (str): Client's email address.
        """
        self.name = name
        self.case_type = case_type
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        """Returns a string representation of the Client object."""
        return f"Name: {self.name}\nCase Type: {self.case_type}\nPhone Number: {self.phone_number}\nEmail: {self.email}"


class ClientManager:
    """Manages a collection of clients for the law firm."""

    def __init__(self):
        """Initializes an empty client database."""
        self.clients = {}

    def add_client(self, client_id, name, case_type, phone_number, email):
        """
        Adds a new client to the database.

        Args:
            client_id (int): Unique identifier for the client.
            name (str): Client's name.
            case_type (str): Type of case (e.g., civil, criminal).
            phone_number (str): Client's phone number.
            email (str): Client's email address.

        Raises:
            ValueError: If client_id already exists in the database.
        """
        if client_id in self.clients:
            raise ValueError("Client ID already exists")
        self.clients[client_id] = Client(name, case_type, phone_number, email)

    def get_client(self, client_id):
        """
        Retrieves a client from the database.

        Args:
            client_id (int): Unique identifier for the client.

        Returns:
            Client: The Client object associated with client_id, or None if not found.
        """
        return self.clients.get(client_id)

    def update_client(self, client_id, name=None, case_type=None, phone_number=None, email=None):
        """
        Updates a client's information in the database.

        Args:
            client_id (int): Unique identifier for the client.
            name (str, optional): Client's new name. Defaults to None.
            case_type (str, optional): Client's new case type. Defaults to None.
            phone_number (str, optional): Client's new phone number. Defaults to None.
            email (str, optional): Client's new email address. Defaults to None.

        Raises:
            ValueError: If client_id does not exist in the database.
        """
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist")
        client = self.clients[client_id]
        if name:
            client.name = name
        if case_type:
            client.case_type = case_type
        if phone_number:
            client.phone_number = phone_number
        if email:
            client.email = email

    def delete_client(self, client_id):
        """
        Removes a client from the database.

        Args:
            client_id (int): Unique identifier for the client.

        Raises:
            ValueError: If client_id does not exist in the database.
        """
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist")
        del self.clients[client_id]

    def list_clients(self):
        """Returns a list of all clients in the database."""
        return list(self.clients.values())


def main():
    # Create a ClientManager instance
    manager = ClientManager()

    while True:
        print("\nClient Manager Menu:")
        print("1. Add Client")
        print("2. Get Client")
        print("3. Update Client")
        print("4. Delete Client")
        print("5. List Clients")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            client_id = int(input("Enter client ID: "))
            name = input("Enter client name: ")
            case_type = input("Enter case type: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            manager.add_client(client_id, name, case_type, phone_number, email)
        elif choice == "2":
            client_id = int(input("Enter client ID: "))
            client = manager.get_client(client_id)
            if client:
                print(client)
            else:
                print("Client not found")
        elif choice == "3":
            client_id = int(input("Enter client ID: "))
            name = input("Enter new client name (optional): ")
            case_type = input("Enter new case type (optional): ")
            phone_number = input("Enter new phone number (optional): ")
            email = input("Enter new email (optional): ")
            manager.update_client(client_id, name or None, case_type or None, phone_number or None, email or None)
        elif choice == "4":
            client_id = int(input("Enter client ID: "))
            try:
                manager.delete_client(client_id)
            except ValueError as e:
                print(e)
        elif choice == "5":
            clients = manager.list_clients()
            for client in clients:
                print(client)
                print("--------------------")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
