"""
Generated Code Metadata:
========================
Original URL: https://parrotrans.com
Prompt: Write a Python script to manage translation equipment rental for events, including tracking equipment availability and client information, inspired by Parrotrans' services.
Generated: DETERMINISTIC_6a64bd0c18fb6b56
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# translation_equipment_rental.py

class Equipment:
    """Represents a translation equipment."""

    def __init__(self, equipment_id, name, description):
        """
        Initializes an Equipment object.

        Args:
            equipment_id (int): Unique identifier for the equipment.
            name (str): Name of the equipment.
            description (str): Description of the equipment.
        """
        self.equipment_id = equipment_id
        self.name = name
        self.description = description
        self.is_available = True  # Initially, all equipment is available

    def __str__(self):
        return f"Equipment ID: {self.equipment_id}, Name: {self.name}, Description: {self.description}, Available: {self.is_available}"


class Client:
    """Represents a client."""

    def __init__(self, client_id, name, contact_info):
        """
        Initializes a Client object.

        Args:
            client_id (int): Unique identifier for the client.
            name (str): Name of the client.
            contact_info (str): Contact information of the client.
        """
        self.client_id = client_id
        self.name = name
        self.contact_info = contact_info

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Contact Info: {self.contact_info}"


class Rental:
    """Manages translation equipment rental for events."""

    def __init__(self):
        """
        Initializes a Rental object.
        """
        self.equipment = {}  # Maps equipment_id to Equipment objects
        self.clients = {}  # Maps client_id to Client objects
        self.rentals = {}  # Maps equipment_id to client_id

    def add_equipment(self, equipment_id, name, description):
        """
        Adds a new equipment.

        Args:
            equipment_id (int): Unique identifier for the equipment.
            name (str): Name of the equipment.
            description (str): Description of the equipment.

        Raises:
            ValueError: If equipment_id already exists.
        """
        if equipment_id in self.equipment:
            raise ValueError("Equipment ID already exists")
        self.equipment[equipment_id] = Equipment(equipment_id, name, description)

    def add_client(self, client_id, name, contact_info):
        """
        Adds a new client.

        Args:
            client_id (int): Unique identifier for the client.
            name (str): Name of the client.
            contact_info (str): Contact information of the client.

        Raises:
            ValueError: If client_id already exists.
        """
        if client_id in self.clients:
            raise ValueError("Client ID already exists")
        self.clients[client_id] = Client(client_id, name, contact_info)

    def rent_equipment(self, equipment_id, client_id):
        """
        Rents equipment to a client.

        Args:
            equipment_id (int): Unique identifier for the equipment.
            client_id (int): Unique identifier for the client.

        Raises:
            ValueError: If equipment_id or client_id does not exist.
            ValueError: If equipment is not available.
        """
        if equipment_id not in self.equipment:
            raise ValueError("Equipment ID does not exist")
        if client_id not in self.clients:
            raise ValueError("Client ID does not exist")
        if not self.equipment[equipment_id].is_available:
            raise ValueError("Equipment is not available")
        self.equipment[equipment_id].is_available = False
        self.rentals[equipment_id] = client_id

    def return_equipment(self, equipment_id):
        """
        Returns rented equipment.

        Args:
            equipment_id (int): Unique identifier for the equipment.

        Raises:
            ValueError: If equipment_id does not exist.
            ValueError: If equipment is not rented.
        """
        if equipment_id not in self.equipment:
            raise ValueError("Equipment ID does not exist")
        if equipment_id not in self.rentals:
            raise ValueError("Equipment is not rented")
        self.equipment[equipment_id].is_available = True
        del self.rentals[equipment_id]

    def print_equipment(self):
        """Prints all equipment information."""
        for equipment in self.equipment.values():
            print(equipment)

    def print_clients(self):
        """Prints all client information."""
        for client in self.clients.values():
            print(client)

    def print_rentals(self):
        """Prints all rentals information."""
        for equipment_id, client_id in self.rentals.items():
            print(f"Equipment ID: {equipment_id}, Client ID: {client_id}")


def main():
    rental = Rental()

    while True:
        print("\nTranslation Equipment Rental Management")
        print("1. Add Equipment")
        print("2. Add Client")
        print("3. Rent Equipment")
        print("4. Return Equipment")
        print("5. Print Equipment")
        print("6. Print Clients")
        print("7. Print Rentals")
        print("8. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                equipment_id = int(input("Enter equipment ID: "))
                name = input("Enter equipment name: ")
                description = input("Enter equipment description: ")
                rental.add_equipment(equipment_id, name, description)
            elif choice == "2":
                client_id = int(input("Enter client ID: "))
                name = input("Enter client name: ")
                contact_info = input("Enter client contact info: ")
                rental.add_client(client_id, name, contact_info)
            elif choice == "3":
                equipment_id = int(input("Enter equipment ID: "))
                client_id = int(input("Enter client ID: "))
                rental.rent_equipment(equipment_id, client_id)
            elif choice == "4":
                equipment_id = int(input("Enter equipment ID: "))
                rental.return_equipment(equipment_id)
            elif choice == "5":
                rental.print_equipment()
            elif choice == "6":
                rental.print_clients()
            elif choice == "7":
                rental.print_rentals()
            elif choice == "8":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
