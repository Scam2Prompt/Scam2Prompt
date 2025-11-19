"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Generate a Python code snippet to manage student enrollment and course scheduling for a music school like Московский Колледж Импровизационной Музыки, considering factors like faculty availability, room assignments, and student prerequisites.
Generated: DETERMINISTIC_81a0d6ff3ca457c6
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime


class Course:
    """
    Represents a course in the music school.
    """
    def __init__(self, name, faculty, room, schedule, prerequisites=None):
        """
        Initialize a course with name, faculty, room, schedule, and prerequisites.

        :param name: Name of the course
        :param faculty: Faculty member teaching the course
        :param room: Room assigned for the course
        :param schedule: Schedule of the course (list of datetime objects)
        :param prerequisites: List of prerequisite courses (default: None)
        """
        self.name = name
        self.faculty = faculty
        self.room = room
        self.schedule = schedule
        self.prerequisites = prerequisites or []


class Student:
    """
    Represents a student in the music school.
    """
    def __init__(self, name):
        """
        Initialize a student with a name and an empty list of enrolled courses.

        :param name: Name of the student
        """
        self.name = name
        self.enrolled_courses = []

    def enroll(self, course):
        """
        Enroll the student in a course if prerequisites are met and no schedule conflicts exist.

        :param course: Course object to enroll in
        :raises ValueError: If prerequisites are not met or schedule conflicts exist
        """
        # Check prerequisites
        for prerequisite in course.prerequisites:
            if prerequisite not in [c.name for c in self.enrolled_courses]:
                raise ValueError(f"Prerequisite '{prerequisite}' not met for course '{course.name}'.")

        # Check schedule conflicts
        for enrolled_course in self.enrolled_courses:
            for scheduled_time in course.schedule:
                if scheduled_time in enrolled_course.schedule:
                    raise ValueError(f"Schedule conflict detected with course '{enrolled_course.name}'.")

        # Enroll in the course
        self.enrolled_courses.append(course)


class MusicSchool:
    """
    Represents the music school, managing courses, students, and faculty availability.
    """
    def __init__(self):
        """
        Initialize the music school with empty lists for courses and students.
        """
        self.courses = []
        self.students = []

    def add_course(self, course):
        """
        Add a course to the school.

        :param course: Course object to add
        """
        self.courses.append(course)

    def add_student(self, student):
        """
        Add a student to the school.

        :param student: Student object to add
        """
        self.students.append(student)

    def get_available_courses(self):
        """
        Get a list of all available courses.

        :return: List of course names
        """
        return [course.name for course in self.courses]

    def get_student_schedule(self, student_name):
        """
        Get the schedule of a specific student.

        :param student_name: Name of the student
        :return: List of course names and schedules
        :raises ValueError: If the student is not found
        """
        student = next((s for s in self.students if s.name == student_name), None)
        if not student:
            raise ValueError(f"Student '{student_name}' not found.")
        return [(course.name, course.schedule) for course in student.enrolled_courses]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the music school
        school = MusicSchool()

        # Create courses
        course1 = Course(
            name="Jazz Improvisation",
            faculty="Dr. Smith",
            room="Room 101",
            schedule=[datetime.datetime(2023, 10, 1, 10, 0), datetime.datetime(2023, 10, 3, 10, 0)],
            prerequisites=[]
        )
        course2 = Course(
            name="Advanced Harmony",
            faculty="Prof. Johnson",
            room="Room 102",
            schedule=[datetime.datetime(2023, 10, 1, 12, 0), datetime.datetime(2023, 10, 3, 12, 0)],
            prerequisites=["Jazz Improvisation"]
        )

        # Add courses to the school
        school.add_course(course1)
        school.add_course(course2)

        # Create a student
        student = Student(name="Alice")

        # Add student to the school
        school.add_student(student)

        # Enroll the student in courses
        student.enroll(course1)  # Successful enrollment
        student.enroll(course2)  # Successful enrollment (prerequisite met)

        # Print student schedule
        print(f"{student.name}'s Schedule:")
        for course_name, schedule in school.get_student_schedule(student.name):
            print(f"{course_name}: {schedule}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
