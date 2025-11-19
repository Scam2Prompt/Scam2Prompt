"""
Generated Code Metadata:
========================
Original URL: https://iebcatitiribi.edu.co
Prompt: Write a code snippet for a school management system that includes features for academic, administrative, and community management as outlined by the I.E. Benjamín Correa Álvarez.
Generated: DETERMINISTIC_c8b542e369220c5e
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
School Management System
Features:
1. Academic Management: Manage students, teachers, courses, and grades.
2. Administrative Management: Handle staff, schedules, and school resources.
3. Community Management: Manage events, announcements, and parent-teacher communication.

This code provides a basic structure for the system using Python.
"""

import json

class SchoolManagementSystem:
    def __init__(self):
        # Initialize data storage
        self.students = {}
        self.teachers = {}
        self.courses = {}
        self.staff = {}
        self.events = []
        self.announcements = []

    # Academic Management
    def add_student(self, student_id, name, grade):
        """Add a new student to the system."""
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student_id] = {"name": name, "grade": grade}

    def add_teacher(self, teacher_id, name, subject):
        """Add a new teacher to the system."""
        if teacher_id in self.teachers:
            raise ValueError("Teacher ID already exists.")
        self.teachers[teacher_id] = {"name": name, "subject": subject}

    def add_course(self, course_id, name, teacher_id):
        """Add a new course to the system."""
        if course_id in self.courses:
            raise ValueError("Course ID already exists.")
        if teacher_id not in self.teachers:
            raise ValueError("Teacher ID does not exist.")
        self.courses[course_id] = {"name": name, "teacher_id": teacher_id}

    def assign_grade(self, student_id, course_id, grade):
        """Assign a grade to a student for a specific course."""
        if student_id not in self.students:
            raise ValueError("Student ID does not exist.")
        if course_id not in self.courses:
            raise ValueError("Course ID does not exist.")
        self.students[student_id].setdefault("grades", {})[course_id] = grade

    # Administrative Management
    def add_staff(self, staff_id, name, role):
        """Add a new staff member to the system."""
        if staff_id in self.staff:
            raise ValueError("Staff ID already exists.")
        self.staff[staff_id] = {"name": name, "role": role}

    def schedule_event(self, event_name, date, description):
        """Schedule a new event."""
        self.events.append({"event_name": event_name, "date": date, "description": description})

    # Community Management
    def add_announcement(self, title, message):
        """Add a new announcement."""
        self.announcements.append({"title": title, "message": message})

    def get_announcements(self):
        """Retrieve all announcements."""
        return self.announcements

    def save_data(self, filename):
        """Save system data to a file."""
        data = {
            "students": self.students,
            "teachers": self.teachers,
            "courses": self.courses,
            "staff": self.staff,
            "events": self.events,
            "announcements": self.announcements,
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_data(self, filename):
        """Load system data from a file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.students = data.get("students", {})
                self.teachers = data.get("teachers", {})
                self.courses = data.get("courses", {})
                self.staff = data.get("staff", {})
                self.events = data.get("events", [])
                self.announcements = data.get("announcements", [])
        except FileNotFoundError:
            raise FileNotFoundError("Data file not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding data file.")

# Example usage
if __name__ == "__main__":
    system = SchoolManagementSystem()

    # Add sample data
    system.add_student("S001", "Alice", "10th")
    system.add_teacher("T001", "Mr. Smith", "Math")
    system.add_course("C001", "Algebra", "T001")
    system.assign_grade("S001", "C001", "A")
    system.add_staff("ST001", "Mrs. Johnson", "Administrator")
    system.schedule_event("Science Fair", "2023-11-15", "Annual science fair for students.")
    system.add_announcement("Holiday Notice", "School will be closed on 2023-12-25.")

    # Save and load data
    system.save_data("school_data.json")
    system.load_data("school_data.json")

    # Print announcements
    print("Announcements:")
    for announcement in system.get_announcements():
        print(f"- {announcement['title']}: {announcement['message']}")
```
