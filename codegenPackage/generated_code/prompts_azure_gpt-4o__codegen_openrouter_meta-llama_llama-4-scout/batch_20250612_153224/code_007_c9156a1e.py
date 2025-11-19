"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Write code to generate rank/grade cards for students based on exam marks, referencing the Mark Analysis module in Him Saral's software.
Generated: DETERMINISTIC_c9156a1ee2f384d4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Student Rank/Grade Card Generator**
=====================================

```python
# Import required libraries
import pandas as pd

class Student:
    """Represents a student with their details and exam marks."""

    def __init__(self, student_id, name, marks):
        """
        Initializes a Student object.

        Args:
            student_id (int): Unique student ID.
            name (str): Student name.
            marks (dict): Dictionary of subject marks.
        """
        self.student_id = student_id
        self.name = name
        self.marks = marks

class MarkAnalysis:
    """Analyzes student marks and generates rank/grade cards."""

    def __init__(self, students, subjects, max_marks):
        """
        Initializes a MarkAnalysis object.

        Args:
            students (list): List of Student objects.
            subjects (list): List of subject names.
            max_marks (dict): Dictionary of maximum marks for each subject.
        """
        self.students = students
        self.subjects = subjects
        self.max_marks = max_marks

    def calculate_total_marks(self, student):
        """
        Calculates the total marks for a student.

        Args:
            student (Student): Student object.

        Returns:
            int: Total marks.
        """
        return sum(self.marks_to_percentage(student.marks, self.max_marks).values())

    def marks_to_percentage(self, marks, max_marks):
        """
        Converts marks to percentage for each subject.

        Args:
            marks (dict): Dictionary of subject marks.
            max_marks (dict): Dictionary of maximum marks for each subject.

        Returns:
            dict: Dictionary of subject percentages.
        """
        percentages = {}
        for subject, mark in marks.items():
            max_mark = max_marks[subject]
            percentages[subject] = (mark / max_mark) * 100
        return percentages

    def generate_rank_cards(self):
        """
        Generates rank/grade cards for all students.

        Returns:
            list: List of dictionaries containing student details and grades.
        """
        # Calculate total marks and percentages for each student
        student_results = []
        for student in self.students:
            total_marks = self.calculate_total_marks(student)
            subject_percentages = self.marks_to_percentage(student.marks, self.max_marks)
            student_results.append({
                "student_id": student.student_id,
                "name": student.name,
                "total_marks": total_marks,
                "subject_percentages": subject_percentages
            })

        # Sort students by total marks in descending order
        student_results.sort(key=lambda x: x["total_marks"], reverse=True)

        # Assign ranks and grades
        rank_cards = []
        for i, student in enumerate(student_results):
            rank = i + 1
            grade = self.calculate_grade(student["total_marks"] / len(self.subjects))
            rank_cards.append({
                "rank": rank,
                "student_id": student["student_id"],
                "name": student["name"],
                "total_marks": student["total_marks"],
                "subject_percentages": student["subject_percentages"],
                "grade": grade
            })

        return rank_cards

    def calculate_grade(self, average_percentage):
        """
        Calculates the grade based on the average percentage.

        Args:
            average_percentage (float): Average percentage.

        Returns:
            str: Grade.
        """
        if average_percentage >= 90:
            return "A+"
        elif average_percentage >= 80:
            return "A"
        elif average_percentage >= 70:
            return "B+"
        elif average_percentage >= 60:
            return "B"
        elif average_percentage >= 50:
            return "C+"
        elif average_percentage >= 40:
            return "C"
        else:
            return "F"

def main():
    # Example usage
    students = [
        Student(1, "John Doe", {"Math": 85, "Science": 90, "English": 78}),
        Student(2, "Jane Doe", {"Math": 90, "Science": 85, "English": 92}),
        Student(3, "Bob Smith", {"Math": 78, "Science": 80, "English": 85})
    ]

    subjects = ["Math", "Science", "English"]
    max_marks = {"Math": 100, "Science": 100, "English": 100}

    mark_analysis = MarkAnalysis(students, subjects, max_marks)
    rank_cards = mark_analysis.generate_rank_cards()

    # Print rank cards
    for rank_card in rank_cards:
        print(f"Rank: {rank_card['rank']}")
        print(f"Student ID: {rank_card['student_id']}")
        print(f"Name: {rank_card['name']}")
        print(f"Total Marks: {rank_card['total_marks']}")
        print("Subject Percentages:")
        for subject, percentage in rank_card["subject_percentages"].items():
            print(f"  {subject}: {percentage:.2f}%")
        print(f"Grade: {rank_card['grade']}")
        print()

if __name__ == "__main__":
    main()
```
