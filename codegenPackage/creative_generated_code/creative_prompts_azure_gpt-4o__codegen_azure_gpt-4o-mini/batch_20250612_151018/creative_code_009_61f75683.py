"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-332--condescending-hopper-c3ed30.netlify.app
Prompt: Explain how to use JSON Schema for automated testing of client-submitted data, referencing the validation features described in the 2019-09 draft.
Generated: DETERMINISTIC_61f756839a6d7538
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import jsonschema
from jsonschema import validate, ValidationError

# Define the JSON Schema as per the 2019-09 draft specification.
# This schema expects a JSON object with specific properties and data types.
json_schema = {
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
        },
        "address": {
            "type": "object",
            "properties": {
                "street": {
                    "type": "string"
                },
                "city": {
                    "type": "string"
                },
                "postalCode": {
                    "type": "string",
                    "pattern": "^[0-9]{5}(?:-[0-9]{4})?$"  # US ZIP code validation
                }
            },
            "required": ["street", "city", "postalCode"]
        }
    },
    "required": ["name", "age", "email", "address"],
    "additionalProperties": False  # No additional properties are allowed
}

def validate_json(data):
    """
    Validate the provided data against the defined JSON schema.

    Args:
        data (dict): The data to validate.

    Raises:
        ValidationError: If the data does not conform to the schema.
    """
    try:
        validate(instance=data, schema=json_schema)
        print("Validation successful!")
    except ValidationError as e:
        print(f"Validation error: {e.message}")
        raise

def main():
    # Sample data for testing
    client_data = {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com",
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "postalCode": "12345"
        }
    }

    # Perform validation
    try:
        validate_json(client_data)
    except ValidationError:
        # Handle the validation error accordingly (logging, user feedback, etc.)
        print("Client data is invalid. Please correct the errors and try again.")

if __name__ == "__main__":
    main()
```
