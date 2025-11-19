"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-re.was-systems.com
Prompt: Generate a code snippet that validates user input for a recommendation system, ensuring that all fields are filled out correctly before submission.
Generated: DETERMINISTIC_0bf9b748e34c5491
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import re

def validate_user_input(data):
    """
    Validates user input for a recommendation system.

    Parameters:
    data (dict): Dictionary containing user input fields and their values.

    Returns:
    bool: True if validation passes, False otherwise.
    str: Error message if validation fails, empty string if validation passes.
    """
    # Ensure all required fields are present
    required_fields = ['name', 'email', 'recommendation']
    for field in required_fields:
        if field not in data or not data[field].strip():
            return False, f"Error: The field '{field}' is required and cannot be empty."

    # Validate email format
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, data['email']):
        return False, "Error: Invalid email format."

    # Validate name (only alphabets and spaces, between 1 and 50 characters)
    name_pattern = r'^[A-Za-z\s]{1,50}$'
    if not re.match(name_pattern, data['name']):
        return False, "Error: Name must contain only letters and spaces, and must be between 1 and 50 characters."

    # Validate recommendation (max length 500 characters)
    if len(data['recommendation']) > 500:
        return False, "Error: Recommendation must not exceed 500 characters."

    # If all validations pass
    return True, ""

# Example usage
if __name__ == "__main__":
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "recommendation": "I recommend this product because it is excellent."
    }

    is_valid, message = validate_user_input(user_data)
    if is_valid:
        print("Validation successful. Form can be submitted.")
    else:
        print(message)
```
