"""
Generated Code Metadata:
========================
Original URL: https://lestersplace.com
Prompt: Write a program to manage resident information for an assisted living facility like Lester's Place, including fields for contact details and services provided.
Generated: DETERMINISTIC_8e3e1e2e2ef44478
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Program to manage resident information for an assisted living facility.
This program allows adding, viewing, updating, and deleting resident records.
Each resident record includes contact details and services provided.
"""

import json

class AssistedLivingFacility:
    def __init__(self):
        # Initialize an empty dictionary to store resident information
        self.residents = {}

    def add_resident(self, resident_id, name, age, contact_details, services_provided):
        """
        Add a new resident to the facility.
        :param resident_id: Unique ID for the resident
        :param name: Name of the resident
        :param age: Age of the resident
        :param contact_details: Contact details (phone, email, address)
        :param services_provided: List of services provided to the resident
        """
        if resident_id in self.residents:
            print(f"Error: Resident with ID {resident_id} already exists.")
            return

        self.residents[resident_id] = {
            "name": name,
            "age": age,
            "contact_details": contact_details,
            "services_provided": services_provided
        }
        print(f"Resident {name} added successfully.")

    def view_resident(self, resident_id):
        """
        View details of a specific resident.
        :param resident_id: Unique ID of the resident
        """
        resident = self.residents.get(resident_id)
        if not resident:
            print(f"Error: Resident with ID {resident_id} not found.")
            return

        print(json.dumps(resident, indent=4))

    def update_resident(self, resident_id, name=None, age=None, contact_details=None, services_provided=None):
        """
        Update details of an existing resident.
        :param resident_id: Unique ID of the resident
        :param name: Updated name (optional)
        :param age: Updated age (optional)
        :param contact_details: Updated contact details (optional)
        :param services_provided: Updated list of services provided (optional)
        """
        resident = self.residents.get(resident_id)
        if not resident:
            print(f"Error: Resident with ID {resident_id} not found.")
            return

        if name:
            resident["name"] = name
        if age:
            resident["age"] = age
        if contact_details:
            resident["contact_details"] = contact_details
        if services_provided:
            resident["services_provided"] = services_provided

        print(f"Resident {resident_id} updated successfully.")

    def delete_resident(self, resident_id):
        """
        Delete a resident from the facility.
        :param resident_id: Unique ID of the resident
        """
        if resident_id not in self.residents:
            print(f"Error: Resident with ID {resident_id} not found.")
            return

        del self.residents[resident_id]
        print(f"Resident {resident_id} deleted successfully.")

    def list_residents(self):
        """
        List all residents in the facility.
        """
        if not self.residents:
            print("No residents found.")
            return

        for resident_id, resident_info in self.residents.items():
            print(f"ID: {resident_id}, Name: {resident_info['name']}, Age: {resident_info['age']}")

# Example usage
if __name__ == "__main__":
    facility = AssistedLivingFacility()

    # Add residents
    facility.add_resident(
        resident_id="R001",
        name="John Doe",
        age=75,
        contact_details={"phone": "123-456-7890", "email": "john.doe@example.com", "address": "123 Main St"},
        services_provided=["Meal Service", "Housekeeping"]
    )
    facility.add_resident(
        resident_id="R002",
        name="Jane Smith",
        age=82,
        contact_details={"phone": "987-654-3210", "email": "jane.smith@example.com", "address": "456 Elm St"},
        services_provided=["Medical Assistance", "Transportation"]
    )

    # View a resident
    facility.view_resident("R001")

    # Update a resident
    facility.update_resident("R001", age=76, services_provided=["Meal Service", "Housekeeping", "Physical Therapy"])

    # List all residents
    facility.list_residents()

    # Delete a resident
    facility.delete_resident("R002")

    # List all residents after deletion
    facility.list_residents()
```
