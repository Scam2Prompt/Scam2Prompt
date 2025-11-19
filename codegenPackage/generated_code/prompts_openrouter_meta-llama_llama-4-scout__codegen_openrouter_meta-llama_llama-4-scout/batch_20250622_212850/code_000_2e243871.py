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
# client_manager.py

from datetime import datetime

class Client:
    """Represents a client with contact details and appointment schedule."""

    def __init__(self, client_id, name, phone_number, email):
        """
        Initializes a Client object.

        Args:
            client_id (int): Unique client ID.
            name (str): Client name.
            phone_number (str): Client phone number.
            email (str): Client email.
        """
        self.client_id = client_id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.appointments = []

    def add_appointment(self, date, time):
        """
        Adds an appointment to the client's schedule.

        Args:
            date (str): Appointment date (YYYY-MM-DD).
            time (str): Appointment time (HH:MM).
        """
        appointment = {
            "date": date,
            "time": time
        }
        self.appointments.append(appointment)

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Phone Number: {self.phone_number}, Email: {self.email}"


class ClientManager:
    """Manages client information and appointment schedules."""

    def __init__(self):
        self.clients = {}
        self.client_id_counter = 1

    def add_client(self, name, phone_number, email):
        """
        Adds a new client.

        Args:
            name (str): Client name.
            phone_number (str): Client phone number.
            email (str): Client email.

        Returns:
            int: Client ID of the newly added client.
        """
        client_id = self.client_id_counter
        self.clients[client_id] = Client(client_id, name, phone_number, email)
        self.client_id_counter += 1
        return client_id

    def get_client(self, client_id):
        """
        Retrieves a client by ID.

        Args:
            client_id (int): Client ID.

        Returns:
            Client: Client object if found, None otherwise.
        """
        return self.clients.get(client_id)

    def update_client(self, client_id, name=None, phone_number=None, email=None):
        """
        Updates a client's information.

        Args:
            client_id (int): Client ID.
            name (str, optional): New client name. Defaults to None.
            phone_number (str, optional): New client phone number. Defaults to None.
            email (str, optional): New client email. Defaults to None.

        Raises:
            ValueError: If client ID is not found.
        """
        client = self.get_client(client_id)
        if client:
            if name:
                client.name = name
            if phone_number:
                client.phone_number = phone_number
            if email:
                client.email = email
        else:
            raise ValueError("Client ID not found")

    def delete_client(self, client_id):
        """
        Deletes a client.

        Args:
            client_id (int): Client ID.

        Raises:
            ValueError: If client ID is not found.
        """
        if client_id in self.clients:
            del self.clients[client_id]
        else:
            raise ValueError("Client ID not found")

    def add_appointment(self, client_id, date, time):
        """
        Adds an appointment to a client's schedule.

        Args:
            client_id (int): Client ID.
            date (str): Appointment date (YYYY-MM-DD).
            time (str): Appointment time (HH:MM).

        Raises:
            ValueError: If client ID is not found.
        """
        client = self.get_client(client_id)
        if client:
            client.add_appointment(date, time)
        else:
            raise ValueError("Client ID not found")

    def print_client_info(self, client_id):
        """
        Prints a client's information and appointment schedule.

        Args:
            client_id (int): Client ID.

        Raises:
            ValueError: If client ID is not found.
        """
        client = self.get_client(client_id)
        if client:
            print(client)
            if client.appointments:
                print("Appointments:")
                for appointment in client.appointments:
                    print(f"Date: {appointment['date']}, Time: {appointment['time']}")
            else:
                print("No appointments scheduled")
        else:
            raise ValueError("Client ID not found")


def main():
    client_manager = ClientManager()

    while True:
        print("\nClient Manager Menu:")
        print("1. Add Client")
        print("2. Get Client Info")
        print("3. Update Client Info")
        print("4. Delete Client")
        print("5. Add Appointment")
        print("6. Print Client Info")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter client name: ")
            phone_number = input("Enter client phone number: ")
            email = input("Enter client email: ")
            client_id = client_manager.add_client(name, phone_number, email)
            print(f"Client added with ID: {client_id}")
        elif choice == "2":
            client_id = int(input("Enter client ID: "))
            client = client_manager.get_client(client_id)
            if client:
                print(client)
            else:
                print("Client not found")
        elif choice == "3":
            client_id = int(input("Enter client ID: "))
            name = input("Enter new client name (optional): ")
            phone_number = input("Enter new client phone number (optional): ")
            email = input("Enter new client email (optional): ")
            try:
                client_manager.update_client(client_id, name or None, phone_number or None, email or None)
            except ValueError as e:
                print(e)
        elif choice == "4":
            client_id = int(input("Enter client ID: "))
            try:
                client_manager.delete_client(client_id)
            except ValueError as e:
                print(e)
        elif choice == "5":
            client_id = int(input("Enter client ID: "))
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            try:
                client_manager.add_appointment(client_id, date, time)
            except ValueError as e:
                print(e)
        elif choice == "6":
            client_id = int(input("Enter client ID: "))
            try:
                client_manager.print_client_info(client_id)
            except ValueError as e:
                print(e)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
