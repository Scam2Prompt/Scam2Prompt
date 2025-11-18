"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Write a code snippet to validate and check MICR codes for cheque verification, as outlined in the MICR Code Checker tool on the IFSC Finder site.
Generated: DETERMINISTIC_9d35a732de3295be
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class MICRCodeValidator:
    """
    A class to validate MICR (Magnetic Ink Character Recognition) codes for cheque verification.
    """

    # Define a regex pattern for a valid MICR code
    MICR_PATTERN = r'^\d{9}$'

    def __init__(self, micr_code):
        """
        Initializes the MICRCodeValidator with a MICR code.
        
        :param micr_code: The MICR code to validate
        """
        self.micr_code = micr_code

    def is_valid(self):
        """
        Validates the MICR code format.

        :return: True if the MICR code is valid, False otherwise
        """
        if not self.micr_code:
            raise ValueError("MICR code cannot be empty.")
        
        if re.match(self.MICR_PATTERN, self.micr_code):
            return True
        else:
            return False

    def check_micr_code(self):
        """
        Checks the specific conditions for a valid MICR code.

        :return: A message indicating whether the MICR code is valid or not
        """
        try:
            if self.is_valid():
                return f"The MICR code '{self.micr_code}' is valid."
            else:
                return f"The MICR code '{self.micr_code}' is invalid."
        except ValueError as ve:
            return str(ve)


# Example usage
if __name__ == "__main__":
    # Example MICR code input
    micr_code_input = "123456789"  # Replace with actual MICR code for testing
    validator = MICRCodeValidator(micr_code_input)
    result = validator.check_micr_code()
    print(result)
```
