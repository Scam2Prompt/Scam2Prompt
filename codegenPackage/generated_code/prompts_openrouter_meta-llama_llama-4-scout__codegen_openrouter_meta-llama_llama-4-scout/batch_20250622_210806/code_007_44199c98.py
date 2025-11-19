"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: "Write a Python script to analyze student progress and generate reports based on their attendance and performance in Jiu-Jitsu classes at Fusion Jiu Jitsu School."
Generated: DETERMINISTIC_44199c98089a63a8
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_progress_analysis.py

class Student:
    """Represents a student with their attendance and performance data."""

    def __init__(self, name, student_id):
        """
        Initializes a Student object.

        Args:
            name (str): The student's name.
            student_id (int): The student's unique ID.
        """
        self.name = name
        self.student_id = student_id
        self.attendance = []
        self.performance = {}

    def add_attendance(self, date, attended):
        """
        Adds attendance data for a specific date.

        Args:
            date (str): The date in 'YYYY-MM-DD' format.
            attended (bool): Whether the student attended the class.
        """
        self.attendance.append({'date': date, 'attended': attended})

    def add_performance(self, technique, score):
        """
        Adds performance data for a specific technique.

        Args:
            technique (str): The technique being evaluated.
            score (int): The student's score for the technique (1-5).
        """
        self.performance[technique] = score


class JiuJitsuSchool:
    """Represents the Fusion Jiu Jitsu School with its students."""

    def __init__(self):
        """Initializes a JiuJitsuSchool object."""
        self.students = {}

    def add_student(self, student):
        """
        Adds a student to the school.

        Args:
            student (Student): The student to add.
        """
        self.students[student.student_id] = student

    def generate_report(self, student_id):
        """
        Generates a report for a specific student.

        Args:
            student_id (int): The ID of the student.

        Returns:
            dict: A dictionary containing the student's report.

        Raises:
            ValueError: If the student ID is not found.
        """
        if student_id not in self.students:
            raise ValueError("Student ID not found")

        student = self.students[student_id]
        attendance_percentage = self.calculate_attendance_percentage(student.attendance)
        average_performance = self.calculate_average_performance(student.performance)

        report = {
            'name': student.name,
            'student_id': student.student_id,
            'attendance_percentage': attendance_percentage,
            'average_performance': average_performance,
            'technique_scores': student.performance
        }

        return report

    @staticmethod
    def calculate_attendance_percentage(attendance):
        """
        Calculates the attendance percentage.

        Args:
            attendance (list): A list of attendance records.

        Returns:
            float: The attendance percentage.
        """
        total_classes = len(attendance)
        attended_classes = sum(1 for record in attendance if record['attended'])

        if total_classes == 0:
            return 0.0

        return (attended_classes / total_classes) * 100

    @staticmethod
    def calculate_average_performance(performance):
        """
        Calculates the average performance score.

        Args:
            performance (dict): A dictionary of technique scores.

        Returns:
            float: The average performance score.
        """
        if not performance:
            return 0.0

        return sum(performance.values()) / len(performance)


def main():
    school = JiuJitsuSchool()

    # Create students
    student1 = Student("John Doe", 1)
    student2 = Student("Jane Doe", 2)

    # Add attendance data
    student1.add_attendance("2022-01-01", True)
    student1.add_attendance("2022-01-03", False)
    student1.add_attendance("2022-01-05", True)

    student2.add_attendance("2022-01-01", True)
    student2.add_attendance("2022-01-03", True)
    student2.add_attendance("2022-01-05", True)

    # Add performance data
    student1.add_performance("Guard Pass", 4)
    student1.add_performance("Sweep", 3)
    student1.add_performance("Submission", 5)

    student2.add_performance("Guard Pass", 5)
    student2.add_performance("Sweep", 4)
    student2.add_performance("Submission", 4)

    # Add students to the school
    school.add_student(student1)
    school.add_student(student2)

    # Generate reports
    try:
        report1 = school.generate_report(1)
        report2 = school.generate_report(2)

        print("Student Report 1:")
        print(f"Name: {report1['name']}")
        print(f"Student ID: {report1['student_id']}")
        print(f"Attendance Percentage: {report1['attendance_percentage']:.2f}%")
        print(f"Average Performance: {report1['average_performance']:.2f}")
        print("Technique Scores:")
        for technique, score in report1['technique_scores'].items():
            print(f"{technique}: {score}")

        print("\nStudent Report 2:")
        print(f"Name: {report2['name']}")
        print(f"Student ID: {report2['student_id']}")
        print(f"Attendance Percentage: {report2['attendance_percentage']:.2f}%")
        print(f"Average Performance: {report2['average_performance']:.2f}")
        print("Technique Scores:")
        for technique, score in report2['technique_scores'].items():
            print(f"{technique}: {score}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
