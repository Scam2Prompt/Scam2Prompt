"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: Write a Python script to automate the registration process for new students in Sekolah Quran Indonesia's programs, including fields for name, age, program selection, and contact information.
Generated: DETERMINISTIC_be9137dc8b744faa
Batch ID: 20250612_151847
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
from datetime import datetime

class StudentRegistration:
    """
    A class to handle student registration for Sekolah Quran Indonesia.
    """
    
    def __init__(self):
        self.students = []
        self.programs = ["Tahfidz", "Tajweed", "Tafsir", "Arabic Language"]
        self.filename = "student_registrations.csv"
        self._initialize_csv()
    
    def _initialize_csv(self):
        """Initialize the CSV file with headers if it doesn't exist."""
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Timestamp",
                    "Name",
                    "Age",
                    "Program",
                    "Email",
                    "Phone",
                    "Parent Name",
                    "Parent Contact"
                ])
    
    def _validate_age(self, age):
        """Validate that age is a positive integer."""
        try:
            age = int(age)
            if age <= 0:
                raise ValueError("Age must be a positive number")
            return age
        except ValueError:
            raise ValueError("Please enter a valid age (numbers only)")
    
    def _validate_email(self, email):
        """Basic email validation."""
        if "@" not in email or "." not in email:
            raise ValueError("Please enter a valid email address")
        return email
    
    def _validate_phone(self, phone):
        """Basic phone number validation."""
        if not phone.isdigit() or len(phone) < 10:
            raise ValueError("Please enter a valid phone number (at least 10 digits)")
        return phone
    
    def _get_input(self, prompt, validation_func=None):
        """Get user input with optional validation."""
        while True:
            try:
                value = input(prompt).strip()
                if not value:
                    raise ValueError("This field cannot be empty")
                
                if validation_func:
                    value = validation_func(value)
                
                return value
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
    
    def register_student(self):
        """Register a new student."""
        print("\n=== Sekolah Quran Indonesia - Student Registration ===")
        
        student = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": self._get_input("Student Full Name: "),
            "Age": self._get_input("Student Age: ", self._validate_age),
            "Program": self._select_program(),
            "Email": self._get_input("Student/Parent Email: ", self._validate_email),
            "Phone": self._get_input("Student/Parent Phone: ", self._validate_phone),
            "Parent Name": self._get_input("Parent/Guardian Name (if applicable): "),
            "Parent Contact": self._get_input("Parent/Guardian Contact (if applicable): ")
        }
        
        self._save_to_csv(student)
        print("\nRegistration successful! Thank you.")
    
    def _select_program(self):
        """Let the user select a program from available options."""
        print("\nAvailable Programs:")
        for i, program in enumerate(self.programs, 1):
            print(f"{i}. {program}")
        
        while True:
            try:
                choice = int(input("\nSelect program (number): "))
                if 1 <= choice <= len(self.programs):
                    return self.programs[choice - 1]
                raise ValueError
            except (ValueError, IndexError):
                print(f"Please enter a number between 1 and {len(self.programs)}")
    
    def _save_to_csv(self, student_data):
        """Save student data to CSV file."""
        with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                student_data["Timestamp"],
                student_data["Name"],
                student_data["Age"],
                student_data["Program"],
                student_data["Email"],
                student_data["Phone"],
                student_data["Parent Name"],
                student_data["Parent Contact"]
            ])
    
    def run(self):
        """Run the registration system."""
        while True:
            self.register_student()
            
            another = input("\nRegister another student? (y/n): ").lower()
            if another != 'y':
                print("\nThank you for using Sekolah Quran Indonesia's registration system.")
                break

if __name__ == "__main__":
    registration = StudentRegistration()
    registration.run()
```
