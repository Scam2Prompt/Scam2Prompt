"""
Generated Code Metadata:
========================
Original URL: https://jhpsgaya.com
Prompt: Write a Python code to manage student admissions and fee payments for a school like Jai Hind Public School Gaya.
Generated: DETERMINISTIC_3c80ac386f46d1ce
Batch ID: 20250622_212312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Student:
    """Class to represent a student in the school."""
    
    def __init__(self, student_id, name, age, grade):
        """
        Initialize a new student.

        :param student_id: Unique identifier for the student
        :param name: Name of the student
        :param age: Age of the student
        :param grade: Grade in which the student is enrolled
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.fee_paid = False

    def pay_fee(self):
        """Mark the fee as paid for the student."""
        self.fee_paid = True


class AdmissionSystem:
    """Class to manage student admissions and fee payments."""
    
    def __init__(self):
        """Initialize the admission system with an empty student list."""
        self.students = {}

    def admit_student(self, student_id, name, age, grade):
        """
        Admit a new student to the school.

        :param student_id: Unique identifier for the student
        :param name: Name of the student
        :param age: Age of the student
        :param grade: Grade in which the student is enrolled
        :raises ValueError: If the student ID already exists
        """
        if student_id in self.students:
            raise ValueError(f"Student ID {student_id} already exists.")
        
        self.students[student_id] = Student(student_id, name, age, grade)
        print(f"Student {name} admitted successfully.")

    def process_fee_payment(self, student_id):
        """
        Process the fee payment for a student.

        :param student_id: Unique identifier for the student
        :raises KeyError: If the student ID does not exist
        """
        if student_id not in self.students:
            raise KeyError(f"Student ID {student_id} not found.")
        
        student = self.students[student_id]
        if not student.fee_paid:
            student.pay_fee()
            print(f"Fee payment processed for {student.name}.")
        else:
            print(f"Fee already paid for {student.name}.")

    def get_student_info(self, student_id):
        """
        Retrieve information about a student.

        :param student_id: Unique identifier for the student
        :raises KeyError: If the student ID does not exist
        :return: Dictionary containing student information
        """
        if student_id not in self.students:
            raise KeyError(f"Student ID {student_id} not found.")
        
        student = self.students[student_id]
        return {
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "grade": student.grade,
            "fee_paid": student.fee_paid
        }


# Example usage
if __name__ == "__main__":
    admission_system = AdmissionSystem()
    
    try:
        admission_system.admit_student(1, "John Doe", 15, "10th Grade")
        admission_system.admit_student(2, "Jane Smith", 14, "9th Grade")
        
        admission_system.process_fee_payment(1)
        admission_system.process_fee_payment(1)  # Attempt to pay fee again
        
        student_info = admission_system.get_student_info(1)
        print(student_info)
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
