"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-re.was-systems.com
Prompt: Generate a code snippet that validates user input for a recommendation system, ensuring that all fields are filled out correctly before submission.
Generated: DETERMINISTIC_0bf9b748e34c5491
Batch ID: 20250612_155233
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
    A class to validate user input for a recommendation system.
    """

    def __init__(self, name: str, email: str, recommendation: str):
        self.name = name
        self.email = email
        self.recommendation = recommendation

    def validate(self) -> bool:
        """
        Validate the user input fields.
        
        Returns:
            bool: True if all fields are valid, False otherwise.
        """
        if not self.validate_name(self.name):
            raise ValueError("Invalid name. Name must be between 1 and 50 characters.")
        
        if not self.validate_email(self.email):
            raise ValueError("Invalid email address.")
        
        if not self.validate_recommendation(self.recommendation):
            raise ValueError("Recommendation must be between 1 and 500 characters.")
        
        return True

    @staticmethod
    def validate_name(name: str) -> bool:
        """
        Validates the name input.
        
        Args:
            name (str): The name to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        return 1 <= len(name) <= 50

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validates the email input using regex.
        
        Args:
            email (str): The email to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def validate_recommendation(recommendation: str) -> bool:
        """
        Validates the recommendation input.
        
        Args:
            recommendation (str): The recommendation to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        return 1 <= len(recommendation) <= 500


# Example usage
if __name__ == "__main__":
    try:
        user_input = UserInputValidator(name="John Doe", email="john.doe@example.com", recommendation="This is a great product!")
        if user_input.validate():
            print("User input is valid. Proceeding with submission.")
    except ValueError as e:
        print(f"Input validation error: {e}")
```
