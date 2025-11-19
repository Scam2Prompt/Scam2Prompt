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
# staff_management.py

import json
from typing import List, Dict, Any

class Staff:
    """Class to represent a staff member in the school management system."""
    
    def __init__(self, staff_id: int, name: str, role: str, contact: str):
        """
        Initialize a new staff member.

        Args:
            staff_id (int): Unique identifier for the staff member.
            name (str): Name of the staff member.
            role (str): Role of the staff member in the school.
            contact (str): Contact information of the staff member.
        """
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.contact = contact

    def to_dict(self) -> Dict[str, Any]:
        """Convert staff member information to a dictionary."""
        return {
            'staff_id': self.staff_id,
            'name': self.name,
            'role': self.role,
            'contact': self.contact
        }


class StaffManager:
    """Class to manage staff details in the school management system."""
    
    def __init__(self, filename: str):
        """
        Initialize the StaffManager with a filename for data persistence.

        Args:
            filename (str): The file where staff data will be stored.
        """
        self.filename = filename
        self.staff_list: List[Staff] = []
        self.load_staff()

    def load_staff(self):
        """Load staff details from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                staff_data = json.load(file)
                self.staff_list = [Staff(**data) for data in staff_data]
        except FileNotFoundError:
            print(f"Warning: {self.filename} not found. Starting with an empty staff list.")
            self.staff_list = []
        except json.JSONDecodeError as e:
            print(f"Error reading {self.filename}: {e}. Starting with an empty staff list.")
            self.staff_list = []

    def save_staff(self):
        """Save staff details to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([staff.to_dict() for staff in self.staff_list], file, indent=4)
        except IOError as e:
            print(f"Error saving staff data to {self.filename}: {e}")

    def add_staff(self, staff: Staff):
        """Add a new staff member to the staff list.

        Args:
            staff (Staff): The staff member to be added.
        """
        self.staff_list.append(staff)
        self.save_staff()

    def remove_staff(self, staff_id: int):
        """Remove a staff member from the staff list by staff_id.

        Args:
            staff_id (int): The unique identifier of the staff member to remove.
        """
        self.staff_list = [staff for staff in self.staff_list if staff.staff_id != staff_id]
        self.save_staff()

    def get_staff(self) -> List[Staff]:
        """Get the list of all staff members.

        Returns:
            List[Staff]: List of staff members.
        """
        return self.staff_list

    def find_staff(self, staff_id: int) -> Staff:
        """Find a staff member by staff_id.

        Args:
            staff_id (int): The unique identifier of the staff member to find.

        Returns:
            Staff: The staff member if found; None otherwise.
        """
        for staff in self.staff_list:
            if staff.staff_id == staff_id:
                return staff
        return None


# Example usage
if __name__ == "__main__":
    manager = StaffManager('staff_data.json')
    
    # Adding staff members
    manager.add_staff(Staff(1, 'John Doe', 'Teacher', 'john.doe@example.com'))
    manager.add_staff(Staff(2, 'Jane Smith', 'Administrator', 'jane.smith@example.com'))

    # Display all staff
    for staff in manager.get_staff():
        print(staff.to_dict())

    # Find a staff member
    staff_member = manager.find_staff(1)
    if staff_member:
        print(f"Found staff member: {staff_member.to_dict()}")
    
    # Remove a staff member
    manager.remove_staff(1)
```
