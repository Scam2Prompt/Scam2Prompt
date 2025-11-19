"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Design a system to track student progress and certification for various courses offered by Global Healthcare Management College, including the Advanced Diploma of Civil Construction Design (RII60520).
Generated: DETERMINISTIC_5ae8f605d220a69c
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Student:
    """Class to represent a student."""
    
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.courses: Dict[str, CourseProgress] = {}

    def enroll_course(self, course: 'Course'):
        """Enroll the student in a course."""
        if course.course_id not in self.courses:
            self.courses[course.course_id] = CourseProgress(course)
            print(f"{self.name} enrolled in {course.title}.")
        else:
            print(f"{self.name} is already enrolled in {course.title}.")

    def complete_module(self, course_id: str, module_id: str):
        """Mark a module as completed for a specific course."""
        if course_id in self.courses:
            self.courses[course_id].complete_module(module_id)
        else:
            print(f"Course ID {course_id} not found for student {self.name}.")

    def get_progress(self) -> Dict[str, Dict]:
        """Get the progress of the student in all courses."""
        return {course_id: progress.get_progress() for course_id, progress in self.courses.items()}


class Course:
    """Class to represent a course."""
    
    def __init__(self, course_id: str, title: str, modules: List[str]):
        self.course_id = course_id
        self.title = title
        self.modules = modules


class CourseProgress:
    """Class to track progress in a specific course."""
    
    def __init__(self, course: Course):
        self.course = course
        self.completed_modules: List[str] = []

    def complete_module(self, module_id: str):
        """Mark a module as completed."""
        if module_id in self.course.modules and module_id not in self.completed_modules:
            self.completed_modules.append(module_id)
            print(f"Module {module_id} completed in course {self.course.title}.")
        else:
            print(f"Module {module_id} is either not part of the course or already completed.")

    def get_progress(self) -> Dict:
        """Get the progress of the course."""
        return {
            "course_id": self.course.course_id,
            "title": self.course.title,
            "completed_modules": self.completed_modules,
            "total_modules": len(self.course.modules)
        }


class CertificationSystem:
    """Class to manage the certification system for students."""
    
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.courses: Dict[str, Course] = {}

    def add_student(self, student_id: str, name: str):
        """Add a new student to the system."""
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added with ID {student_id}.")
        else:
            print(f"Student ID {student_id} already exists.")

    def add_course(self, course_id: str, title: str, modules: List[str]):
        """Add a new course to the system."""
        if course_id not in self.courses:
            self.courses[course_id] = Course(course_id, title, modules)
            print(f"Course {title} added with ID {course_id}.")
        else:
            print(f"Course ID {course_id} already exists.")

    def enroll_student_in_course(self, student_id: str, course_id: str):
        """Enroll a student in a course."""
        if student_id in self.students and course_id in self.courses:
            self.students[student_id].enroll_course(self.courses[course_id])
        else:
            print(f"Student ID {student_id} or Course ID {course_id} not found.")

    def get_student_progress(self, student_id: str) -> Optional[Dict]:
        """Get the progress of a student."""
        if student_id in self.students:
            return self.students[student_id].get_progress()
        else:
            print(f"Student ID {student_id} not found.")
            return None

    def save_data(self, filename: str):
        """Save the current state of the system to a JSON file."""
        try:
            with open(filename, 'w') as file:
                data = {
                    "students": {student_id: student.get_progress() for student_id, student in self.students.items()},
                    "courses": {course_id: {"title": course.title, "modules": course.modules} for course_id, course in self.courses.items()}
                }
                json.dump(data, file, indent=4)
                print(f"Data saved to {filename}.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename: str):
        """Load the system state from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for student_id, progress in data['students'].items():
                    student = Student(student_id, student_id)  # Placeholder for name
                    for course_id, course_progress in progress.items():
                        if course_id in self.courses:
                            student.courses[course_id] = CourseProgress(self.courses[course_id])
                            student.courses[course_id].completed_modules = course_progress['completed_modules']
                    self.students[student_id] = student
                for course_id, course_info in data['courses'].items():
                    self.courses[course_id] = Course(course_id, course_info['title'], course_info['modules'])
                print(f"Data loaded from {filename}.")
        except Exception as e:
            print(f"Error loading data: {e}")


# Example usage
if __name__ == "__main__":
    system = CertificationSystem()
    
    # Adding courses
    system.add_course("RII60520", "Advanced Diploma of Civil Construction Design", ["Module1", "Module2", "Module3"])
    
    # Adding students
    system.add_student("S001", "Alice Smith")
    system.add_student("S002", "Bob Johnson")
    
    # Enrolling students in courses
    system.enroll_student_in_course("S001", "RII60520")
    system.enroll_student_in_course("S002", "RII60520")
    
    # Completing modules
    system.students["S001"].complete_module("RII60520", "Module1")
    system.students["S001"].complete_module("RII60520", "Module2")
    
    # Getting progress
    print(system.get_student_progress("S001"))
    
    # Saving and loading data
    system.save_data("student_data.json")
    system.load_data("student_data.json")
```
