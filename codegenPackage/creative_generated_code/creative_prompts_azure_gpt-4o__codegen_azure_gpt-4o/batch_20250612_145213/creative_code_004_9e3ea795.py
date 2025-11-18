"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledger-live-ledger.org
Prompt: Write code to automate user registration on a betting platform like Vavada, including validation for required fields and bonus eligibility checks.
Generated: DETERMINISTIC_9e3ea795b07b8e76
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import re
from datetime import datetime

class UserRegistration:
    def __init__(self):
        # Initialize a list to store registered users
        self.registered_users = []

    def validate_registration_data(self, username, email, password, dob):
        """
        Validate required fields for user registration.
        """
        # Check if username is provided and within the acceptable length
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters long.")
        
        # Validate email format using a regex pattern
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not email or not re.match(email_pattern, email):
            raise ValueError("Invalid email address.")
        
        # Validate password complexity (must be at least 8 characters long)
        if not password or len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        
        # Validate date of birth format and check age (must be above 18)
        try:
            dob_date = datetime.strptime(dob, '%Y-%m-%d')
            age = (datetime.now() - dob_date).days // 365
            if age < 18:
                raise ValueError("User must be at least 18 years old to register.")
        except ValueError:
            raise ValueError("Invalid date of birth format. Use YYYY-MM-DD.")

        # All validations passed
        return True

    def check_bonus_eligibility(self, dob):
        """
        Check bonus eligibility based on the user's age.
        """
        dob_date = datetime.strptime(dob, '%Y-%m-%d')
        age = (datetime.now() - dob_date).days // 365
        # Example rule: Users between 18-25 years old are eligible for a bonus
        if 18 <= age <= 25:
            return True
        return False

    def register_user(self, username, email, password, dob):
        """
        Handle the user registration process.
        """
        try:
            # Validate user inputs
            self.validate_registration_data(username, email, password, dob)

            # Check bonus eligibility
            bonus_eligible = self.check_bonus_eligibility(dob)

            # Create a user object and store it in the registered users list
            user = {
                "username": username,
                "email": email,
                "password": password,  # Note: Password handling should be hashed in production
                "dob": dob,
                "bonus_eligible": bonus_eligible
            }
            self.registered_users.append(user)
            return f"User {username} registered successfully. Bonus eligible: {bonus_eligible}"

        except ValueError as e:
            # Handle validation errors
            return f"Registration failed: {str(e)}"

# Example Usage
if __name__ == "__main__":
    registration_system = UserRegistration()
    try:
        # Test with valid input
        print(registration_system.register_user("JohnDoe", "john@example.com", "Password123", "1999-05-15"))
        
        # Test with invalid input (e.g., underage user)
        print(registration_system.register_user("Alice", "alice@example.com", "Password123", "2010-07-20"))
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
