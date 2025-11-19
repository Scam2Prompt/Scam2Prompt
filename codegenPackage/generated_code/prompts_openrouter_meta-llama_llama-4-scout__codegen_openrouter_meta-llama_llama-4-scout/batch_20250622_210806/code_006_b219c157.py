"""
Generated Code Metadata:
========================
Original URL: https://ihsh.edu.bd
Prompt: Develop a system for tracking student results and generating reports, similar to Ideal High School's result management system.
Generated: DETERMINISTIC_b219c1572c06a9de
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_result_tracker.py

class Student:
    """Represents a student with their results."""

    def __init__(self, student_id, name):
        """
        Initializes a Student object.

        Args:
            student_id (int): Unique identifier for the student.
            name (str): Name of the student.
        """
        self.student_id = student_id
        self.name = name
        self.results = {}

    def add_result(self, subject, score):
        """
        Adds a result for a subject.

        Args:
            subject (str): Name of the subject.
            score (float): Score achieved in the subject.

        Raises:
            ValueError: If the score is not between 0 and 100.
        """
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")
        self.results[subject] = score

    def update_result(self, subject, score):
        """
        Updates a result for a subject.

        Args:
            subject (str): Name of the subject.
            score (float): New score achieved in the subject.

        Raises:
            ValueError: If the score is not between 0 and 100.
            KeyError: If the subject does not exist.
        """
        if subject not in self.results:
            raise KeyError("Subject does not exist")
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")
        self.results[subject] = score

    def delete_result(self, subject):
        """
        Deletes a result for a subject.

        Args:
            subject (str): Name of the subject.

        Raises:
            KeyError: If the subject does not exist.
        """
        if subject not in self.results:
            raise KeyError("Subject does not exist")
        del self.results[subject]


class StudentResultTracker:
    """Manages student results and generates reports."""

    def __init__(self):
        """Initializes a StudentResultTracker object."""
        self.students = {}

    def add_student(self, student_id, name):
        """
        Adds a student to the tracker.

        Args:
            student_id (int): Unique identifier for the student.
            name (str): Name of the student.

        Raises:
            ValueError: If the student ID already exists.
        """
        if student_id in self.students:
            raise ValueError("Student ID already exists")
        self.students[student_id] = Student(student_id, name)

    def get_student(self, student_id):
        """
        Retrieves a student from the tracker.

        Args:
            student_id (int): Unique identifier for the student.

        Returns:
            Student: The student object.

        Raises:
            KeyError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise KeyError("Student ID does not exist")
        return self.students[student_id]

    def generate_report(self, student_id):
        """
        Generates a report for a student.

        Args:
            student_id (int): Unique identifier for the student.

        Returns:
            dict: A dictionary containing the student's results.

        Raises:
            KeyError: If the student ID does not exist.
        """
        student = self.get_student(student_id)
        return student.results

    def calculate_gpa(self, student_id):
        """
        Calculates the GPA for a student.

        Args:
            student_id (int): Unique identifier for the student.

        Returns:
            float: The student's GPA.

        Raises:
            KeyError: If the student ID does not exist.
            ValueError: If the student has no results.
        """
        student = self.get_student(student_id)
        if not student.results:
            raise ValueError("Student has no results")
        return sum(student.results.values()) / len(student.results)


def main():
    tracker = StudentResultTracker()

    while True:
        print("1. Add student")
        print("2. Add result")
        print("3. Update result")
        print("4. Delete result")
        print("5. Generate report")
        print("6. Calculate GPA")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            tracker.add_student(student_id, name)
        elif choice == "2":
            student_id = int(input("Enter student ID: "))
            subject = input("Enter subject: ")
            score = float(input("Enter score: "))
            student = tracker.get_student(student_id)
            student.add_result(subject, score)
        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            subject = input("Enter subject: ")
            score = float(input("Enter new score: "))
            student = tracker.get_student(student_id)
            student.update_result(subject, score)
        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            subject = input("Enter subject: ")
            student = tracker.get_student(student_id)
            student.delete_result(subject)
        elif choice == "5":
            student_id = int(input("Enter student ID: "))
            report = tracker.generate_report(student_id)
            print(report)
        elif choice == "6":
            student_id = int(input("Enter student ID: "))
            gpa = tracker.calculate_gpa(student_id)
            print(f"GPA: {gpa:.2f}")
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
