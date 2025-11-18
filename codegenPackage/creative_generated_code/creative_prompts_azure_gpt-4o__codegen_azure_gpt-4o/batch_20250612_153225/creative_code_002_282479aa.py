"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Develop a program using Python to manage online registration for school admissions, referencing the admission procedure described on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_282479aa1bd34aea
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime

# Class to represent an applicant
class Applicant:
    def __init__(self, name, age, email, phone_number, grade_applied):
        self.name = name
        self.age = age
        self.email = email
        self.phone_number = phone_number
        self.grade_applied = grade_applied
        self.application_date = datetime.now()

    def __str__(self):
        return (f"Name: {self.name}\nAge: {self.age}\nEmail: {self.email}\n"
                f"Phone Number: {self.phone_number}\nGrade Applied: {self.grade_applied}\n"
                f"Application Date: {self.application_date.strftime('%Y-%m-%d %H:%M:%S')}")

# Function to validate email address format
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Function to validate phone number format
def validate_phone_number(phone_number):
    phone_regex = r'^\d{10}$'  # Matches a 10-digit phone number
    return re.match(phone_regex, phone_number) is not None

# Main function to manage registration
def manage_registration():
    print("\nWelcome to Deepti Convent Higher Secondary School Admissions!")
    print("Please provide the following details for registration.")

    try:
        # Collect applicant details
        name = input("Enter your full name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        
        age = int(input("Enter your age: ").strip())
        if age < 3 or age > 18:
            raise ValueError("Age must be between 3 and 18 years.")
        
        email = input("Enter your email address: ").strip()
        if not validate_email(email):
            raise ValueError("Invalid email format.")
        
        phone_number = input("Enter your phone number (10 digits): ").strip()
        if not validate_phone_number(phone_number):
            raise ValueError("Invalid phone number format. It must be 10 digits.")
        
        grade_applied = input("Enter the grade you are applying for (e.g., 'Grade 1', 'Grade 10'): ").strip()
        if not grade_applied:
            raise ValueError("Grade applied cannot be empty.")

        # Create an Applicant instance
        applicant = Applicant(name, age, email, phone_number, grade_applied)

        # Display confirmation
        print("\nThank you! Your registration details are as follows:\n")
        print(applicant)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    manage_registration()
```
