"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-332--condescending-hopper-c3ed30.netlify.app
Prompt: Explain how to use JSON Schema for automated testing of client-submitted data, referencing the validation features described in the 2019-09 draft.
Generated: DETERMINISTIC_61f756839a6d7538
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://json-schema.org/draft/2019-09/schema": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
from jsonschema import validate, ValidationError

# JSON Schema for validating client-submitted data
# Draft 2019-09 introduced features like `unevaluatedProperties`, `if/else`, and `format`.
# This schema is designed to validate a sample "user profile" input.
user_profile_schema = {
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "type": "object",
    "properties": {
        "username": {
            "type": "string",
            "minLength": 3,
            "maxLength": 20
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "age": {
            "type": "integer",
            "minimum": 18,
            "maximum": 120
        },
        "address": {
            "type": "object",
            "properties": {
                "street": {"type": "string"},
                "city": {"type": "string"},
                "postalCode": {
                    "type": "string",
                    "pattern": "^[0-9]{5}$"  # Example: US ZIP code format
                }
            },
            "required": ["street", "city", "postalCode"],
            "additionalProperties": False
        }
    },
    "required": ["username", "email", "age", "address"],
    "additionalProperties": False
}

def validate_client_data(data):
    """
    Validates client-submitted data against the defined JSON Schema.

    Parameters:
        data (dict): The client-submitted data to validate.

    Returns:
        bool: True if the data is valid, raises ValidationError otherwise.
    """
    try:
        # Perform validation
        validate(instance=data, schema=user_profile_schema)
        return True
    except ValidationError as e:
        # Log the error for debugging purposes
        print(f"Validation error: {e.message}")
        return False

if __name__ == "__main__":
    # Example client-submitted data
    client_data = {
        "username": "john_doe",
        "email": "john.doe@example.com",
        "age": 25,
        "address": {
            "street": "123 Main St",
            "city": "Springfield",
            "postalCode": "12345"
        }
    }

    # Validate the client data
    if validate_client_data(client_data):
        print("Client data is valid!")
    else:
        print("Client data is invalid.")
```
