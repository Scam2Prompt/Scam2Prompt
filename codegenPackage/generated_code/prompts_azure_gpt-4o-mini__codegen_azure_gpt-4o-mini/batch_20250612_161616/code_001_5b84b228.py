"""
Generated Code Metadata:
========================
Original URL: https://academiamedicinaestetica.cl
Prompt: Write a code snippet to manage student registrations for the various aesthetic medicine courses available at Academia Medicina Estética.
Generated: DETERMINISTIC_5b84b228770de2b9
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Course:
    """Class representing a course in aesthetic medicine."""
    
    def __init__(self, course_id, name, capacity):
        """
        Initialize a new course.

        :param course_id: Unique identifier for the course
        :param name: Name of the course
        :param capacity: Maximum number of students that can enroll
        """
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.enrolled_students = []

    def enroll_student(self, student_name):
        """
        Enroll a student in the course if there is capacity.

        :param student_name: Name of the student to enroll
        :raises ValueError: If the course is full
        """
        if len(self.enrolled_students) >= self.capacity:
            raise ValueError(f"Cannot enroll {student_name}: Course '{self.name}' is full.")
        self.enrolled_students.append(student_name)

    def get_enrolled_students(self):
        """Return a list of students currently enrolled in the course."""
        return self.enrolled_students


class RegistrationSystem:
    """Class to manage student registrations for courses."""
    
    def __init__(self):
        """Initialize the registration system with an empty course list."""
        self.courses = {}

    def add_course(self, course):
        """
        Add a new course to the registration system.

        :param course: Course object to add
        :raises ValueError: If a course with the same ID already exists
        """
        if course.course_id in self.courses:
            raise ValueError(f"Course with ID {course.course_id} already exists.")
        self.courses[course.course_id] = course

    def register_student(self, course_id, student_name):
        """
        Register a student for a specific course.

        :param course_id: ID of the course to register the student in
        :param student_name: Name of the student to register
        :raises KeyError: If the course ID does not exist
        :raises ValueError: If the student cannot be enrolled
        """
        if course_id not in self.courses:
            raise KeyError(f"Course with ID {course_id} does not exist.")
        
        course = self.courses[course_id]
        course.enroll_student(student_name)

    def get_course_enrollment(self, course_id):
        """
        Get the list of enrolled students for a specific course.

        :param course_id: ID of the course to check
        :raises KeyError: If the course ID does not exist
        :return: List of enrolled students
        """
        if course_id not in self.courses:
            raise KeyError(f"Course with ID {course_id} does not exist.")
        
        return self.courses[course_id].get_enrolled_students()


# Example usage
if __name__ == "__main__":
    try:
        # Create a registration system
        registration_system = RegistrationSystem()

        # Create courses
        course1 = Course(course_id="AEST101", name="Introduction to Aesthetic Medicine", capacity=2)
        course2 = Course(course_id="AEST102", name="Advanced Aesthetic Techniques", capacity=3)

        # Add courses to the registration system
        registration_system.add_course(course1)
        registration_system.add_course(course2)

        # Register students
        registration_system.register_student("AEST101", "Alice Smith")
        registration_system.register_student("AEST101", "Bob Johnson")
        
        # Attempt to register a third student in a full course
        registration_system.register_student("AEST101", "Charlie Brown")  # This will raise an error

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

    # Display enrolled students for a course
    print("Enrolled students in AEST101:", registration_system.get_course_enrollment("AEST101"))
    print("Enrolled students in AEST102:", registration_system.get_course_enrollment("AEST102"))
```
