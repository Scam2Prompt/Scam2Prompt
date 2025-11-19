"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Generate a Python script that registers a student for the Endeavor Plus extracurricular programs, including options for Active Athletes, Art, Dance, and STEM.
Generated: DETERMINISTIC_6f40ce19a8fcf5c8
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Endeavor Plus Student Registration System
# Python script to register students for extracurricular programs

import sys

def display_programs():
    """
    Display available programs to the student.
    """
    print("Welcome to Endeavor Plus Extracurricular Programs!")
    print("Please select one of the following programs:")
    print("1. Active Athletes")
    print("2. Art")
    print("3. Dance")
    print("4. STEM")

def register_student():
    """
    Main function to handle student registration.
    """
    try:
        student_name = input("Enter your full name: ").strip()
        if not student_name:
            raise ValueError("Student name cannot be empty.")
        
        display_programs()
        
        # Get the program choice from the student
        program_choice = input("Enter the number corresponding to your choice: ").strip()
        programs = {
            "1": "Active Athletes",
            "2": "Art",
            "3": "Dance",
            "4": "STEM"
        }

        if program_choice not in programs:
            raise ValueError("Invalid choice. Please select a valid program number.")
        
        # Confirm registration
        selected_program = programs[program_choice]
        print(f"Thank you for registering, {student_name}!")
        print(f"You have successfully enrolled in the {selected_program} program.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        register_student()
    except KeyboardInterrupt:
        print("\nRegistration process interrupted. Goodbye!")
        sys.exit(1)
```
