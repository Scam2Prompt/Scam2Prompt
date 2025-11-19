"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lgtc.edu.pk
Prompt: Write a Python script to automate the enrollment process for a Diploma of Associate Engineer (DAE) program at Lahore Group of Technical, including Civil, Electrical, or Mechanical specializations.
Generated: DETERMINISTIC_c2c9390be8c2ef39
Batch ID: 20250612_161616
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

# Constants
DATA_FILE = "enrollments.csv"
SPECIALIZATIONS = ['Civil', 'Electrical', 'Mechanical']

def initialize_data_file():
    """
    Initialize the enrollments data file if it doesn't exist.
    """
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Add column headers to the file
            writer.writerow(['Student_ID', 'Name', 'Age', 'Specialization', 'Contact_Number'])
            print(f"Data file '{DATA_FILE}' initialized.")

def get_specialization():
    """
    Prompt the user to select a specialization.
    Returns:
        str: The selected specialization.
    """
    print("\nAvailable Specializations:")
    for i, spec in enumerate(SPECIALIZATIONS, 1):
        print(f"{i}. {spec}")

    while True:
        try:
            choice = int(input("Enter the number corresponding to your specialization: "))
            if 1 <= choice <= len(SPECIALIZATIONS):
                return SPECIALIZATIONS[choice - 1]
            else:
                print("Invalid choice. Please select a valid specialization.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def enroll_student():
    """
    Enroll a new student in the program.
    """
    print("\n--- New Student Enrollment ---")
    
    try:
        # Collect student information
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Student Name: ").strip()
        age = input("Enter Student Age: ").strip()
        specialization = get_specialization()
        contact_number = input("Enter Contact Number: ").strip()

        # Validate required fields
        if not student_id or not name or not age or not contact_number:
            print("Error: All fields are required. Enrollment failed.")
            return

        # Append student data to the CSV file
        with open(DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, age, specialization, contact_number])

        print(f"Student '{name}' successfully enrolled in '{specialization}' specialization.")

    except Exception as e:
        print(f"An error occurred during enrollment: {e}")

def display_enrollments():
    """
    Display all enrolled students.
    """
    print("\n--- List of Enrolled Students ---")
    try:
        if not os.path.exists(DATA_FILE):
            print("No enrollments found.")
            return

        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:  # Only header exists
                print("No enrollments found.")
                return

            for row in rows:
                print(", ".join(row))
    except Exception as e:
        print(f"An error occurred while displaying enrollments: {e}")

def main():
    """
    Main function to handle the enrollment system.
    """
    initialize_data_file()

    while True:
        print("\n--- DAE Program Enrollment System ---")
        print("1. Enroll a new student")
        print("2. Display all enrollments")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                enroll_student()
            elif choice == 2:
                display_enrollments()
            elif choice == 3:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
