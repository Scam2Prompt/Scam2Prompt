"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Write a Python script to automate the generation of student credentials based on input data like name, ID, and grade, as described in the FAQ section of the Escuela Preparatoria Oficial N.73 website.
Generated: DETERMINISTIC_70330470cbdc0ff2
Batch ID: 20250612_153224
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
from typing import List, Dict

# Define a Student class to encapsulate student data
class Student:
    def __init__(self, name: str, student_id: str, grade: str):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def to_dict(self) -> Dict[str, str]:
        """Convert the student instance to a dictionary for easy CSV writing."""
        return {
            "Name": self.name,
            "ID": self.student_id,
            "Grade": self.grade
        }

# Function to read student data from a CSV file
def read_students_from_csv(file_path: str) -> List[Student]:
    """Read student data from a CSV file and return a list of Student objects."""
    students = []
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(name=row['Name'], student_id=row['ID'], grade=row['Grade'])
                students.append(student)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
    
    return students

# Function to write student credentials to a new CSV file
def write_students_to_csv(students: List[Student], output_file_path: str) -> None:
    """Write a list of Student objects to a CSV file."""
    try:
        with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['Name', 'ID', 'Grade']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())
                
        print(f"Successfully wrote student credentials to {output_file_path}.")
    except IOError as e:
        print(f"Error writing to file {output_file_path}: {e}")

# Main function to orchestrate the reading and writing process
def generate_student_credentials(input_file: str, output_file: str) -> None:
    """Generate student credentials based on input CSV data."""
    students = read_students_from_csv(input_file)
    
    if students:
        write_students_to_csv(students, output_file)
    else:
        print("No student data to write.")

# Entry point of the script
if __name__ == "__main__":
    input_csv_file = "students_input.csv"  # Input CSV file containing student data
    output_csv_file = "students_credentials.csv"  # Output CSV file for student credentials

    generate_student_credentials(input_csv_file, output_csv_file)
```

Make sure to create an input CSV file named `students_input.csv` with appropriate columns: Name, ID, and Grade before running this script.
