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
  "title": "Sundance Spas Retail Advantage Dealer Information",
  "description": "Schema for storing dealer information required by the Sundance Spas Retail Advantage program",
  "type": "object",
  "required": [
    "companyName",
    "zipCode",
    "country",
    "showroom"
  ],
  "properties": {
    "companyName": {
      "type": "string",
      "description": "Legal name of the dealership",
      "minLength": 1,
      "maxLength": 100
    },
    "zipCode": {
      "type": "string",
      "description": "Postal/ZIP code of the dealership",
      "pattern": "^[a-zA-Z0-9\\- ]+$"
    },
    "country": {
      "type": "string",
      "description": "Country where the dealership is located",
      "enum": ["US", "CA", "UK", "AU", "NZ", "DE", "FR", "IT", "ES", "Other"]
    },
    "address": {
      "type": "object",
      "description": "Physical address of the dealership",
      "properties": {
        "street": {
          "type": "string",
          "description": "Street address",
          "minLength": 1,
          "maxLength": 100
        },
        "city": {
          "type": "string",
          "description": "City",
          "minLength": 1,
          "maxLength": 50
        },
        "state": {
          "type": "string",
          "description": "State/Province/Region",
          "minLength": 1,
          "maxLength": 50
        }
      }
    },
    "phone": {
      "type": "string",
      "description": "Primary contact phone number",
      "pattern": "^\\+?[0-9\\- ]+$"
    },
    "email": {
      "type": "string",
      "description": "Primary contact email",
      "format": "email"
    },
    "website": {
      "type": "string",
      "description": "Company website URL",
      "format": "uri"
    },
    "showroom": {
      "type": "object",
      "description": "Showroom details",
      "required": ["hasShowroom"],
      "properties": {
        "hasShowroom": {
          "type": "boolean",
          "description": "Whether the dealer has a physical showroom"
        },
        "size": {
          "type": "string",
          "description": "Showroom size category",
          "enum": ["small", "medium", "large", "x-large"]
        },
        "displayModels": {
          "type": "array",
          "description": "List of spa models displayed in showroom",
          "items": {
            "type": "string"
          }
        },
        "features": {
          "type": "array",
          "description": "Showroom features",
          "items": {
            "type": "string",
            "enum": ["wet-floor", "theater", "lighting", "sound-system", "seating-area"]
          }
        }
      }
    },
    "certifications": {
      "type": "array",
      "description": "Dealer certifications",
      "items": {
        "type": "string",
        "enum": ["elite", "premier", "gold", "silver", "bronze"]
      }
    },
    "yearsInBusiness": {
      "type": "integer",
      "description": "Number of years the dealer has been in business",
      "minimum": 0
    },
    "additionalNotes": {
      "type": "string",
      "description": "Additional information about the dealer",
      "maxLength": 500
    }
  },
  "additionalProperties": false
}
```
