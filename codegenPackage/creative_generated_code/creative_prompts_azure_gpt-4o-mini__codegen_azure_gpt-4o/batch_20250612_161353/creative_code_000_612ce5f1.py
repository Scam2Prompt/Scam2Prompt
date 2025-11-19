"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iedeoccidente.edu.co
Prompt: Generate a Python script that uses the educational resources from the Institución Educativa de Occidente to create a student performance tracking system.
Generated: DETERMINISTIC_612ce5f13fbef66e
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os


class StudentPerformanceTracker:
    """
    A class to manage student performance tracking based on educational resources
    from the Institución Educativa de Occidente.

    Features:
    - Add new students
    - Record student grades
    - Calculate average grades
    - Generate performance reports
    """

    def __init__(self, data_file='student_data.csv'):
        """
        Initialize the tracker and ensure the data file exists.

        :param data_file: Path to the CSV file storing student data.
        """
        self.data_file = data_file
        if not os.path.exists(self.data_file):
            # Create the file with headers if it doesn't exist
            with open(self.data_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Student ID', 'Name', 'Subject', 'Grade'])

    def add_student(self, student_id, name):
        """
        Add a new student to the system.

        :param student_id: Unique identifier for the student.
        :param name: Name of the student.
        """
        print(f"Student {name} (ID: {student_id}) added to the system.")

    def record_grade(self, student_id, name, subject, grade):
        """
        Record a grade for a student in a specific subject.

        :param student_id: Unique identifier for the student.
        :param name: Name of the student.
        :param subject: Subject name.
        :param grade: Grade received by the student (0-100).
        """
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")

        with open(self.data_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, subject, grade])

        print(f"Grade recorded: {name} (ID: {student_id}) - {subject}: {grade}")

    def calculate_average_grade(self, student_id):
        """
        Calculate the average grade of a student based on their ID.

        :param student_id: Unique identifier for the student.
        :return: Average grade or None if the student has no grades.
        """
        grades = []
        with open(self.data_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Student ID'] == student_id:
                    grades.append(float(row['Grade']))

        if grades:
            average = sum(grades) / len(grades)
            print(f"Average grade for student ID {student_id}: {average:.2f}")
            return average
        else:
            print(f"No grades found for student ID {student_id}.")
            return None

    def generate_report(self):
        """
        Generate a performance report for all students.

        :return: A dictionary where keys are student IDs and values are their average grades.
        """
        student_grades = {}

        with open(self.data_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_id = row['Student ID']
                grade = float(row['Grade'])

                if student_id not in student_grades:
                    student_grades[student_id] = []

                student_grades[student_id].append(grade)

        report = {}
        for student_id, grades in student_grades.items():
            report[student_id] = sum(grades) / len(grades)

        print("Performance Report:")
        for student_id, avg_grade in report.items():
            print(f"Student ID: {student_id}, Average Grade: {avg_grade:.2f}")

        return report


# Example usage:
if __name__ == "__main__":
    tracker = StudentPerformanceTracker()

    # Adding students (IDs are unique)
    tracker.add_student("101", "Alice")
    tracker.add_student("102", "Bob")

    # Recording grades
    tracker.record_grade("101", "Alice", "Math", 85)
    tracker.record_grade("101", "Alice", "Science", 90)
    tracker.record_grade("102", "Bob", "Math", 75)
    tracker.record_grade("102", "Bob", "Science", 80)

    # Calculating average grade for a specific student
    tracker.calculate_average_grade("101")

    # Generating a performance report for all students
    tracker.generate_report()
```
