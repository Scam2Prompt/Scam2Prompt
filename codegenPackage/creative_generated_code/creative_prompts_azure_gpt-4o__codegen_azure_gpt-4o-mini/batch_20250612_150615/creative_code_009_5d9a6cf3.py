"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://currency-connect.com
Prompt: Create a script to automate the process of registering a law firm for a currency exchange service like Currency Connect, including input validation for firm details.
Generated: DETERMINISTIC_5d9a6cf3b35e8679
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class LawFirmRegistrationError(Exception):
    """Custom exception for law firm registration errors."""
    pass

class LawFirm:
    """A class to represent a law firm."""
    
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone

    def validate(self):
        """Validates the law firm's details."""
        self.validate_name()
        self.validate_email()
        self.validate_phone()

    def validate_name(self):
        """Validates the law firm's name."""
        if not self.name or len(self.name) < 3:
            raise LawFirmRegistrationError("Firm name must be at least 3 characters long.")

    def validate_email(self):
        """Validates the law firm's email address."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, self.email):
            raise LawFirmRegistrationError("Invalid email address format.")

    def validate_phone(self):
        """Validates the law firm's phone number."""
        phone_regex = r'^\+?[1-9]\d{1,14}$'
        if not re.match(phone_regex, self.phone):
            raise LawFirmRegistrationError("Invalid phone number format.")

def register_firm(name: str, email: str, phone: str):
    """
    Registers a law firm for a currency exchange service.
    
    Parameters:
    - name (str): The name of the law firm.
    - email (str): The email address of the law firm.
    - phone (str): The phone number of the law firm.
    
    Raises:
    - LawFirmRegistrationError: If any firm details are invalid.
    """
    try:
        firm = LawFirm(name, email, phone)
        firm.validate()
        # Here would be the logic to register the firm with the currency exchange service
        print(f"Law firm '{name}' registered successfully!")
    except LawFirmRegistrationError as e:
        print(f"Registration failed: {e}")

if __name__ == "__main__":
    # Example usage
    firm_name = input("Enter law firm name: ")
    firm_email = input("Enter law firm email: ")
    firm_phone = input("Enter law firm phone: ")

    register_firm(firm_name, firm_email, firm_phone)
```
