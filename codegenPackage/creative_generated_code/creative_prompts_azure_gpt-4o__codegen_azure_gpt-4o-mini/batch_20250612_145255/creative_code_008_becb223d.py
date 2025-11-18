"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudsverse-opsec.com
Prompt: Generate a script to validate user input for contacting M2 Earn Ltd, ensuring the data aligns with their secure and transparent operations policy.
Generated: DETERMINISTIC_becb223dab30d03d
Batch ID: 20250612_145255
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
    A class to validate user input for contacting M2 Earn Ltd.
    """

    def __init__(self):
        # Regular expressions for validation
        self.email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.phone_regex = r'^\+?[1-9]\d{1,14}$'  # E.164 phone format

    def validate_email(self, email: str) -> bool:
        """
        Validate email address.
        
        Args:
            email (str): The email address to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        if not email:
            raise ValueError("Email cannot be empty.")
        if re.match(self.email_regex, email):
            return True
        return False

    def validate_phone(self, phone: str) -> bool:
        """
        Validate phone number.
        
        Args:
            phone (str): The phone number to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        if not phone:
            raise ValueError("Phone number cannot be empty.")
        if re.match(self.phone_regex, phone):
            return True
        return False
    
    def validate_message(self, message: str) -> bool:
        """
        Validate message length.
        
        Args:
            message (str): The message to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        if not message:
            raise ValueError("Message cannot be empty.")
        if len(message) > 500:
            raise ValueError("Message exceeds 500 characters.")
        return True

def main():
    # Example user input
    user_input = {
        'email': 'user@example.com',
        'phone': '+1234567890',
        'message': 'Hello, I would like to know more about your services.'
    }

    validator = UserInputValidator()

    try:
        # Validate user input
        if (validator.validate_email(user_input['email']) and
                validator.validate_phone(user_input['phone']) and
                validator.validate_message(user_input['message'])):
            print("All inputs are valid. Proceed to contact M2 Earn Ltd.")
        else:
            print("Invalid input detected.")

    except ValueError as e:
        print(f"Input validation error: {e}")

if __name__ == "__main__":
    main()
```
