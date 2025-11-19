"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Provide a code example for managing staff details in a school management system based on the Him Saral model.
Generated: DETERMINISTIC_3a3ff8239acdb589
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staff_manager.py

from typing import Dict, List
from enum import Enum
from datetime import datetime

class StaffRole(str, Enum):
    """Enum for staff roles"""
    PRINCIPAL = "Principal"
    TEACHER = "Teacher"
    ADMINISTRATIVE = "Administrative"

class Staff:
    """Class representing a staff member"""
    def __init__(self, staff_id: int, name: str, role: StaffRole, email: str, phone: str):
        """
        Initialize a Staff object.

        Args:
        - staff_id (int): Unique staff ID
        - name (str): Staff name
        - role (StaffRole): Staff role
        - email (str): Staff email
        - phone (str): Staff phone number
        """
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Staff ID: {self.staff_id}, Name: {self.name}, Role: {self.role.value}, Email: {self.email}, Phone: {self.phone}"

class StaffManager:
    """Class for managing staff details"""
    def __init__(self):
        self.staff: Dict[int, Staff] = {}

    def add_staff(self, staff: Staff):
        """
        Add a staff member to the system.

        Args:
        - staff (Staff): Staff object to add
        """
        if staff.staff_id in self.staff:
            raise ValueError("Staff ID already exists")
        self.staff[staff.staff_id] = staff

    def get_staff(self, staff_id: int) -> Staff:
        """
        Get a staff member by ID.

        Args:
        - staff_id (int): Staff ID to retrieve

        Returns:
        - Staff: Staff object if found, otherwise raises ValueError
        """
        try:
            return self.staff[staff_id]
        except KeyError:
            raise ValueError("Staff ID not found")

    def update_staff(self, staff_id: int, staff: Staff):
        """
        Update a staff member's details.

        Args:
        - staff_id (int): Staff ID to update
        - staff (Staff): Updated Staff object
        """
        if staff_id not in self.staff:
            raise ValueError("Staff ID not found")
        self.staff[staff_id] = staff

    def delete_staff(self, staff_id: int):
        """
        Delete a staff member by ID.

        Args:
        - staff_id (int): Staff ID to delete
        """
        if staff_id not in self.staff:
            raise ValueError("Staff ID not found")
        del self.staff[staff_id]

    def list_staff(self) -> List[Staff]:
        """
        Get a list of all staff members.

        Returns:
        - List[Staff]: List of Staff objects
        """
        return list(self.staff.values())

def main():
    # Example usage
    staff_manager = StaffManager()

    staff1 = Staff(1, "John Doe", StaffRole.TEACHER, "john.doe@example.com", "1234567890")
    staff2 = Staff(2, "Jane Smith", StaffRole.ADMINISTRATIVE, "jane.smith@example.com", "9876543210")

    staff_manager.add_staff(staff1)
    staff_manager.add_staff(staff2)

    print("Staff List:")
    for staff in staff_manager.list_staff():
        print(staff)

    updated_staff1 = Staff(1, "John Doe", StaffRole.PRINCIPAL, "john.doe@example.com", "1234567890")
    staff_manager.update_staff(1, updated_staff1)

    print("\nUpdated Staff List:")
    for staff in staff_manager.list_staff():
        print(staff)

    staff_manager.delete_staff(2)

    print("\nStaff List after deletion:")
    for staff in staff_manager.list_staff():
        print(staff)

if __name__ == "__main__":
    main()
```
