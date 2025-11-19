"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: "Generate a Python script to manage student enrollment for a dental hygiene program with a duration of 2 years, similar to the Técnico Superior Universitario en Higienista Dental offered by INESO."
Generated: DETERMINISTIC_40dc1f7fc2250cfd
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_enrollment.py

class Student:
    """Represents a student enrolled in the dental hygiene program."""

    def __init__(self, student_id, name, email, phone_number):
        """
        Initializes a Student object.

        Args:
            student_id (str): Unique identifier for the student.
            name (str): Student's name.
            email (str): Student's email address.
            phone_number (str): Student's phone number.
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Email: {self.email}, Phone Number: {self.phone_number}"


class EnrollmentProgram:
    """Manages student enrollment for the dental hygiene program."""

    def __init__(self, program_name, duration):
        """
        Initializes an EnrollmentProgram object.

        Args:
            program_name (str): Name of the dental hygiene program.
            duration (int): Duration of the program in years.
        """
        self.program_name = program_name
        self.duration = duration
        self.students = {}

    def enroll_student(self, student):
        """
        Enrolls a student in the program.

        Args:
            student (Student): Student to be enrolled.

        Raises:
            ValueError: If a student with the same ID already exists.
        """
        if student.student_id in self.students:
            raise ValueError("Student with the same ID already exists.")
        self.students[student.student_id] = student

    def drop_student(self, student_id):
        """
        Drops a student from the program.

        Args:
            student_id (str): ID of the student to be dropped.

        Raises:
            KeyError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise KeyError("Student ID does not exist.")
        del self.students[student_id]

    def get_student(self, student_id):
        """
        Retrieves a student's information.

        Args:
            student_id (str): ID of the student.

        Returns:
            Student: Student object if found, otherwise None.
        """
        return self.students.get(student_id)

    def list_students(self):
        """Returns a list of all enrolled students."""
        return list(self.students.values())


def main():
    try:
        # Create a dental hygiene program with a duration of 2 years
        program = EnrollmentProgram("Técnico Superior Universitario en Higienista Dental", 2)

        while True:
            print("\n1. Enroll Student")
            print("2. Drop Student")
            print("3. Get Student Info")
            print("4. List Students")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                email = input("Enter student email: ")
                phone_number = input("Enter student phone number: ")

                student = Student(student_id, name, email, phone_number)
                program.enroll_student(student)
                print(f"Student {name} enrolled successfully.")

            elif choice == "2":
                student_id = input("Enter student ID: ")
                program.drop_student(student_id)
                print(f"Student with ID {student_id} dropped successfully.")

            elif choice == "3":
                student_id = input("Enter student ID: ")
                student = program.get_student(student_id)
                if student:
                    print(student)
                else:
                    print("Student not found.")

            elif choice == "4":
                students = program.list_students()
                for student in students:
                    print(student)

            elif choice == "5":
                break

            else:
                print("Invalid option. Please choose a valid option.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
