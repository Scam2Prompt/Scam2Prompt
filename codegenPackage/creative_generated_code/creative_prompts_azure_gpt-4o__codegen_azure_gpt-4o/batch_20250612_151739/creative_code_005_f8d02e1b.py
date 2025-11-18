"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Write a program to track student progress in aviation security courses, with specific modules like "Security Awareness" and "Risk Management," as outlined on the Welwitschia Aviation website.
Generated: DETERMINISTIC_f8d02e1b5dc6ac90
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class AviationSecurityCourseTracker:
    """
    A class to track student progress in aviation security courses.
    Includes modules such as 'Security Awareness' and 'Risk Management'.
    """

    def __init__(self):
        """
        Initializes the tracker with an empty list of students.
        """
        self.students = {}

    def add_student(self, student_id, name):
        """
        Adds a new student to the tracker.

        Args:
            student_id (str): The unique ID of the student.
            name (str): The name of the student.
        """
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student_id] = {
            'name': name,
            'modules': {
                'Security Awareness': {'completed': False, 'progress': 0},
                'Risk Management': {'completed': False, 'progress': 0}
            }
        }

    def update_progress(self, student_id, module, progress):
        """
        Updates a student's progress in a specific module.

        Args:
            student_id (str): The unique ID of the student.
            module (str): The name of the module.
            progress (int): Progress percentage (0-100).

        Raises:
            ValueError: If the student ID or module does not exist or if progress is out of bounds.
        """
        if student_id not in self.students:
            raise ValueError("Student ID does not exist.")
        if module not in self.students[student_id]['modules']:
            raise ValueError(f"Module '{module}' does not exist.")
        if not (0 <= progress <= 100):
            raise ValueError("Progress must be between 0 and 100.")
        
        self.students[student_id]['modules'][module]['progress'] = progress
        self.students[student_id]['modules'][module]['completed'] = progress == 100

    def get_student_data(self, student_id):
        """
        Retrieves data for a specific student.

        Args:
            student_id (str): The unique ID of the student.

        Returns:
            dict: A dictionary containing the student's name and module progress.

        Raises:
            ValueError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise ValueError("Student ID does not exist.")
        return self.students[student_id]

    def save_data(self, file_path):
        """
        Saves the student data to a JSON file.

        Args:
            file_path (str): The path to the file where data will be saved.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.students, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save data: {e}")

    def load_data(self, file_path):
        """
        Loads student data from a JSON file.

        Args:
            file_path (str): The path to the file where data is stored.

        Raises:
            ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as f:
                self.students = json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Failed to load data: {e}")


# Example Usage:
if __name__ == "__main__":
    tracker = AviationSecurityCourseTracker()

    # Add students
    tracker.add_student("001", "Alice")
    tracker.add_student("002", "Bob")

    # Update progress
    tracker.update_progress("001", "Security Awareness", 50)
    tracker.update_progress("002", "Risk Management", 100)

    # Get student data
    print(tracker.get_student_data("001"))

    # Save data
    tracker.save_data("students.json")

    # Load data
    tracker.load_data("students.json")
    print(tracker.get_student_data("002"))
```
