"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amandiorodrigues.com
Prompt: How can I implement a phone number validation feature in a contact form for a tech support website?
Generated: DETERMINISTIC_a42a9df4ba7dc3ea
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class PhoneNumberValidator:
    """
    A class to validate phone numbers based on specific formats.
    """

    def __init__(self):
        # Define a regex pattern for valid phone numbers
        # This pattern covers various formats including:
        # (123) 456-7890, 123-456-7890, 1234567890, +31636363634, 075-63546725
        self.phone_pattern = re.compile(r'^(?:\+?\d{1,3})?[-. ]?\(?\d{1,4}?[)]?[-. ]?\d{1,4}[-. ]?\d{1,9}$')

    def validate(self, phone_number):
        """
        Validate a phone number against the defined pattern.

        Parameters:
        phone_number (str): The phone number to validate.

        Returns:
        bool: True if valid, False otherwise.
        """
        if not isinstance(phone_number, str):
            raise ValueError("Phone number must be a string.")

        # Check if the phone number matches the regex pattern
        is_valid = bool(self.phone_pattern.match(phone_number))
        
        if not is_valid:
            print(f"Invalid phone number format: {phone_number}")
        
        return is_valid

def main():
    """Main function to demonstrate phone number validation."""
    validator = PhoneNumberValidator()
    
    # Sample phone numbers for testing
    phone_numbers = [
        "(123) 456-7890",
        "123-456-7890",
        "1234567890",
        "+31636363634",
        "075-63546725",
        "invalid-phone-number"
    ]
    
    # Validate each phone number
    for number in phone_numbers:
        try:
            is_valid = validator.validate(number)
            print(f"Phone number '{number}' is valid: {is_valid}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```
