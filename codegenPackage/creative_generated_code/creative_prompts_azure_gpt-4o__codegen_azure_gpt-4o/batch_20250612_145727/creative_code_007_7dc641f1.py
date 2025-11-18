"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://official-trumpcoin.web.app
Prompt: Write a function to validate user input for a subscription form on a collectible coin website, ensuring email addresses are properly formatted.
Generated: DETERMINISTIC_7dc641f1f9b61801
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_subscription_form(input_data):
    """
    Validates the user input for a subscription form.
    
    Args:
        input_data (dict): A dictionary containing form fields. 
                           Example: {'email': 'user@example.com'}
                           
    Returns:
        bool: True if validation passes, False otherwise.
        str: A message indicating success or the validation error.
    """
    
    # Email validation regex pattern
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    try:
        # Check if email field is present
        if 'email' not in input_data:
            return False, "Email is required."
        
        email = input_data['email']
        
        # Check if email is not empty
        if not email.strip():
            return False, "Email cannot be empty."
        
        # Validate email format
        if not re.match(email_regex, email):
            return False, "Invalid email format."
        
        # All validations passed
        return True, "Validation successful."
    
    except Exception as e:
        # Log the unexpected exception in real-world scenarios
        return False, f"An unexpected error occurred: {str(e)}"


# Example usage:
# result, message = validate_subscription_form({'email': 'test@example.com'})
# print(result, message)
```
