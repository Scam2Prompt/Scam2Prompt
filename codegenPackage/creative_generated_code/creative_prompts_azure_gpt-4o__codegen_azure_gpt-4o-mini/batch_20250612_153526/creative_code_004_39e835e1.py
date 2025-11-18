"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aveaorg.com
Prompt: Write code to implement a student-centered, competency-based learning system inspired by the TAFE vocational education mode reform project described on the AVEA website.
Generated: DETERMINISTIC_39e835e1df5d0e58
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# student_learning_system.py

class Student:
    """
    A class to represent a student in the learning system.

    Attributes:
        student_id (int): Unique identifier for the student
        name (str): Name of the student
        competencies (dict): A dictionary of competencies the student has achieved
    """

    def __init__(self, student_id, name):
        """
        Initializes a new student with a unique ID and name.

        Args:
            student_id (int): Unique identifier for the student
            name (str): Name of the student
        """
        self.student_id = student_id
        self.name = name
        self.competencies = {}

    def add_competency(self, competency_name, status):
        """
        Adds or updates a competency status for the student.

        Args:
            competency_name (str): Name of the competency
            status (bool): True if achieved, False otherwise
        """
        self.competencies[competency_name] = status

    def get_competencies(self):
        """
        Returns the student's competencies.

        Returns:
            dict: A dictionary of competencies
        """
        return self.competencies


class Competency:
    """
    A class to represent a competency in the learning system.

    Attributes:
        name (str): Name of the competency
        description (str): Description of the competency
    """

    def __init__(self, name, description):
        """
        Initializes a new competency with a name and description.

        Args:
            name (str): Name of the competency
            description (str): Description of the competency
        """
        self.name = name
        self.description = description


class LearningSystem:
    """
    A class to manage the learning system for students and competencies.

    Attributes:
        students (list): List of students in the system
        competencies (list): List of competencies in the system
    """

    def __init__(self):
        """Initializes an empty learning system."""
        self.students = []
        self.competencies = []

    def register_student(self, student_id, name):
        """
        Registers a new student in the learning system.

        Args:
            student_id (int): Unique identifier for the student
            name (str): Name of the student
        
        Returns:
            Student: The newly created Student object
        """
        if any(student.student_id == student_id for student in self.students):
            raise ValueError(f'Student ID {student_id} already exists.')
        student = Student(student_id, name)
        self.students.append(student)
        return student

    def add_competency(self, name, description):
        """
        Adds a new competency to the system.

        Args:
            name (str): Name of the competency
            description (str): Description of the competency
        """
        competency = Competency(name, description)
        self.competencies.append(competency)

    def assign_competency_to_student(self, student_id, competency_name, status):
        """
        Assigns a competency to a student with a given status.

        Args:
            student_id (int): Unique identifier for the student
            competency_name (str): Name of the competency
            status (bool): True if achieved, False otherwise
        
        Raises:
            ValueError: If the student ID or competency does not exist
        """
        student = next((student for student in self.students if student.student_id == student_id), None)
        if student is None:
            raise ValueError(f'Student ID {student_id} not found.')
        
        if competency_name not in [c.name for c in self.competencies]:
            raise ValueError(f'Competency {competency_name} not found.')

        student.add_competency(competency_name, status)

    def get_student_competencies(self, student_id):
        """
        Retrieves the competencies of a student by their ID.

        Args:
            student_id (int): Unique identifier for the student
        
        Returns:
            dict: A dictionary of competencies
        
        Raises:
            ValueError: If the student ID does not exist
        """
        student = next((student for student in self.students if student.student_id == student_id), None)
        if student is None:
            raise ValueError(f'Student ID {student_id} not found.')
         
        return student.get_competencies()


# Example usage
if __name__ == "__main__":
    try:
        learning_system = LearningSystem()

        # Registering students
        student1 = learning_system.register_student(1, "Alice")
        student2 = learning_system.register_student(2, "Bob")

        # Adding competencies
        learning_system.add_competency("Programming Basics", "Understand the fundamentals of programming.")
        learning_system.add_competency("Data Analysis", "Analyze data using statistical methods.")

        # Assigning competencies
        learning_system.assign_competency_to_student(1, "Programming Basics", True)
        learning_system.assign_competency_to_student(2, "Data Analysis", False)

        # Fetching student competencies
        print(student1.get_competencies())
        print(student2.get_competencies())

    except ValueError as e:
        print(f"Error: {e}")
```
