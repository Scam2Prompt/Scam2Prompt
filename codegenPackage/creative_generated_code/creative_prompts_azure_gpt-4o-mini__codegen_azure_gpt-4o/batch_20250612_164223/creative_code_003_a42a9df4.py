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

def validate_phone_number(phone_number):
    """
    Validates a phone number for the contact form.
    
    Phone numbers must:
    - Start with an optional '+' sign followed by country code
    - Contain digits (minimum 7 and maximum 15 digits)
    - Allow spaces, dashes, or parentheses as separators
    
    Args:
        phone_number (str): The phone number input
    
    Returns:
        tuple: (bool, str) Validation result and error message (if invalid)
    """
    # Define the regex pattern for phone number validation
    phone_number_pattern = re.compile(r"^\+?[0-9]{1,3}[-\s()]?[0-9]{3,15}$")
    
    # Check if the phone number matches the pattern
    if not phone_number:
        return False, "Phone number cannot be empty."
    if phone_number_pattern.match(phone_number):
        return True, "Phone number is valid."
    else:
        return False, (
            "Invalid phone number format. Please enter a valid phone number "
            "with optional country code, and ensure it contains 7 to 15 digits."
        )

def main():
    """
    Main function to demonstrate phone number validation.
    """
    print("Tech Support Contact Form - Phone Number Validation")
    phone_number = input("Enter your phone number: ")
    
    # Validate the phone number
    is_valid, message = validate_phone_number(phone_number)
    
    if is_valid:
        print("Success:", message)
    else:
        print("Error:", message)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Handle unexpected errors gracefully
        print("An unexpected error occurred:", str(e))
```
