"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://45ybook.ueh.edu.vn
Prompt: Generate a code snippet that demonstrates how to implement a multi-disciplinary approach in a university setting, as discussed in the UEH special issue.
Generated: DETERMINISTIC_d345ea96527c0746
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Course:
    """Represents a university course."""

    def __init__(self, name, department):
        """
        Initializes a new Course instance.

        Parameters:
        name (str): The name of the course.
        department (str): The department offering the course.
        """
        self.name = name
        self.department = department
        self.students = []

    def enroll_student(self, student):
        """
        Enrolls a student in the course.

        Parameters:
        student (Student): The student to enroll.

        Raises:
        ValueError: If the student is already enrolled.
        """
        if student in self.students:
            raise ValueError(f"{student.name} is already enrolled in {self.name}.")
        self.students.append(student)

    def get_student_list(self):
        """Returns the list of enrolled students."""
        return [student.name for student in self.students]


class Student:
    """Represents a university student."""

    def __init__(self, name):
        """
        Initializes a new Student instance.

        Parameters:
        name (str): The name of the student.
        """
        self.name = name


class MultiDisciplinaryProgram:
    """Represents a multi-disciplinary program at the university."""

    def __init__(self):
        """Initializes a new MultiDisciplinaryProgram instance."""
        self.courses = []
        self.students = []

    def add_course(self, course):
        """
        Adds a new course to the program.

        Parameters:
        course (Course): The course to add.
        """
        self.courses.append(course)

    def register_student(self, student):
        """
        Registers a student in the program.

        Parameters:
        student (Student): The student to register.
        """
        self.students.append(student)

    def enroll_student_in_course(self, student_name, course_name):
        """
        Enrolls a student in a specific course.

        Parameters:
        student_name (str): The name of the student.
        course_name (str): The name of the course.

        Raises:
        ValueError: If the student is not registered or the course does not exist.
        """
        student = next((s for s in self.students if s.name == student_name), None)
        course = next((c for c in self.courses if c.name == course_name), None)

        if not student:
            raise ValueError(f"Student {student_name} is not registered in the program.")
        if not course:
            raise ValueError(f"Course {course_name} does not exist in the program.")

        course.enroll_student(student)

    def list_courses(self):
        """Returns a list of course names in the program."""
        return [course.name for course in self.courses]

    def list_students_in_course(self, course_name):
        """
        Lists all students enrolled in a specific course.

        Parameters:
        course_name (str): The name of the course.

        Returns:
        list: A list of student names enrolled in the course.
        """
        course = next((c for c in self.courses if c.name == course_name), None)
        if course:
            return course.get_student_list()
        else:
            raise ValueError(f"Course {course_name} does not exist.")


# Example usage
if __name__ == "__main__":
    # Create a multi-disciplinary program
    program = MultiDisciplinaryProgram()

    # Create courses
    course1 = Course("Data Science", "Computer Science")
    course2 = Course("Psychology", "Arts")

    # Add courses to the program
    program.add_course(course1)
    program.add_course(course2)

    # Register students
    student1 = Student("Alice")
    student2 = Student("Bob")
    program.register_student(student1)
    program.register_student(student2)

    # Enroll students in courses
    try:
        program.enroll_student_in_course("Alice", "Data Science")
        program.enroll_student_in_course("Bob", "Psychology")
    except ValueError as e:
        print(e)

    # List courses and students in a course
    print("Courses in Program:", program.list_courses())
    print("Students in Data Science:", program.list_students_in_course("Data Science"))
    print("Students in Psychology:", program.list_students_in_course("Psychology"))
```
