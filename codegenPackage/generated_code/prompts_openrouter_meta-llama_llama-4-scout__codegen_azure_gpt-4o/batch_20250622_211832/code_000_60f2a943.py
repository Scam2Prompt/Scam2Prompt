"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Write a Python script to manage student information for SMKN 1 Kadipaten's academic programs, including student names, classes, and exam schedules for subjects like Pendidikan Agama & Budi Pekerti and Matematika.
Generated: DETERMINISTIC_60f2a943620ac24d
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class StudentManagementSystem:
    """
    A class to manage student information for SMKN 1 Kadipaten's academic programs.
    Includes functionality for managing student names, classes, and exam schedules.
    """

    def __init__(self):
        # Initialize the system with empty data structures
        self.students = {}  # Dictionary to store student information
        self.exam_schedule = {}  # Dictionary to store exam schedules

    def add_student(self, student_id, name, class_name):
        """
        Add a new student to the system.

        Args:
            student_id (str): Unique identifier for the student.
            name (str): Name of the student.
            class_name (str): Class the student belongs to.
        """
        if student_id in self.students:
            print(f"Error: Student ID {student_id} already exists.")
            return

        self.students[student_id] = {
            "name": name,
            "class": class_name
        }
        print(f"Student {name} added successfully.")

    def remove_student(self, student_id):
        """
        Remove a student from the system.

        Args:
            student_id (str): Unique identifier for the student.
        """
        if student_id not in self.students:
            print(f"Error: Student ID {student_id} not found.")
            return

        removed_student = self.students.pop(student_id)
        print(f"Student {removed_student['name']} removed successfully.")

    def add_exam_schedule(self, subject, date, time):
        """
        Add an exam schedule for a subject.

        Args:
            subject (str): Name of the subject.
            date (str): Date of the exam (format: YYYY-MM-DD).
            time (str): Time of the exam (format: HH:MM).
        """
        if subject in self.exam_schedule:
            print(f"Error: Exam schedule for {subject} already exists.")
            return

        self.exam_schedule[subject] = {
            "date": date,
            "time": time
        }
        print(f"Exam schedule for {subject} added successfully.")

    def view_students(self):
        """
        View all students in the system.
        """
        if not self.students:
            print("No students found.")
            return

        print("Student List:")
        for student_id, info in self.students.items():
            print(f"ID: {student_id}, Name: {info['name']}, Class: {info['class']}")

    def view_exam_schedule(self):
        """
        View all exam schedules.
        """
        if not self.exam_schedule:
            print("No exam schedules found.")
            return

        print("Exam Schedule:")
        for subject, schedule in self.exam_schedule.items():
            print(f"Subject: {subject}, Date: {schedule['date']}, Time: {schedule['time']}")

    def save_data(self, filename):
        """
        Save student and exam schedule data to a JSON file.

        Args:
            filename (str): Name of the file to save data to.
        """
        data = {
            "students": self.students,
            "exam_schedule": self.exam_schedule
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Data saved to {filename} successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename):
        """
        Load student and exam schedule data from a JSON file.

        Args:
            filename (str): Name of the file to load data from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.students = data.get("students", {})
                self.exam_schedule = data.get("exam_schedule", {})
            print(f"Data loaded from {filename} successfully.")
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from {filename}.")
        except Exception as e:
            print(f"Error loading data: {e}")


# Example usage
if __name__ == "__main__":
    system = StudentManagementSystem()

    # Add students
    system.add_student("S001", "Alice", "X-A")
    system.add_student("S002", "Bob", "X-B")

    # Add exam schedules
    system.add_exam_schedule("Pendidikan Agama & Budi Pekerti", "2023-12-01", "09:00")
    system.add_exam_schedule("Matematika", "2023-12-02", "10:00")

    # View students and exam schedules
    system.view_students()
    system.view_exam_schedule()

    # Save data to file
    system.save_data("school_data.json")

    # Load data from file
    system.load_data("school_data.json")
```
