"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Generate a Python script that demonstrates how to manage student enrollment for the Graduate Diploma of Management (Learning) at Global Healthcare Management College.
Generated: DETERMINISTIC_3706fc22b7e63889
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Student:
    """Class representing a student enrolled in the Graduate Diploma of Management (Learning)."""
    
    def __init__(self, student_id: str, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email

    def to_dict(self) -> Dict[str, Any]:
        """Convert the student object to a dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email
        }

class EnrollmentManager:
    """Class to manage student enrollments for the Graduate Diploma of Management (Learning)."""
    
    def __init__(self):
        self.enrolled_students: List[Student] = []

    def enroll_student(self, student: Student) -> None:
        """Enroll a new student in the program."""
        if self.is_student_enrolled(student.student_id):
            raise ValueError(f"Student with ID {student.student_id} is already enrolled.")
        self.enrolled_students.append(student)

    def is_student_enrolled(self, student_id: str) -> bool:
        """Check if a student is already enrolled."""
        return any(student.student_id == student_id for student in self.enrolled_students)

    def remove_student(self, student_id: str) -> None:
        """Remove a student from the enrollment list."""
        for student in self.enrolled_students:
            if student.student_id == student_id:
                self.enrolled_students.remove(student)
                return
        raise ValueError(f"Student with ID {student_id} not found.")

    def list_enrolled_students(self) -> List[Dict[str, Any]]:
        """List all enrolled students."""
        return [student.to_dict() for student in self.enrolled_students]

    def save_enrollment(self, filename: str) -> None:
        """Save the current enrollment list to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_enrolled_students(), file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save enrollment data: {e}")

    def load_enrollment(self, filename: str) -> None:
        """Load enrollment data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                students_data = json.load(file)
                for student_data in students_data:
                    student = Student(**student_data)
                    self.enroll_student(student)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load enrollment data: {e}")

def main():
    """Main function to demonstrate the enrollment management system."""
    manager = EnrollmentManager()

    # Example usage
    try:
        # Enroll students
        student1 = Student("S001", "Alice Smith", "alice.smith@example.com")
        student2 = Student("S002", "Bob Johnson", "bob.johnson@example.com")
        
        manager.enroll_student(student1)
        manager.enroll_student(student2)

        # List enrolled students
        print("Enrolled Students:")
        print(manager.list_enrolled_students())

        # Save enrollment to a file
        manager.save_enrollment("enrollment_data.json")

        # Load enrollment from a file
        manager.load_enrollment("enrollment_data.json")
        print("Loaded Students:")
        print(manager.list_enrolled_students())

        # Remove a student
        manager.remove_student("S001")
        print("Students after removal:")
        print(manager.list_enrolled_students())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
