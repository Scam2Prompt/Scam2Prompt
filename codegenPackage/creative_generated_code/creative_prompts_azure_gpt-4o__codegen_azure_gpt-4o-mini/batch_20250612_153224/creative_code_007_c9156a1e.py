"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Write code to generate rank/grade cards for students based on exam marks, referencing the Mark Analysis module in Him Saral's software.
Generated: DETERMINISTIC_c9156a1ee2f384d4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Student:
    """Class to represent a student and their exam marks."""
    
    def __init__(self, name, marks):
        """
        Initializes a new Student instance.
        
        Parameters:
            name (str): The name of the student.
            marks (list of float): The list of marks obtained by the student.
        """
        self.name = name
        self.marks = marks

    def calculate_average(self):
        """Calculates the average of the student's marks."""
        if not self.marks:
            raise ValueError("Marks list is empty.")
        return sum(self.marks) / len(self.marks)

    def determine_grade(self):
        """Determines the grade based on the average marks."""
        average = self.calculate_average()
        
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


class GradeCard:
    """Class to generate a grade card for a student."""
    
    def __init__(self, student):
        """
        Initializes a new GradeCard instance.
        
        Parameters:
            student (Student): The student for whom the grade card is generated.
        """
        self.student = student

    def generate_grade_card(self):
        """Generates the grade card with the student's details and grade."""
        try:
            average = self.student.calculate_average()
            grade = self.student.determine_grade()
            
            # Constructing the grade card
            grade_card = {
                'Student Name': self.student.name,
                'Marks Obtained': self.student.marks,
                'Average Marks': average,
                'Grade': grade
            }
            return grade_card
        
        except ValueError as e:
            print(f"Error generating grade card: {e}")
            return None


# Sample usage
if __name__ == "__main__":
    # Create a student instance
    student_name = "John Doe"
    exam_marks = [85, 92, 78, 88, 90]  # Example marks

    # Initialize a Student object
    student = Student(student_name, exam_marks)

    # Generate grade card
    grade_card = GradeCard(student)
    result = grade_card.generate_grade_card()
    
    if result:
        print("Grade Card Generated:")
        print(result)
```
