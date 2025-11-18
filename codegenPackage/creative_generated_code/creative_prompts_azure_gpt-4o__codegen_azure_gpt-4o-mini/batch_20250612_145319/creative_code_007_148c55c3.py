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
import json
import re

class UserProfile:
    """
    A class to represent a user profile for job seekers.
    """

    def __init__(self, name, email, career_alignment, resume):
        """
        Initialize the user profile with basic details.

        :param name: str - The full name of the user.
        :param email: str - The email address of the user.
        :param career_alignment: str - The career alignment of the user.
        :param resume: str - The raw resume text of the user.
        """
        self.name = name
        self.email = self.validate_email(email)
        self.career_alignment = career_alignment
        self.resume = self.parse_resume(resume)

    @staticmethod
    def validate_email(email):
        """
        Validates the email format.

        :param email: str - The email to validate.
        :return: str - Validated email.
        :raises ValueError: If email format is invalid.
        """
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        raise ValueError("Invalid email format.")

    @staticmethod
    def parse_resume(resume):
        """
        Parses the resume text to extract relevant sections.

        :param resume: str - The raw resume text.
        :return: dict - Parsed resume sections.
        """
        # Simple parsing logic for demonstration purposes
        sections = resume.split("\n\n")
        parsed_resume = {}
        
        for section in sections:
            # Assume the first line is the section title
            lines = section.split("\n")
            title = lines[0].strip()
            content = "\n".join(lines[1:]).strip()
            parsed_resume[title] = content
        
        return parsed_resume

    def to_dict(self):
        """
        Converts the user profile to a dictionary format for easy handling.

        :return: dict - The user profile as a dictionary.
        """
        return {
            "name": self.name,
            "email": self.email,
            "career_alignment": self.career_alignment,
            "resume": self.resume
        }

    def save_to_file(self, filename):
        """
        Saves the user profile to a JSON file.

        :param filename: str - The filename to save the profile.
        :raises IOError: If an error occurs during file writing.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        user_profile = UserProfile(
            name="John Doe",
            email="john.doe@example.com",
            career_alignment="Software Development",
            resume="Education:\nB.S. in Computer Science\n\nExperience:\nSoftware Developer at XYZ Corp."
        )
        user_profile.save_to_file("user_profile.json")
        print("User profile saved successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
