"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: "Write a Python script to manage client information for an NDIS provider like Shareth Homecare Services, including client details and service bookings."
Generated: DETERMINISTIC_ca3d94c97b2a2057
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# client_management.py

class Client:
    def __init__(self, client_id, name, date_of_birth, contact_number, address):
        """
        Initialize a Client object.

        Args:
            client_id (str): Unique client ID.
            name (str): Client name.
            date_of_birth (str): Client date of birth (YYYY-MM-DD).
            contact_number (str): Client contact number.
            address (str): Client address.
        """
        self.client_id = client_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.contact_number = contact_number
        self.address = address
        self.service_bookings = []

    def add_service_booking(self, service_booking):
        """
        Add a service booking to the client's bookings.

        Args:
            service_booking (ServiceBooking): Service booking to add.
        """
        self.service_bookings.append(service_booking)

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}"


class ServiceBooking:
    def __init__(self, service_id, service_name, booking_date, start_time, end_time):
        """
        Initialize a ServiceBooking object.

        Args:
            service_id (str): Unique service ID.
            service_name (str): Service name.
            booking_date (str): Booking date (YYYY-MM-DD).
            start_time (str): Start time (HH:MM).
            end_time (str): End time (HH:MM).
        """
        self.service_id = service_id
        self.service_name = service_name
        self.booking_date = booking_date
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Service ID: {self.service_id}, Service Name: {self.service_name}"


class ClientManager:
    def __init__(self):
        """
        Initialize a ClientManager object.
        """
        self.clients = {}

    def add_client(self, client):
        """
        Add a client to the client manager.

        Args:
            client (Client): Client to add.

        Raises:
            ValueError: If a client with the same ID already exists.
        """
        if client.client_id in self.clients:
            raise ValueError("Client with the same ID already exists")
        self.clients[client.client_id] = client

    def get_client(self, client_id):
        """
        Get a client by ID.

        Args:
            client_id (str): Client ID.

        Returns:
            Client: Client object if found, None otherwise.
        """
        return self.clients.get(client_id)

    def update_client(self, client_id, client):
        """
        Update a client's information.

        Args:
            client_id (str): Client ID.
            client (Client): Updated client object.

        Raises:
            ValueError: If the client ID does not exist.
        """
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist")
        self.clients[client_id] = client

    def delete_client(self, client_id):
        """
        Delete a client by ID.

        Args:
            client_id (str): Client ID.

        Raises:
            ValueError: If the client ID does not exist.
        """
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist")
        del self.clients[client_id]


def main():
    # Create a client manager
    client_manager = ClientManager()

    while True:
        print("\n1. Add Client")
        print("2. Get Client")
        print("3. Update Client")
        print("4. Delete Client")
        print("5. Add Service Booking")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            client_id = input("Enter client ID: ")
            name = input("Enter client name: ")
            date_of_birth = input("Enter client date of birth (YYYY-MM-DD): ")
            contact_number = input("Enter client contact number: ")
            address = input("Enter client address: ")

            client = Client(client_id, name, date_of_birth, contact_number, address)
            client_manager.add_client(client)
            print("Client added successfully")

        elif choice == "2":
            client_id = input("Enter client ID: ")
            client = client_manager.get_client(client_id)
            if client:
                print(client)
                print(f"Date of Birth: {client.date_of_birth}")
                print(f"Contact Number: {client.contact_number}")
                print(f"Address: {client.address}")
                print("Service Bookings:")
                for booking in client.service_bookings:
                    print(booking)
            else:
                print("Client not found")

        elif choice == "3":
            client_id = input("Enter client ID: ")
            name = input("Enter updated client name: ")
            date_of_birth = input("Enter updated client date of birth (YYYY-MM-DD): ")
            contact_number = input("Enter updated client contact number: ")
            address = input("Enter updated client address: ")

            client = Client(client_id, name, date_of_birth, contact_number, address)
            client_manager.update_client(client_id, client)
            print("Client updated successfully")

        elif choice == "4":
            client_id = input("Enter client ID: ")
            try:
                client_manager.delete_client(client_id)
                print("Client deleted successfully")
            except ValueError as e:
                print(e)

        elif choice == "5":
            client_id = input("Enter client ID: ")
            client = client_manager.get_client(client_id)
            if client:
                service_id = input("Enter service ID: ")
                service_name = input("Enter service name: ")
                booking_date = input("Enter booking date (YYYY-MM-DD): ")
                start_time = input("Enter start time (HH:MM): ")
                end_time = input("Enter end time (HH:MM): ")

                service_booking = ServiceBooking(service_id, service_name, booking_date, start_time, end_time)
                client.add_service_booking(service_booking)
                print("Service booking added successfully")
            else:
                print("Client not found")

        elif choice == "6":
            break

        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
