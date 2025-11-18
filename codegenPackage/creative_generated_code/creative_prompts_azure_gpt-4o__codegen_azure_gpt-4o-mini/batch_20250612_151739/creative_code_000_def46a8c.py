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
class Course:
    """Class representing a course in the aviation security system."""
    
    def __init__(self, name, description, capacity):
        self.name = name
        self.description = description
        self.capacity = capacity
        self.enrolled_students = []

    def enroll_student(self, student_name):
        """Enroll a student in the course if there's available capacity."""
        if len(self.enrolled_students) < self.capacity:
            self.enrolled_students.append(student_name)
            return True
        else:
            return False

    def get_enrollment_status(self):
        """Return the current enrollment status of the course."""
        return len(self.enrolled_students), self.capacity

class RegistrationSystem:
    """Class to manage the registration for aviation security courses."""

    def __init__(self):
        self.courses = {
            "Avsec Instructors Course": Course(
                "Avsec Instructors Course",
                "Course for aspiring aviation security instructors.",
                30
            ),
            "Risk Management Course": Course(
                "Risk Management Course",
                "Course focusing on risk management in aviation.",
                25
            ),
        }

    def register_student(self, course_name, student_name):
        """Register a student for the specified course."""
        try:
            if course_name in self.courses:
                course = self.courses[course_name]
                if course.enroll_student(student_name):
                    return f"{student_name} has been successfully enrolled in {course_name}."
                else:
                    return f"{course_name} is full. Unable to enroll {student_name}."
            else:
                return f"Course '{course_name}' does not exist."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def get_courses(self):
        """Return a list of available courses with their enrollment status."""
        course_info = {}
        for course_name, course in self.courses.items():
            enrolled, capacity = course.get_enrollment_status()
            course_info[course_name] = {
                "description": course.description,
                "enrolled": enrolled,
                "capacity": capacity
            }
        return course_info

def main():
    """Main function to simulate the registration system."""
    system = RegistrationSystem()

    # Display available courses
    print("Available Courses:")
    for course_name, info in system.get_courses().items():
        print(f"{course_name}: {info['description']} (Enrolled: {info['enrolled']}/{info['capacity']})")

    # Simulate student registrations
    print(system.register_student("Avsec Instructors Course", "Alice Smith"))
    print(system.register_student("Risk Management Course", "Bob Johnson"))
    print(system.register_student("Risk Management Course", "Charlie Brown"))
    print(system.register_student("Non-existent Course", "David Wilson"))  # Testing invalid course

    # Display updated courses enrollment
    print("\nUpdated Courses:")
    for course_name, info in system.get_courses().items():
        print(f"{course_name}: {info['description']} (Enrolled: {info['enrolled']}/{info['capacity']})")

if __name__ == "__main__":
    main()
```
