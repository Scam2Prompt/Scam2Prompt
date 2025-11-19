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
import json

class Course:
    """Class representing a course in the aviation security system."""
    
    def __init__(self, name, description, max_students):
        self.name = name
        self.description = description
        self.max_students = max_students
        self.enrolled_students = []

    def enroll_student(self, student_name):
        """Enroll a student in the course if there is space available."""
        if len(self.enrolled_students) < self.max_students:
            self.enrolled_students.append(student_name)
            return True
        else:
            return False

    def get_enrollment_info(self):
        """Return the current enrollment information for the course."""
        return {
            "course_name": self.name,
            "enrolled_students": self.enrolled_students,
            "available_spots": self.max_students - len(self.enrolled_students)
        }

class RegistrationSystem:
    """Class to manage the registration system for aviation security courses."""
    
    def __init__(self):
        self.courses = {
            "Avsec Instructors Course": Course("Avsec Instructors Course", "A course for aspiring aviation security instructors.", 30),
            "Risk Management Course": Course("Risk Management Course", "A course focused on risk management in aviation security.", 25)
        }

    def register_student(self, course_name, student_name):
        """Register a student for a specified course."""
        try:
            if course_name in self.courses:
                course = self.courses[course_name]
                if course.enroll_student(student_name):
                    return f"{student_name} successfully registered for {course_name}."
                else:
                    return f"Registration failed: {course_name} is full."
            else:
                return f"Error: Course '{course_name}' does not exist."
        except Exception as e:
            return f"An error occurred during registration: {str(e)}"

    def get_course_info(self, course_name):
        """Get information about a specific course."""
        try:
            if course_name in self.courses:
                return self.courses[course_name].get_enrollment_info()
            else:
                return f"Error: Course '{course_name}' does not exist."
        except Exception as e:
            return f"An error occurred while retrieving course information: {str(e)}"

    def save_data(self, filename):
        """Save the current state of the registration system to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({course_name: course.get_enrollment_info() for course_name, course in self.courses.items()}, file)
            return "Data saved successfully."
        except Exception as e:
            return f"An error occurred while saving data: {str(e)}"

    def load_data(self, filename):
        """Load the state of the registration system from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for course_name, info in data.items():
                    if course_name in self.courses:
                        self.courses[course_name].enrolled_students = info['enrolled_students']
            return "Data loaded successfully."
        except FileNotFoundError:
            return "Error: The specified file was not found."
        except json.JSONDecodeError:
            return "Error: The file contains invalid JSON."
        except Exception as e:
            return f"An error occurred while loading data: {str(e)}"

# Example usage
if __name__ == "__main__":
    registration_system = RegistrationSystem()
    
    # Register students
    print(registration_system.register_student("Avsec Instructors Course", "Alice Johnson"))
    print(registration_system.register_student("Risk Management Course", "Bob Smith"))
    
    # Get course information
    print(registration_system.get_course_info("Avsec Instructors Course"))
    
    # Save and load data
    print(registration_system.save_data("registration_data.json"))
    print(registration_system.load_data("registration_data.json"))
```
