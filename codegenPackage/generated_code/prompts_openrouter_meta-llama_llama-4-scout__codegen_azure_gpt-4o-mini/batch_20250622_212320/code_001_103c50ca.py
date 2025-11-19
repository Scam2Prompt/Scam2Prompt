"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Write a Python code snippet to manage student notes for the Sistema de notas used by the Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa".
Generated: DETERMINISTIC_103c50cab239ed29
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Student:
    """
    A class to represent a student and their associated notes.
    """

    def __init__(self, student_id, name):
        """
        Initializes a new student with an ID and name.

        :param student_id: Unique identifier for the student
        :param name: Name of the student
        """
        self.student_id = student_id
        self.name = name
        self.notes = []

    def add_note(self, note):
        """
        Adds a note to the student's record.

        :param note: The note to be added (float)
        :raises ValueError: If the note is not between 0 and 20
        """
        if not (0 <= note <= 20):
            raise ValueError("Note must be between 0 and 20.")
        self.notes.append(note)

    def calculate_average(self):
        """
        Calculates the average of the student's notes.

        :return: The average of the notes (float)
        :raises ZeroDivisionError: If there are no notes to average
        """
        if not self.notes:
            raise ZeroDivisionError("No notes available to calculate average.")
        return sum(self.notes) / len(self.notes)

    def __str__(self):
        """
        Returns a string representation of the student and their notes.

        :return: String representation of the student
        """
        return f"Student ID: {self.student_id}, Name: {self.name}, Notes: {self.notes}"


class StudentManager:
    """
    A class to manage multiple students and their notes.
    """

    def __init__(self):
        """
        Initializes the student manager with an empty list of students.
        """
        self.students = {}

    def add_student(self, student_id, name):
        """
        Adds a new student to the manager.

        :param student_id: Unique identifier for the student
        :param name: Name of the student
        :raises KeyError: If a student with the same ID already exists
        """
        if student_id in self.students:
            raise KeyError(f"Student with ID {student_id} already exists.")
        self.students[student_id] = Student(student_id, name)

    def add_note_to_student(self, student_id, note):
        """
        Adds a note to a specific student.

        :param student_id: Unique identifier for the student
        :param note: The note to be added (float)
        :raises KeyError: If the student does not exist
        """
        if student_id not in self.students:
            raise KeyError(f"Student with ID {student_id} does not exist.")
        self.students[student_id].add_note(note)

    def get_student_average(self, student_id):
        """
        Retrieves the average note for a specific student.

        :param student_id: Unique identifier for the student
        :return: The average of the student's notes (float)
        :raises KeyError: If the student does not exist
        :raises ZeroDivisionError: If the student has no notes
        """
        if student_id not in self.students:
            raise KeyError(f"Student with ID {student_id} does not exist.")
        return self.students[student_id].calculate_average()

    def __str__(self):
        """
        Returns a string representation of all students and their notes.

        :return: String representation of all students
        """
        return "\n".join(str(student) for student in self.students.values())


# Example usage
if __name__ == "__main__":
    manager = StudentManager()
    
    # Adding students
    try:
        manager.add_student(1, "Juan Pérez")
        manager.add_student(2, "María López")
        
        # Adding notes
        manager.add_note_to_student(1, 15.5)
        manager.add_note_to_student(1, 18.0)
        manager.add_note_to_student(2, 17.0)
        
        # Calculating averages
        print(f"Average for Juan Pérez: {manager.get_student_average(1)}")
        print(f"Average for María López: {manager.get_student_average(2)}")
        
        # Display all students
        print(manager)
        
    except (ValueError, KeyError, ZeroDivisionError) as e:
        print(f"Error: {e}")
```
