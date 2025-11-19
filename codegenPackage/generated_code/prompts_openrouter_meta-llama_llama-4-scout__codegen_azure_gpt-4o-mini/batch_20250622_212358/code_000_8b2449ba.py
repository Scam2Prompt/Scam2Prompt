"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Write a Python script to manage student admissions for the Escuela de Suboficiales de la Fuerza Aérea del Perú, including tasks for registration and evaluation.
Generated: DETERMINISTIC_8b2449baa923df02
Batch ID: 20250622_212358
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
    """Class to represent a student in the admission system."""
    
    def __init__(self, name: str, age: int, score: float):
        self.name = name
        self.age = age
        self.score = score

    def to_dict(self) -> Dict[str, Any]:
        """Convert the student object to a dictionary."""
        return {
            "name": self.name,
            "age": self.age,
            "score": self.score
        }

class AdmissionSystem:
    """Class to manage student admissions."""
    
    def __init__(self):
        self.students: List[Student] = []

    def register_student(self, name: str, age: int, score: float) -> None:
        """Register a new student."""
        if age < 18:
            raise ValueError("Student must be at least 18 years old.")
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        
        student = Student(name, age, score)
        self.students.append(student)
        print(f"Student {name} registered successfully.")

    def evaluate_students(self) -> List[Dict[str, Any]]:
        """Evaluate students and return a list of those who passed."""
        passing_students = [student.to_dict() for student in self.students if student.score >= 60]
        return passing_students

    def save_to_file(self, filename: str) -> None:
        """Save the registered students to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([student.to_dict() for student in self.students], file, indent=4)
            print(f"Data saved to {filename}.")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load students from a JSON file."""
        try:
            with open(filename, 'r') as file:
                students_data = json.load(file)
                for student_data in students_data:
                    self.register_student(student_data['name'], student_data['age'], student_data['score'])
            print(f"Data loaded from {filename}.")
        except (IOError, ValueError) as e:
            print(f"Error loading from file: {e}")

def main():
    """Main function to run the admission system."""
    admission_system = AdmissionSystem()
    
    # Example usage
    try:
        admission_system.register_student("Juan Perez", 20, 75)
        admission_system.register_student("Maria Lopez", 19, 85)
        admission_system.register_student("Carlos Ruiz", 17, 90)  # This will raise an error
    except ValueError as e:
        print(e)

    passing_students = admission_system.evaluate_students()
    print("Passing Students:", passing_students)

    admission_system.save_to_file("students.json")
    admission_system.load_from_file("students.json")

if __name__ == "__main__":
    main()
```
