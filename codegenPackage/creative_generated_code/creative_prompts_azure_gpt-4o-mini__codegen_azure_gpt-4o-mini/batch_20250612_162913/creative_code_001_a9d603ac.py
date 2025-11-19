"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metrorrl.com
Prompt: How can I implement a code snippet that validates user input against the policies outlined by Metro Wholesale?
Generated: DETERMINISTIC_a9d603ac66ad6742
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class UserInputValidator:
    """
    A class to validate user input against the policies outlined by Metro Wholesale.
    """

    def __init__(self):
        # Define the policies for validation
        self.policies = {
            'username': r'^[a-zA-Z0-9._-]{3,20}$',  # Alphanumeric, 3-20 characters
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',  # Standard email format
            'phone': r'^\+?[0-9]{10,15}$',  # International format, 10-15 digits
        }

    def validate_username(self, username):
        """
        Validates the username against the defined policy.

        :param username: The username to validate
        :return: Boolean indicating whether the username is valid
        """
        if re.match(self.policies['username'], username):
            return True
        return False

    def validate_email(self, email):
        """
        Validates the email against the defined policy.

        :param email: The email to validate
        :return: Boolean indicating whether the email is valid
        """
        if re.match(self.policies['email'], email):
            return True
        return False

    def validate_phone(self, phone):
        """
        Validates the phone number against the defined policy.

        :param phone: The phone number to validate
        :return: Boolean indicating whether the phone number is valid
        """
        if re.match(self.policies['phone'], phone):
            return True
        return False

def main():
    """
    Main function to test user input validation.
    """
    validator = UserInputValidator()

    # Sample inputs for testing
    test_inputs = {
        'username': 'user_name123',
        'email': 'user@example.com',
        'phone': '+1234567890'
    }

    # Validate and print results
    try:
        username_valid = validator.validate_username(test_inputs['username'])
        email_valid = validator.validate_email(test_inputs['email'])
        phone_valid = validator.validate_phone(test_inputs['phone'])

        print(f"Username valid: {username_valid}")
        print(f"Email valid: {email_valid}")
        print(f"Phone valid: {phone_valid}")

    except Exception as e:
        print(f"An error occurred during validation: {e}")

if __name__ == '__main__':
    main()
```
