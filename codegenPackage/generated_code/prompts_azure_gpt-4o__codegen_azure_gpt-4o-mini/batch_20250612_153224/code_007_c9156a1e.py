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

```python
class Student:
    """
    A class to represent a student and their exam marks.
    """

    def __init__(self, name, marks):
        """
        Initializes a new student with a name and a dictionary of marks.

        :param name: str - The name of the student
        :param marks: dict - A dictionary containing subject names as keys and marks as values
        """
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        """
        Calculates the grade based on the average of the marks.

        :return: str - The grade of the student
        """
        try:
            average = sum(self.marks.values()) / len(self.marks)
            if average >= 90:
                return 'A+'
            elif average >= 80:
                return 'A'
            elif average >= 70:
                return 'B'
            elif average >= 60:
                return 'C'
            elif average >= 50:
                return 'D'
            else:
                return 'F'
        except ZeroDivisionError:
            return 'No marks available to calculate grade.'
        except Exception as e:
            return f'Error calculating grade: {str(e)}'


class GradeCard:
    """
    A class to generate a grade card for a student.
    """

    def __init__(self, student):
        """
        Initializes a grade card for a given student.

        :param student: Student - The student for whom the grade card is generated
        """
        self.student = student

    def generate_card(self):
        """
        Generates the grade card for the student.

        :return: str - The formatted grade card
        """
        try:
            grade = self.student.calculate_grade()
            marks_str = ', '.join(f"{subject}: {mark}" for subject, mark in self.student.marks.items())
            card = f"Grade Card for {self.student.name}\n"
            card += "Marks:\n" + marks_str + "\n"
            card += f"Grade: {grade}\n"
            return card
        except Exception as e:
            return f'Error generating grade card: {str(e)}'


def main():
    """
    Main function to create students and generate their grade cards.
    """
    # Example student data
    students_data = {
        "Alice": {"Math": 95, "Science": 88, "English": 92},
        "Bob": {"Math": 75, "Science": 80, "English": 70},
        "Charlie": {"Math": 45, "Science": 50, "English": 55},
    }

    # Generate and print grade cards for each student
    for student_name, marks in students_data.items():
        student = Student(student_name, marks)
        grade_card = GradeCard(student)
        print(grade_card.generate_card())


if __name__ == "__main__":
    main()
```
