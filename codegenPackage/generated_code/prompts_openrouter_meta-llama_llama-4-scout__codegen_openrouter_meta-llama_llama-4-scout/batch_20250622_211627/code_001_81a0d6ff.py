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
from datetime import datetime, timedelta

class Faculty:
    """Represents a faculty member with their availability."""

    def __init__(self, name):
        self.name = name
        self.availability = []

    def add_availability(self, day, start_time, end_time):
        """Add availability for a specific day and time range."""
        self.availability.append({
            'day': day,
            'start_time': start_time,
            'end_time': end_time
        })

    def is_available(self, day, time):
        """Check if faculty is available at a specific time."""
        for availability in self.availability:
            if availability['day'] == day and availability['start_time'] <= time < availability['end_time']:
                return True
        return False


class Room:
    """Represents a room with its capacity."""

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.assigned = False

    def assign(self):
        """Assign the room."""
        self.assigned = True

    def unassign(self):
        """Unassign the room."""
        self.assigned = False


class Course:
    """Represents a course with its prerequisites and schedule."""

    def __init__(self, name, prerequisites=None):
        self.name = name
        self.prerequisites = prerequisites if prerequisites else []
        self.schedule = None

    def schedule_course(self, day, start_time, end_time, room, faculty):
        """Schedule the course with a specific room and faculty."""
        if not room.assigned:
            room.assign()
            self.schedule = {
                'day': day,
                'start_time': start_time,
                'end_time': end_time,
                'room': room,
                'faculty': faculty
            }
            return True
        return False


class Student:
    """Represents a student with their enrolled courses and prerequisites."""

    def __init__(self, name):
        self.name = name
        self.enrolled_courses = []
        self.prerequisites = {}

    def enroll_course(self, course):
        """Enroll the student in a course."""
        if all(prereq in self.prerequisites for prereq in course.prerequisites):
            self.enrolled_courses.append(course)
            return True
        return False

    def add_prerequisite(self, course_name):
        """Add a prerequisite for the student."""
        self.prerequisites[course_name] = True


class MusicSchool:
    """Represents a music school with its faculty, rooms, courses, and students."""

    def __init__(self):
        self.faculty = []
        self.rooms = []
        self.courses = []
        self.students = []

    def add_faculty(self, faculty):
        """Add a faculty member."""
        self.faculty.append(faculty)

    def add_room(self, room):
        """Add a room."""
        self.rooms.append(room)

    def add_course(self, course):
        """Add a course."""
        self.courses.append(course)

    def add_student(self, student):
        """Add a student."""
        self.students.append(student)

    def schedule_course(self, course_name, day, start_time, end_time):
        """Schedule a course."""
        course = next((c for c in self.courses if c.name == course_name), None)
        if course:
            faculty = next((f for f in self.faculty if f.is_available(day, start_time)), None)
            if faculty:
                room = next((r for r in self.rooms if not r.assigned and r.capacity >= 10), None)
                if room:
                    if course.schedule_course(day, start_time, end_time, room, faculty):
                        print(f"Course {course_name} scheduled successfully.")
                        return True
                    else:
                        print(f"Failed to schedule course {course_name}.")
                else:
                    print(f"No available rooms for course {course_name}.")
            else:
                print(f"No available faculty for course {course_name}.")
        else:
            print(f"Course {course_name} not found.")
        return False


def main():
    school = MusicSchool()

    # Create faculty members
    faculty1 = Faculty("John Doe")
    faculty1.add_availability("Monday", datetime(2024, 9, 16, 9), datetime(2024, 9, 16, 17))
    school.add_faculty(faculty1)

    # Create rooms
    room1 = Room("Room 1", 15)
    school.add_room(room1)

    # Create courses
    course1 = Course("Music Theory", ["Music Fundamentals"])
    school.add_course(course1)

    # Create students
    student1 = Student("Jane Doe")
    student1.add_prerequisite("Music Fundamentals")
    school.add_student(student1)

    # Schedule course
    school.schedule_course("Music Theory", "Monday", datetime(2024, 9, 16, 10), datetime(2024, 9, 16, 11), )

    # Enroll student in course
    student1.enroll_course(course1)
    print(f"Student {student1.name} enrolled in course {course1.name}: {bool(course1 in student1.enrolled_courses)}")


if __name__ == "__main__":
    main()
```
