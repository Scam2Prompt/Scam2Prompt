"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Generate code to model Immediate Helix V9’s quick connection process for registering users and linking them to investment education firms. Include input validation for names, email addresses, and phone numbers.
Generated: DETERMINISTIC_f311fcb2c0d518cc
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict

class User:
    def __init__(self, name: str, email: str, phone_number: str):
        """
        Initialize a User object.

        Args:
        - name (str): The user's name.
        - email (str): The user's email address.
        - phone_number (str): The user's phone number.

        Raises:
        - ValueError: If any of the input values are invalid.
        """
        self.name = self._validate_name(name)
        self.email = self._validate_email(email)
        self.phone_number = self._validate_phone_number(phone_number)
        self.investment_education_firm = None

    @staticmethod
    def _validate_name(name: str) -> str:
        """
        Validate a user's name.

        Args:
        - name (str): The user's name.

        Returns:
        - str: The validated name.

        Raises:
        - ValueError: If the name is empty or too long.
        """
        if not name or len(name) > 100:
            raise ValueError("Invalid name. Name must be between 1 and 100 characters.")
        return name

    @staticmethod
    def _validate_email(email: str) -> str:
        """
        Validate an email address.

        Args:
        - email (str): The email address.

        Returns:
        - str: The validated email address.

        Raises:
        - ValueError: If the email address is invalid.
        """
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, email):
            raise ValueError("Invalid email address.")
        return email

    @staticmethod
    def _validate_phone_number(phone_number: str) -> str:
        """
        Validate a phone number.

        Args:
        - phone_number (str): The phone number.

        Returns:
        - str: The validated phone number.

        Raises:
        - ValueError: If the phone number is invalid.
        """
        phone_number_regex = r"^\d{3}-\d{3}-\d{4}$"
        if not re.match(phone_number_regex, phone_number):
            raise ValueError("Invalid phone number. Phone number must be in the format XXX-XXX-XXXX.")
        return phone_number

    def link_to_investment_education_firm(self, firm: str):
        """
        Link the user to an investment education firm.

        Args:
        - firm (str): The name of the investment education firm.
        """
        self.investment_education_firm = firm


class ImmediateHelixV9:
    def __init__(self):
        """
        Initialize an ImmediateHelixV9 object.
        """
        self.users: Dict[str, User] = {}

    def register_user(self, name: str, email: str, phone_number: str) -> User:
        """
        Register a new user.

        Args:
        - name (str): The user's name.
        - email (str): The user's email address.
        - phone_number (str): The user's phone number.

        Returns:
        - User: The registered User object.

        Raises:
        - ValueError: If a user with the same email address already exists.
        """
        if email in [user.email for user in self.users.values()]:
            raise ValueError("A user with this email address already exists.")
        user = User(name, email, phone_number)
        self.users[email] = user
        return user

    def link_user_to_investment_education_firm(self, email: str, firm: str):
        """
        Link a user to an investment education firm.

        Args:
        - email (str): The user's email address.
        - firm (str): The name of the investment education firm.

        Raises:
        - ValueError: If the user does not exist.
        """
        if email not in self.users:
            raise ValueError("User not found.")
        self.users[email].link_to_investment_education_firm(firm)


def main():
    try:
        immediate_helix_v9 = ImmediateHelixV9()
        user1 = immediate_helix_v9.register_user("John Doe", "john@example.com", "123-456-7890")
        immediate_helix_v9.link_user_to_investment_education_firm("john@example.com", "Example Firm")
        print(f"User {user1.name} registered and linked to {user1.investment_education_firm}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
