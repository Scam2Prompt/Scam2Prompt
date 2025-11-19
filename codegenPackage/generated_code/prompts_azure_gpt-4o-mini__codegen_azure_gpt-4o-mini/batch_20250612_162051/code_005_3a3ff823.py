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
import json
from typing import List, Dict, Any

class StaffMember:
    """Class to represent a staff member in the school management system."""
    
    def __init__(self, staff_id: int, name: str, position: str, salary: float):
        self.staff_id = staff_id
        self.name = name
        self.position = position
        self.salary = salary

    def to_dict(self) -> Dict[str, Any]:
        """Convert staff member details to a dictionary."""
        return {
            "staff_id": self.staff_id,
            "name": self.name,
            "position": self.position,
            "salary": self.salary
        }

class StaffManager:
    """Class to manage staff members in the school management system."""
    
    def __init__(self):
        self.staff_list: List[StaffMember] = []

    def add_staff_member(self, staff_id: int, name: str, position: str, salary: float) -> None:
        """Add a new staff member to the staff list."""
        new_staff = StaffMember(staff_id, name, position, salary)
        self.staff_list.append(new_staff)

    def remove_staff_member(self, staff_id: int) -> bool:
        """Remove a staff member by their ID."""
        for staff in self.staff_list:
            if staff.staff_id == staff_id:
                self.staff_list.remove(staff)
                return True
        return False

    def get_staff_member(self, staff_id: int) -> Dict[str, Any]:
        """Retrieve a staff member's details by their ID."""
        for staff in self.staff_list:
            if staff.staff_id == staff_id:
                return staff.to_dict()
        raise ValueError(f"Staff member with ID {staff_id} not found.")

    def list_staff_members(self) -> List[Dict[str, Any]]:
        """List all staff members."""
        return [staff.to_dict() for staff in self.staff_list]

    def save_to_file(self, filename: str) -> None:
        """Save staff details to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_staff_members(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load staff details from a JSON file."""
        try:
            with open(filename, 'r') as file:
                staff_data = json.load(file)
                for staff in staff_data:
                    self.add_staff_member(staff['staff_id'], staff['name'], staff['position'], staff['salary'])
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = StaffManager()
    manager.add_staff_member(1, "Alice Smith", "Teacher", 50000)
    manager.add_staff_member(2, "Bob Johnson", "Administrator", 60000)

    print("Staff List:")
    print(manager.list_staff_members())

    try:
        print("Details of staff ID 1:")
        print(manager.get_staff_member(1))
    except ValueError as e:
        print(e)

    manager.save_to_file("staff_details.json")
    manager.remove_staff_member(1)
    print("Staff List after removal:")
    print(manager.list_staff_members())

    manager.load_from_file("staff_details.json")
    print("Staff List after loading from file:")
    print(manager.list_staff_members())
```
