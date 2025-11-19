"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Write a program to track and evaluate academic work for students, incorporating the evaluation methods described on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_e2d6c4c24110cf07
Batch ID: 20250612_153225
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
    A class to represent a student and their academic work.
    """

    def __init__(self, name, student_id):
        """
        Initializes a new student with a name and student ID.

        :param name: str - The name of the student
        :param student_id: str - The unique identifier for the student
        """
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, grade):
        """
        Adds a grade for a specific subject.

        :param subject: str - The subject for which the grade is being added
        :param grade: float - The grade received in the subject
        """
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self, subject):
        """
        Calculates the average grade for a specific subject.

        :param subject: str - The subject for which the average is calculated
        :return: float - The average grade for the subject
        :raises ValueError: If the subject does not exist
        """
        if subject not in self.grades:
            raise ValueError(f"No grades recorded for subject: {subject}")

        return sum(self.grades[subject]) / len(self.grades[subject])

    def __str__(self):
        """
        Returns a string representation of the student and their grades.

        :return: str - The student's name and their grades
        """
        return f"Student: {self.name}, ID: {self.student_id}, Grades: {self.grades}"


class AcademicTracker:
    """
    A class to manage multiple students and their academic records.
    """

    def __init__(self):
        """
        Initializes the academic tracker with an empty student list.
        """
        self.students = {}

    def add_student(self, name, student_id):
        """
        Adds a new student to the tracker.

        :param name: str - The name of the student
        :param student_id: str - The unique identifier for the student
        :raises ValueError: If a student with the same ID already exists
        """
        if student_id in self.students:
            raise ValueError(f"Student with ID {student_id} already exists.")
        self.students[student_id] = Student(name, student_id)

    def add_grade(self, student_id, subject, grade):
        """
        Adds a grade for a specific student and subject.

        :param student_id: str - The unique identifier for the student
        :param subject: str - The subject for which the grade is being added
        :param grade: float - The grade received in the subject
        :raises KeyError: If the student ID does not exist
        """
        if student_id not in self.students:
            raise KeyError(f"Student with ID {student_id} not found.")
        self.students[student_id].add_grade(subject, grade)

    def get_student_average(self, student_id, subject):
        """
        Retrieves the average grade for a specific student and subject.

        :param student_id: str - The unique identifier for the student
        :param subject: str - The subject for which the average is calculated
        :return: float - The average grade for the student in the subject
        :raises KeyError: If the student ID does not exist
        :raises ValueError: If the subject does not exist for the student
        """
        if student_id not in self.students:
            raise KeyError(f"Student with ID {student_id} not found.")
        return self.students[student_id].calculate_average(subject)

    def __str__(self):
        """
        Returns a string representation of all students in the tracker.

        :return: str - A list of all students and their grades
        """
        return "\n".join(str(student) for student in self.students.values())


# Example usage
if __name__ == "__main__":
    tracker = AcademicTracker()
    
    # Adding students
    tracker.add_student("Alice Johnson", "S001")
    tracker.add_student("Bob Smith", "S002")

    # Adding grades
    tracker.add_grade("S001", "Mathematics", 85.0)
    tracker.add_grade("S001", "Mathematics", 90.0)
    tracker.add_grade("S002", "Mathematics", 78.0)

    # Calculating averages
    try:
        alice_avg = tracker.get_student_average("S001", "Mathematics")
        print(f"Alice's average in Mathematics: {alice_avg:.2f}")
    except (KeyError, ValueError) as e:
        print(e)

    # Display all students
    print(tracker)
```
