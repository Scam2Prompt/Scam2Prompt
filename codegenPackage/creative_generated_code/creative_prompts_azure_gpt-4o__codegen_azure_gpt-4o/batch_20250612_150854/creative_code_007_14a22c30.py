"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.io
Prompt: Write code to validate and process user input for an investment education platform, ensuring compliance with Immediate Peak's data privacy notice.
Generated: DETERMINISTIC_14a22c3098c6f631
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_and_process_user_input(user_data):
    """
    Validates and processes user input for an investment education platform.
    Ensures compliance with Immediate Peak's data privacy notice.
    
    Parameters:
        user_data (dict): A dictionary containing user-provided data.
                          Expected keys: 'name', 'email', 'age', 'investment_interest'
    
    Returns:
        dict: Processed user data if validation succeeds.
              Contains 'name', 'email', 'age', and 'investment_interest'.
    Raises:
        ValueError: If any validation check fails.
    """

    # Helper function to validate email format
    def validate_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format.")

    # Helper function to validate age
    def validate_age(age):
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        if age < 18:
            raise ValueError("User must be at least 18 years old.")

    # Validate 'name'
    if not user_data.get('name') or not isinstance(user_data['name'], str):
        raise ValueError("Name is required and must be a string.")

    # Validate 'email'
    if not user_data.get('email') or not isinstance(user_data['email'], str):
        raise ValueError("Email is required and must be a string.")
    validate_email(user_data['email'])

    # Validate 'age'
    if 'age' not in user_data:
        raise ValueError("Age is required.")
    validate_age(user_data['age'])

    # Validate 'investment_interest'
    if not user_data.get('investment_interest') or not isinstance(user_data['investment_interest'], str):
        raise ValueError("Investment interest is required and must be a string.")

    # Process validated data
    processed_data = {
        "name": user_data['name'].strip(),
        "email": user_data['email'].strip().lower(),
        "age": user_data['age'],
        "investment_interest": user_data['investment_interest'].strip(),
    }

    return processed_data


# Example usage:
if __name__ == "__main__":
    try:
        user_input = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "age": 30,
            "investment_interest": "Stock Market",
        }
        processed_data = validate_and_process_user_input(user_input)
        print("Processed Data:", processed_data)
    except ValueError as e:
        print(f"Error: {e}")
```
