"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-xzen.com
Prompt: Write a script to simulate the verification process for user registration on Immediate ZenX, including checks for valid email addresses and phone numbers.
Generated: DETERMINISTIC_c1044af504352cea
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class UserRegistration:
    def __init__(self):
        self.users = []

    def is_valid_email(self, email):
        """
        Validate the email address format using regex.
        :param email: str - Email address to validate.
        :return: bool - True if valid email, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        is_valid = re.match(email_regex, email) is not None
        return is_valid

    def is_valid_phone(self, phone):
        """
        Validate the phone number format.
        For simplicity, we assume valid phone numbers are 10 digits long.
        :param phone: str - Phone number to validate.
        :return: bool - True if valid phone number, False otherwise.
        """
        phone_regex = r'^\d{10}$'
        is_valid = re.match(phone_regex, phone) is not None
        return is_valid

    def register_user(self, email, phone):
        """
        Register a new user after validation of email and phone number.
        :param email: str - User's email address.
        :param phone: str - User's phone number.
        :raises ValueError: If email or phone number is invalid.
        """
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address provided.")
        
        if not self.is_valid_phone(phone):
            raise ValueError("Invalid phone number provided.")
        
        # Store the user information
        user_info = {'email': email, 'phone': phone}
        self.users.append(user_info)
        return user_info

    def display_users(self):
        """Display all registered users."""
        for user in self.users:
            print(f"Email: {user['email']}, Phone: {user['phone']}")

if __name__ == "__main__":
    registration_system = UserRegistration()

    # Sample user registration
    try:
        user1 = registration_system.register_user("test@example.com", "1234567890")
        print("User registered successfully:", user1)
        
        user2 = registration_system.register_user("invalid-email", "12345")
        print("User registered successfully:", user2)
    except ValueError as e:
        print(e)

    # Display all registered users
    registration_system.display_users()
```
