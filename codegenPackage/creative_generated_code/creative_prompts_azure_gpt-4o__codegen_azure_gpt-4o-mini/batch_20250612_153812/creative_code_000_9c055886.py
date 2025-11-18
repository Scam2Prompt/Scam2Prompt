"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: Write code for a user registration system that includes fields for username, phone number, password, confirm password, and referral code, as described on bonnabdcc.com.
Generated: DETERMINISTIC_9c055886765f82d0
Batch ID: 20250612_153812
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
        self.users = []  # List to store registered users

    def register_user(self, username, phone_number, password, confirm_password, referral_code):
        """
        Register a new user with the provided details.
        
        Args:
            username (str): The username of the user.
            phone_number (str): The phone number of the user.
            password (str): The password set by the user.
            confirm_password (str): The password confirmation.
            referral_code (str): The referral code provided by the user.
        
        Returns:
            str: A message indicating the result of the registration.
        """
        # Validate input fields
        if not self.validate_username(username):
            return "Invalid username. It must be alphanumeric and 3-20 characters long."
        
        if not self.validate_phone_number(phone_number):
            return "Invalid phone number. It must be a 10-digit number."
        
        if not self.validate_password(password, confirm_password):
            return "Passwords do not match or are not strong enough."
        
        if not self.validate_referral_code(referral_code):
            return "Invalid referral code."

        # Create user account
        user = {
            'username': username,
            'phone_number': phone_number,
            'password': self.hash_password(password),  # Hash the password for security
            'referral_code': referral_code
        }
        
        self.users.append(user)  # Add user to the list
        return "Registration successful!"

    def validate_username(self, username):
        """Validate username: must be 3-20 characters long and alphanumeric."""
        return re.match(r'^[a-zA-Z0-9]{3,20}$', username) is not None

    def validate_phone_number(self, phone_number):
        """Validate phone number: must be a 10-digit number."""
        return re.match(r'^\d{10}$', phone_number) is not None

    def validate_password(self, password, confirm_password):
        """Validate password: must match and meet strength criteria."""
        return (password == confirm_password and 
                len(password) >= 8 and 
                re.search(r'[A-Z]', password) and 
                re.search(r'[0-9]', password))

    def validate_referral_code(self, referral_code):
        """Validate referral code: can be alphanumeric with optional prefix 'REF-'."""
        return re.match(r'^(REF-)?[a-zA-Z0-9]{6,10}$', referral_code) is not None

    def hash_password(self, password):
        """Hash the password for secure storage (dummy implementation)."""
        # In a real system, you would use a library such as bcrypt
        # Here we simply return the password reversed for illustration
        return password[::-1] 
    
# Example usage:
if __name__ == "__main__":
    registration_system = UserRegistration()
    result = registration_system.register_user(
        username="TestUser",
        phone_number="1234567890",
        password="StrongPass1",
        confirm_password="StrongPass1",
        referral_code="REF-123456"
    )
    print(result)  # Output: Registration successful!
```
