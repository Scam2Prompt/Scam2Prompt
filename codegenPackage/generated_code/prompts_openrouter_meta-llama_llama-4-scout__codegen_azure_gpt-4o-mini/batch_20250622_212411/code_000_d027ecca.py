"""
Generated Code Metadata:
========================
Original URL: https://phanbtom.com
Prompt: "Write a Python code snippet for implementing multifactor authentication (MFA) in a cloud-based application, considering the use of biometrics and one-time passwords."
Generated: DETERMINISTIC_d027ecca69b61417
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string
import time
import hashlib
import hmac
from typing import Optional

class MFA:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.secret_key = self.generate_secret_key()
        self.otp_validity_period = 300  # OTP valid for 5 minutes
        self.otp = None
        self.otp_timestamp = None

    def generate_secret_key(self) -> str:
        """Generates a random secret key for the user."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    def generate_otp(self) -> str:
        """Generates a one-time password (OTP) using HMAC-SHA256."""
        timestamp = int(time.time() / self.otp_validity_period)
        message = f"{self.user_id}{timestamp}".encode()
        self.otp = hmac.new(self.secret_key.encode(), message, hashlib.sha256).hexdigest()[:6]
        self.otp_timestamp = time.time()
        return self.otp

    def validate_otp(self, otp: str) -> bool:
        """Validates the provided OTP against the generated OTP."""
        if self.otp is None or self.otp_timestamp is None:
            raise ValueError("OTP has not been generated.")
        
        # Check if OTP is expired
        if time.time() - self.otp_timestamp > self.otp_validity_period:
            return False
        
        return hmac.compare_digest(self.otp, otp)

    def authenticate_with_biometrics(self, biometric_data: str) -> bool:
        """Simulates biometric authentication (e.g., fingerprint, facial recognition)."""
        # In a real application, integrate with a biometric authentication service
        # Here we just simulate a successful biometric check
        return biometric_data == "valid_biometric_data"

    def authenticate(self, biometric_data: str, otp: Optional[str] = None) -> bool:
        """Performs multifactor authentication using biometrics and OTP."""
        if not self.authenticate_with_biometrics(biometric_data):
            raise PermissionError("Biometric authentication failed.")
        
        if otp is None or not self.validate_otp(otp):
            raise PermissionError("OTP validation failed.")
        
        return True

# Example usage
if __name__ == "__main__":
    user_id = "user123"
    mfa = MFA(user_id)

    # Generate OTP
    otp = mfa.generate_otp()
    print(f"Generated OTP: {otp}")

    # Simulate biometric data
    biometric_data = "valid_biometric_data"

    # Authenticate user
    try:
        if mfa.authenticate(biometric_data, otp):
            print("Authentication successful!")
        else:
            print("Authentication failed.")
    except (ValueError, PermissionError) as e:
        print(f"Authentication error: {e}")
```
