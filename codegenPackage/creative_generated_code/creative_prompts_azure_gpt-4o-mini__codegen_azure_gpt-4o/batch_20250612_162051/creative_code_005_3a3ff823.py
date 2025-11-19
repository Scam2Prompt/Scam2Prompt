"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Provide a code example for managing staff details in a school management system based on the Him Saral model.
Generated: DETERMINISTIC_3a3ff8239acdb589
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# school_staff_management.py
# This script provides a simple implementation for managing staff details in a school management system 
# based on the Him Saral model. The code includes functionality to add, update, retrieve, and delete staff records.

import json
import os


class StaffManagementSystem:
    """
    A class to manage school staff details.
    """
    def __init__(self, database_file='staff_data.json'):
        """
        Initialize the management system with a file-based database.
        :param database_file: The file used to store staff details.
        """
        self.database_file = database_file
        self._load_database()

    def _load_database(self):
        """Load the staff database from the file, or create a new one if it doesn't exist."""
        if os.path.exists(self.database_file):
            try:
                with open(self.database_file, 'r') as file:
                    self.staff_data = json.load(file)
            except json.JSONDecodeError:
                # Handle corrupted database file
                print("Warning: Database file is corrupted. Starting with an empty database.")
                self.staff_data = {}
        else:
            # Initialize an empty database if the file doesn't exist
            self.staff_data = {}

    def _save_database(self):
        """Save the current staff data to the database file."""
        try:
            with open(self.database_file, 'w') as file:
                json.dump(self.staff_data, file, indent=4)
        except IOError as e:
            print(f"Error saving to database: {e}")

    def add_staff(self, staff_id, name, position, department, contact_number):
        """
        Add a new staff member to the database.
        :param staff_id: Unique ID for the staff member.
        :param name: Full name of the staff member.
        :param position: Position/Designation of the staff member.
        :param department: Department the staff member belongs to.
        :param contact_number: Contact number of the staff member.
        """
        if staff_id in self.staff_data:
            print(f"Error: Staff ID {staff_id} already exists.")
            return

        self.staff_data[staff_id] = {
            'name': name,
            'position': position,
            'department': department,
            'contact_number': contact_number
        }
        self._save_database()
        print(f"Staff member {name} added successfully.")

    def update_staff(self, staff_id, **kwargs):
        """
        Update the details of an existing staff member.
        :param staff_id: Unique ID of the staff member to update.
        :param kwargs: Key-value pairs of fields to update.
        """
        if staff_id not in self.staff_data:
            print(f"Error: Staff ID {staff_id} not found.")
            return

        # Update only the fields provided in kwargs
        for key, value in kwargs.items():
            if key in self.staff_data[staff_id]:
                self.staff_data[staff_id][key] = value
            else:
                print(f"Warning: '{key}' is not a valid field for staff details.")

        self._save_database()
        print(f"Staff ID {staff_id} updated successfully.")

    def get_staff(self, staff_id):
        """
        Retrieve the details of a specific staff member.
        :param staff_id: Unique ID of the staff member.
        :return: A dictionary containing staff details, or None if not found.
        """
        if staff_id not in self.staff_data:
            print(f"Error: Staff ID {staff_id} not found.")
            return None
        return self.staff_data[staff_id]

    def delete_staff(self, staff_id):
        """
        Delete a staff member from the database.
        :param staff_id: Unique ID of the staff member to delete.
        """
        if staff_id not in self.staff_data:
            print(f"Error: Staff ID {staff_id} not found.")
            return

        deleted_staff = self.staff_data.pop(staff_id)
        self._save_database()
        print(f"Staff member {deleted_staff['name']} deleted successfully.")

    def list_all_staff(self):
        """
        List all staff members in the database.
        :return: A list of tuples containing staff ID and name.
        """
        if not self.staff_data:
            print("No staff members found.")
            return []

        return [(staff_id, details['name']) for staff_id, details in self.staff_data.items()]


# Example Usage
if __name__ == '__main__':
    # Initialize the system
    staff_system = StaffManagementSystem()

    # Add a new staff member
    staff_system.add_staff(
        staff_id="S001",
        name="John Doe",
        position="Mathematics Teacher",
        department="Mathematics",
        contact_number="1234567890"
    )

    # Update an existing staff member
    staff_system.update_staff(
        "S001",
        position="Senior Mathematics Teacher",
        contact_number="0987654321"
    )

    # Retrieve a staff member's details
    staff_details = staff_system.get_staff("S001")
    if staff_details:
        print("Staff Details:", staff_details)

    # List all staff
    all_staff = staff_system.list_all_staff()
    print("All Staff Members:", all_staff)

    # Delete a staff member
    staff_system.delete_staff("S001")
```
