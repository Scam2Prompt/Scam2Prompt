"""
Generated Code Metadata:
========================
Original URL: https://prcboards.blogspot.com
Prompt: Write a script to parse the DEPED Cash Assistance application form from the PRC Board website and validate the required fields, such as "Mobile Phone Number" and "Email."
Generated: DETERMINISTIC_db2b161621d41a6b
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, Optional, Tuple

class DEPEDFormValidator:
    """
    A class to validate the DEPED Cash Assistance application form fields.
    """

    def __init__(self):
        # Regular expressions for validation
        self.email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        self.phone_regex = re.compile(r'^\+?\d{10,15}$')  # Supports international numbers

    def validate_email(self, email: str) -> Tuple[bool, Optional[str]]:
        """
        Validates the email format.
        
        Args:
            email: The email address to validate.
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not email:
            return False, "Email is required."
        if not self.email_regex.match(email):
            return False, "Invalid email format."
        return True, None

    def validate_phone(self, phone: str) -> Tuple[bool, Optional[str]]:
        """
        Validates the phone number format.
        
        Args:
            phone: The phone number to validate.
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not phone:
            return False, "Phone number is required."
        if not self.phone_regex.match(phone):
            return False, "Invalid phone number format. Must be 10-15 digits, optionally starting with +."
        return True, None

    def validate_form(self, form_data: Dict[str, str]) -> Dict[str, str]:
        """
        Validates all required fields in the form data.
        
        Args:
            form_data: Dictionary containing form field values.
            
        Returns:
            Dictionary of field errors (empty if no errors).
        """
        errors = {}
        
        # Validate email
        email = form_data.get('email', '').strip()
        is_valid, error_msg = self.validate_email(email)
        if not is_valid:
            errors['email'] = error_msg
            
        # Validate phone
        phone = form_data.get('phone', '').strip()
        is_valid, error_msg = self.validate_phone(phone)
        if not is_valid:
            errors['phone'] = error_msg
            
        return errors


# Example usage
if __name__ == "__main__":
    validator = DEPEDFormValidator()
    
    # Test cases
    test_cases = [
        {"email": "test@example.com", "phone": "+639123456789"},
        {"email": "invalid-email", "phone": "123"},
        {"email": "", "phone": ""},
    ]
    
    for i, form_data in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print("Input:", form_data)
        errors = validator.validate_form(form_data)
        if errors:
            print("Errors found:")
            for field, error in errors.items():
                print(f"  {field}: {error}")
        else:
            print("All fields are valid.")
```
