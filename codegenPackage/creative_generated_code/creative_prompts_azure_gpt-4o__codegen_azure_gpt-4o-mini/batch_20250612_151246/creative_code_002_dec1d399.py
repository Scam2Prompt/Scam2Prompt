"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olliivveemmaaiinn12893891bndjdbiqw.pages.dev
Prompt: Generate code to validate an invite code entered by a user, ensuring it matches the format and requirements of the "Early Access Airdrop" system.
Generated: DETERMINISTIC_dec1d39981dbf925
Batch ID: 20250612_151246
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
    A class to validate invite codes for the 'Early Access Airdrop' system.
    """

    def __init__(self, code_pattern: str):
        """
        Initializes the InviteCodeValidator with a specific regex pattern.

        :param code_pattern: A regex pattern that defines the valid format for the invite code.
        """
        self.code_pattern = code_pattern

    def validate_code(self, invite_code: str) -> bool:
        """
        Validates the provided invite code against the predefined pattern.

        :param invite_code: The invite code to validate.
        :return: True if the invite code is valid, False otherwise.
        """
        if not invite_code:
            raise ValueError("Invite code cannot be empty.")

        # Check if the invite code matches the defined pattern
        is_valid = re.match(self.code_pattern, invite_code) is not None

        return is_valid


def main():
    """
    Main function to demonstrate the use of InviteCodeValidator.
    """
    # Define the regex pattern for a valid invite code
    # Example pattern: starts with 'EAA-' followed by 4 alphanumeric characters
    invite_code_pattern = r'^EAA-[A-Za-z0-9]{4}$'

    # Create an instance of the InviteCodeValidator
    validator = InviteCodeValidator(invite_code_pattern)

    # Sample invite code to validate
    sample_code = input("Enter your invite code: ")

    try:
        # Validate the invite code
        if validator.validate_code(sample_code):
            print("The invite code is valid.")
        else:
            print("The invite code is invalid.")
    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()
```
