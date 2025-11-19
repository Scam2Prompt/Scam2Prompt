"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: "Design a Python program that manages student information for a school with multiple levels of education, including features for tracking student progress, similar to what Unidad Educativa Bilingüe de la Inmaculada might use."
Generated: DETERMINISTIC_624e47e96c2df147
Batch ID: 20250622_204729
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
    
    def __init__(self, student_id: int, name: str, level: str):
        self.student_id = student_id
        self.name = name
        self.level = level
        self.grades: List[float] = []
    
    def add_grade(self, grade: float) -> None:
        """Add a grade to the student's record."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100.")
    
    def get_average_grade(self) -> Optional[float]:
        """Calculate and return the average grade of the student."""
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

class School:
    """Class to manage a collection of students."""
    
    def __init__(self):
        self.students: Dict[int, Student] = {}
    
    def add_student(self, student: Student) -> None:
        """Add a new student to the school."""
        if student.student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student.student_id] = student
    
    def remove_student(self, student_id: int) -> None:
        """Remove a student from the school by their ID."""
        if student_id not in self.students:
            raise KeyError("Student ID not found.")
        del self.students[student_id]
    
    def get_student(self, student_id: int) -> Optional[Student]:
        """Retrieve a student by their ID."""
        return self.students.get(student_id, None)
    
    def save_to_file(self, filename: str) -> None:
        """Save the student information to a JSON file."""
        with open(filename, 'w') as file:
            json.dump({student_id: student.__dict__ for student_id, student in self.students.items()}, file)
    
    def load_from_file(self, filename: str) -> None:
        """Load student information from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for student_id, student_data in data.items():
                    student = Student(student_id=int(student_id), name=student_data['name'], level=student_data['level'])
                    student.grades = student_data['grades']
                    self.students[int(student_id)] = student
        except FileNotFoundError:
            print("File not found. Starting with an empty student list.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")

def main():
    """Main function to demonstrate the student management system."""
    school = School()
    
    # Example usage
    try:
        # Adding students
        student1 = Student(student_id=1, name="Alice", level="Primary")
        student1.add_grade(85)
        student1.add_grade(90)
        school.add_student(student1)

        student2 = Student(student_id=2, name="Bob", level="Secondary")
        student2.add_grade(78)
        student2.add_grade(82)
        school.add_student(student2)

        # Saving to file
        school.save_to_file("students.json")

        # Loading from file
        school.load_from_file("students.json")

        # Retrieving a student
        retrieved_student = school.get_student(1)
        if retrieved_student:
            print(f"Retrieved Student: {retrieved_student.name}, Average Grade: {retrieved_student.get_average_grade()}")

    except (ValueError, KeyError) as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
