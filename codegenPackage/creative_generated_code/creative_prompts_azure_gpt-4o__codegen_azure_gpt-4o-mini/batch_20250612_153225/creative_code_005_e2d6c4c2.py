"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Write a program to track and evaluate academic work for students, incorporating the evaluation methods described on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_e2d6c4c24110cf07
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Student:
    """
    A class to represent a student.

    Attributes:
    ----------
    name : str
        Name of the student
    grades : dict
        A dictionary to hold subject and corresponding grades
    """

    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        """
        Add a grade for a specific subject.

        Parameters:
        ----------
        subject : str
            The subject for which the grade is assigned
        grade : float
            The grade received in the subject
        """
        if subject in self.grades:
            raise ValueError(f"Grade for {subject} already exists.")
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")
        self.grades[subject] = grade

    def get_average_grade(self):
        """
        Calculate the average grade of the student.

        Returns:
        -------
        float
            The average of the grades
        """
        if not self.grades:
            raise ValueError("No grades available for averaging.")
        return sum(self.grades.values()) / len(self.grades)


class AcademicEvaluation:
    """
    A class to evaluate academic performance of students.

    Attributes:
    ----------
    students : list
        A list of Student objects
    """

    def __init__(self):
        self.students = []

    def add_student(self, student):
        """
        Add a student to the evaluation system.

        Parameters:
        ----------
        student : Student
            A Student object to be added
        """
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added.")
        self.students.append(student)

    def evaluate_all_students(self):
        """
        Evaluate all students and print their average grades.

        Returns:
        -------
        dict
            A dictionary with student names and their average grades
        """
        evaluations = {}
        for student in self.students:
            try:
                average = student.get_average_grade()
                evaluations[student.name] = average
            except ValueError as e:
                evaluations[student.name] = str(e)
        return evaluations


def main():
    """
    Main function to run the academic evaluation program.
    """
    evaluator = AcademicEvaluation()

    # Example usage:
    try:
        student1 = Student("Alice")
        student1.add_grade("Mathematics", 85)
        student1.add_grade("Science", 90)
        evaluator.add_student(student1)

        student2 = Student("Bob")
        student2.add_grade("Mathematics", 75)
        student2.add_grade("Science", 80)
        evaluator.add_student(student2)

        # Evaluate all students
        results = evaluator.evaluate_all_students()
        for name, average in results.items():
            print(f"{name}: Average Grade = {average}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
