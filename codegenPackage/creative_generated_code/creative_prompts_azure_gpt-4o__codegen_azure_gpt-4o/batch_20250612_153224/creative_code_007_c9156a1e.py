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
import os
import csv

# Constants for grade boundaries
GRADE_BOUNDARIES = {
    "A+": [90, 100],
    "A": [80, 89],
    "B+": [70, 79],
    "B": [60, 69],
    "C": [50, 59],
    "D": [40, 49],
    "F": [0, 39]
}

# Function to calculate grade based on marks
def calculate_grade(marks):
    for grade, boundary in GRADE_BOUNDARIES.items():
        if boundary[0] <= marks <= boundary[1]:
            return grade
    return "Invalid Marks"

# Function to generate rank/grade cards for students
def generate_grade_cards(input_file, output_folder):
    try:
        # Ensure output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Read data from the CSV file
        with open(input_file, mode='r') as file:
            reader = csv.DictReader(file)
            students = list(reader)
        
        # Check if input file contains required headers
        required_fields = ["Student Name", "Marks"]
        for field in required_fields:
            if field not in students[0]:
                raise ValueError(f"Missing required field: {field} in input file.")
        
        # Generate grade cards for each student
        for student in students:
            name = student["Student Name"]
            marks = int(student["Marks"])
            grade = calculate_grade(marks)

            # Create individual grade card file
            grade_card_path = os.path.join(output_folder, f"{name}_GradeCard.txt")
            with open(grade_card_path, mode='w') as grade_card_file:
                grade_card_file.write(f"Student Name: {name}\n")
                grade_card_file.write(f"Marks: {marks}\n")
                grade_card_file.write(f"Grade: {grade}\n")
        
        print(f"Grade cards generated successfully in '{output_folder}' folder.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Input file containing student data
    input_csv_file = "student_marks.csv"
    # Output folder to save grade cards
    output_directory = "GradeCards"
    
    generate_grade_cards(input_csv_file, output_directory)
```
