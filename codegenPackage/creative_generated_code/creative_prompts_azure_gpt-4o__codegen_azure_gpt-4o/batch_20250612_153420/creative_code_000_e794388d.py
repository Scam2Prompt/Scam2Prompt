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

class ReferralCodeGenerator:
    """
    A class to generate and validate referral codes for a platform.
    """

    def __init__(self, code_length=8):
        """
        Initializes the ReferralCodeGenerator.

        :param code_length: Length of the referral codes to be generated.
        """
        self.code_length = code_length
        self.generated_codes = set()  # Stores generated codes to ensure uniqueness

    def generate_code(self):
        """
        Generates a unique referral code.

        :return: A unique referral code.
        """
        while True:
            # Generate a random alphanumeric code of specified length
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=self.code_length))
            if code not in self.generated_codes:
                self.generated_codes.add(code)
                return code

    def validate_code(self, code):
        """
        Validates whether a referral code exists in the system.

        :param code: The referral code to validate.
        :return: True if the code exists, False otherwise.
        """
        return code in self.generated_codes

    def get_all_codes(self):
        """
        Returns all generated referral codes.

        :return: A list of all generated referral codes.
        """
        return list(self.generated_codes)


# Example usage
if __name__ == "__main__":
    try:
        generator = ReferralCodeGenerator(code_length=8)

        # Generate and print 5 referral codes
        print("Generated Referral Codes:")
        for _ in range(5):
            print(generator.generate_code())

        # Validate a code
        test_code = "TEST1234"  # Example of a code to validate
        print(f"\nValidation of code '{test_code}': {generator.validate_code(test_code)}")

        # Retrieve all codes
        print("\nAll Generated Codes:")
        print(generator.get_all_codes())

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
