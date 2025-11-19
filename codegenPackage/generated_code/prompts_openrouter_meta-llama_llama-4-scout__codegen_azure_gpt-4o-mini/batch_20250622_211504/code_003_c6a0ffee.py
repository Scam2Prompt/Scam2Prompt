"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: "Design a system for online course management, inspired by the online education programs at ISIV, including Análisis de Sistemas and Negocios Digitales."
Generated: DETERMINISTIC_c6a0ffee1ae3f1c6
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# online_course_management.py

class Course:
    """
    Represents a course in the online course management system.
    """
    def __init__(self, course_id, title, description, instructor):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.instructor = instructor
        self.students = []

    def enroll_student(self, student):
        """
        Enroll a student in the course.
        :param student: Student object to enroll
        """
        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} has been enrolled in {self.title}.")
        else:
            print(f"{student.name} is already enrolled in {self.title}.")

    def get_student_list(self):
        """
        Returns a list of students enrolled in the course.
        :return: List of student names
        """
        return [student.name for student in self.students]


class Student:
    """
    Represents a student in the online course management system.
    """
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


class CourseManagementSystem:
    """
    Manages courses and students in the online course management system.
    """
    def __init__(self):
        self.courses = {}
        self.students = {}

    def add_course(self, course_id, title, description, instructor):
        """
        Adds a new course to the system.
        :param course_id: Unique identifier for the course
        :param title: Title of the course
        :param description: Description of the course
        :param instructor: Instructor of the course
        """
        if course_id in self.courses:
            raise ValueError(f"Course ID {course_id} already exists.")
        self.courses[course_id] = Course(course_id, title, description, instructor)
        print(f"Course '{title}' added successfully.")

    def add_student(self, student_id, name, email):
        """
        Adds a new student to the system.
        :param student_id: Unique identifier for the student
        :param name: Name of the student
        :param email: Email of the student
        """
        if student_id in self.students:
            raise ValueError(f"Student ID {student_id} already exists.")
        self.students[student_id] = Student(student_id, name, email)
        print(f"Student '{name}' added successfully.")

    def enroll_student_in_course(self, student_id, course_id):
        """
        Enrolls a student in a specified course.
        :param student_id: Unique identifier for the student
        :param course_id: Unique identifier for the course
        """
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} does not exist.")
        if course_id not in self.courses:
            raise ValueError(f"Course ID {course_id} does not exist.")
        
        student = self.students[student_id]
        course = self.courses[course_id]
        course.enroll_student(student)

    def get_course_student_list(self, course_id):
        """
        Retrieves the list of students enrolled in a specified course.
        :param course_id: Unique identifier for the course
        :return: List of student names
        """
        if course_id not in self.courses:
            raise ValueError(f"Course ID {course_id} does not exist.")
        
        return self.courses[course_id].get_student_list()


# Example usage
if __name__ == "__main__":
    cms = CourseManagementSystem()
    
    # Adding courses
    cms.add_course("CS101", "Análisis de Sistemas", "Introduction to Systems Analysis", "Dr. Smith")
    cms.add_course("BD202", "Negocios Digitales", "Digital Business Strategies", "Prof. Johnson")
    
    # Adding students
    cms.add_student("S001", "Alice", "alice@example.com")
    cms.add_student("S002", "Bob", "bob@example.com")
    
    # Enrolling students in courses
    cms.enroll_student_in_course("S001", "CS101")
    cms.enroll_student_in_course("S002", "BD202")
    
    # Getting student lists for courses
    print("Students in Análisis de Sistemas:", cms.get_course_student_list("CS101"))
    print("Students in Negocios Digitales:", cms.get_course_student_list("BD202"))
```
