"""
Generated Code Metadata:
========================
Original URL: https://openseas.jp
Prompt: Can you write a simple Python script to handle inquiries about Open Seas, including name, school/organization, position, and email address?
Generated: DETERMINISTIC_582ce0a3c162ad3d
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class Inquiry:
    """
    A class to represent an inquiry about Open Seas.

    Attributes:
        name (str): The name of the person making the inquiry.
        organization (str): The school or organization of the person.
        position (str): The position of the person in the organization.
        email (str): The email address of the person.
    """

    def __init__(self, name, organization, position, email):
        self.name = name
        self.organization = organization
        self.position = position
        self.email = email

    def validate_email(self):
        """
        Validates the email address format.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, self.email) is not None

    def display_inquiry(self):
        """
        Displays the inquiry details.
        """
        print("Inquiry Details:")
        print(f"Name: {self.name}")
        print(f"Organization: {self.organization}")
        print(f"Position: {self.position}")
        print(f"Email: {self.email}")

def main():
    """
    Main function to handle user inquiries.
    """
    try:
        # Collecting user input
        name = input("Enter your name: ")
        organization = input("Enter your school/organization: ")
        position = input("Enter your position: ")
        email = input("Enter your email address: ")

        # Creating an Inquiry object
        inquiry = Inquiry(name, organization, position, email)

        # Validating email
        if not inquiry.validate_email():
            raise ValueError("Invalid email address format.")

        # Displaying the inquiry details
        inquiry.display_inquiry()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
