"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-332--condescending-hopper-c3ed30.netlify.app
Prompt: Write a JSON Schema that uses relative JSON pointers to reference a field within the same schema. Provide an example where the schema validates a JSON object with a `parent` field and a `child` field, ensuring the `child` field matches the `parent` field.
Generated: DETERMINISTIC_d90f977aff32a317
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://json-schema.org/draft/2020-12/schema": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Parent Child Schema",
  "description": "A schema that validates a JSON object with a parent and child field",
  "type": "object",
  "properties": {
    "parent": {"type": "string"},
    "child": {"type": "string"}
  },
  "required": ["parent", "child"],
  "allOf": [
    {
      "properties": {
        "child": {
          "$ref": "#/properties/parent"
        }
      }
    }
  ]
}
```

```python
import json
import jsonschema

# Define the JSON schema
schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Parent Child Schema",
  "description": "A schema that validates a JSON object with a parent and child field",
  "type": "object",
  "properties": {
    "parent": {"type": "string"},
    "child": {"type": "string"}
  },
  "required": ["parent", "child"],
  "allOf": [
    {
      "properties": {
        "child": {
          "$ref": "#/properties/parent"
        }
      }
    }
  ]
}

# Example JSON object with matching parent and child fields
valid_json = '''
{
  "parent": "value",
  "child": "value"
}
'''

# Example JSON object with non-matching parent and child fields
invalid_json = '''
{
  "parent": "value",
  "child": "other_value"
}
'''

def validate_json(schema, json_string):
  try:
    jsonschema.validate(instance=json.loads(json_string), schema=schema)
    print("JSON is valid")
  except jsonschema.exceptions.ValidationError as err:
    print(f"JSON is invalid: {err}")

# Validate the JSON objects
validate_json(schema, valid_json)
validate_json(schema, invalid_json)
```
