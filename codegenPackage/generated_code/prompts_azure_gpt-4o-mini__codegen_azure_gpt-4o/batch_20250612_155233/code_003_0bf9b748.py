"""
Generated Code Metadata:
========================
Original URL: https://proximus-re.was-systems.com
Prompt: Generate a code snippet that validates user input for a recommendation system, ensuring that all fields are filled out correctly before submission.
Generated: DETERMINISTIC_0bf9b748e34c5491
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import re

def validate_user_input(user_input):
    """
    Validates user input for a recommendation system.
    
    Parameters:
        user_input (dict): A dictionary containing user input fields and their values.
        
    Returns:
        bool: True if all fields are valid, False otherwise.
        str: Error message if validation fails, empty string if validation passes.
    """
    # Define required fields and their validation rules
    required_fields = {
        "name": {
            "type": str,
            "required": True,
            "min_length": 1,
            "error_message": "Name is required and must be a non-empty string."
        },
        "email": {
            "type": str,
            "required": True,
            "pattern": r"^[\w\.-]+@[\w\.-]+\.\w+$",
            "error_message": "Email is required and must be a valid email address."
        },
        "age": {
            "type": int,
            "required": True,
            "min_value": 18,
            "max_value": 120,
            "error_message": "Age is required and must be between 18 and 120."
        },
        "recommendation": {
            "type": str,
            "required": True,
            "min_length": 10,
            "error_message": "Recommendation is required and must be at least 10 characters long."
        }
    }
    
    # Validate each field
    for field, rules in required_fields.items():
        value = user_input.get(field)
        
        # Check if the field is required and missing
        if rules["required"] and value is None:
            return False, rules["error_message"]
        
        # Check type
        if not isinstance(value, rules["type"]):
            return False, f"{field.capitalize()} must be of type {rules['type'].__name__}."
        
        # Check minimum length for strings
        if rules["type"] == str and "min_length" in rules and len(value) < rules["min_length"]:
            return False, rules["error_message"]
        
        # Check pattern for strings
        if rules["type"] == str and "pattern" in rules:
            if not re.match(rules["pattern"], value):
                return False, rules["error_message"]
        
        # Check range for integers
        if rules["type"] == int:
            if "min_value" in rules and value < rules["min_value"]:
                return False, rules["error_message"]
            if "max_value" in rules and value > rules["max_value"]:
                return False, rules["error_message"]
    
    # If all validations pass
    return True, ""

# Example usage
if __name__ == "__main__":
    user_input = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 25,
        "recommendation": "I recommend this product because it is amazing!"
    }
    
    is_valid, error_message = validate_user_input(user_input)
    if is_valid:
        print("User input is valid.")
    else:
        print(f"Validation failed: {error_message}")
```
