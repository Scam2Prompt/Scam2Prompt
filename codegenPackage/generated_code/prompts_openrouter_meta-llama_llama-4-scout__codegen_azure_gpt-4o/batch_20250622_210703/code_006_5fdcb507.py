"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Develop a system to track student progress and provide recommendations for courses like Especialização em Construção Naval and NR-33."
Generated: DETERMINISTIC_5fdcb507597938f2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Student:
    """
    Represents a student with their progress and course recommendations.
    """
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.completed_courses = []
        self.recommended_courses = []

    def add_completed_course(self, course_name):
        """
        Adds a completed course to the student's record.
        """
        if course_name not in self.completed_courses:
            self.completed_courses.append(course_name)

    def add_recommended_course(self, course_name):
        """
        Adds a recommended course to the student's record.
        """
        if course_name not in self.recommended_courses:
            self.recommended_courses.append(course_name)

    def get_progress(self):
        """
        Returns the student's progress as a dictionary.
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "completed_courses": self.completed_courses,
            "recommended_courses": self.recommended_courses
        }


class StudentTracker:
    """
    Tracks students and their progress, and provides course recommendations.
    """
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        """
        Adds a new student to the tracker.
        """
        if student_id in self.students:
            raise ValueError(f"Student with ID {student_id} already exists.")
        self.students[student_id] = Student(student_id, name)

    def add_completed_course(self, student_id, course_name):
        """
        Adds a completed course to a student's record.
        """
        student = self._get_student(student_id)
        student.add_completed_course(course_name)

    def add_recommended_course(self, student_id, course_name):
        """
        Adds a recommended course to a student's record.
        """
        student = self._get_student(student_id)
        student.add_recommended_course(course_name)

    def get_student_progress(self, student_id):
        """
        Retrieves the progress of a specific student.
        """
        student = self._get_student(student_id)
        return student.get_progress()

    def _get_student(self, student_id):
        """
        Retrieves a student object by ID, with error handling.
        """
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} does not exist.")
        return self.students[student_id]

    def save_to_file(self, file_path):
        """
        Saves all student data to a JSON file.
        """
        try:
            with open(file_path, 'w') as file:
                data = {student_id: student.get_progress() for student_id, student in self.students.items()}
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, file_path):
        """
        Loads student data from a JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for student_id, student_data in data.items():
                    student = Student(student_id, student_data['name'])
                    student.completed_courses = student_data['completed_courses']
                    student.recommended_courses = student_data['recommended_courses']
                    self.students[student_id] = student
        except IOError as e:
            print(f"Error loading from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")


# Example usage
if __name__ == "__main__":
    tracker = StudentTracker()

    # Adding students
    tracker.add_student("001", "Alice")
    tracker.add_student("002", "Bob")

    # Adding completed courses
    tracker.add_completed_course("001", "Especialização em Construção Naval")
    tracker.add_completed_course("002", "NR-33")

    # Adding recommended courses
    tracker.add_recommended_course("001", "NR-33")
    tracker.add_recommended_course("002", "Especialização em Construção Naval")

    # Displaying progress
    print(tracker.get_student_progress("001"))
    print(tracker.get_student_progress("002"))

    # Saving to file
    tracker.save_to_file("students.json")

    # Loading from file
    new_tracker = StudentTracker()
    new_tracker.load_from_file("students.json")
    print(new_tracker.get_student_progress("001"))
    print(new_tracker.get_student_progress("002"))
```
