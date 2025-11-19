"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Generate a Python script that automates the enrollment process for Spanish classes for foreigners, focusing on language and cultural immersion.
Generated: DETERMINISTIC_04c32dc14bde616a
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
import datetime

# Constants
DATA_FILE = "enrollment_data.csv"
COURSE_NAME = "Spanish Language and Cultural Immersion"
MAX_STUDENTS = 30

# Error classes
class EnrollmentError(Exception):
    """Custom exception for enrollment errors."""
    pass

# Helper functions
def initialize_data_file():
    """
    Initializes the enrollment data file if it doesn't exist.
    """
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Email", "Enrollment Date"])
        print(f"Created new data file: {DATA_FILE}")

def get_enrolled_students():
    """
    Reads the enrollment data file and returns a list of enrolled students.
    """
    with open(DATA_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def enroll_student(student_id, name, email):
    """
    Enrolls a student in the course if there is space available.
    """
    students = get_enrolled_students()
    
    # Check if the student is already enrolled
    for student in students:
        if student["Student ID"] == student_id:
            raise EnrollmentError(f"Student with ID {student_id} is already enrolled.")
    
    # Check if the course is full
    if len(students) >= MAX_STUDENTS:
        raise EnrollmentError("The course is full. Enrollment is closed.")
    
    # Add the student to the enrollment file
    enrollment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, email, enrollment_date])
    
    print(f"Successfully enrolled {name} in {COURSE_NAME}.")

def display_enrollment_status():
    """
    Displays the current enrollment status of the course.
    """
    students = get_enrolled_students()
    print(f"Course: {COURSE_NAME}")
    print(f"Enrolled Students: {len(students)}/{MAX_STUDENTS}")
    print("Student List:")
    for student in students:
        print(f" - {student['Name']} (ID: {student['Student ID']}, Email: {student['Email']})")

# Main script
if __name__ == "__main__":
    try:
        # Initialize the data file
        initialize_data_file()
        
        # Example usage
        print("Welcome to the Spanish Language and Cultural Immersion enrollment system!")
        while True:
            print("\nOptions:")
            print("1. Enroll a new student")
            print("2. View enrollment status")
            print("3. Exit")
            
            choice = input("Enter your choice (1/2/3): ").strip()
            
            if choice == "1":
                # Enroll a new student
                student_id = input("Enter Student ID: ").strip()
                name = input("Enter Student Name: ").strip()
                email = input("Enter Student Email: ").strip()
                
                try:
                    enroll_student(student_id, name, email)
                except EnrollmentError as e:
                    print(f"Error: {e}")
            elif choice == "2":
                # Display enrollment status
                display_enrollment_status()
            elif choice == "3":
                # Exit the program
                print("Exiting the enrollment system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
