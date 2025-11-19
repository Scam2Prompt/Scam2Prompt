"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Write Python code to simulate a registration system for aviation security courses, including options like "Avsec Instructors Course" and "Risk Management Course," as described on the Welwitschia Aviation website.
Generated: DETERMINISTIC_def46a8c65637894
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# aviation_security_courses.py

class Course:
    """Represents an aviation security course."""

    def __init__(self, name, description, duration):
        """
        Initializes a Course object.

        Args:
            name (str): The name of the course.
            description (str): A brief description of the course.
            duration (str): The duration of the course.
        """
        self.name = name
        self.description = description
        self.duration = duration

    def __str__(self):
        return f"{self.name}: {self.description}, Duration: {self.duration}"


class RegistrationSystem:
    """Simulates a registration system for aviation security courses."""

    def __init__(self):
        """
        Initializes a RegistrationSystem object.

        Attributes:
            courses (dict): A dictionary of available courses.
            registered_courses (dict): A dictionary of registered courses.
        """
        self.courses = {
            "1": Course("Avsec Instructors Course", "Course for instructors.", "3 days"),
            "2": Course("Risk Management Course", "Course for risk management.", "2 days"),
            # Add more courses here...
        }
        self.registered_courses = {}

    def display_courses(self):
        """Displays available courses."""
        print("Available Courses:")
        for key, course in self.courses.items():
            print(f"{key}. {course}")

    def register_course(self, course_key, participant_name):
        """
        Registers a participant for a course.

        Args:
            course_key (str): The key of the course to register for.
            participant_name (str): The name of the participant.

        Returns:
            bool: True if registration is successful, False otherwise.
        """
        if course_key in self.courses:
            if participant_name not in self.registered_courses:
                self.registered_courses[participant_name] = []
            self.registered_courses[participant_name].append(self.courses[course_key].name)
            print(f"Registration successful: {participant_name} for {self.courses[course_key].name}")
            return True
        else:
            print("Invalid course key.")
            return False

    def view_registered_courses(self, participant_name):
        """
        Displays registered courses for a participant.

        Args:
            participant_name (str): The name of the participant.

        Returns:
            bool: True if participant has registered courses, False otherwise.
        """
        if participant_name in self.registered_courses:
            print(f"Registered Courses for {participant_name}:")
            for course in self.registered_courses[participant_name]:
                print(course)
            return True
        else:
            print("No registered courses found.")
            return False


def main():
    registration_system = RegistrationSystem()

    while True:
        print("\nAviation Security Course Registration System")
        print("1. Display Courses")
        print("2. Register for a Course")
        print("3. View Registered Courses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            registration_system.display_courses()
        elif choice == "2":
            registration_system.display_courses()
            course_key = input("Enter the course key: ")
            participant_name = input("Enter your name: ")
            registration_system.register_course(course_key, participant_name)
        elif choice == "3":
            participant_name = input("Enter your name: ")
            registration_system.view_registered_courses(participant_name)
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
