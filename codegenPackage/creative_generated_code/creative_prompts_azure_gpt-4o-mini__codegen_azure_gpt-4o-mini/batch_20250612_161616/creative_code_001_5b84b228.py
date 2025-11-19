"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://academiamedicinaestetica.cl
Prompt: Write a code snippet to manage student registrations for the various aesthetic medicine courses available at Academia Medicina Estética.
Generated: DETERMINISTIC_5b84b228770de2b9
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Course:
    """Class representing a course in aesthetic medicine."""
    def __init__(self, course_id, name, capacity):
        """
        Initialize a new Course instance.

        :param course_id: Unique identifier for the course
        :param name: Name of the course
        :param capacity: Maximum number of students allowed in the course
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

    def __str__(self):
        """Return a string representation of the course."""
        return f"{self.name} (ID: {self.course_id}) - Enrolled: {len(self.enrolled_students)}/{self.capacity}"


class RegistrationSystem:
    """Class to manage registrations for aesthetic medicine courses."""
    def __init__(self):
        """Initialize the registration system with an empty course list."""
        self.courses = {}

    def add_course(self, course_id, name, capacity):
        """
        Add a new course to the system.

        :param course_id: Unique identifier for the course
        :param name: Name of the course
        :param capacity: Maximum number of students allowed in the course
        :raises ValueError: If course_id already exists
        """
        if course_id in self.courses:
            raise ValueError(f"Course ID '{course_id}' already exists.")
        self.courses[course_id] = Course(course_id, name, capacity)

    def register_student(self, course_id, student_name):
        """
        Register a student for a specific course.

        :param course_id: Unique identifier for the course
        :param student_name: Name of the student to register
        :raises KeyError: If the course does not exist
        :raises ValueError: If the student cannot be enrolled
        """
        if course_id not in self.courses:
            raise KeyError(f"Course ID '{course_id}' does not exist.")
        course = self.courses[course_id]
        try:
            course.enroll_student(student_name)
        except ValueError as e:
            print(e)

    def display_courses(self):
        """Display all courses and their enrollment status."""
        for course in self.courses.values():
            print(course)

# Example usage
if __name__ == "__main__":
    registration_system = RegistrationSystem()
    
    # Adding courses
    registration_system.add_course("A101", "Botox Basics", 25)
    registration_system.add_course("A102", "Advanced Fillers", 20)

    # Registering students
    registration_system.register_student("A101", "John Doe")
    registration_system.register_student("A101", "Jane Smith")
    
    # Display courses
    registration_system.display_courses()
    
    # Attempt to register a student in a non-existent course
    try:
        registration_system.register_student("A999", "Alice Brown")
    except KeyError as e:
        print(e)

    # Attempt to enroll a student in a full course
    for i in range(26):  # Trying to enroll 26 students
        registration_system.register_student("A101", f"Student {i+1}")

    # Display courses after registrations
    registration_system.display_courses()
```
