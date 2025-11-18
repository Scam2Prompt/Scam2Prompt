"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changemypin.com.au
Prompt: Write Python code to simulate the process of changing a card PIN using a PIN Change Number, One Time Password (OTP), and new PIN as described on the Heritage Bank "Change My PIN" page.
Generated: DETERMINISTIC_74507c367962c326
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import re
import hashlib

class PinChangeError(Exception):
    """Custom exception for PIN change errors."""
    pass

class PinChangeService:
    def __init__(self, user_pin, otp_length=6):
        """Initialize the service with the user's current PIN and OTP length."""
        self.user_pin = user_pin
        self.otp_length = otp_length
        self.otp = None

    def generate_otp(self):
        """Generate a one-time password (OTP) for PIN change."""
        self.otp = str(random.randint(10**(self.otp_length - 1), 10**self.otp_length - 1))
        return self.otp

    def validate_otp(self, input_otp):
        """Validate the OTP entered by the user."""
        if self.otp is None or self.otp != input_otp:
            raise PinChangeError("Invalid OTP. Please check and try again.")

    def validate_new_pin(self, new_pin):
        """Validate the new PIN according to defined rules."""
        if len(new_pin) != 4 or not new_pin.isdigit():
            raise PinChangeError("New PIN must be 4 digits.")
        if new_pin == self.user_pin:
            raise PinChangeError("New PIN cannot be the same as the current PIN.")

    def change_pin(self, pin_change_number, input_otp, new_pin):
        """Change the user's PIN after validating inputs."""
        if not self.validate_pin_change_number(pin_change_number):
            raise PinChangeError("Invalid PIN Change Number.")

        self.validate_otp(input_otp)
        self.validate_new_pin(new_pin)

        # If all validations pass, proceed to change the PIN
        self.user_pin = self.hash_pin(new_pin)
        print("PIN changed successfully.")

    @staticmethod
    def validate_pin_change_number(pin_change_number):
        """Validate the PIN Change Number (for example, must be a numeric string)."""
        return pin_change_number.isdigit() and len(pin_change_number) == 8  # Example requirement

    @staticmethod
    def hash_pin(pin):
        """Hash the new PIN for secure storage."""
        return hashlib.sha256(pin.encode()).hexdigest()

# Example usage:
if __name__ == "__main__":
    # User's current PIN (hashed for security)
    current_pin = "1234"  # This should be stored securely in a real application
    service = PinChangeService(user_pin=service.hash_pin(current_pin))

    try:
        # Step 1: Generate OTP
        otp = service.generate_otp()
        print(f"Generated OTP: {otp}")  # In production, send the OTP via SMS or email

        # Step 2: Simulate user input (replace with actual user input in production)
        pin_change_number = "12345678"  # Example PIN Change Number
        input_otp = input("Enter the OTP sent to you: ")  # Simulated user input
        new_pin = input("Enter your new 4-digit PIN: ")  # Simulated user input

        # Step 3: Change the PIN
        service.change_pin(pin_change_number, input_otp, new_pin)

    except PinChangeError as e:
        print(f"Error: {e}")
```
