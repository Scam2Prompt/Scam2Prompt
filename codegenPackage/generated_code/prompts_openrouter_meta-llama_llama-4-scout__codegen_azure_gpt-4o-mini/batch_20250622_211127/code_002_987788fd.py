"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: "Write a code snippet to implement a student information system for managing student data and performance tracking in educational institutions like Potencia Academy."
Generated: DETERMINISTIC_987788fd3590f445
Batch ID: 20250622_211127
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
    A class to represent a student.

    Attributes:
    ----------
    student_id : int
        Unique identifier for the student
    name : str
        Name of the student
    grades : dict
        Dictionary to hold subject names and their corresponding grades
    """

    def __init__(self, student_id, name):
        """
        Initializes a new student with an ID and name.

        Parameters:
        ----------
        student_id : int
            Unique identifier for the student
        name : str
            Name of the student
        """
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        """
        Adds a grade for a specific subject.

        Parameters:
        ----------
        subject : str
            The subject for which the grade is being added
        grade : float
            The grade received in the subject
        """
        if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
            raise ValueError("Grade must be a number between 0 and 100.")
        self.grades[subject] = grade

    def get_average_grade(self):
        """
        Calculates the average grade of the student.

        Returns:
        -------
        float
            The average grade of the student
        """
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)


class StudentInformationSystem:
    """
    A class to manage student information and performance tracking.

    Attributes:
    ----------
    students : dict
        Dictionary to hold student objects with their IDs as keys
    """

    def __init__(self):
        """Initializes the student information system with an empty student list."""
        self.students = {}

    def add_student(self, student_id, name):
        """
        Adds a new student to the system.

        Parameters:
        ----------
        student_id : int
            Unique identifier for the student
        name : str
            Name of the student

        Raises:
        ------
        ValueError
            If the student ID already exists
        """
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student_id] = Student(student_id, name)

    def add_student_grade(self, student_id, subject, grade):
        """
        Adds a grade for a specific student.

        Parameters:
        ----------
        student_id : int
            Unique identifier for the student
        subject : str
            The subject for which the grade is being added
        grade : float
            The grade received in the subject

        Raises:
        ------
        KeyError
            If the student ID does not exist
        """
        if student_id not in self.students:
            raise KeyError("Student ID does not exist.")
        self.students[student_id].add_grade(subject, grade)

    def get_student_average(self, student_id):
        """
        Retrieves the average grade for a specific student.

        Parameters:
        ----------
        student_id : int
            Unique identifier for the student

        Returns:
        -------
        float
            The average grade of the student

        Raises:
        ------
        KeyError
            If the student ID does not exist
        """
        if student_id not in self.students:
            raise KeyError("Student ID does not exist.")
        return self.students[student_id].get_average_grade()


# Example usage
if __name__ == "__main__":
    sis = StudentInformationSystem()
    
    # Adding students
    try:
        sis.add_student(1, "Alice Johnson")
        sis.add_student(2, "Bob Smith")
        
        # Adding grades
        sis.add_student_grade(1, "Math", 95)
        sis.add_student_grade(1, "Science", 88)
        sis.add_student_grade(2, "Math", 76)
        
        # Retrieving average grades
        print(f"Alice's average grade: {sis.get_student_average(1)}")
        print(f"Bob's average grade: {sis.get_student_average(2)}")
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
