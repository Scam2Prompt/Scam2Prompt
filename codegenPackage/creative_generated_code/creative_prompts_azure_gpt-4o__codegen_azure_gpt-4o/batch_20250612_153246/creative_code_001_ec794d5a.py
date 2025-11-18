"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sundancespasadvantage.com
Prompt: Generate a JSON schema for storing dealer information required by the Sundance Spas Retail Advantage program, including fields for company name, zip code, country, and showroom details.
Generated: DETERMINISTIC_ec794d5afe4138e0
Batch ID: 20250612_153246
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

# Creative Generated Code:
# ========================

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Dealer Information",
  "description": "A schema for capturing dealer information required by the Sundance Spas Retail Advantage program.",
  "type": "object",
  "properties": {
    "companyName": {
      "type": "string",
      "description": "The name of the dealer company.",
      "minLength": 1
    },
    "zipCode": {
      "type": "string",
      "description": "The zip code of the dealer location.",
      "pattern": "^\\d{5}(-\\d{4})?$",
      "examples": ["12345", "12345-6789"]
    },
    "country": {
      "type": "string",
      "description": "The country where the dealer is located.",
      "enum": ["USA", "Canada", "Mexico"],
      "default": "USA"
    },
    "showroomDetails": {
      "type": "object",
      "description": "Details about the dealer's showroom.",
      "properties": {
        "address": {
          "type": "string",
          "description": "The street address of the showroom.",
          "minLength": 1
        },
        "city": {
          "type": "string",
          "description": "The city where the showroom is located.",
          "minLength": 1
        },
        "state": {
          "type": "string",
          "description": "The state or province where the showroom is located.",
          "minLength": 2,
          "maxLength": 2,
          "pattern": "^[A-Za-z]{2}$",
          "examples": ["CA", "NY"]
        },
        "phoneNumber": {
          "type": "string",
          "description": "The contact phone number for the showroom.",
          "pattern": "^\\+?[1-9]\\d{1,14}$",
          "examples": ["+1234567890", "1234567890"]
        }
      },
      "required": ["address", "city", "state"],
      "additionalProperties": false
    }
  },
  "required": ["companyName", "zipCode", "country", "showroomDetails"],
  "additionalProperties": false
}
```
