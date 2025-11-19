"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Develop a Python script to analyze student performance in CBSE exams, specifically for classes X and XII.
Generated: DETERMINISTIC_ec5292af8e12bbc9
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import statistics
from typing import List, Dict, Tuple

# Define a class to represent a student
class Student:
    def __init__(self, name: str, roll_number: str, grade: str, marks: Dict[str, int]):
        """
        Initialize a Student object.

        :param name: Name of the student
        :param roll_number: Roll number of the student
        :param grade: Grade (e.g., 'X' or 'XII')
        :param marks: Dictionary of subject marks
        """
        self.name = name
        self.roll_number = roll_number
        self.grade = grade
        self.marks = marks

    def calculate_total_marks(self) -> int:
        """
        Calculate the total marks obtained by the student.

        :return: Total marks
        """
        return sum(self.marks.values())

    def calculate_percentage(self) -> float:
        """
        Calculate the percentage of marks obtained by the student.

        :return: Percentage of marks
        """
        total_marks = self.calculate_total_marks()
        max_marks = len(self.marks) * 100  # Assuming each subject is out of 100
        return (total_marks / max_marks) * 100


def read_student_data(file_path: str) -> List[Student]:
    """
    Read student data from a CSV file.

    :param file_path: Path to the CSV file
    :return: List of Student objects
    """
    students = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                roll_number = row['Roll Number']
                grade = row['Grade']
                marks = {subject: int(row[subject]) for subject in row if subject not in ['Name', 'Roll Number', 'Grade']}
                students.append(Student(name, roll_number, grade, marks))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as e:
        print(f"Error: Invalid data format in file. {e}")
    return students


def analyze_performance(students: List[Student]) -> Dict[str, Dict[str, float]]:
    """
    Analyze student performance and calculate statistics.

    :param students: List of Student objects
    :return: Dictionary containing performance statistics
    """
    performance = {'X': {}, 'XII': {}}

    for grade in ['X', 'XII']:
        grade_students = [student for student in students if student.grade == grade]
        if grade_students:
            percentages = [student.calculate_percentage() for student in grade_students]
            performance[grade]['Average Percentage'] = statistics.mean(percentages)
            performance[grade]['Highest Percentage'] = max(percentages)
            performance[grade]['Lowest Percentage'] = min(percentages)
        else:
            performance[grade] = {'Average Percentage': 0, 'Highest Percentage': 0, 'Lowest Percentage': 0}

    return performance


def main():
    """
    Main function to execute the script.
    """
    # Path to the CSV file containing student data
    file_path = 'student_data.csv'

    # Read student data
    students = read_student_data(file_path)

    if not students:
        print("No student data available for analysis.")
        return

    # Analyze performance
    performance = analyze_performance(students)

    # Display results
    print("CBSE Exam Performance Analysis:")
    for grade, stats in performance.items():
        print(f"\nGrade {grade}:")
        print(f"  Average Percentage: {stats['Average Percentage']:.2f}%")
        print(f"  Highest Percentage: {stats['Highest Percentage']:.2f}%")
        print(f"  Lowest Percentage: {stats['Lowest Percentage']:.2f}%")


if __name__ == '__main__':
    main()
```
