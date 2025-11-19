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
class SchoolManagementSystem:
    """
    A class to represent a school management system that includes features for 
    academic, administrative, and community management.
    """

    def __init__(self):
        """Initialize the school management system with empty records."""
        self.students = {}
        self.teachers = {}
        self.courses = {}
        self.administrative_staff = {}
        self.community_events = []

    def add_student(self, student_id, name):
        """Add a new student to the system."""
        if student_id in self.students:
            raise ValueError(f"Student ID {student_id} already exists.")
        self.students[student_id] = {'name': name, 'courses': []}
        print(f"Added student: {name} with ID: {student_id}")

    def add_teacher(self, teacher_id, name):
        """Add a new teacher to the system."""
        if teacher_id in self.teachers:
            raise ValueError(f"Teacher ID {teacher_id} already exists.")
        self.teachers[teacher_id] = {'name': name, 'courses': []}
        print(f"Added teacher: {name} with ID: {teacher_id}")

    def add_course(self, course_id, course_name):
        """Add a new course to the system."""
        if course_id in self.courses:
            raise ValueError(f"Course ID {course_id} already exists.")
        self.courses[course_id] = {'course_name': course_name, 'students': []}
        print(f"Added course: {course_name} with ID: {course_id}")

    def enroll_student_in_course(self, student_id, course_id):
        """Enroll a student in a course."""
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} does not exist.")
        if course_id not in self.courses:
            raise ValueError(f"Course ID {course_id} does not exist.")
        
        self.students[student_id]['courses'].append(course_id)
        self.courses[course_id]['students'].append(student_id)
        print(f"Enrolled student ID {student_id} in course ID {course_id}")

    def add_administrative_staff(self, staff_id, name):
        """Add a new administrative staff member to the system."""
        if staff_id in self.administrative_staff:
            raise ValueError(f"Staff ID {staff_id} already exists.")
        self.administrative_staff[staff_id] = {'name': name}
        print(f"Added administrative staff: {name} with ID: {staff_id}")

    def schedule_community_event(self, event_name, date):
        """Schedule a new community event."""
        event = {'event_name': event_name, 'date': date}
        self.community_events.append(event)
        print(f"Scheduled community event: {event_name} on {date}")

    def get_student_info(self, student_id):
        """Retrieve information about a student."""
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} does not exist.")
        return self.students[student_id]

    def get_teacher_info(self, teacher_id):
        """Retrieve information about a teacher."""
        if teacher_id not in self.teachers:
            raise ValueError(f"Teacher ID {teacher_id} does not exist.")
        return self.teachers[teacher_id]

    def get_course_info(self, course_id):
        """Retrieve information about a course."""
        if course_id not in self.courses:
            raise ValueError(f"Course ID {course_id} does not exist.")
        return self.courses[course_id]

    def list_community_events(self):
        """List all scheduled community events."""
        return self.community_events


# Example usage
if __name__ == "__main__":
    sms = SchoolManagementSystem()
    try:
        sms.add_student(1, "Alice Johnson")
        sms.add_teacher(101, "Mr. Smith")
        sms.add_course(201, "Mathematics")
        sms.enroll_student_in_course(1, 201)
        sms.add_administrative_staff(301, "Mrs. Brown")
        sms.schedule_community_event("Science Fair", "2023-05-15")
        
        print(sms.get_student_info(1))
        print(sms.get_teacher_info(101))
        print(sms.get_course_info(201))
        print(sms.list_community_events())
    except ValueError as e:
        print(f"Error: {e}")
```
