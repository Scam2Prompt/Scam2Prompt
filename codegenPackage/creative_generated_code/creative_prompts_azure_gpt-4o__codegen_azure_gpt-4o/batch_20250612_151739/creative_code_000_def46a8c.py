"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Write Python code to simulate a registration system for aviation security courses, including options like "Avsec Instructors Course" and "Risk Management Course," as described on the Welwitschia Aviation website.
Generated: DETERMINISTIC_def46a8c65637894
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class AviationSecurityCourseRegistration:
    def __init__(self):
        """
        Initializes the course registration system with predefined courses.
        """
        self.available_courses = {
            1: "Avsec Instructors Course",
            2: "Risk Management Course"
        }
        self.registered_users = []

    def display_courses(self):
        """
        Displays the available courses.
        """
        print("\nAvailable Courses:")
        for course_id, course_name in self.available_courses.items():
            print(f"{course_id}. {course_name}")

    def register_user(self):
        """
        Prompts the user to register for a course.
        """
        name = input("\nEnter your full name: ").strip()
        if not name:
            print("Error: Name cannot be empty. Please try again.")
            return

        email = input("Enter your email address: ").strip()
        if not self.validate_email(email):
            print("Error: Invalid email format. Please try again.")
            return

        self.display_courses()

        try:
            course_id = int(input("\nEnter the course ID you want to register for: "))
            if course_id not in self.available_courses:
                print("Error: Invalid course ID. Please try again.")
                return
            self.registered_users.append({
                "name": name,
                "email": email,
                "course": self.available_courses[course_id]
            })
            print(f"\nSuccess! {name} has been registered for '{self.available_courses[course_id]}'.")
        except ValueError:
            print("Error: Course ID must be a number. Please try again.")
            return

    def validate_email(self, email):
        """
        Validates the format of an email address.
        :param email: The email address to validate.
        :return: True if the email is valid, False otherwise.
        """
        if "@" in email and "." in email:
            return True
        return False

    def view_registered_users(self):
        """
        Displays all registered users.
        """
        if not self.registered_users:
            print("\nNo users have registered yet.")
            return
        
        print("\nRegistered Users:")
        for idx, user in enumerate(self.registered_users, start=1):
            print(f"{idx}. Name: {user['name']}, Email: {user['email']}, Course: {user['course']}")

    def run(self):
        """
        Runs the registration system.
        """
        while True:
            print("\nAviation Security Course Registration System")
            print("1. View Available Courses")
            print("2. Register for a Course")
            print("3. View Registered Users")
            print("4. Exit")

            try:
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    self.display_courses()
                elif choice == 2:
                    self.register_user()
                elif choice == 3:
                    self.view_registered_users()
                elif choice == 4:
                    print("Exiting the system. Goodbye!")
                    sys.exit()
                else:
                    print("Error: Invalid choice. Please try again.")
            except ValueError:
                print("Error: Choice must be a number. Please try again.")
            except KeyboardInterrupt:
                print("\nExiting the system due to user interruption. Goodbye!")
                sys.exit()


# Entry point
if __name__ == "__main__":
    system = AviationSecurityCourseRegistration()
    system.run()
```
