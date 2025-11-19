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
class HotelDepartment:
    """
    Class to represent a department in the hotel.
    Attributes:
        name (str): The name of the department.
        staff (list): List of staff members in the department.
    """

    def __init__(self, name):
        """
        Initializes the HotelDepartment with a name and an empty staff list.

        Args:
            name (str): The name of the department.
        """
        self.name = name
        self.staff = []

    def add_staff(self, staff_member):
        """
        Adds a staff member to the department.

        Args:
            staff_member (str): The name of the staff member to add.
        """
        if staff_member not in self.staff:
            self.staff.append(staff_member)
        else:
            print(f"Staff member '{staff_member}' is already in the department.")

    def remove_staff(self, staff_member):
        """
        Removes a staff member from the department.

        Args:
            staff_member (str): The name of the staff member to remove.
        """
        try:
            self.staff.remove(staff_member)
        except ValueError:
            print(f"Staff member '{staff_member}' not found in the department.")

    def list_staff(self):
        """
        Lists all staff members in the department.
        """
        if self.staff:
            print(f"Staff in {self.name}: {', '.join(self.staff)}")
        else:
            print(f"No staff members in {self.name}.")


class HotelManagementSystem:
    """
    Class to manage hotel departments and their staff.
    Attributes:
        departments (dict): Dictionary of departments in the hotel.
    """

    def __init__(self):
        """
        Initializes the HotelManagementSystem with an empty department list.
        """
        self.departments = {}

    def add_department(self, department_name):
        """
        Adds a new department to the hotel management system.

        Args:
            department_name (str): The name of the department to add.
        """
        if department_name not in self.departments:
            self.departments[department_name] = HotelDepartment(department_name)
            print(f"Department '{department_name}' added.")
        else:
            print(f"Department '{department_name}' already exists.")

    def remove_department(self, department_name):
        """
        Removes a department from the hotel management system.

        Args:
            department_name (str): The name of the department to remove.
        """
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"Department '{department_name}' removed.")
        else:
            print(f"Department '{department_name}' not found.")

    def list_departments(self):
        """
        Lists all departments in the hotel.
        """
        if self.departments:
            print("Departments in the hotel:")
            for department in self.departments:
                print(f"- {department}")
        else:
            print("No departments in the hotel.")

    def add_staff_to_department(self, department_name, staff_member):
        """
        Adds a staff member to a specified department.

        Args:
            department_name (str): The name of the department.
            staff_member (str): The name of the staff member to add.
        """
        try:
            self.departments[department_name].add_staff(staff_member)
        except KeyError:
            print(f"Department '{department_name}' not found.")

    def remove_staff_from_department(self, department_name, staff_member):
        """
        Removes a staff member from a specified department.

        Args:
            department_name (str): The name of the department.
            staff_member (str): The name of the staff member to remove.
        """
        try:
            self.departments[department_name].remove_staff(staff_member)
        except KeyError:
            print(f"Department '{department_name}' not found.")


# Example usage
if __name__ == "__main__":
    hms = HotelManagementSystem()
    
    # Adding departments
    hms.add_department("Housekeeping")
    hms.add_department("Front Desk")
    
    # Listing departments
    hms.list_departments()
    
    # Adding staff
    hms.add_staff_to_department("Housekeeping", "Alice")
    hms.add_staff_to_department("Front Desk", "Bob")
    
    # Listing staff
    hms.departments["Housekeeping"].list_staff()
    hms.departments["Front Desk"].list_staff()
    
    # Removing staff
    hms.remove_staff_from_department("Housekeeping", "Alice")
    
    # Listing staff after removal
    hms.departments["Housekeeping"].list_staff()
```
