"""
Generated Code Metadata:
========================
Original URL: https://vanaclochayasociados.com
Prompt: Write a Python script to manage client information for a law firm that specializes in civil, labor, and penal law, including fields for client name, case type, and contact information.
Generated: DETERMINISTIC_72e784766dbf155a
Batch ID: 20250622_210650
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
    """Represents a client with their information."""

    def __init__(self, name, case_type, phone_number, email):
        """
        Initializes a Client object.

        Args:
            name (str): Client's name.
            case_type (str): Type of case (civil, labor, or penal).
            phone_number (str): Client's phone number.
            email (str): Client's email address.

        Raises:
            ValueError: If case type is not one of civil, labor, or penal.
        """
        if case_type.lower() not in ["civil", "labor", "penal"]:
            raise ValueError("Invalid case type. Must be civil, labor, or penal.")

        self.name = name
        self.case_type = case_type.lower()
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nCase Type: {self.case_type}\nPhone Number: {self.phone_number}\nEmail: {self.email}"


class ClientManager:
    """Manages a collection of clients."""

    def __init__(self):
        self.clients = []

    def add_client(self, client):
        """
        Adds a client to the collection.

        Args:
            client (Client): Client object to add.

        Raises:
            TypeError: If client is not a Client object.
        """
        if not isinstance(client, Client):
            raise TypeError("Client must be a Client object.")

        self.clients.append(client)

    def remove_client(self, client_name):
        """
        Removes a client by name.

        Args:
            client_name (str): Name of the client to remove.

        Returns:
            bool: True if client was removed, False if not found.
        """
        self.clients = [client for client in self.clients if client.name != client_name]

    def get_clients(self, case_type=None):
        """
        Retrieves a list of clients.

        Args:
            case_type (str, optional): Filter by case type. Defaults to None.

        Returns:
            list: List of Client objects.
        """
        if case_type:
            return [client for client in self.clients if client.case_type == case_type.lower()]
        return self.clients

    def __str__(self):
        clients_str = "\n\n".join([str(client) for client in self.clients])
        return clients_str


def main():
    try:
        manager = ClientManager()

        while True:
            print("\nClient Manager Menu:")
            print("1. Add Client")
            print("2. Remove Client")
            print("3. Get Clients")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter client name: ")
                case_type = input("Enter case type (civil, labor, or penal): ")
                phone_number = input("Enter phone number: ")
                email = input("Enter email: ")

                client = Client(name, case_type, phone_number, email)
                manager.add_client(client)
                print("Client added successfully.")

            elif choice == "2":
                client_name = input("Enter client name to remove: ")
                manager.remove_client(client_name)
                print("Client removed successfully.")

            elif choice == "3":
                case_type = input("Enter case type to filter (optional): ")
                if case_type:
                    clients = manager.get_clients(case_type)
                else:
                    clients = manager.get_clients()

                if clients:
                    print("\nClients:")
                    print(manager)
                else:
                    print("No clients found.")

            elif choice == "4":
                break

            else:
                print("Invalid option. Please choose a valid option.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
