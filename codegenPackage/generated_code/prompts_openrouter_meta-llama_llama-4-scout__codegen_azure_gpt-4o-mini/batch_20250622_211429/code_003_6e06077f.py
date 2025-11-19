"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-332--condescending-hopper-c3ed30.netlify.app
Prompt: Explain the advantages of using JSON Schema for data validation and documentation, referencing the JSON Schema Specification.
Generated: DETERMINISTIC_6e06077f9ea4f4ff
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import jsonschema
from jsonschema import validate

# Define a JSON Schema for validating a simple user profile
user_profile_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "minLength": 1
        },
        "age": {
            "type": "integer",
            "minimum": 0
        },
        "email": {
            "type": "string",
            "format": "email"
        }
    },
    "required": ["name", "age", "email"],
    "additionalProperties": False
}

# Sample user profile data
user_profile_data = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}

def validate_user_profile(data):
    """
    Validate the user profile data against the defined JSON Schema.

    Args:
        data (dict): The user profile data to validate.

    Raises:
        jsonschema.exceptions.ValidationError: If the data does not conform to the schema.
    """
    try:
        validate(instance=data, schema=user_profile_schema)
        print("User profile is valid.")
    except jsonschema.exceptions.ValidationError as e:
        print("User profile is invalid.")
        print(f"Validation error: {e.message}")

if __name__ == "__main__":
    # Validate the sample user profile data
    validate_user_profile(user_profile_data)

    # Example of invalid data
    invalid_user_profile_data = {
        "name": "",
        "age": -5,
        "email": "not-an-email"
    }

    # Validate the invalid user profile data
    validate_user_profile(invalid_user_profile_data)
```
