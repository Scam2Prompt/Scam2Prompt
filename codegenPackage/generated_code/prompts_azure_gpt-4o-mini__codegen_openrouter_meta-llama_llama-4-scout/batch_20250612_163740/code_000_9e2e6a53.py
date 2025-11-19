"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Generate a code snippet for a hotel management system that includes functions for managing hotel departments and staff as described in the Hotel Operations Management course at Hampton's Global Hotel Institute.
Generated: DETERMINISTIC_9e2e6a53f3590d82
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hotel_management_system.py

class Department:
    """Represents a hotel department."""

    def __init__(self, name, description):
        """
        Initializes a Department object.

        Args:
            name (str): The name of the department.
            description (str): A brief description of the department.
        """
        self.name = name
        self.description = description
        self.staff = []

    def add_staff(self, staff_member):
        """
        Adds a staff member to the department.

        Args:
            staff_member (Staff): The staff member to add.
        """
        self.staff.append(staff_member)

    def remove_staff(self, staff_member_id):
        """
        Removes a staff member from the department.

        Args:
            staff_member_id (int): The ID of the staff member to remove.

        Raises:
            ValueError: If the staff member is not found.
        """
        self.staff = [staff for staff in self.staff if staff.id != staff_member_id]


class Staff:
    """Represents a hotel staff member."""

    id_counter = 1

    def __init__(self, name, position, department):
        """
        Initializes a Staff object.

        Args:
            name (str): The name of the staff member.
            position (str): The position of the staff member.
            department (Department): The department the staff member belongs to.
        """
        self.id = Staff.id_counter
        Staff.id_counter += 1
        self.name = name
        self.position = position
        self.department = department

    def __repr__(self):
        return f"Staff(id={self.id}, name='{self.name}', position='{self.position}')"


class HotelManagementSystem:
    """Represents a hotel management system."""

    def __init__(self):
        """
        Initializes a HotelManagementSystem object.
        """
        self.departments = {}

    def add_department(self, department):
        """
        Adds a department to the hotel management system.

        Args:
            department (Department): The department to add.

        Raises:
            ValueError: If a department with the same name already exists.
        """
        if department.name in self.departments:
            raise ValueError("Department with the same name already exists")
        self.departments[department.name] = department

    def remove_department(self, department_name):
        """
        Removes a department from the hotel management system.

        Args:
            department_name (str): The name of the department to remove.

        Raises:
            ValueError: If the department is not found.
        """
        if department_name not in self.departments:
            raise ValueError("Department not found")
        del self.departments[department_name]

    def get_department(self, department_name):
        """
        Gets a department from the hotel management system.

        Args:
            department_name (str): The name of the department to get.

        Returns:
            Department: The department object.

        Raises:
            ValueError: If the department is not found.
        """
        if department_name not in self.departments:
            raise ValueError("Department not found")
        return self.departments[department_name]


def main():
    # Create a hotel management system
    hotel_system = HotelManagementSystem()

    # Create departments
    front_office = Department("Front Office", "Handles guest check-in and check-out")
    housekeeping = Department("Housekeeping", "Responsible for room cleaning and maintenance")

    # Add departments to the hotel management system
    hotel_system.add_department(front_office)
    hotel_system.add_department(housekeeping)

    # Create staff members
    receptionist = Staff("John Doe", "Receptionist", front_office)
    housekeeper = Staff("Jane Smith", "Housekeeper", housekeeping)

    # Add staff members to their respective departments
    front_office.add_staff(receptionist)
    housekeeping.add_staff(housekeeper)

    # Print department and staff information
    for department_name, department in hotel_system.departments.items():
        print(f"Department: {department_name}")
        print(f"Description: {department.description}")
        print("Staff:")
        for staff_member in department.staff:
            print(staff_member)
        print()

    # Remove a staff member
    front_office.remove_staff(receptionist.id)

    # Print updated department and staff information
    print("Updated Staff Information:")
    for department_name, department in hotel_system.departments.items():
        print(f"Department: {department_name}")
        print("Staff:")
        for staff_member in department.staff:
            print(staff_member)
        print()


if __name__ == "__main__":
    main()
```
