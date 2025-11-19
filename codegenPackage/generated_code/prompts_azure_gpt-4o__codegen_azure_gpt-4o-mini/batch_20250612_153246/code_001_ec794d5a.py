"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Generate a JSON schema for storing dealer information required by the Sundance Spas Retail Advantage program, including fields for company name, zip code, country, and showroom details.
Generated: DETERMINISTIC_ec794d5afe4138e0
Batch ID: 20250612_153246
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

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Dealer Information Schema",
  "description": "A JSON schema for storing dealer information required by the Sundance Spas Retail Advantage program.",
  "type": "object",
  "properties": {
    "companyName": {
      "type": "string",
      "description": "The name of the dealer's company.",
      "minLength": 1
    },
    "zipCode": {
      "type": "string",
      "description": "The zip code of the dealer's location.",
      "pattern": "^[0-9]{5}(?:-[0-9]{4})?$"
    },
    "country": {
      "type": "string",
      "description": "The country where the dealer is located.",
      "minLength": 1
    },
    "showroomDetails": {
      "type": "object",
      "description": "Details about the dealer's showroom.",
      "properties": {
        "address": {
          "type": "string",
          "description": "The address of the showroom.",
          "minLength": 1
        },
        "phone": {
          "type": "string",
          "description": "The contact phone number for the showroom.",
          "pattern": "^\\+?[0-9]*$"
        },
        "email": {
          "type": "string",
          "description": "The contact email for the showroom.",
          "format": "email"
        }
      },
      "required": ["address"],
      "additionalProperties": false
    }
  },
  "required": ["companyName", "zipCode", "country", "showroomDetails"],
  "additionalProperties": false
}
```
