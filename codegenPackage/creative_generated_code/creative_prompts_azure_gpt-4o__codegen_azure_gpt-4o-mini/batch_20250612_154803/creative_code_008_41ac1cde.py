"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://public-bridge-cdn.gorgias.help
Prompt: Create a script to enable 2FA time lock functionality for transactions managed through Trezor Bridge.
Generated: DETERMINISTIC_41ac1cde572811e1
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json
import hmac
import hashlib
from typing import Optional, Dict
from datetime import datetime, timedelta

class TwoFALock:
    """
    A class to implement a Time-based One-Time Password (TOTP) for enabling 
    2FA time lock functionality on transactions.
    """

    def __init__(self, secret: str, time_step: int = 30):
        """
        Initializes the TwoFALock with a secret key and time step.

        Args:
            secret (str): The shared secret key for generating TOTP.
            time_step (int): The time step in seconds for TOTP generation.
        """
        self.secret = secret.encode('utf-8')
        self.time_step = time_step

    def _generate_totp(self, timestamp: Optional[int] = None) -> str:
        """
        Generates a TOTP based on the current time or a provided timestamp.

        Args:
            timestamp (Optional[int]): The timestamp to generate TOTP for. 
                                        If None, the current time is used.

        Returns:
            str: The generated TOTP.
        """
        if timestamp is None:
            timestamp = int(time.time())

        # Calculate the time counter
        counter = timestamp // self.time_step

        # Create a byte array from the counter
        counter_bytes = counter.to_bytes(8, byteorder='big')

        # Generate HMAC-SHA1 using the secret key and the counter
        hmac_hash = hmac.new(self.secret, counter_bytes, hashlib.sha1).digest()

        # Truncate to get the 6-digit OTP
        offset = hmac_hash[-1] & 0x0F
        truncated_hash = hmac_hash[offset:offset + 4]
        code = int.from_bytes(truncated_hash, 'big') & 0x7FFFFFFF
        otp = str(code % 1000000).zfill(6)

        return otp

    def is_locked(self, last_transaction_time: str, lock_duration: int) -> bool:
        """
        Checks if the 2FA lock is active based on the last transaction time.

        Args:
            last_transaction_time (str): The ISO format time string of the last transaction.
            lock_duration (int): Duration (in seconds) for which the lock is active.

        Returns:
            bool: True if the lock is active, False otherwise.
        """
        try:
            last_time = datetime.fromisoformat(last_transaction_time)
        except ValueError as e:
            raise ValueError("Invalid last_transaction_time format. Expected ISO format.") from e

        current_time = datetime.now()
        return (current_time - last_time).total_seconds() < lock_duration

    def generate_and_send_otp(self) -> str:
        """
        Generates an OTP and sends it to the user (simulated here).

        Returns:
            str: The generated OTP.
        """
        otp = self._generate_totp()
        # Simulate sending OTP (e.g., via email or SMS)
        print(f"Sending OTP: {otp}")  # Replace with actual sending logic
        return otp

# Example usage
if __name__ == "__main__":
    secret_key = "your_secret_key_here"  # Replace with your actual secret
    time_lock = TwoFALock(secret=secret_key)

    # Generate OTP and simulate sending it
    otp = time_lock.generate_and_send_otp()

    # Check if the time lock is active based on a last transaction time
    last_transaction_time = "2023-10-01T12:00:00"  # Example last transaction time in ISO format
    lock_duration = 300  # 5 minutes lock duration

    if time_lock.is_locked(last_transaction_time, lock_duration):
        print("Transactions are locked due to recent activity.")
    else:
        print("Transactions are unlocked.")
```
