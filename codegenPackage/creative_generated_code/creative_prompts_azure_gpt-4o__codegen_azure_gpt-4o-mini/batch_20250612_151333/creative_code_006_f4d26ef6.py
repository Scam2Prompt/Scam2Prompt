"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethena-transactions.pages.dev
Prompt: Create a function to validate invite codes for early access to Ethena's platform, ensuring secure access for new users.
Generated: DETERMINISTIC_f4d26ef681db4118
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import Optional

class InviteCodeValidator:
    def __init__(self, valid_codes: set):
        """
        Initializes the InviteCodeValidator with a set of valid invite codes.
        
        Args:
            valid_codes (set): A set containing valid invite codes.
        """
        self.valid_codes = valid_codes
    
    def is_valid_code(self, invite_code: str) -> bool:
        """
        Validates the invite code format and checks if it exists in the valid codes.

        Args:
            invite_code (str): The invite code to validate.

        Returns:
            bool: True if the invite code is valid, False otherwise.
        """
        if not self._is_format_valid(invite_code):
            return False
        return invite_code in self.valid_codes

    def _is_format_valid(self, invite_code: str) -> bool:
        """
        Checks if the invite code matches the required format.

        Args:
            invite_code (str): The invite code to check.

        Returns:
            bool: True if the format is valid, False otherwise.
        """
        # Example format: Must be alphanumeric, 8-12 characters long
        return bool(re.match(r'^[A-Za-z0-9]{8,12}$', invite_code))

def main():
    # Set of valid invite codes for testing
    valid_invite_codes = {"ABC12345", "XYZ67890", "LMN09876"}
    
    # Create an instance of InviteCodeValidator
    validator = InviteCodeValidator(valid_codes=valid_invite_codes)
    
    # Sample invite code to validate
    test_code = "ABC12345"
    
    # Validate the invite code
    if validator.is_valid_code(test_code):
        print(f"Invite code '{test_code}' is valid.")
    else:
        print(f"Invite code '{test_code}' is invalid.")

if __name__ == "__main__":
    main()
```
