"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Generate a Python script to manage student enrollment data for an educational institution like I.E Politécnico Municipal Cali, focusing on handling multiple campuses and student levels.
Generated: DETERMINISTIC_07585f23b5f809c4
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_enrollment_manager.py

class Campus:
    """Represents a campus of the educational institution."""

    def __init__(self, name):
        """
        Initializes a Campus object.

        Args:
            name (str): The name of the campus.
        """
        self.name = name
        self.students = {}

    def add_student(self, student_id, level, name):
        """
        Adds a student to the campus.

        Args:
            student_id (str): The unique ID of the student.
            level (str): The level of the student (e.g., freshman, sophomore, etc.).
            name (str): The name of the student.

        Raises:
            ValueError: If the student ID already exists.
        """
        if student_id in self.students:
            raise ValueError("Student ID already exists")
        self.students[student_id] = {"level": level, "name": name}

    def remove_student(self, student_id):
        """
        Removes a student from the campus.

        Args:
            student_id (str): The unique ID of the student.

        Raises:
            KeyError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise KeyError("Student ID does not exist")
        del self.students[student_id]

    def update_student(self, student_id, level=None, name=None):
        """
        Updates a student's information.

        Args:
            student_id (str): The unique ID of the student.
            level (str, optional): The new level of the student. Defaults to None.
            name (str, optional): The new name of the student. Defaults to None.

        Raises:
            KeyError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise KeyError("Student ID does not exist")
        if level:
            self.students[student_id]["level"] = level
        if name:
            self.students[student_id]["name"] = name

    def get_student(self, student_id):
        """
        Retrieves a student's information.

        Args:
            student_id (str): The unique ID of the student.

        Returns:
            dict: The student's information.

        Raises:
            KeyError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise KeyError("Student ID does not exist")
        return self.students[student_id]


class EnrollmentManager:
    """Manages student enrollment data for multiple campuses."""

    def __init__(self):
        """Initializes an EnrollmentManager object."""
        self.campuses = {}

    def add_campus(self, campus_name):
        """
        Adds a campus to the enrollment manager.

        Args:
            campus_name (str): The name of the campus.

        Raises:
            ValueError: If the campus name already exists.
        """
        if campus_name in self.campuses:
            raise ValueError("Campus name already exists")
        self.campuses[campus_name] = Campus(campus_name)

    def remove_campus(self, campus_name):
        """
        Removes a campus from the enrollment manager.

        Args:
            campus_name (str): The name of the campus.

        Raises:
            KeyError: If the campus name does not exist.
        """
        if campus_name not in self.campuses:
            raise KeyError("Campus name does not exist")
        del self.campuses[campus_name]

    def get_campus(self, campus_name):
        """
        Retrieves a campus object.

        Args:
            campus_name (str): The name of the campus.

        Returns:
            Campus: The campus object.

        Raises:
            KeyError: If the campus name does not exist.
        """
        if campus_name not in self.campuses:
            raise KeyError("Campus name does not exist")
        return self.campuses[campus_name]


def main():
    enrollment_manager = EnrollmentManager()

    while True:
        print("\n1. Add campus")
        print("2. Remove campus")
        print("3. Add student")
        print("4. Remove student")
        print("5. Update student")
        print("6. Get student")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            campus_name = input("Enter campus name: ")
            try:
                enrollment_manager.add_campus(campus_name)
                print(f"Campus '{campus_name}' added successfully.")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            campus_name = input("Enter campus name: ")
            try:
                enrollment_manager.remove_campus(campus_name)
                print(f"Campus '{campus_name}' removed successfully.")
            except KeyError as e:
                print(str(e))
        elif choice == "3":
            campus_name = input("Enter campus name: ")
            student_id = input("Enter student ID: ")
            level = input("Enter student level: ")
            name = input("Enter student name: ")
            try:
                campus = enrollment_manager.get_campus(campus_name)
                campus.add_student(student_id, level, name)
                print(f"Student '{name}' added successfully to campus '{campus_name}'.")
            except (KeyError, ValueError) as e:
                print(str(e))
        elif choice == "4":
            campus_name = input("Enter campus name: ")
            student_id = input("Enter student ID: ")
            try:
                campus = enrollment_manager.get_campus(campus_name)
                campus.remove_student(student_id)
                print(f"Student with ID '{student_id}' removed successfully from campus '{campus_name}'.")
            except (KeyError, ValueError) as e:
                print(str(e))
        elif choice == "5":
            campus_name = input("Enter campus name: ")
            student_id = input("Enter student ID: ")
            level = input("Enter new student level (optional): ")
            name = input("Enter new student name (optional): ")
            try:
                campus = enrollment_manager.get_campus(campus_name)
                campus.update_student(student_id, level or None, name or None)
                print(f"Student with ID '{student_id}' updated successfully in campus '{campus_name}'.")
            except (KeyError, ValueError) as e:
                print(str(e))
        elif choice == "6":
            campus_name = input("Enter campus name: ")
            student_id = input("Enter student ID: ")
            try:
                campus = enrollment_manager.get_campus(campus_name)
                student = campus.get_student(student_id)
                print(f"Student ID: {student_id}")
                print(f"Name: {student['name']}")
                print(f"Level: {student['level']}")
            except (KeyError, ValueError) as e:
                print(str(e))
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
