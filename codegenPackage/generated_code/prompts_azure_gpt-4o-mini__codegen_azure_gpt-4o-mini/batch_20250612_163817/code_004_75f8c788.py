"""
Generated Code Metadata:
========================
Original URL: https://devoursol.com
Prompt: Create a Python script that simulates a security verification process similar to Cloudflare's.
Generated: DETERMINISTIC_75f8c7883fddb8a6
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class SecurityVerification:
    def __init__(self):
        self.verification_code = None

    def generate_verification_code(self):
        """Generates a random 6-digit verification code."""
        self.verification_code = str(random.randint(100000, 999999))
        return self.verification_code

    def send_verification_code(self, user_email):
        """Simulates sending a verification code to the user's email."""
        if not self.is_valid_email(user_email):
            raise ValueError("Invalid email address provided.")
        
        print(f"Sending verification code {self.verification_code} to {user_email}...")
        # Simulate email sending delay
        time.sleep(1)
        print("Verification code sent successfully.")

    def is_valid_email(self, email):
        """Validates the email format."""
        return "@" in email and "." in email.split("@")[-1]

    def verify_code(self, user_input_code):
        """Verifies the user's input against the generated verification code."""
        if self.verification_code is None:
            raise RuntimeError("Verification code has not been generated.")
        
        if user_input_code == self.verification_code:
            print("Verification successful!")
            return True
        else:
            print("Verification failed. Incorrect code.")
            return False

def main():
    """Main function to run the security verification process."""
    verifier = SecurityVerification()
    
    # Generate and send verification code
    code = verifier.generate_verification_code()
    user_email = input("Enter your email address: ")
    
    try:
        verifier.send_verification_code(user_email)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # User input for verification
    user_input_code = input("Enter the verification code sent to your email: ")
    
    # Verify the code
    verifier.verify_code(user_input_code)

if __name__ == "__main__":
    main()
```
