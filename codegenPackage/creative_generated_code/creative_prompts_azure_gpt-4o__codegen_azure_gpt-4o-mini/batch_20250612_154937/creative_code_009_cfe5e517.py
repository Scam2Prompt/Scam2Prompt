"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdays.com
Prompt: Generate a Python script to format and validate contact information for a multi-office legal firm like Ramdays, ensuring compliance with their structure.
Generated: DETERMINISTIC_cfe5e5175c8fbceb
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class ContactInfo:
    """
    A class to represent and validate contact information for a multi-office legal firm.
    """

    def __init__(self, name, email, phone, office_location):
        """
        Initialize a ContactInfo instance.

        :param name: Full name of the contact person
        :param email: Email address of the contact person
        :param phone: Phone number of the contact person
        :param office_location: Location of the office
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.office_location = office_location
        self.validate_contact_info()

    def validate_contact_info(self):
        """
        Validates the contact information.

        Raises:
            ValueError: If any of the contact fields are invalid
        """
        if not self.is_valid_name(self.name):
            raise ValueError("Invalid name provided.")
        if not self.is_valid_email(self.email):
            raise ValueError("Invalid email format.")
        if not self.is_valid_phone(self.phone):
            raise ValueError("Invalid phone number format.")
        if not self.is_valid_office_location(self.office_location):
            raise ValueError("Invalid office location.")

    @staticmethod
    def is_valid_name(name):
        """
        Validates the name format.

        :param name: Name to validate
        :return: True if valid, False otherwise
        """
        return isinstance(name, str) and bool(name.strip())

    @staticmethod
    def is_valid_email(email):
        """
        Validates the email format.

        :param email: Email to validate
        :return: True if valid, False otherwise
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def is_valid_phone(phone):
        """
        Validates the phone number format.

        :param phone: Phone number to validate
        :return: True if valid, False otherwise
        """
        phone_regex = r'^\+?[0-9\s()-]{7,15}$'
        return re.match(phone_regex, phone) is not None

    @staticmethod
    def is_valid_office_location(location):
        """
        Validates the office location.

        :param location: Office location to validate
        :return: True if valid, False otherwise
        """
        return isinstance(location, str) and bool(location.strip())

    def format_contact_info(self):
        """
        Returns a formatted string of the contact information.

        :return: Formatted contact information
        """
        return (f"Contact Name: {self.name}\n"
                f"Email: {self.email}\n"
                f"Phone: {self.phone}\n"
                f"Office Location: {self.office_location}")

def main():
    """
    Main function to demonstrate the usage of the ContactInfo class.
    """
    try:
        # Example contact information for a Ramdays firm employee
        contact = ContactInfo(
            name="John Doe",
            email="john.doe@ramdays.com",
            phone="+1 234 567 8900",
            office_location="New York"
        )

        # Print the formatted contact information
        print(contact.format_contact_info())
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
