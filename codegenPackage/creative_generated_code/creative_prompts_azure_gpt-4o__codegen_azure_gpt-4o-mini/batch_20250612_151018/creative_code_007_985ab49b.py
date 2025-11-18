"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-332--condescending-hopper-c3ed30.netlify.app
Prompt: Write a JSON Schema that uses the `properties` keyword to define a schema for an object with optional fields `title` (string) and `description` (string), and a required field `id` (integer).
Generated: DETERMINISTIC_985ab49bdd039e95
Batch ID: 20250612_151018
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

# Creative Generated Code:
# ========================

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "description": "A unique identifier for the object. This field is required."
    },
    "title": {
      "type": "string",
      "description": "An optional title for the object."
    },
    "description": {
      "type": "string",
      "description": "An optional description for the object."
    }
  },
  "required": ["id"],
  "additionalProperties": false,
  "examples": [
    {
      "id": 1,
      "title": "Sample Item",
      "description": "This is a description of the sample item."
    },
    {
      "id": 2
    }
  ]
}
```
