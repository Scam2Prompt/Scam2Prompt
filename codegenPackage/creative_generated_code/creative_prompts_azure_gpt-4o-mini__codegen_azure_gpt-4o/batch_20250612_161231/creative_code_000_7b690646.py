"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treasury.casino
Prompt: Generate a Python script to automate the registration process for new users at Treasury Brisbane Casino, including handling deposit methods and bonus application.
Generated: DETERMINISTIC_7b690646322111e9
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class CasinoRegistrationSystem:
    """
    Automates the registration process for new users at Treasury Brisbane Casino.
    Handles deposit methods and bonus application.
    """
    
    def __init__(self):
        # Supported deposit methods
        self.deposit_methods = ["Credit Card", "Debit Card", "PayPal", "Bank Transfer"]
        # Bonus information
        self.bonus_threshold = 100  # Minimum deposit for bonus eligibility
        self.bonus_percentage = 10  # Bonus percentage (e.g., 10% of deposit)

    def validate_email(self, email):
        """
        Validates the format of the email address.
        Returns True if valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def register_user(self, name, email, deposit_amount, deposit_method):
        """
        Registers a new user and applies bonuses if applicable.
        :param name: Full name of the user
        :param email: Email address of the user
        :param deposit_amount: Initial deposit amount
        :param deposit_method: Selected deposit method
        """
        # Validate user input
        if not name or not name.strip():
            raise ValueError("Invalid name. Name cannot be empty.")
        
        if not self.validate_email(email):
            raise ValueError("Invalid email address.")

        if deposit_method not in self.deposit_methods:
            raise ValueError(f"Invalid deposit method. Supported methods: {', '.join(self.deposit_methods)}")
        
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        # Apply bonus if eligible
        bonus = 0
        if deposit_amount >= self.bonus_threshold:
            bonus = deposit_amount * self.bonus_percentage / 100
        
        # Simulate saving to a database (stubbed for this example)
        user_data = {
            "name": name,
            "email": email,
            "deposit_amount": deposit_amount,
            "deposit_method": deposit_method,
            "bonus": bonus
        }
        # For demonstration purposes, print user data
        print("User successfully registered!")
        print(f"User Details:\n{user_data}")

    def display_deposit_methods(self):
        """
        Displays the supported deposit methods.
        """
        print("Supported Deposit Methods:")
        for method in self.deposit_methods:
            print(f"- {method}")

# Example usage
if __name__ == "__main__":
    try:
        system = CasinoRegistrationSystem()

        # Display available deposit methods
        system.display_deposit_methods()

        # Register a new user (replace inputs with user-provided data in production)
        user_name = "John Doe"
        user_email = "john.doe@example.com"
        user_deposit_amount = 150
        user_deposit_method = "Credit Card"

        system.register_user(user_name, user_email, user_deposit_amount, user_deposit_method)

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
