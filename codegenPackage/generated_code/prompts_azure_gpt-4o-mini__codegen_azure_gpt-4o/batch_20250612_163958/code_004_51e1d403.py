"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Create a code snippet that automates the enrollment process for a training program like those offered by SMART Training Resources.
Generated: DETERMINISTIC_51e1d403625aee7f
Batch ID: 20250612_163958
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

class TrainingEnrollment:
    """
    A class to handle the enrollment process for a training program.
    """

    def __init__(self, enrollment_file='enrollments.csv'):
        """
        Initializes the TrainingEnrollment class.

        Args:
            enrollment_file (str): Path to the CSV file where enrollment data will be stored.
        """
        self.enrollment_file = enrollment_file
        # Ensure the enrollment file exists
        if not os.path.exists(self.enrollment_file):
            with open(self.enrollment_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Email', 'Phone', 'Program'])  # Write header row

    def enroll(self, name, email, phone, program):
        """
        Enrolls a participant in the training program.

        Args:
            name (str): Name of the participant.
            email (str): Email address of the participant.
            phone (str): Phone number of the participant.
            program (str): Name of the training program.

        Returns:
            str: Success message if enrollment is successful.
        """
        # Validate input data
        if not name or not email or not phone or not program:
            raise ValueError("All fields (name, email, phone, program) are required.")

        if not self._is_valid_email(email):
            raise ValueError("Invalid email format.")

        # Append enrollment data to the CSV file
        with open(self.enrollment_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, phone, program])

        return f"Enrollment successful for {name} in the {program} program."

    def _is_valid_email(self, email):
        """
        Validates the format of an email address.

        Args:
            email (str): Email address to validate.

        Returns:
            bool: True if the email format is valid, False otherwise.
        """
        # Simple email validation
        return '@' in email and '.' in email

    def list_enrollments(self):
        """
        Lists all enrollments in the training program.

        Returns:
            list: A list of dictionaries containing enrollment data.
        """
        enrollments = []
        with open(self.enrollment_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                enrollments.append(row)
        return enrollments


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the enrollment system
        enrollment_system = TrainingEnrollment()

        # Enroll a participant
        print(enrollment_system.enroll(
            name="John Doe",
            email="john.doe@example.com",
            phone="1234567890",
            program="Python Programming"
        ))

        # List all enrollments
        print("Current enrollments:")
        for enrollment in enrollment_system.list_enrollments():
            print(enrollment)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
