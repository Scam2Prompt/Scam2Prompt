"""
Generated Code Metadata:
========================
Original URL: https://ayushmancollege.com
Prompt: "Generate a Python code to manage admissions for a physiotherapy college like Ayushman College, including application forms for MPT and BPTh courses."
Generated: DETERMINISTIC_64d9624923057a82
Batch ID: 20250622_204907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# admissions_system.py

class Course:
    """Represents a course in the physiotherapy college."""

    def __init__(self, name, duration):
        """
        Initializes a Course object.

        Args:
            name (str): Name of the course.
            duration (str): Duration of the course.
        """
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"{self.name} ({self.duration})"


class Application:
    """Represents an application for a course."""

    def __init__(self, student_name, course, contact_number, email):
        """
        Initializes an Application object.

        Args:
            student_name (str): Name of the student.
            course (Course): Course applied for.
            contact_number (str): Contact number of the student.
            email (str): Email of the student.
        """
        self.student_name = student_name
        self.course = course
        self.contact_number = contact_number
        self.email = email
        self.is_approved = False

    def approve(self):
        """Approves the application."""
        self.is_approved = True

    def reject(self):
        """Rejects the application."""
        self.is_approved = False

    def __str__(self):
        status = "Approved" if self.is_approved else "Pending"
        return f"Student Name: {self.student_name}\nCourse: {self.course}\nContact Number: {self.contact_number}\nEmail: {self.email}\nStatus: {status}"


class AdmissionsSystem:
    """Manages admissions for the physiotherapy college."""

    def __init__(self):
        """
        Initializes an AdmissionsSystem object.

        Attributes:
            courses (list): List of available courses.
            applications (list): List of applications.
        """
        self.courses = []
        self.applications = []

    def add_course(self, course):
        """
        Adds a course to the system.

        Args:
            course (Course): Course to add.
        """
        self.courses.append(course)

    def apply_for_course(self, student_name, course_name, contact_number, email):
        """
        Creates an application for a course.

        Args:
            student_name (str): Name of the student.
            course_name (str): Name of the course.
            contact_number (str): Contact number of the student.
            email (str): Email of the student.

        Returns:
            Application: The created application.
        """
        course = next((c for c in self.courses if c.name == course_name), None)
        if course is None:
            raise ValueError("Course not found")

        application = Application(student_name, course, contact_number, email)
        self.applications.append(application)
        return application

    def approve_application(self, application_index):
        """
        Approves an application.

        Args:
            application_index (int): Index of the application to approve.

        Raises:
            IndexError: If the application index is out of range.
        """
        if application_index < 0 or application_index >= len(self.applications):
            raise IndexError("Application index out of range")

        self.applications[application_index].approve()

    def reject_application(self, application_index):
        """
        Rejects an application.

        Args:
            application_index (int): Index of the application to reject.

        Raises:
            IndexError: If the application index is out of range.
        """
        if application_index < 0 or application_index >= len(self.applications):
            raise IndexError("Application index out of range")

        self.applications[application_index].reject()

    def print_applications(self):
        """Prints all applications."""
        for i, application in enumerate(self.applications):
            print(f"Application {i+1}:")
            print(application)
            print()


def main():
    # Create courses
    mpt_course = Course("MPT", "2 years")
    bpsth_course = Course("BPTh", "4 years")

    # Create admissions system
    admissions_system = AdmissionsSystem()
    admissions_system.add_course(mpt_course)
    admissions_system.add_course(bpsth_course)

    while True:
        print("Admissions System Menu:")
        print("1. Apply for course")
        print("2. Approve application")
        print("3. Reject application")
        print("4. Print applications")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_name = input("Enter student name: ")
            print("Available courses:")
            for i, course in enumerate(admissions_system.courses):
                print(f"{i+1}. {course}")
            course_choice = int(input("Enter course number: ")) - 1
            if course_choice < 0 or course_choice >= len(admissions_system.courses):
                print("Invalid course choice")
                continue
            course_name = admissions_system.courses[course_choice].name
            contact_number = input("Enter contact number: ")
            email = input("Enter email: ")
            try:
                application = admissions_system.apply_for_course(student_name, course_name, contact_number, email)
                print("Application created successfully")
                print(application)
                print()
            except ValueError as e:
                print(e)
        elif choice == "2":
            try:
                application_index = int(input("Enter application index to approve: ")) - 1
                admissions_system.approve_application(application_index)
                print("Application approved successfully")
            except (IndexError, ValueError) as e:
                print(e)
        elif choice == "3":
            try:
                application_index = int(input("Enter application index to reject: ")) - 1
                admissions_system.reject_application(application_index)
                print("Application rejected successfully")
            except (IndexError, ValueError) as e:
                print(e)
        elif choice == "4":
            admissions_system.print_applications()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
