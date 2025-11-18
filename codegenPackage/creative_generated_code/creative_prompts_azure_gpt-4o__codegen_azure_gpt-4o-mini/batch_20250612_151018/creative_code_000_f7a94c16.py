"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-332--condescending-hopper-c3ed30.netlify.app
Prompt: Write a JSON Schema that validates a JSON object containing a user's profile information, including fields for `name` (string), `age` (integer), and `email` (string). Use the validation keywords described in the 2019-09 draft.
Generated: DETERMINISTIC_f7a94c1649d4b731
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://json-schema.org/draft-2019-09/schema#": {
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
  "$schema": "http://json-schema.org/draft-2019-09/schema#",
  "title": "UserProfile",
  "description": "A JSON Schema to validate a user's profile information.",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "The user's full name.",
      "minLength": 1
    },
    "age": {
      "type": "integer",
      "description": "The user's age.",
      "minimum": 0
    },
    "email": {
      "type": "string",
      "description": "The user's email address.",
      "format": "email"
    }
  },
  "required": ["name", "age", "email"],
  "additionalProperties": false
}
```
