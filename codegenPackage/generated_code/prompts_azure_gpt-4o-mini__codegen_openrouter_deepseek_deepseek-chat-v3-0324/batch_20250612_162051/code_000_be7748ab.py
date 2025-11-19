"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: Generate a Python script to automate the registration process for a sewing course at Workshop Granada, including options for both online and in-person classes.
Generated: DETERMINISTIC_be7748ab9af4be65
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
import json
from datetime import datetime
from typing import Dict, Optional, List

class SewingCourseRegistration:
    """
    A class to handle the registration process for a sewing course at Workshop Granada.
    Supports both online and in-person class registrations.
    """

    def __init__(self):
        """Initialize the registration system with default values."""
        self.available_courses = {
            "beginner": {
                "online": {"schedule": "Mon/Wed 6-8pm", "price": 120, "seats": 15},
                "in_person": {"schedule": "Tue/Thu 6-8pm", "price": 150, "seats": 10}
            },
            "intermediate": {
                "online": {"schedule": "Mon/Wed 8-10pm", "price": 140, "seats": 15},
                "in_person": {"schedule": "Tue/Thu 8-10pm", "price": 170, "seats": 10}
            },
            "advanced": {
                "online": {"schedule": "Fri 4-8pm", "price": 160, "seats": 12},
                "in_person": {"schedule": "Sat 10am-2pm", "price": 190, "seats": 8}
            }
        }
        self.registrations = []

    def display_courses(self) -> None:
        """Display available courses with their details."""
        print("\nAvailable Sewing Courses at Workshop Granada:")
        print("-------------------------------------------")
        for level, modes in self.available_courses.items():
            print(f"\n{level.capitalize()} Level:")
            for mode, details in modes.items():
                mode_display = "Online" if mode == "online" else "In-Person"
                print(f"  {mode_display}:")
                print(f"    Schedule: {details['schedule']}")
                print(f"    Price: ${details['price']}")
                print(f"    Seats Available: {details['seats']}")

    def validate_input(self, prompt: str, valid_options: List[str]) -> str:
        """
        Validate user input against a list of valid options.
        
        Args:
            prompt: The input prompt to display to the user
            valid_options: List of valid input options
            
        Returns:
            The validated user input
        """
        while True:
            user_input = input(prompt).strip().lower()
            if user_input in valid_options:
                return user_input
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

    def collect_student_info(self) -> Dict:
        """
        Collect student registration information.
        
        Returns:
            Dictionary containing student information
        """
        print("\nPlease provide your registration details:")
        student = {
            "name": input("Full Name: ").strip(),
            "email": input("Email: ").strip(),
            "phone": input("Phone Number: ").strip(),
            "level": self.validate_input(
                "Course Level (beginner/intermediate/advanced): ",
                ["beginner", "intermediate", "advanced"]
            ),
            "mode": self.validate_input(
                "Class Mode (online/in_person): ",
                ["online", "in_person"]
            )
        }
        return student

    def process_registration(self, student: Dict) -> bool:
        """
        Process the student registration if seats are available.
        
        Args:
            student: Dictionary containing student information
            
        Returns:
            True if registration was successful, False otherwise
        """
        course = self.available_courses[student["level"]][student["mode"]]
        
        if course["seats"] <= 0:
            print("\nSorry, no seats available for this course.")
            return False
        
        # Reduce available seats
        course["seats"] -= 1
        
        # Create registration record
        registration = {
            "student": student,
            "course_details": course.copy(),
            "registration_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "confirmation_number": f"WG-{datetime.now().timestamp():.0f}"
        }
        self.registrations.append(registration)
        return True

    def display_confirmation(self, registration: Dict) -> None:
        """Display registration confirmation details."""
        student = registration["student"]
        course = registration["course_details"]
        mode_display = "Online" if student["mode"] == "online" else "In-Person"
        
        print("\nRegistration Confirmation")
        print("------------------------")
        print(f"Confirmation Number: {registration['confirmation_number']}")
        print(f"Student Name: {student['name']}")
        print(f"Email: {student['email']}")
        print(f"Phone: {student['phone']}")
        print(f"\nCourse: {student['level'].capitalize()} Level Sewing")
        print(f"Mode: {mode_display}")
        print(f"Schedule: {course['schedule']}")
        print(f"Price: ${course['price']}")
        print(f"\nRegistration Date: {registration['registration_date']}")
        print("\nThank you for registering with Workshop Granada!")

    def save_registration(self, registration: Dict) -> None:
        """Save registration to a JSON file."""
        filename = f"registration_{registration['confirmation_number']}.json"
        try:
            with open(filename, 'w') as f:
                json.dump(registration, f, indent=2)
            print(f"\nRegistration details saved to {filename}")
        except IOError as e:
            print(f"\nError saving registration: {e}")

    def run(self) -> None:
        """Main method to run the registration process."""
        print("Welcome to Workshop Granada Sewing Course Registration")
        print("----------------------------------------------------")
        
        while True:
            self.display_courses()
            
            # Collect student information
            student = self.collect_student_info()
            
            # Process registration
            if self.process_registration(student):
                registration = self.registrations[-1]
                self.display_confirmation(registration)
                self.save_registration(registration)
            else:
                print("Registration could not be completed.")
            
            # Ask if user wants to register another student
            another = self.validate_input(
                "\nRegister another student? (yes/no): ",
                ["yes", "no"]
            )
            if another == "no":
                print("\nThank you for using Workshop Granada Registration System!")
                break

if __name__ == "__main__":
    try:
        registration_system = SewingCourseRegistration()
        registration_system.run()
    except KeyboardInterrupt:
        print("\nRegistration process cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)
```
