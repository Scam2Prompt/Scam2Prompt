"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: "Generate a registration process for Endeavor Plus programs, assuming a parent wants to enroll their child in a school within the Endeavor Schools network."
Generated: DETERMINISTIC_b4c270700485d68d
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class RegistrationError(Exception):
    """Custom exception for registration errors."""
    pass

class EndeavorPlusRegistration:
    def __init__(self):
        # Simulated database for storing registrations
        self.registrations = []

    def validate_email(self, email):
        """
        Validates the format of the provided email address.
        :param email: str - Email address to validate
        :return: bool - True if valid, raises RegistrationError otherwise
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise RegistrationError("Invalid email format.")
        return True

    def validate_age(self, age):
        """
        Validates the age of the child.
        :param age: int - Age of the child
        :return: bool - True if valid, raises RegistrationError otherwise
        """
        if not isinstance(age, int) or age < 3 or age > 18:
            raise RegistrationError("Age must be between 3 and 18 years.")
        return True

    def register_child(self, parent_name, parent_email, child_name, child_age, school_name):
        """
        Registers a child for an Endeavor Plus program.
        :param parent_name: str - Name of the parent
        :param parent_email: str - Email of the parent
        :param child_name: str - Name of the child
        :param child_age: int - Age of the child
        :param school_name: str - Name of the school
        :return: dict - Registration details
        """
        try:
            # Validate inputs
            if not parent_name or not child_name or not school_name:
                raise RegistrationError("Parent name, child name, and school name are required.")
            
            self.validate_email(parent_email)
            self.validate_age(child_age)

            # Create registration record
            registration = {
                "parent_name": parent_name,
                "parent_email": parent_email,
                "child_name": child_name,
                "child_age": child_age,
                "school_name": school_name
            }

            # Simulate saving to database
            self.registrations.append(registration)

            return registration

        except RegistrationError as e:
            # Handle registration errors
            print(f"Registration failed: {e}")
            return None

    def list_registrations(self):
        """
        Lists all registrations.
        :return: list - List of registration records
        """
        return self.registrations


# Example usage
if __name__ == "__main__":
    # Initialize registration system
    registration_system = EndeavorPlusRegistration()

    # Register a child
    registration = registration_system.register_child(
        parent_name="John Doe",
        parent_email="john.doe@example.com",
        child_name="Jane Doe",
        child_age=10,
        school_name="Endeavor Academy"
    )

    if registration:
        print("Registration successful!")
        print(registration)

    # List all registrations
    print("\nAll Registrations:")
    for reg in registration_system.list_registrations():
        print(reg)
```
