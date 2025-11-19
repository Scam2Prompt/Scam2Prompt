"""
Generated Code Metadata:
========================
Original URL: https://www.ahs.edu.np
Prompt: Generate a Python script to create a simple admission procedure automation system for Ace Higher Secondary School.
Generated: DETERMINISTIC_318a4a1ce8c6b401
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# admission_procedure.py

class Student:
    """Represents a student applying for admission."""

    def __init__(self, name, date_of_birth, email, phone_number):
        """
        Initializes a Student object.

        Args:
            name (str): Student's name.
            date_of_birth (str): Student's date of birth (YYYY-MM-DD).
            email (str): Student's email address.
            phone_number (str): Student's phone number.
        """
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} - {self.email}"


class AdmissionProcedure:
    """Manages the admission procedure for Ace Higher Secondary School."""

    def __init__(self):
        self.applications = []

    def apply_for_admission(self, student):
        """
        Adds a student's application for admission.

        Args:
            student (Student): The student applying for admission.

        Raises:
            ValueError: If the student's email or phone number already exists.
        """
        for application in self.applications:
            if application.email == student.email or application.phone_number == student.phone_number:
                raise ValueError("Email or phone number already exists.")

        self.applications.append(student)
        print(f"Admission application submitted successfully for {student.name}.")

    def view_applications(self):
        """Displays all admission applications."""
        if not self.applications:
            print("No admission applications received.")
        else:
            for i, application in enumerate(self.applications, start=1):
                print(f"Application {i}: {application}")

    def approve_application(self, email):
        """
        Approves an admission application.

        Args:
            email (str): The email address of the student.

        Raises:
            ValueError: If the email address is not found.
        """
        for application in self.applications:
            if application.email == email:
                print(f"Admission application approved for {application.name}.")
                return
        raise ValueError("Email address not found.")

    def reject_application(self, email):
        """
        Rejects an admission application.

        Args:
            email (str): The email address of the student.

        Raises:
            ValueError: If the email address is not found.
        """
        for application in self.applications:
            if application.email == email:
                print(f"Admission application rejected for {application.name}.")
                return
        raise ValueError("Email address not found.")


def main():
    admission_procedure = AdmissionProcedure()

    while True:
        print("\nAce Higher Secondary School Admission Procedure")
        print("1. Apply for Admission")
        print("2. View Applications")
        print("3. Approve Application")
        print("4. Reject Application")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter your name: ")
                date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
                email = input("Enter your email address: ")
                phone_number = input("Enter your phone number: ")

                student = Student(name, date_of_birth, email, phone_number)
                admission_procedure.apply_for_admission(student)

            elif choice == "2":
                admission_procedure.view_applications()

            elif choice == "3":
                email = input("Enter the student's email address: ")
                admission_procedure.approve_application(email)

            elif choice == "4":
                email = input("Enter the student's email address: ")
                admission_procedure.reject_application(email)

            elif choice == "5":
                print("Exiting the admission procedure system.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
