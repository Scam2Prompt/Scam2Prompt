"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spanishupdate.com
Prompt: Generate a Python script that automates the enrollment process for Spanish classes for foreigners, focusing on language and cultural immersion.
Generated: DETERMINISTIC_04c32dc14bde616a
Batch ID: 20250612_155356
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
from datetime import datetime

# Define constants for file paths
ENROLLMENT_FILE = "enrollments.csv"
LOG_FILE = "enrollment_log.txt"

# Define a class to handle enrollment processes
class SpanishClassEnrollment:
    def __init__(self, enrollment_file, log_file):
        self.enrollment_file = enrollment_file
        self.log_file = log_file
        self.ensure_files_exist()

    def ensure_files_exist(self):
        """Ensure required files exist. Create them if not."""
        if not os.path.exists(self.enrollment_file):
            with open(self.enrollment_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Email", "Preferred Start Date", "Course Level", "Comments"])
        
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode="w", encoding="utf-8") as file:
                file.write(f"Log initiated on {datetime.now()}\n")

    def enroll_student(self, name, email, preferred_date, level, comments=None):
        """Enroll a student and log the operation."""
        try:
            # Validate inputs
            if not name or not email or not preferred_date or not level:
                raise ValueError("All fields except 'comments' are mandatory.")

            # Append the student's data to the CSV file
            with open(self.enrollment_file, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([name, email, preferred_date, level, comments])

            # Log the enrollment
            self.log_operation(f"Enrolled student: {name} | Email: {email}")

        except Exception as e:
            self.log_operation(f"Error enrolling student: {str(e)}")
            raise

    def log_operation(self, message):
        """Log an operation to the log file."""
        with open(self.log_file, mode="a", encoding="utf-8") as file:
            file.write(f"{datetime.now()} - {message}\n")

    def list_enrollments(self):
        """List all enrolled students."""
        try:
            with open(self.enrollment_file, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                return [row for row in reader]
        except Exception as e:
            self.log_operation(f"Error listing enrollments: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Create an instance of SpanishClassEnrollment
    enrollment_handler = SpanishClassEnrollment(ENROLLMENT_FILE, LOG_FILE)

    # Enroll a student (this can be replaced with inputs from a user interface)
    try:
        enrollment_handler.enroll_student(
            name="John Doe",
            email="john.doe@example.com",
            preferred_date="2023-11-01",
            level="Beginner",
            comments="Interested in cultural immersion activities."
        )
        print("Student enrolled successfully!")
    except Exception as e:
        print(f"Failed to enroll student: {e}")

    # List all enrollments
    try:
        enrollments = enrollment_handler.list_enrollments()
        for enrollment in enrollments:
            print(enrollment)
    except Exception as e:
        print(f"Failed to list enrollments: {e}")
```
