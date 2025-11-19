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
import csv
from typing import List, Dict, Optional

class Student:
    """Represents a student with their exam marks and personal details."""
    
    def __init__(self, roll_no: str, name: str, marks: Dict[str, float]):
        """
        Initialize a Student instance.
        
        Args:
            roll_no: Unique identifier for the student
            name: Full name of the student
            marks: Dictionary of subject names to marks obtained
        """
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.total = sum(marks.values())
        self.percentage = (self.total / (len(marks) * 100)) * 100
        
    def calculate_grade(self) -> str:
        """Calculate grade based on percentage."""
        if self.percentage >= 90:
            return 'A+'
        elif self.percentage >= 80:
            return 'A'
        elif self.percentage >= 70:
            return 'B+'
        elif self.percentage >= 60:
            return 'B'
        elif self.percentage >= 50:
            return 'C'
        elif self.percentage >= 40:
            return 'D'
        else:
            return 'F'

class MarkAnalysis:
    """Handles mark analysis and grade card generation."""
    
    def __init__(self):
        self.students: List[Student] = []
        
    def load_from_csv(self, file_path: str) -> None:
        """
        Load student data from a CSV file.
        
        Args:
            file_path: Path to the CSV file
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the CSV data is malformed
        """
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        roll_no = row['RollNo']
                        name = row['Name']
                        marks = {k: float(v) for k, v in row.items() 
                                if k not in ['RollNo', 'Name']}
                        self.students.append(Student(roll_no, name, marks))
                    except (KeyError, ValueError) as e:
                        raise ValueError(f"Invalid data in row: {row}") from e
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {file_path}") from e
            
    def calculate_ranks(self) -> None:
        """Calculate ranks based on total marks."""
        sorted_students = sorted(self.students, 
                               key=lambda x: x.total, 
                               reverse=True)
        for rank, student in enumerate(sorted_students, start=1):
            student.rank = rank
            
    def generate_grade_card(self, student: Student) -> Dict[str, str]:
        """
        Generate grade card for a single student.
        
        Args:
            student: Student instance
            
        Returns:
            Dictionary containing grade card details
        """
        return {
            'Roll No': student.roll_no,
            'Name': student.name,
            **{subject: str(mark) for subject, mark in student.marks.items()},
            'Total': f"{student.total:.2f}",
            'Percentage': f"{student.percentage:.2f}%",
            'Grade': student.calculate_grade(),
            'Rank': str(getattr(student, 'rank', 'N/A'))
        }
        
    def generate_all_grade_cards(self, output_file: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Generate grade cards for all students.
        
        Args:
            output_file: Optional path to save CSV output
            
        Returns:
            List of grade card dictionaries
            
        Raises:
            ValueError: If no students are loaded
        """
        if not self.students:
            raise ValueError("No student data available")
            
        self.calculate_ranks()
        grade_cards = [self.generate_grade_card(student) for student in self.students]
        
        if output_file:
            try:
                fieldnames = ['Roll No', 'Name'] + \
                            list(self.students[0].marks.keys()) + \
                            ['Total', 'Percentage', 'Grade', 'Rank']
                
                with open(output_file, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(grade_cards)
            except IOError as e:
                print(f"Warning: Could not save to file - {e}")
                
        return grade_cards

# Example usage
if __name__ == "__main__":
    try:
        analyzer = MarkAnalysis()
        analyzer.load_from_csv('student_marks.csv')
        grade_cards = analyzer.generate_all_grade_cards('grade_cards.csv')
        
        # Print first student's grade card for verification
        if grade_cards:
            print("Sample Grade Card:")
            for key, value in grade_cards[0].items():
                print(f"{key}: {value}")
                
    except Exception as e:
        print(f"Error: {e}")
```
