"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prcboards.blogspot.com
Prompt: Write a script to parse the DEPED Cash Assistance application form from the PRC Board website and validate the required fields, such as "Mobile Phone Number" and "Email."
Generated: DETERMINISTIC_db2b161621d41a6b
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json

class CashAssistanceApplication:
    def __init__(self, mobile_phone, email):
        self.mobile_phone = mobile_phone
        self.email = email

    def validate_mobile_phone(self):
        """Validate the mobile phone number format."""
        pattern = r'^\+?[0-9]{10,15}$'  # Basic pattern for international phone numbers
        if not re.match(pattern, self.mobile_phone):
            raise ValueError("Invalid mobile phone number format.")

    def validate_email(self):
        """Validate the email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, self.email):
            raise ValueError("Invalid email format.")

    def validate(self):
        """Validate all fields in the application."""
        self.validate_mobile_phone()
        self.validate_email()

def parse_application_form(form_data):
    """Parse the application form data and create a CashAssistanceApplication object."""
    try:
        # Load form data (assuming it's a JSON string)
        data = json.loads(form_data)

        # Extract required fields
        mobile_phone = data.get("Mobile Phone Number")
        email = data.get("Email")

        # Validate fields
        application = CashAssistanceApplication(mobile_phone, email)
        application.validate()

        return application
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format.")
    except KeyError as e:
        raise ValueError(f"Missing required field: {e}")
    except ValueError as e:
        raise ValueError(f"Validation error: {e}")

# Example usage
if __name__ == "__main__":
    form_data = '{"Mobile Phone Number": "+639123456789", "Email": "test@example.com"}'
    try:
        application = parse_application_form(form_data)
        print("Application parsed and validated successfully.")
    except ValueError as e:
        print(f"Error: {e}")
```
