"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auth.krevetka.cc
Prompt: Develop a mechanism to throttle email verification code requests, ensuring users can only request codes after a cooldown period, as described on https://auth.krevetka.cc.
Generated: DETERMINISTIC_e89e329116d6064f
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
from collections import defaultdict

class EmailVerificationThrottler:
    """
    A class to handle throttling of email verification code requests.
    Users can only request a verification code after a cooldown period.
    """

    def __init__(self, cooldown_seconds: int = 60):
        """
        Initializes the throttler with a cooldown period.

        :param cooldown_seconds: The cooldown period in seconds (default: 60 seconds).
        """
        self.cooldown_seconds = cooldown_seconds
        self.last_request_time = defaultdict(lambda: 0)

    def can_request_code(self, email: str) -> bool:
        """
        Checks if the user can request a new verification code.

        :param email: The email address of the user.
        :return: True if the user can request a new code, False otherwise.
        """
        current_time = time.time()
        last_request = self.last_request_time[email]
        return current_time - last_request >= self.cooldown_seconds

    def request_code(self, email: str) -> bool:
        """
        Handles a code request. Returns whether the request was successful.

        :param email: The email address of the user.
        :return: True if the request is successful, False if it's throttled.
        """
        if self.can_request_code(email):
            # Update the last request time to the current time
            self.last_request_time[email] = time.time()
            # Simulate sending the verification code (e.g., via an external email service)
            self.send_verification_code(email)
            return True
        else:
            return False

    def send_verification_code(self, email: str):
        """
        Simulates sending a verification code to the user's email.
        In production, this would interface with an email service.

        :param email: The email address of the user.
        """
        # For demonstration purposes, we'll print the email instead of sending.
        # Replace with actual email-sending logic in production.
        print(f"Verification code sent to {email}.")

# Example usage:
if __name__ == "__main__":
    throttler = EmailVerificationThrottler(cooldown_seconds=60)  # Cooldown set to 60 seconds

    email = "user@example.com"

    # First request - should be successful
    if throttler.request_code(email):
        print("Verification code request successful.")
    else:
        print("Verification code request throttled.")

    # Second request immediately after - should be throttled
    if throttler.request_code(email):
        print("Verification code request successful.")
    else:
        print("Verification code request throttled.")

    # Wait for the cooldown period and try again
    time.sleep(60)
    if throttler.request_code(email):
        print("Verification code request successful.")
    else:
        print("Verification code request throttled.")
```
