"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hypr.pages.dev
Prompt: Write code to automate the process of generating and validating referral codes for a platform like Hyperliquid.
Generated: DETERMINISTIC_e794388d382c2c5d
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string

class ReferralCodeManager:
    def __init__(self, code_length=8, code_prefix='REF'):
        """
        Initializes the ReferralCodeManager with a specific code length and prefix.

        :param code_length: Length of the referral code (excluding prefix).
        :param code_prefix: Prefix for the referral code.
        """
        self.code_length = code_length
        self.code_prefix = code_prefix
        self.generated_codes = set()

    def generate_referral_code(self):
        """
        Generates a unique referral code.

        :return: A unique referral code string.
        :raises Exception: If it fails to generate a unique code after multiple attempts.
        """
        attempts = 0
        max_attempts = 100  # Limit the number of attempts to avoid infinite loops
        
        while attempts < max_attempts:
            # Generate a random code consisting of uppercase letters and digits
            random_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=self.code_length))
            referral_code = f"{self.code_prefix}-{random_code}"

            # Ensure the generated code is unique
            if referral_code not in self.generated_codes:
                self.generated_codes.add(referral_code)
                return referral_code
            
            attempts += 1
        
        raise Exception("Failed to generate a unique referral code after multiple attempts.")

    def validate_referral_code(self, code):
        """
        Validates if the provided referral code is in the set of generated codes.

        :param code: Referral code to validate.
        :return: True if valid, False otherwise.
        """
        return code in self.generated_codes

# Example of usage
if __name__ == "__main__":
    try:
        manager = ReferralCodeManager()
        
        # Generate a referral code
        new_code = manager.generate_referral_code()
        print(f"Generated Referral Code: {new_code}")
        
        # Validate the generated code
        is_valid = manager.validate_referral_code(new_code)
        print(f"Is the code '{new_code}' valid? {is_valid}")

        # Validate a non-existent code
        non_existent_code = "REF-INVALID"
        is_valid_non_existent = manager.validate_referral_code(non_existent_code)
        print(f"Is the code '{non_existent_code}' valid? {is_valid_non_existent}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
