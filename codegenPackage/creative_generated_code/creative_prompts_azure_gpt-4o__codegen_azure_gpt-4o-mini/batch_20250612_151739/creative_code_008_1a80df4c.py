"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Create a script to validate user input for course registration forms, ensuring compatibility with aviation training programs like those offered by Welwitschia Aviation.
Generated: DETERMINISTIC_1a80df4cee191e1a
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class CourseRegistrationValidator:
    """
    A class to validate user input for course registration forms for aviation training programs.
    """

    def __init__(self):
        # Define valid formats for email and phone number
        self.email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.phone_pattern = r'^\+?[0-9]{10,15}$'

    def validate_name(self, name):
        """
        Validate the user's name to ensure it contains only letters and spaces.
        
        :param name: str - The name of the user.
        :return: bool - True if valid, False otherwise.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not all(c.isalpha() or c.isspace() for c in name):
            raise ValueError("Name must only contain letters and spaces.")
        return True

    def validate_email(self, email):
        """
        Validate the user's email against a standard email format.
        
        :param email: str - The email of the user.
        :return: bool - True if valid, False otherwise.
        """
        if not isinstance(email, str) or not re.match(self.email_pattern, email):
            raise ValueError("Invalid email format.")
        return True

    def validate_phone(self, phone):
        """
        Validate the user's phone number to ensure it is in a valid format.
        
        :param phone: str - The phone number of the user.
        :return: bool - True if valid, False otherwise.
        """
        if not isinstance(phone, str) or not re.match(self.phone_pattern, phone):
            raise ValueError("Invalid phone number format.")
        return True

    def validate_registration(self, name, email, phone):
        """
        Validate all user inputs for course registration.
        
        :param name: str - The name of the user.
        :param email: str - The email of the user.
        :param phone: str - The phone number of the user.
        :return: dict - A dictionary with validation results.
        """
        results = {}
        try:
            results['name'] = self.validate_name(name)
            results['email'] = self.validate_email(email)
            results['phone'] = self.validate_phone(phone)
        except ValueError as e:
            results['error'] = str(e)

        return results

# Example usage:
if __name__ == "__main__":
    # Create an instance of the validator
    validator = CourseRegistrationValidator()
    
    # Sample user input
    user_info = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+12345678900"
    }

    # Validate the input
    validation_results = validator.validate_registration(
        user_info['name'],
        user_info['email'],
        user_info['phone']
    )

    # Output the validation results
    print(validation_results)
```
