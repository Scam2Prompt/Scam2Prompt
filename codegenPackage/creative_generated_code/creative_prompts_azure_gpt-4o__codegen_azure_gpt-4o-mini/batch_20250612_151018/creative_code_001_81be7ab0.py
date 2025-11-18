"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-332--condescending-hopper-c3ed30.netlify.app
Prompt: Generate a JSON Schema that uses the `type` keyword to restrict a JSON instance to an array of strings, ensuring the array contains at least three items.
Generated: DETERMINISTIC_81be7ab0480f6c69
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
  "title": "String Array Schema",
  "description": "A JSON schema that validates an array of strings with at least three items.",
  "type": "array",
  "minItems": 3,  // Ensure at least three items in the array
  "items": {
    "type": "string"  // Each item in the array must be a string
  },
  "uniqueItems": true  // Ensure that all items in the array are unique
}
```
