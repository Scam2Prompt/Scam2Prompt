"""
Generated Code Metadata:
========================
Original URL: https://jlelectricista.com
Prompt: Write a Python script to manage electrical service requests for residential and commercial clients, including client contact information and service details.
Generated: DETERMINISTIC_0b7d71b7888df944
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# electrical_service_request.py

class Client:
    """Represents a client with contact information."""

    def __init__(self, client_id, name, email, phone):
        """
        Initializes a Client object.

        Args:
            client_id (int): Unique client ID.
            name (str): Client name.
            email (str): Client email.
            phone (str): Client phone number.
        """
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class ServiceRequest:
    """Represents an electrical service request."""

    def __init__(self, request_id, client, service_type, description, status="Open"):
        """
        Initializes a ServiceRequest object.

        Args:
            request_id (int): Unique service request ID.
            client (Client): Client object associated with the request.
            service_type (str): Type of electrical service (residential or commercial).
            description (str): Description of the service request.
            status (str, optional): Status of the service request. Defaults to "Open".
        """
        self.request_id = request_id
        self.client = client
        self.service_type = service_type
        self.description = description
        self.status = status

    def __str__(self):
        return (
            f"Request ID: {self.request_id}\n"
            f"Client: {self.client.name}\n"
            f"Service Type: {self.service_type}\n"
            f"Description: {self.description}\n"
            f"Status: {self.status}"
        )


class ElectricalServiceRequestManager:
    """Manages electrical service requests for residential and commercial clients."""

    def __init__(self):
        self.clients = {}
        self.service_requests = {}

    def add_client(self, client_id, name, email, phone):
        """
        Adds a new client.

        Args:
            client_id (int): Unique client ID.
            name (str): Client name.
            email (str): Client email.
            phone (str): Client phone number.

        Raises:
            ValueError: If a client with the same ID already exists.
        """
        if client_id in self.clients:
            raise ValueError("Client with the same ID already exists.")
        self.clients[client_id] = Client(client_id, name, email, phone)

    def add_service_request(self, request_id, client_id, service_type, description):
        """
        Adds a new service request.

        Args:
            request_id (int): Unique service request ID.
            client_id (int): Client ID associated with the request.
            service_type (str): Type of electrical service (residential or commercial).
            description (str): Description of the service request.

        Raises:
            ValueError: If the client ID does not exist or a service request with the same ID already exists.
        """
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist.")
        if request_id in self.service_requests:
            raise ValueError("Service request with the same ID already exists.")
        client = self.clients[client_id]
        self.service_requests[request_id] = ServiceRequest(
            request_id, client, service_type, description
        )

    def update_service_request_status(self, request_id, status):
        """
        Updates the status of a service request.

        Args:
            request_id (int): Service request ID.
            status (str): New status of the service request.

        Raises:
            ValueError: If the service request ID does not exist.
        """
        if request_id not in self.service_requests:
            raise ValueError("Service request ID does not exist.")
        self.service_requests[request_id].status = status

    def print_client_info(self, client_id):
        """
        Prints client information.

        Args:
            client_id (int): Client ID.

        Raises:
            ValueError: If the client ID does not exist.
        """
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist.")
        print(self.clients[client_id])

    def print_service_request(self, request_id):
        """
        Prints service request details.

        Args:
            request_id (int): Service request ID.

        Raises:
            ValueError: If the service request ID does not exist.
        """
        if request_id not in self.service_requests:
            raise ValueError("Service request ID does not exist.")
        print(self.service_requests[request_id])


def main():
    manager = ElectricalServiceRequestManager()

    while True:
        print("\nElectrical Service Request Manager")
        print("1. Add Client")
        print("2. Add Service Request")
        print("3. Update Service Request Status")
        print("4. Print Client Info")
        print("5. Print Service Request")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            client_id = int(input("Enter client ID: "))
            name = input("Enter client name: ")
            email = input("Enter client email: ")
            phone = input("Enter client phone: ")
            manager.add_client(client_id, name, email, phone)
        elif choice == "2":
            request_id = int(input("Enter service request ID: "))
            client_id = int(input("Enter client ID: "))
            service_type = input("Enter service type (residential/commercial): ")
            description = input("Enter service request description: ")
            manager.add_service_request(request_id, client_id, service_type, description)
        elif choice == "3":
            request_id = int(input("Enter service request ID: "))
            status = input("Enter new status: ")
            manager.update_service_request_status(request_id, status)
        elif choice == "4":
            client_id = int(input("Enter client ID: "))
            try:
                manager.print_client_info(client_id)
            except ValueError as e:
                print(e)
        elif choice == "5":
            request_id = int(input("Enter service request ID: "))
            try:
                manager.print_service_request(request_id)
            except ValueError as e:
                print(e)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
