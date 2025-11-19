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
import json
from datetime import datetime

class Equipment:
    """Class to represent a piece of translation equipment."""
    
    def __init__(self, equipment_id, name, available=True):
        self.equipment_id = equipment_id
        self.name = name
        self.available = available

    def __repr__(self):
        return f"Equipment({self.equipment_id}, {self.name}, Available: {self.available})"


class Client:
    """Class to represent a client renting equipment."""
    
    def __init__(self, client_id, name, contact_info):
        self.client_id = client_id
        self.name = name
        self.contact_info = contact_info

    def __repr__(self):
        return f"Client({self.client_id}, {self.name})"


class Rental:
    """Class to represent a rental transaction."""
    
    def __init__(self, rental_id, client, equipment, rental_date, return_date):
        self.rental_id = rental_id
        self.client = client
        self.equipment = equipment
        self.rental_date = rental_date
        self.return_date = return_date

    def __repr__(self):
        return (f"Rental({self.rental_id}, Client: {self.client.name}, "
                f"Equipment: {self.equipment.name}, "
                f"Rental Date: {self.rental_date}, Return Date: {self.return_date})")


class RentalManagementSystem:
    """Class to manage the rental of translation equipment."""
    
    def __init__(self):
        self.equipments = []
        self.clients = []
        self.rentals = []
        self.load_data()

    def load_data(self):
        """Load equipment and client data from JSON files."""
        try:
            with open('equipments.json', 'r') as f:
                self.equipments = [Equipment(**item) for item in json.load(f)]
            with open('clients.json', 'r') as f:
                self.clients = [Client(**item) for item in json.load(f)]
        except FileNotFoundError as e:
            print(f"Error loading data: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    def save_data(self):
        """Save equipment and client data to JSON files."""
        try:
            with open('equipments.json', 'w') as f:
                json.dump([vars(e) for e in self.equipments], f, indent=4)
            with open('clients.json', 'w') as f:
                json.dump([vars(c) for c in self.clients], f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_equipment(self, equipment_id, name):
        """Add new equipment to the system."""
        new_equipment = Equipment(equipment_id, name)
        self.equipments.append(new_equipment)
        self.save_data()

    def add_client(self, client_id, name, contact_info):
        """Add a new client to the system."""
        new_client = Client(client_id, name, contact_info)
        self.clients.append(new_client)
        self.save_data()

    def rent_equipment(self, client_id, equipment_id, rental_date, return_date):
        """Process the rental of equipment to a client."""
        client = next((c for c in self.clients if c.client_id == client_id), None)
        equipment = next((e for e in self.equipments if e.equipment_id == equipment_id), None)

        if not client:
            print("Client not found.")
            return
        if not equipment:
            print("Equipment not found.")
            return
        if not equipment.available:
            print("Equipment is not available for rent.")
            return

        rental_id = len(self.rentals) + 1
        rental = Rental(rental_id, client, equipment, rental_date, return_date)
        self.rentals.append(rental)
        equipment.available = False  # Mark equipment as rented
        self.save_data()
        print(f"Rental successful: {rental}")

    def return_equipment(self, rental_id):
        """Process the return of rented equipment."""
        rental = next((r for r in self.rentals if r.rental_id == rental_id), None)

        if not rental:
            print("Rental not found.")
            return

        rental.equipment.available = True  # Mark equipment as available
        self.rentals.remove(rental)  # Remove rental record
        self.save_data()
        print(f"Equipment returned: {rental.equipment.name}")

    def list_available_equipment(self):
        """List all available equipment."""
        available_equipment = [e for e in self.equipments if e.available]
        print("Available Equipment:")
        for equipment in available_equipment:
            print(equipment)

    def list_clients(self):
        """List all clients."""
        print("Clients:")
        for client in self.clients:
            print(client)


if __name__ == "__main__":
    # Example usage of the RentalManagementSystem
    rms = RentalManagementSystem()
    rms.list_available_equipment()
    rms.list_clients()
    rms.add_client("C001", "John Doe", "john@example.com")
    rms.add_equipment("E001", "Translation Device A")
    rms.rent_equipment("C001", "E001", datetime.now().isoformat(), (datetime.now().isoformat()))
    rms.return_equipment(1)
```

Make sure to create `equipments.json` and `clients.json` files in the same directory as this script to store the data. The files should be empty or contain valid JSON arrays to start with.
