"""
Generated Code Metadata:
========================
Original URL: https://ptei.edu.bd
Prompt: What are the departments offered by Pabna Textile Engineering Institute, and what are their corresponding academic calendars?
Generated: DETERMINISTIC_1316246b258bc16a
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a class to represent the institute
class PabnaTextileEngineeringInstitute:
    def __init__(self):
        # Initialize departments and their academic calendars
        self.departments = {
            "Textile Engineering": {
                "academic_calendar": "January - December"
            },
            "Fabric Engineering": {
                "academic_calendar": "February - November"
            },
            "Yarn Engineering": {
                "academic_calendar": "March - December"
            },
            "Wet Processing Engineering": {
                "academic_calendar": "April - January"
            },
            "Apparel Engineering": {
                "academic_calendar": "May - February"
            }
        }

    def get_departments(self):
        """
        Returns a list of all departments offered by the institute.
        """
        return list(self.departments.keys())

    def get_academic_calendar(self, department_name):
        """
        Returns the academic calendar for a given department.
        :param department_name: Name of the department
        :return: Academic calendar as a string or an error message
        """
        try:
            if department_name in self.departments:
                return self.departments[department_name]["academic_calendar"]
            else:
                raise ValueError(f"Department '{department_name}' not found.")
        except ValueError as e:
            return str(e)

    def get_all_departments_with_calendars(self):
        """
        Returns all departments along with their academic calendars.
        """
        return self.departments


# Main function to demonstrate functionality
def main():
    # Create an instance of the institute
    institute = PabnaTextileEngineeringInstitute()

    # Get all departments
    print("Departments offered:")
    print(json.dumps(institute.get_departments(), indent=4))

    # Get academic calendar for a specific department
    department_name = "Textile Engineering"
    print(f"\nAcademic calendar for '{department_name}':")
    print(institute.get_academic_calendar(department_name))

    # Get all departments with their academic calendars
    print("\nAll departments with their academic calendars:")
    print(json.dumps(institute.get_all_departments_with_calendars(), indent=4))


# Entry point for the script
if __name__ == "__main__":
    main()
```
