"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prgmea.pk
Prompt: Write a code snippet to automate the visitor registration process for the Pakistan Readymade Garments Manufacturers & Exporters Association.
Generated: DETERMINISTIC_a9aec1fe30300f3d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class VisitorRegistration:
    """Class to manage visitor registration for the Pakistan Readymade Garments Manufacturers & Exporters Association."""

    def __init__(self):
        """Initializes the registration system and loads existing registrations."""
        self.registrations_file = 'registrations.json'
        self.registrations = self.load_registrations()

    def load_registrations(self):
        """Loads existing registrations from a JSON file."""
        try:
            with open(self.registrations_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            return []
        except json.JSONDecodeError:
            # Handle JSON decoding errors
            print("Error loading registrations. Starting with an empty list.")
            return []

    def save_registrations(self):
        """Saves the current registrations to a JSON file."""
        try:
            with open(self.registrations_file, 'w') as file:
                json.dump(self.registrations, file, indent=4)
        except IOError as e:
            print(f"Error saving registrations: {e}")

    def register_visitor(self, name, email, organization):
        """Registers a new visitor with the provided details.

        Args:
            name (str): The name of the visitor.
            email (str): The email address of the visitor.
            organization (str): The organization the visitor represents.

        Returns:
            dict: The registration details if successful, otherwise None.
        """
        # Validate input
        if not self.validate_email(email):
            print("Invalid email address.")
            return None

        # Create registration entry
        registration = {
            'name': name,
            'email': email,
            'organization': organization,
            'registration_date': datetime.now().isoformat()
        }

        # Add to registrations
        self.registrations.append(registration)
        self.save_registrations()  # Save to file

        return registration

    def validate_email(self, email):
        """Validates the email format.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        import re
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_pattern, email) is not None

# Example of using the VisitorRegistration class
if __name__ == "__main__":
    registration_system = VisitorRegistration()
    
    # Simulating visitor registration
    visitor_name = input("Enter your name: ")
    visitor_email = input("Enter your email: ")
    visitor_organization = input("Enter your organization: ")

    registration = registration_system.register_visitor(visitor_name, visitor_email, visitor_organization)
    
    if registration:
        print("Registration successful!")
        print("Details:", registration)
    else:
        print("Registration failed.")
```
