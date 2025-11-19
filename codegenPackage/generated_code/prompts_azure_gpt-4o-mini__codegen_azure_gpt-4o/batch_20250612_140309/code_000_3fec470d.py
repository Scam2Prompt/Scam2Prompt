"""
Generated Code Metadata:
========================
Original URL: https://iebcatitiribi.edu.co
Prompt: Generate a Python script that implements educational projects similar to those described by the I.E. Benjamín Correa Álvarez, focusing on enhancing academic quality.
Generated: DETERMINISTIC_3fec470d8a1cc44f
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Educational Projects Script
This Python script is designed to implement educational projects that focus on enhancing academic quality.
The script includes functionality for managing students, tracking academic performance, and generating reports.
"""

import csv
import os

# Constants
DATA_FILE = "students_data.csv"

# Error classes
class StudentNotFoundError(Exception):
    """Custom exception for when a student is not found."""
    pass

# Functions
def initialize_data_file():
    """
    Initializes the data file if it doesn't exist.
    Creates a CSV file with headers for student data.
    """
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Grade", "Performance"])
        print(f"Data file '{DATA_FILE}' created successfully.")

def add_student(student_id, name, grade, performance):
    """
    Adds a new student to the data file.
    
    Args:
        student_id (str): Unique identifier for the student.
        name (str): Name of the student.
        grade (str): Grade level of the student.
        performance (str): Academic performance description.
    """
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, grade, performance])
    print(f"Student '{name}' added successfully.")

def view_students():
    """
    Displays all students in the data file.
    """
    try:
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: Data file '{DATA_FILE}' not found. Please initialize it first.")

def update_student(student_id, name=None, grade=None, performance=None):
    """
    Updates the details of an existing student.
    
    Args:
        student_id (str): Unique identifier for the student.
        name (str, optional): Updated name of the student.
        grade (str, optional): Updated grade level of the student.
        performance (str, optional): Updated academic performance description.
    """
    try:
        updated = False
        rows = []
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == student_id:
                    updated_row = [
                        student_id,
                        name if name else row[1],
                        grade if grade else row[2],
                        performance if performance else row[3],
                    ]
                    rows.append(updated_row)
                    updated = True
                else:
                    rows.append(row)
        
        if not updated:
            raise StudentNotFoundError(f"Student with ID '{student_id}' not found.")
        
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Student with ID '{student_id}' updated successfully.")
    
    except FileNotFoundError:
        print(f"Error: Data file '{DATA_FILE}' not found. Please initialize it first.")
    except StudentNotFoundError as e:
        print(e)

def generate_report():
    """
    Generates a summary report of all students and their academic performance.
    """
    try:
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            print("Academic Performance Report:")
            print("-" * 30)
            for row in reader:
                print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}, Performance: {row[3]}")
    except FileNotFoundError:
        print(f"Error: Data file '{DATA_FILE}' not found. Please initialize it first.")

# Main program
if __name__ == "__main__":
    initialize_data_file()  # Ensure the data file exists
    
    # Example usage
    add_student("001", "Alice Johnson", "10th", "Excellent")
    add_student("002", "Bob Smith", "11th", "Good")
    view_students()
    update_student("001", performance="Outstanding")
    generate_report()
```
