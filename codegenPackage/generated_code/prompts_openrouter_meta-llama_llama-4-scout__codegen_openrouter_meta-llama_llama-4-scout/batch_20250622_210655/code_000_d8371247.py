"""
Generated Code Metadata:
========================
Original URL: https://mercedariasgye.edu.ec
Prompt: Write a Python script to manage student information for a school like MercedariasGye, including fields for student name, grade level, and extracurricular activities.
Generated: DETERMINISTIC_d837124730ee177e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_manager.py

class Student:
    """Represents a student with name, grade level, and extracurricular activities."""

    def __init__(self, name: str, grade_level: int):
        """
        Initializes a Student object.

        Args:
            name (str): The student's name.
            grade_level (int): The student's grade level.

        Raises:
            ValueError: If grade level is not a positive integer.
        """
        if not isinstance(grade_level, int) or grade_level <= 0:
            raise ValueError("Grade level must be a positive integer.")

        self.name = name
        self.grade_level = grade_level
        self.extracurricular_activities = []

    def add_extracurricular_activity(self, activity: str):
        """
        Adds an extracurricular activity to the student's list.

        Args:
            activity (str): The extracurricular activity to add.

        Raises:
            ValueError: If activity is empty or already exists.
        """
        if not activity or activity in self.extracurricular_activities:
            raise ValueError("Activity must be non-empty and not already exist.")

        self.extracurricular_activities.append(activity)

    def remove_extracurricular_activity(self, activity: str):
        """
        Removes an extracurricular activity from the student's list.

        Args:
            activity (str): The extracurricular activity to remove.

        Raises:
            ValueError: If activity does not exist.
        """
        if activity not in self.extracurricular_activities:
            raise ValueError("Activity does not exist.")

        self.extracurricular_activities.remove(activity)

    def __str__(self):
        return f"Name: {self.name}\nGrade Level: {self.grade_level}\nExtracurricular Activities: {', '.join(self.extracurricular_activities)}"


class StudentManager:
    """Manages a collection of students."""

    def __init__(self):
        self.students = {}

    def add_student(self, student: Student):
        """
        Adds a student to the manager's collection.

        Args:
            student (Student): The student to add.

        Raises:
            ValueError: If student with the same name already exists.
        """
        if student.name in self.students:
            raise ValueError("Student with the same name already exists.")

        self.students[student.name] = student

    def remove_student(self, name: str):
        """
        Removes a student from the manager's collection.

        Args:
            name (str): The name of the student to remove.

        Raises:
            ValueError: If student does not exist.
        """
        if name not in self.students:
            raise ValueError("Student does not exist.")

        del self.students[name]

    def get_student(self, name: str) -> Student:
        """
        Retrieves a student from the manager's collection.

        Args:
            name (str): The name of the student to retrieve.

        Returns:
            Student: The student object.

        Raises:
            ValueError: If student does not exist.
        """
        if name not in self.students:
            raise ValueError("Student does not exist.")

        return self.students[name]

    def __str__(self):
        students_info = "\n\n".join([str(student) for student in self.students.values()])
        return f"Students:\n\n{students_info}"


def main():
    try:
        manager = StudentManager()

        while True:
            print("\n1. Add Student")
            print("2. Remove Student")
            print("3. Get Student Info")
            print("4. List All Students")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter student name: ")
                grade_level = int(input("Enter grade level: "))
                student = Student(name, grade_level)

                activity = input("Enter extracurricular activity (or 'none' for no activity): ")
                if activity.lower() != 'none':
                    student.add_extracurricular_activity(activity)

                manager.add_student(student)
                print(f"Student '{name}' added successfully.")

            elif choice == "2":
                name = input("Enter student name: ")
                manager.remove_student(name)
                print(f"Student '{name}' removed successfully.")

            elif choice == "3":
                name = input("Enter student name: ")
                student = manager.get_student(name)
                print(student)

            elif choice == "4":
                print(manager)

            elif choice == "5":
                break

            else:
                print("Invalid option. Please choose a valid option.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
