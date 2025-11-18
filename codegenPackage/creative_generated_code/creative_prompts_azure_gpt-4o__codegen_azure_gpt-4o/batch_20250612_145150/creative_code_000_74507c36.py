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

class PinChangeSystem:
    def __init__(self):
        # Simulated storage for user data (in production, this would be a secure database)
        self.user_data = {
            "card_number": "1234567890123456",  # Example card number
            "pin_change_number": "ABC123",     # Example PIN change number
            "current_pin": "1234",             # Example current PIN
            "otp": None                        # One Time Password (OTP) will be generated dynamically
        }

    def generate_otp(self):
        """Generate a random 6-digit OTP."""
        self.user_data['otp'] = str(random.randint(100000, 999999))
        print(f"OTP Generated: {self.user_data['otp']}")  # In production, send this via SMS or email

    def validate_inputs(self, pin_change_number, otp, new_pin):
        """
        Validate the PIN change number, OTP, and new PIN.
        :param pin_change_number: The PIN change number provided by the user
        :param otp: The OTP provided by the user
        :param new_pin: The new PIN provided by the user
        :return: Boolean indicating if inputs are valid
        """
        # Check if PIN change number matches
        if pin_change_number != self.user_data['pin_change_number']:
            raise ValueError("Invalid PIN change number.")

        # Check if OTP matches
        if otp != self.user_data['otp']:
            raise ValueError("Invalid OTP.")

        # Check if new PIN is valid (must be a 4-digit number)
        if not re.match(r"^\d{4}$", new_pin):
            raise ValueError("New PIN must be a 4-digit number.")

        return True

    def change_pin(self, pin_change_number, otp, new_pin):
        """
        Simulate the process of changing the card PIN.
        :param pin_change_number: The PIN change number provided by the user
        :param otp: The OTP provided by the user
        :param new_pin: The new PIN provided by the user
        :return: Confirmation message
        """
        try:
            # Validate inputs
            if self.validate_inputs(pin_change_number, otp, new_pin):
                # Update the PIN in the simulated storage
                self.user_data['current_pin'] = new_pin
                return "PIN successfully changed."
        except ValueError as e:
            return str(e)

# --- Example Usage ---
if __name__ == "__main__":
    # Create an instance of the PinChangeSystem
    pin_system = PinChangeSystem()

    # Generate an OTP (simulates sending it to the user via SMS or email)
    pin_system.generate_otp()

    # Simulated user inputs
    user_pin_change_number = "ABC123"  # Correct PIN change number
    user_otp = input("Enter the OTP sent to your registered mobile/email: ")  # OTP received by user
    user_new_pin = input("Enter your new 4-digit PIN: ")  # New PIN provided by user

    # Attempt to change the PIN
    result = pin_system.change_pin(user_pin_change_number, user_otp, user_new_pin)

    # Display the result
    print(result)
```
