"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gigzio.com
Prompt: Write a program to create a user profile for job seekers, including fields for career alignment and resume parsing, inspired by Gigzio's tools.
Generated: DETERMINISTIC_148c55c37df0c0ce
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import os

class UserProfile:
    """
    A class to create and manage user profiles for job seekers.
    """
    def __init__(self, name, email, phone, career_alignment, resume_path):
        """
        Initialize the user profile with necessary details.

        :param name: Full name of the user
        :param email: Email address of the user
        :param phone: Phone number of the user
        :param career_alignment: Desired career field or alignment
        :param resume_path: Path to the user's resume file
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.career_alignment = career_alignment
        self.resume_path = resume_path
        self.resume_text = ""

        # Validate inputs
        self.validate_email()
        self.validate_phone()
        self.validate_resume()

    def validate_email(self):
        """
        Validate the email format using a regular expression.
        """
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b$'
        if not re.match(email_regex, self.email):
            raise ValueError(f"Invalid email address: {self.email}")

    def validate_phone(self):
        """
        Validate the phone number format (basic validation for 10 digits).
        """
        phone_regex = r'^\d{10}$'
        if not re.match(phone_regex, self.phone):
            raise ValueError(f"Invalid phone number: {self.phone}. Must be 10 digits.")

    def validate_resume(self):
        """
        Validate that the resume file exists and is readable.
        """
        if not os.path.exists(self.resume_path):
            raise FileNotFoundError(f"Resume file not found: {self.resume_path}")
        if not os.path.isfile(self.resume_path):
            raise ValueError(f"Provided resume path is not a file: {self.resume_path}")

    def parse_resume(self):
        """
        Parse the resume file and extract text content.

        Note: This is a simple plain-text parser. Advanced parsing (e.g., PDFs, DOCX)
        can be implemented using libraries such as PyPDF2 or python-docx.
        """
        try:
            with open(self.resume_path, 'r') as file:
                self.resume_text = file.read()
        except Exception as e:
            raise IOError(f"Error reading resume file: {e}")

    def display_profile(self):
        """
        Display the user profile.
        """
        print("User Profile")
        print("------------")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Career Alignment: {self.career_alignment}")
        print("Resume Content:")
        print(self.resume_text if self.resume_text else "[Resume not parsed yet]")

# Example Usage (uncomment for testing)
# try:
#     profile = UserProfile(
#         name="John Doe",
#         email="john.doe@example.com",
#         phone="1234567890",
#         career_alignment="Software Development",
#         resume_path="path/to/resume.txt"
#     )
#     profile.parse_resume()
#     profile.display_profile()
# except Exception as e:
#     print(f"Error occurred: {e}")
```
