"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeih2wl3ewsfuyky6vpzrkjfownqie7loq3mglk5wqoqifgmwyzrwre.ipfs.dweb.link
Prompt: Write a Python script that automates user registration for NEAR, ensuring it is completed within the specified time frame.
Generated: DETERMINISTIC_f82b7d2aff56007c
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import string
from typing import Tuple

class UserRegistrationError(Exception):
    """Custom exception for user registration errors."""
    pass

class UserRegistration:
    """Class to handle user registration for NEAR."""

    def __init__(self, registration_timeout: int = 30):
        """
        Initialize the UserRegistration class.

        :param registration_timeout: Time in seconds to complete the registration (default is 30 seconds).
        """
        self.registration_timeout = registration_timeout

    def generate_username(self) -> str:
        """
        Generate a random username for the user.

        :return: A random username string.
        """
        username_length = 8
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=username_length))
        return username

    def register_user(self, username: str) -> bool:
        """
        Simulate user registration process.

        :param username: The username to register.
        :return: True if registration was successful, False otherwise.
        """
        # Simulate registration delay
        time.sleep(random.uniform(0.5, 2.0))  # simulate network delay
        # Simulate a success or failure in the registration process
        if random.random() < 0.9:  # 90% chance of success
            return True
        return False

    def run_registration(self) -> Tuple[str, bool]:
        """
        Run the user registration process within the specified timeout.

        :return: A tuple containing the username and the registration result (True/False).
        """
        start_time = time.time()
        username = self.generate_username()
        success = False

        while time.time() - start_time < self.registration_timeout:
            try:
                success = self.register_user(username)
                if success:
                    print(f"User '{username}' was registered successfully.")
                    return username, success
                else:
                    print(f"Registration failed for user '{username}'. Retrying...")
            except Exception as e:
                raise UserRegistrationError(f"An error occurred during registration: {str(e)}")

        raise UserRegistrationError(f"Registration for user '{username}' timed out after {self.registration_timeout} seconds.")

if __name__ == "__main__":
    registration = UserRegistration()
    try:
        username, success = registration.run_registration()
    except UserRegistrationError as e:
        print(e)
```
