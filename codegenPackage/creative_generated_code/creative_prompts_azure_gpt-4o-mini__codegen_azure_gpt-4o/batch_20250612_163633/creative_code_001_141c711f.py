"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walmartgift.io
Prompt: Write a Python function to automate the registration process on Hello88, including input validation for user information.
Generated: DETERMINISTIC_141c711f9d5c5f18
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def register_user_on_hello88(user_info):
    """
    Automates the registration process on Hello88.
    
    Args:
        user_info (dict): A dictionary containing user information with keys:
                          'username', 'email', 'password', 'confirm_password'.
    
    Returns:
        str: Success message if registration is successful, or an error message.
    """
    # Validate user input
    try:
        # Check if all required fields are present
        required_fields = ['username', 'email', 'password', 'confirm_password']
        for field in required_fields:
            if field not in user_info:
                raise ValueError(f"Missing required field: {field}")
        
        # Validate username: must be between 3 and 20 characters long
        username = user_info['username']
        if not (3 <= len(username) <= 20):
            raise ValueError("Username must be between 3 and 20 characters long.")
        
        # Validate email: must follow proper email pattern
        email = user_info['email']
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email address.")
        
        # Validate password: must be at least 8 characters long and match confirm_password
        password = user_info['password']
        confirm_password = user_info['confirm_password']
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if password != confirm_password:
            raise ValueError("Passwords do not match.")
        
        # If all validations pass, simulate registration
        # (In a real-world scenario, this could involve making an API call to Hello88's backend)
        # Simulated registration logic
        # For the purpose of this example, assume registration is always successful after validation.
        return "Registration successful! Welcome to Hello88."
    
    except ValueError as ve:
        return f"Registration failed: {ve}"

# Example usage:
user_info_example = {
    'username': 'JohnDoe',
    'email': 'john.doe@example.com',
    'password': 'securepassword123',
    'confirm_password': 'securepassword123'
}

result = register_user_on_hello88(user_info_example)
print(result)
```
