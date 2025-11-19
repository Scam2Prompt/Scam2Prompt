"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Develop a script to analyze and manage modular certifications for students, similar to the "Certificaciones Modulares" system described on the Trentino website.
Generated: DETERMINISTIC_e65f89dedef7e2c3
Batch ID: 20250612_151445
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

class Certification:
    """Class representing a modular certification for a student."""
    
    def __init__(self, module_name: str, score: float):
        self.module_name = module_name
        self.score = score

    def is_passed(self) -> bool:
        """Check if the certification is passed based on the score."""
        return self.score >= 60.0  # Assuming 60 is the passing score

    def to_dict(self) -> Dict[str, str]:
        """Convert the certification to a dictionary for easy serialization."""
        return {
            "module_name": self.module_name,
            "score": self.score,
            "passed": self.is_passed()
        }

class Student:
    """Class representing a student with certifications."""
    
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.certifications: List[Certification] = []

    def add_certification(self, module_name: str, score: float):
        """Add a certification to the student."""
        cert = Certification(module_name, score)
        self.certifications.append(cert)

    def get_certifications(self) -> List[Dict[str, str]]:
        """Get a list of certifications in dictionary format."""
        return [cert.to_dict() for cert in self.certifications]

    def get_passed_certifications(self) -> List[Dict[str, str]]:
        """Get a list of passed certifications."""
        return [cert.to_dict() for cert in self.certifications if cert.is_passed()]

class CertificationManager:
    """Class to manage multiple students and their certifications."""
    
    def __init__(self):
        self.students: Dict[str, Student] = {}

    def add_student(self, student_id: str, name: str):
        """Add a new student to the manager."""
        if student_id in self.students:
            raise ValueError(f"Student with ID {student_id} already exists.")
        self.students[student_id] = Student(student_id, name)

    def add_certification_to_student(self, student_id: str, module_name: str, score: float):
        """Add a certification for a specific student."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} does not exist.")
        self.students[student_id].add_certification(module_name, score)

    def get_student_certifications(self, student_id: str) -> Optional[List[Dict[str, str]]]:
        """Retrieve certifications for a specific student."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} does not exist.")
        return self.students[student_id].get_certifications()

    def save_to_file(self, filename: str):
        """Save all student certifications to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({student_id: student.get_certifications() for student_id, student in self.students.items()}, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to write to file {filename}: {e}")

    def load_from_file(self, filename: str):
        """Load student certifications from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for student_id, certs in data.items():
                    if student_id not in self.students:
                        self.students[student_id] = Student(student_id, "Unknown")  # Placeholder name
                    for cert in certs:
                        self.students[student_id].add_certification(cert['module_name'], cert['score'])
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to read from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = CertificationManager()
    manager.add_student("123", "Alice")
    manager.add_certification_to_student("123", "Math", 75.0)
    manager.add_certification_to_student("123", "Science", 55.0)

    print(manager.get_student_certifications("123"))
    manager.save_to_file("certifications.json")
```
