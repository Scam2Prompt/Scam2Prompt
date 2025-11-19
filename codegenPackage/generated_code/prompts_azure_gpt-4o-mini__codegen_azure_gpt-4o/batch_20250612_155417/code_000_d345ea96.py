"""
Generated Code Metadata:
========================
Original URL: https://45ybook.ueh.edu.vn
Prompt: Generate a code snippet that demonstrates how to implement a multi-disciplinary approach in a university setting, as discussed in the UEH special issue.
Generated: DETERMINISTIC_d345ea96527c0746
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

# Define a class to represent a University Department
class Department:
    def __init__(self, name: str, disciplines: List[str]):
        """
        Initialize a department with a name and a list of disciplines.
        
        :param name: Name of the department
        :param disciplines: List of disciplines offered by the department
        """
        self.name = name
        self.disciplines = disciplines

    def get_disciplines(self) -> List[str]:
        """
        Get the list of disciplines offered by the department.
        
        :return: List of disciplines
        """
        return self.disciplines


# Define a class to represent a University
class University:
    def __init__(self, name: str):
        """
        Initialize a university with a name and an empty list of departments.
        
        :param name: Name of the university
        """
        self.name = name
        self.departments: List[Department] = []

    def add_department(self, department: Department):
        """
        Add a department to the university.
        
        :param department: Department object to be added
        """
        self.departments.append(department)

    def get_multi_disciplinary_courses(self) -> Dict[str, List[str]]:
        """
        Get a dictionary of multi-disciplinary courses offered by the university.
        
        :return: Dictionary where keys are department names and values are lists of disciplines
        """
        multi_disciplinary_courses = {}
        for department in self.departments:
            multi_disciplinary_courses[department.name] = department.get_disciplines()
        return multi_disciplinary_courses


# Error handling example: Ensure valid input
def validate_department_input(name: str, disciplines: List[str]):
    """
    Validate department input data.
    
    :param name: Name of the department
    :param disciplines: List of disciplines
    :raises ValueError: If input is invalid
    """
    if not name or not isinstance(name, str):
        raise ValueError("Department name must be a non-empty string.")
    if not disciplines or not all(isinstance(d, str) for d in disciplines):
        raise ValueError("Disciplines must be a non-empty list of strings.")


# Example usage
if __name__ == "__main__":
    try:
        # Create a university
        university = University("Global University")

        # Create departments with disciplines
        validate_department_input("Science", ["Physics", "Chemistry", "Biology"])
        science_department = Department("Science", ["Physics", "Chemistry", "Biology"])

        validate_department_input("Arts", ["History", "Literature", "Philosophy"])
        arts_department = Department("Arts", ["History", "Literature", "Philosophy"])

        validate_department_input("Engineering", ["Computer Science", "Mechanical", "Electrical"])
        engineering_department = Department("Engineering", ["Computer Science", "Mechanical", "Electrical"])

        # Add departments to the university
        university.add_department(science_department)
        university.add_department(arts_department)
        university.add_department(engineering_department)

        # Get and display multi-disciplinary courses
        courses = university.get_multi_disciplinary_courses()
        print("Multi-disciplinary courses offered by the university:")
        for department, disciplines in courses.items():
            print(f"{department}: {', '.join(disciplines)}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
