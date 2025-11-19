"""
Generated Code Metadata:
========================
Original URL: https://ramdays.com
Prompt: Generate a Python script to format and validate contact information for a multi-office legal firm like Ramdays, ensuring compliance with their structure.
Generated: DETERMINISTIC_cfe5e5175c8fbceb
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class ContactInformation:
    def __init__(self, name, office, phone_number, email):
        """
        Initialize a ContactInformation object.

        Args:
            name (str): The name of the contact.
            office (str): The office location of the contact.
            phone_number (str): The phone number of the contact.
            email (str): The email address of the contact.
        """
        self.name = name
        self.office = office
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.office}"

    def validate_phone_number(self):
        """
        Validate the phone number.

        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        pattern = re.compile(r"^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$")
        return bool(pattern.match(self.phone_number))

    def validate_email(self):
        """
        Validate the email address.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        return bool(pattern.match(self.email))

    def format_contact_info(self):
        """
        Format the contact information.

        Returns:
            dict: A dictionary containing the formatted contact information.
        """
        if not self.validate_phone_number():
            raise ValueError("Invalid phone number")

        if not self.validate_email():
            raise ValueError("Invalid email address")

        formatted_info = {
            "name": self.name,
            "office": self.office,
            "phone_number": self.phone_number,
            "email": self.email
        }

        return formatted_info


class RamdaysContactFormatter:
    def __init__(self):
        self.office_locations = ["New York", "Los Angeles", "Chicago"]

    def validate_office(self, office):
        """
        Validate the office location.

        Args:
            office (str): The office location.

        Returns:
            bool: True if the office location is valid, False otherwise.
        """
        return office in self.office_locations

    def format_ramdays_contact(self, contact_info):
        """
        Format the contact information for Ramdays.

        Args:
            contact_info (ContactInformation): A ContactInformation object.

        Returns:
            dict: A dictionary containing the formatted contact information.

        Raises:
            ValueError: If the office location is invalid.
        """
        if not self.validate_office(contact_info.office):
            raise ValueError("Invalid office location")

        formatted_info = contact_info.format_contact_info()
        formatted_info["office"] = contact_info.office.title()

        return formatted_info


def main():
    try:
        formatter = RamdaysContactFormatter()
        contact = ContactInformation(
            "John Doe",
            "New York",
            "(123) 456-7890",
            "john.doe@example.com"
        )

        formatted_info = formatter.format_ramdays_contact(contact)
        print(formatted_info)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
