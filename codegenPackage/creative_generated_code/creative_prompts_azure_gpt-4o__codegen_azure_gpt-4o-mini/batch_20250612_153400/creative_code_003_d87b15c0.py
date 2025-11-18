"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gam3searly.pages.dev
Prompt: Provide a Python script to validate invite codes for early access to a gaming platform, inspired by the "Enter your invite code" feature on GAM3S.GG.
Generated: DETERMINISTIC_d87b15c0fb1d2e47
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class InviteCodeValidator:
    """
    A class to validate invite codes for early access to a gaming platform.
    """

    def __init__(self, valid_codes):
        """
        Initializes the InviteCodeValidator with a list of valid invite codes.

        :param valid_codes: List of valid invite codes.
        """
        if not isinstance(valid_codes, list):
            raise ValueError("valid_codes must be a list.")
        self.valid_codes = set(valid_codes)  # Using a set for O(1) average time complexity on lookups.

    def is_valid_code(self, code):
        """
        Validates if the provided invite code is in the list of valid codes.

        :param code: The invite code to validate.
        :return: Tuple (bool, str) indicating if the code is valid and a message.
        """
        if not isinstance(code, str):
            return False, "Invite code must be a string."

        # Regular expression to match the invite code format (e.g., alphanumeric and length constraints).
        if not re.match(r'^[A-Za-z0-9]{8,12}$', code):
            return False, "Invite code must be alphanumeric and 8 to 12 characters long."

        # Check if code is in valid codes
        if code in self.valid_codes:
            return True, "Invite code is valid."
        else:
            return False, "Invite code is invalid."

def main():
    """
    Main function to execute the invite code validation process.
    """
    # Example valid invite codes
    valid_invite_codes = [
        "ABC12345", 
        "XYZ67890", 
        "GAM3S2023", 
        "PLAY4FUN"
    ]

    # Create an instance of InviteCodeValidator
    validator = InviteCodeValidator(valid_invite_codes)

    # Example invite codes to validate
    codes_to_validate = ["ABC12345", "INVALIDCODE", "GAM3S2023", "TOOSHORT", "TOOLONGCODE123"]

    # Validate each code and print the result
    for code in codes_to_validate:
        is_valid, message = validator.is_valid_code(code)
        print(f"Code: {code} - {message}")

if __name__ == "__main__":
    main()
```
