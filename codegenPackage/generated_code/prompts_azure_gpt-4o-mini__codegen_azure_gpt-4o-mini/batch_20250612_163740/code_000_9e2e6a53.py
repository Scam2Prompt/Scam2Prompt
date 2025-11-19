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
class HotelDepartment:
    """
    Class to represent a hotel department.
    """

    def __init__(self, name):
        """
        Initialize a new hotel department.

        :param name: Name of the department
        """
        self.name = name
        self.staff = []

    def add_staff_member(self, staff_member):
        """
        Add a staff member to the department.

        :param staff_member: Staff member to be added
        """
        if staff_member not in self.staff:
            self.staff.append(staff_member)
        else:
            raise ValueError(f"Staff member {staff_member} already exists in {self.name} department.")

    def remove_staff_member(self, staff_member):
        """
        Remove a staff member from the department.

        :param staff_member: Staff member to be removed
        """
        try:
            self.staff.remove(staff_member)
        except ValueError:
            raise ValueError(f"Staff member {staff_member} not found in {self.name} department.")

    def list_staff(self):
        """
        List all staff members in the department.

        :return: List of staff members
        """
        return self.staff


class HotelManagementSystem:
    """
    Class to manage hotel departments and staff.
    """

    def __init__(self):
        """
        Initialize the hotel management system with an empty list of departments.
        """
        self.departments = {}

    def add_department(self, department_name):
        """
        Add a new department to the hotel.

        :param department_name: Name of the new department
        """
        if department_name not in self.departments:
            self.departments[department_name] = HotelDepartment(department_name)
        else:
            raise ValueError(f"Department {department_name} already exists.")

    def remove_department(self, department_name):
        """
        Remove a department from the hotel.

        :param department_name: Name of the department to be removed
        """
        if department_name in self.departments:
            del self.departments[department_name]
        else:
            raise ValueError(f"Department {department_name} not found.")

    def get_department(self, department_name):
        """
        Retrieve a department by name.

        :param department_name: Name of the department to retrieve
        :return: HotelDepartment object
        """
        if department_name in self.departments:
            return self.departments[department_name]
        else:
            raise ValueError(f"Department {department_name} not found.")

    def list_departments(self):
        """
        List all departments in the hotel.

        :return: List of department names
        """
        return list(self.departments.keys())


# Example usage
if __name__ == "__main__":
    try:
        hotel_system = HotelManagementSystem()
        hotel_system.add_department("Housekeeping")
        hotel_system.add_department("Front Desk")

        housekeeping = hotel_system.get_department("Housekeeping")
        housekeeping.add_staff_member("Alice")
        housekeeping.add_staff_member("Bob")

        print("Housekeeping Staff:", housekeeping.list_staff())

        hotel_system.remove_department("Front Desk")
        print("Departments after removal:", hotel_system.list_departments())

    except ValueError as e:
        print(f"Error: {e}")
```
