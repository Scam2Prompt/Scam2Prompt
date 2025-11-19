"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Generate a Python script that automates the enrollment process for a distance learning program in Análisis de Sistemas at ISIV.
Generated: DETERMINISTIC_4fbce2f758f804bd
Batch ID: 20250612_163506
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
import re

# Constants for course and institution
COURSE_NAME = "Análisis de Sistemas"
INSTITUTION_NAME = "ISIV"
DATA_FILE = "enrollment_data.csv"

# Define error classes
class EnrollmentError(Exception):
    """Custom exception for enrollment errors."""
    pass

# Function to validate email format
def is_valid_email(email):
    """
    Validates email format using regex.
    :param email: Email address to validate.
    :return: True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

# Function to validate required fields
def validate_fields(name, email, age):
    """
    Validates the fields required for enrollment.
    :param name: Full name of the student.
    :param email: Email address of the student.
    :param age: Age of the student.
    :return: None
    :raises EnrollmentError: If fields are invalid.
    """
    if not name or not email or not age:
        raise EnrollmentError("All fields are mandatory.")
    
    if not is_valid_email(email):
        raise EnrollmentError("Invalid email address.")
    
    if not age.isdigit() or int(age) < 18:
        raise EnrollmentError("Age must be a number and at least 18.")

# Function to save enrollment data to a CSV file
def save_enrollment(name, email, age):
    """
    Saves enrollment data to a CSV file.
    :param name: Full name of the student.
    :param email: Email address of the student.
    :param age: Age of the student.
    :return: None
    """
    file_exists = os.path.isfile(DATA_FILE)
    with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write header only if file is new
        if not file_exists:
            writer.writerow(["Name", "Email", "Age", "Course", "Institution"])
        
        # Write enrollment data
        writer.writerow([name, email, age, COURSE_NAME, INSTITUTION_NAME])

# Main function to handle the enrollment process
def enroll_student():
    """
    Handles the enrollment process.
    Collects user input, validates fields, and saves enrollment data.
    :return: None
    """
    print(f"Welcome to the {COURSE_NAME} enrollment process at {INSTITUTION_NAME}!\n")
    try:
        # Collect input from the user
        name = input("Enter your full name: ").strip()
        email = input("Enter your email address: ").strip()
        age = input("Enter your age: ").strip()

        # Validate fields
        validate_fields(name, email, age)

        # Save enrollment data
        save_enrollment(name, email, age)
        print("Enrollment successful! Your data has been saved.")
    
    except EnrollmentError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the script
if __name__ == "__main__":
    enroll_student()
```
