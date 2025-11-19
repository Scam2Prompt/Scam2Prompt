"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://excelwithsmart.com
Prompt: Create a code snippet that automates the enrollment process for a training program like those offered by SMART Training Resources.
Generated: DETERMINISTIC_51e1d403625aee7f
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import csv
import os

class TrainingEnrollmentAutomation:
    """
    A class to handle the automation of enrollment for a training program.
    """
    
    def __init__(self, training_program_name, enrollment_file_path):
        """
        Initialize the automation object with the training program name and path to the enrollment file.
        Args:
            training_program_name (str): Name of the training program
            enrollment_file_path (str): Path to the CSV file storing the enrollment data
        """
        self.training_program_name = training_program_name
        self.enrollment_file_path = enrollment_file_path
        
        # Ensure the file exists and is writable
        if not os.path.exists(enrollment_file_path):
            # Create the file with headers if it does not exist
            with open(enrollment_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Email", "Phone", "Program", "Status"])
    
    def enroll_user(self, name, email, phone):
        """
        Enroll a user in the training program.
        Args:
            name (str): Full name of the user
            email (str): Email address of the user
            phone (str): Phone number of the user
        
        Returns:
            bool: True if enrollment is successful, False otherwise
        """
        try:
            # Check if the email is already enrolled
            with open(self.enrollment_file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Email"] == email:
                        print(f"Email {email} is already enrolled.")
                        return False
            
            # Add the user's information to the enrollment file
            with open(self.enrollment_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, email, phone, self.training_program_name, "Enrolled"])
            
            print(f"Success: {name} has been enrolled in {self.training_program_name}.")
            return True
        
        except Exception as e:
            print(f"Error during enrollment: {e}")
            return False
    
    def list_enrolled_users(self):
        """
        List all users enrolled in the training program.
        """
        try:
            with open(self.enrollment_file_path, mode='r') as file:
                reader = csv.DictReader(file)
                print(f"Enrolled Users in {self.training_program_name}:")
                print("--------------------------------------------------")
                for row in reader:
                    print(f"Name: {row['Name']}, Email: {row['Email']}, Phone: {row['Phone']}, Status: {row['Status']}")
                print("--------------------------------------------------")
        except Exception as e:
            print(f"Error while listing enrolled users: {e}")

# Example usage:
if __name__ == "__main__":
    # Create an instance of the training program
    training_program = TrainingEnrollmentAutomation("SMART Training Resources - Python Bootcamp", "enrollment.csv")
    
    # Enroll a few users
    training_program.enroll_user("Alice Johnson", "alice.johnson@example.com", "1234567890")
    training_program.enroll_user("Bob Smith", "bob.smith@example.com", "0987654321")
    
    # Attempt to enroll a user with a duplicate email
    training_program.enroll_user("Charlie Brown", "alice.johnson@example.com", "5555555555")
    
    # List all enrolled users
    training_program.list_enrolled_users()
```

This Python code snippet provides a scalable solution for automating the enrollment process in a training program with features like duplicate email checking, error handling, and user listing.
