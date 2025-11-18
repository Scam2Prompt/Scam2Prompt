"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auth.krevetka.cc
Prompt: Implement a feature to resend email verification codes for a VPN account, with restrictions on the number of attempts and error handling for invalid codes, based on the process described on https://auth.krevetka.cc.
Generated: DETERMINISTIC_3ab314868f8d082d
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta
import random
import string

class EmailVerificationService:
    def __init__(self, max_attempts=3, cooldown_minutes=10):
        """
        Initializes the verification service.
        :param max_attempts: Maximum number of resend attempts allowed.
        :param cooldown_minutes: Cooldown period in minutes before allowing another resend attempt.
        """
        self.max_attempts = max_attempts
        self.cooldown_minutes = cooldown_minutes
        self.verification_codes = {}  # Stores codes and resend attempts by user_id

    def generate_verification_code(self):
        """
        Generates a random verification code.
        :return: A string verification code (6 alphanumeric characters).
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    def send_email(self, user_email, verification_code):
        """
        Simulates sending an email. In production, integrate with an email service.
        :param user_email: The recipient's email address.
        :param verification_code: The verification code to send.
        """
        # Simulated email sending logic
        print(f"Sending verification code '{verification_code}' to {user_email}")

    def resend_verification_code(self, user_id, user_email):
        """
        Resends the verification code to the user's email if conditions are met.
        :param user_id: The unique identifier for the user.
        :param user_email: The email address to send the code to.
        """
        current_time = datetime.now()

        if user_id not in self.verification_codes:
            # If no previous record exists, initialize it
            self.verification_codes[user_id] = {
                "code": self.generate_verification_code(),
                "attempts": 0,
                "last_sent_time": None
            }

        user_data = self.verification_codes[user_id]

        # Check if the user has exceeded the maximum attempts
        if user_data["attempts"] >= self.max_attempts:
            print("Error: Maximum resend attempts exceeded.")
            return

        # Check if the cooldown period has passed
        if user_data["last_sent_time"]:
            elapsed_time = current_time - user_data["last_sent_time"]
            if elapsed_time < timedelta(minutes=self.cooldown_minutes):
                remaining_time = (timedelta(minutes=self.cooldown_minutes) - elapsed_time).seconds
                print(f"Error: Cooldown period active. Please retry in {remaining_time} seconds.")
                return

        # Generate a new code and send it
        user_data["code"] = self.generate_verification_code()
        user_data["attempts"] += 1
        user_data["last_sent_time"] = current_time
        self.send_email(user_email, user_data["code"])
        print("Verification code resent successfully.")

    def validate_verification_code(self, user_id, code):
        """
        Validates the verification code entered by the user.
        :param user_id: The unique identifier for the user.
        :param code: The code entered by the user.
        :return: True if the code is valid, False otherwise.
        """
        if user_id not in self.verification_codes:
            print("Error: No verification code found for the specified user.")
            return False

        user_data = self.verification_codes[user_id]
        if code == user_data["code"]:
            print("Verification code validated successfully.")
            return True
        else:
            print("Error: Invalid verification code.")
            return False


# Example usage:
if __name__ == "__main__":
    # Create an instance of the verification service
    email_service = EmailVerificationService(max_attempts=3, cooldown_minutes=1)

    # Simulated user ID and email
    test_user_id = "user123"
    test_user_email = "user123@example.com"

    # Resend verification code
    email_service.resend_verification_code(test_user_id, test_user_email)

    # Wait for cooldown and resend again (simulate with time.sleep if necessary)
    time.sleep(2)  # Adjust sleep time to test cooldown period behavior
    email_service.resend_verification_code(test_user_id, test_user_email)

    # Validate the verification code
    valid_code = email_service.verification_codes[test_user_id]["code"]
    email_service.validate_verification_code(test_user_id, valid_code)

    # Test invalid code
    email_service.validate_verification_code(test_user_id, "invalid123")
```
