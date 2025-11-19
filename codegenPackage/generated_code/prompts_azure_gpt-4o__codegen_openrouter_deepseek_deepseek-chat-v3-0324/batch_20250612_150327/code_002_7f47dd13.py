"""
Generated Code Metadata:
========================
Original URL: https://linearlive.co.uk
Prompt: Generate code to validate and format user input for a contact form, ensuring proper handling of fields like name, email, subject, and message.
Generated: DETERMINISTIC_7f47dd136a33eb57
Batch ID: 20250612_150327
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

class ContactFormValidator:
    """
    Validates and formats user input for a contact form.
    Handles fields: name, email, subject, and message.
    """
    
    def __init__(self):
        # Regular expression for email validation
        self.email_regex = re.compile(
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        )
        
        # Minimum and maximum lengths for fields
        self.field_constraints = {
            'name': {'min': 2, 'max': 100},
            'email': {'min': 5, 'max': 254},
            'subject': {'min': 3, 'max': 200},
            'message': {'min': 10, 'max': 2000}
        }
    
    def validate_name(self, name: str) -> Tuple[bool, Optional[str]]:
        """
        Validates the name field.
        Returns (is_valid, error_message)
        """
        name = name.strip()
        if not name:
            return False, "Name is required"
        
        if len(name) < self.field_constraints['name']['min']:
            return False, f"Name must be at least {self.field_constraints['name']['min']} characters"
        
        if len(name) > self.field_constraints['name']['max']:
            return False, f"Name must be at most {self.field_constraints['name']['max']} characters"
        
        if not re.match(r'^[a-zA-Z\s\-\.\']+$', name):
            return False, "Name contains invalid characters"
        
        return True, None
    
    def validate_email(self, email: str) -> Tuple[bool, Optional[str]]:
        """
        Validates the email field.
        Returns (is_valid, error_message)
        """
        email = email.strip()
        if not email:
            return False, "Email is required"
        
        if len(email) < self.field_constraints['email']['min']:
            return False, f"Email must be at least {self.field_constraints['email']['min']} characters"
        
        if len(email) > self.field_constraints['email']['max']:
            return False, f"Email must be at most {self.field_constraints['email']['max']} characters"
        
        if not self.email_regex.match(email):
            return False, "Invalid email format"
        
        return True, None
    
    def validate_subject(self, subject: str) -> Tuple[bool, Optional[str]]:
        """
        Validates the subject field.
        Returns (is_valid, error_message)
        """
        subject = subject.strip()
        if not subject:
            return False, "Subject is required"
        
        if len(subject) < self.field_constraints['subject']['min']:
            return False, f"Subject must be at least {self.field_constraints['subject']['min']} characters"
        
        if len(subject) > self.field_constraints['subject']['max']:
            return False, f"Subject must be at most {self.field_constraints['subject']['max']} characters"
        
        return True, None
    
    def validate_message(self, message: str) -> Tuple[bool, Optional[str]]:
        """
        Validates the message field.
        Returns (is_valid, error_message)
        """
        message = message.strip()
        if not message:
            return False, "Message is required"
        
        if len(message) < self.field_constraints['message']['min']:
            return False, f"Message must be at least {self.field_constraints['message']['min']} characters"
        
        if len(message) > self.field_constraints['message']['max']:
            return False, f"Message must be at most {self.field_constraints['message']['max']} characters"
        
        return True, None
    
    def sanitize_input(self, input_str: str) -> str:
        """
        Basic sanitization to prevent XSS attacks.
        """
        return input_str.replace('<', '&lt;').replace('>', '&gt;')
    
    def validate_form(self, form_data: Dict[str, str]) -> Tuple[bool, Dict[str, str], Dict[str, str]]:
        """
        Validates all form fields.
        Returns (is_valid, sanitized_data, error_messages)
        """
        errors = {}
        sanitized_data = {}
        is_valid = True
        
        # Validate and sanitize each field
        for field in ['name', 'email', 'subject', 'message']:
            value = form_data.get(field, '').strip()
            sanitized_value = self.sanitize_input(value)
            sanitized_data[field] = sanitized_value
            
            validation_method = getattr(self, f'validate_{field}')
            valid, error = validation_method(value)
            
            if not valid:
                is_valid = False
                errors[field] = error
        
        return is_valid, sanitized_data, errors


# Example usage
if __name__ == "__main__":
    validator = ContactFormValidator()
    
    # Test data
    test_data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'subject': 'Hello',
        'message': 'This is a test message for the contact form.'
    }
    
    is_valid, sanitized_data, errors = validator.validate_form(test_data)
    
    print(f"Is valid: {is_valid}")
    print(f"Sanitized data: {sanitized_data}")
    if errors:
        print(f"Errors: {errors}")
```
