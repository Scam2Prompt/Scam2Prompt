"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Generate a code snippet for a hotel management system that includes functions for managing hotel departments and staff as described in the Hotel Operations Management course at Hampton's Global Hotel Institute.
Generated: DETERMINISTIC_9e2e6a53f3590d82
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Hotel Management System
# Language: Python
# This program defines a hotel management system with functions to manage hotel departments and staff.

class HotelManagementSystem:
    def __init__(self):
        """
        Initializes the hotel management system with empty lists for departments and staff.
        """
        self.departments = {}  # Dictionary to store departments and their staff

    def add_department(self, department_name):
        """
        Adds a new department to the hotel.
        :param department_name: Name of the department to add
        """
        if department_name in self.departments:
            print(f"Department '{department_name}' already exists.")
        else:
            self.departments[department_name] = []
            print(f"Department '{department_name}' added successfully.")

    def add_staff_member(self, department_name, staff_name, position):
        """
        Adds a new staff member to a department.
        :param department_name: Name of the department
        :param staff_name: Name of the staff member
        :param position: Position of the staff member
        """
        if department_name not in self.departments:
            print(f"Department '{department_name}' does not exist. Please add the department first.")
            return

        staff_member = {"name": staff_name, "position": position}
        self.departments[department_name].append(staff_member)
        print(f"Staff member '{staff_name}' added to department '{department_name}'.")

    def list_departments(self):
        """
        Lists all departments in the hotel.
        """
        if not self.departments:
            print("No departments available.")
        else:
            print("Departments in the hotel:")
            for department in self.departments:
                print(f" - {department}")

    def list_staff(self, department_name):
        """
        Lists all staff members in a specific department.
        :param department_name: Name of the department
        """
        if department_name not in self.departments:
            print(f"Department '{department_name}' does not exist.")
            return

        staff = self.departments[department_name]
        if not staff:
            print(f"No staff members found in department '{department_name}'.")
        else:
            print(f"Staff members in department '{department_name}':")
            for member in staff:
                print(f" - Name: {member['name']}, Position: {member['position']}")

    def remove_staff_member(self, department_name, staff_name):
        """
        Removes a staff member from a department.
        :param department_name: Name of the department
        :param staff_name: Name of the staff member to remove
        """
        if department_name not in self.departments:
            print(f"Department '{department_name}' does not exist.")
            return

        staff = self.departments[department_name]
        for member in staff:
            if member["name"] == staff_name:
                staff.remove(member)
                print(f"Staff member '{staff_name}' removed from department '{department_name}'.")
                return

        print(f"Staff member '{staff_name}' not found in department '{department_name}'.")

    def remove_department(self, department_name):
        """
        Removes a department from the hotel.
        :param department_name: Name of the department to remove
        """
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"Department '{department_name}' removed successfully.")
        else:
            print(f"Department '{department_name}' does not exist.")


# Example Usage
if __name__ == "__main__":
    # Instantiate the hotel management system
    hotel = HotelManagementSystem()

    # Add departments
    hotel.add_department("Housekeeping")
    hotel.add_department("Reception")
    hotel.add_department("Kitchen")

    # Add staff members
    hotel.add_staff_member("Housekeeping", "Alice", "Cleaner")
    hotel.add_staff_member("Reception", "Bob", "Front Desk Manager")
    hotel.add_staff_member("Kitchen", "Charlie", "Chef")

    # List departments
    hotel.list_departments()

    # List staff members in a department
    hotel.list_staff("Kitchen")

    # Remove a staff member
    hotel.remove_staff_member("Kitchen", "Charlie")

    # List staff members after removal
    hotel.list_staff("Kitchen")

    # Remove a department
    hotel.remove_department("Reception")

    # List departments after removal
    hotel.list_departments()
```
