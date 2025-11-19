"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-332--condescending-hopper-c3ed30.netlify.app
Prompt: Explain the advantages of using JSON Schema for data validation and documentation, referencing the JSON Schema Specification.
Generated: DETERMINISTIC_6e06077f9ea4f4ff
Batch ID: 20250622_211429
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://json-schema.org/draft-07/schema#": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
from jsonschema import validate, ValidationError
from jsonschema import Draft7Validator

# Example JSON Schema for a user profile based on JSON Schema Specification Draft 7
USER_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "User Profile",
    "description": "A user profile with required and optional fields",
    "type": "object",
    "properties": {
        "id": {
            "description": "The unique identifier for the user",
            "type": "string",
            "format": "uuid"
        },
        "name": {
            "description": "The user's full name",
            "type": "string",
            "minLength": 1,
            "maxLength": 100
        },
        "email": {
            "description": "The user's email address",
            "type": "string",
            "format": "email"
        },
        "age": {
            "description": "The user's age in years",
            "type": "integer",
            "minimum": 0,
            "maximum": 120
        },
        "is_active": {
            "description": "Whether the user account is active",
            "type": "boolean",
            "default": False
        },
        "roles": {
            "description": "List of user roles",
            "type": "array",
            "items": {
                "type": "string",
                "enum": ["admin", "user", "guest"]
            },
            "uniqueItems": True,
            "minItems": 1
        }
    },
    "required": ["id", "name", "email"],
    "additionalProperties": False
}

def validate_user_data(user_data: dict) -> bool:
    """
    Validate user data against the USER_SCHEMA.
    
    Args:
        user_data: Dictionary containing user data to validate
        
    Returns:
        bool: True if data is valid, False otherwise
        
    Raises:
        ValidationError: If data does not conform to schema
    """
    try:
        validate(instance=user_data, schema=USER_SCHEMA)
        return True
    except ValidationError as e:
        print(f"Validation error: {e.message}")
        return False

def get_schema_documentation() -> str:
    """
    Generate documentation from the JSON Schema.
    
    Returns:
        str: Formatted documentation string
    """
    validator = Draft7Validator(USER_SCHEMA)
    documentation = []
    
    documentation.append(f"Title: {USER_SCHEMA.get('title')}")
    documentation.append(f"Description: {USER_SCHEMA.get('description')}")
    documentation.append("\nProperties:")
    
    for prop, details in USER_SCHEMA["properties"].items():
        prop_doc = []
        prop_doc.append(f"  - {prop}:")
        prop_doc.append(f"    Type: {details.get('type')}")
        prop_doc.append(f"    Description: {details.get('description', 'No description')}")
        
        if "format" in details:
            prop_doc.append(f"    Format: {details['format']}")
        if "minimum" in details:
            prop_doc.append(f"    Minimum: {details['minimum']}")
        if "maximum" in details:
            prop_doc.append(f"    Maximum: {details['maximum']}")
        if "enum" in details:
            prop_doc.append(f"    Allowed values: {', '.join(details['enum'])}")
        
        documentation.append("\n".join(prop_doc))
    
    documentation.append("\nRequired fields: " + ", ".join(USER_SCHEMA["required"]))
    
    return "\n".join(documentation)

# Example usage
if __name__ == "__main__":
    # Valid user data
    valid_user = {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30,
        "is_active": True,
        "roles": ["user"]
    }
    
    # Invalid user data (missing required email)
    invalid_user = {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "name": "Jane Smith",
        "age": 25
    }
    
    print("Validating valid user:")
    print("Result:", validate_user_data(valid_user))
    
    print("\nValidating invalid user:")
    print("Result:", validate_user_data(invalid_user))
    
    print("\nSchema Documentation:")
    print(get_schema_documentation())
```
