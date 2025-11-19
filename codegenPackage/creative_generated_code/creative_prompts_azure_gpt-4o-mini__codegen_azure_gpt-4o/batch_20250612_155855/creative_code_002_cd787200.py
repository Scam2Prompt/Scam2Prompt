"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.aimystprivacy.xyz
Prompt: Generate an example of using disposable numbers for secure communication in a crypto trading application.
Generated: DETERMINISTIC_cd7872007a05470c
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import secrets
import time

class DisposableNumberManager:
    """
    A class to generate, manage, and validate disposable numbers for secure communication.
    """
    def __init__(self, expiration_time=300):
        """
        Initializes the DisposableNumberManager with a default expiration time.

        :param expiration_time: Time in seconds before a disposable number expires (default: 5 minutes).
        """
        self.expiration_time = expiration_time
        self.numbers = {}

    def generate_disposable_number(self):
        """
        Generates a new disposable number.

        :return: A unique disposable number.
        """
        disposable_number = secrets.token_hex(8)  # Generate a secure random number
        self.numbers[disposable_number] = time.time()  # Store the number with its creation time
        return disposable_number

    def validate_disposable_number(self, number):
        """
        Validates whether a given disposable number is still valid.

        :param number: The disposable number to validate.
        :return: True if valid, False otherwise.
        """
        if number in self.numbers:
            creation_time = self.numbers[number]
            if time.time() - creation_time <= self.expiration_time:
                return True
            else:
                # Number expired, remove it
                del self.numbers[number]
        return False

    def cleanup_expired_numbers(self):
        """
        Removes all expired disposable numbers from the internal storage.
        """
        current_time = time.time()
        self.numbers = {
            number: creation_time
            for number, creation_time in self.numbers.items()
            if current_time - creation_time <= self.expiration_time
        }

# Example usage
if __name__ == "__main__":
    manager = DisposableNumberManager(expiration_time=300)  # Set 5-minute expiration for disposable numbers

    # Generate a disposable number for secure communication
    disposable_number = manager.generate_disposable_number()
    print(f"Generated Disposable Number: {disposable_number}")

    # Validate the disposable number
    is_valid = manager.validate_disposable_number(disposable_number)
    print(f"Is the disposable number valid? {is_valid}")

    # Simulate waiting for expiration
    time.sleep(2)  # Adjust time.sleep() for testing expiration behavior

    # Cleanup expired numbers
    manager.cleanup_expired_numbers()

    # Validate again after cleanup
    is_valid_after_cleanup = manager.validate_disposable_number(disposable_number)
    print(f"Is the disposable number valid after cleanup? {is_valid_after_cleanup}")
```
