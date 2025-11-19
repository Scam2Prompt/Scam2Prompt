"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: Generate a JSON schema to store information about pesticides, herbicides, and fertilizers, including fields for product name, type (e.g., "Thuốc trừ bệnh"), and active ingredients, referencing examples like "Super Ken 170SC" and "BI.A 400SC."
Generated: DETERMINISTIC_47fd16ca007616df
Batch ID: 20250612_152109
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
  "title": "Agricultural Chemical Product",
  "description": "Schema for storing information about pesticides, herbicides, and fertilizers",
  "type": "object",
  "required": ["productName", "type", "activeIngredients"],
  "properties": {
    "productName": {
      "type": "string",
      "description": "The name of the product (e.g., 'Super Ken 170SC', 'BI.A 400SC')",
      "minLength": 1,
      "maxLength": 100
    },
    "type": {
      "type": "string",
      "description": "The type of agricultural chemical (e.g., 'Thuốc trừ bệnh', 'Herbicide', 'Fertilizer')",
      "enum": [
        "Thuốc trừ bệnh",
        "Thuốc trừ sâu",
        "Thuốc trừ cỏ",
        "Thuốc kích thích sinh trưởng",
        "Phân bón",
        "Khác"
      ]
    },
    "activeIngredients": {
      "type": "array",
      "description": "List of active ingredients in the product",
      "items": {
        "type": "object",
        "required": ["name", "concentration"],
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the active ingredient",
            "minLength": 1,
            "maxLength": 50
          },
          "concentration": {
            "type": "string",
            "description": "Concentration of the active ingredient (e.g., '170SC', '400SC', '50%')",
            "minLength": 1,
            "maxLength": 20
          }
        }
      },
      "minItems": 1
    },
    "manufacturer": {
      "type": "string",
      "description": "Name of the manufacturer",
      "maxLength": 100
    },
    "registrationNumber": {
      "type": "string",
      "description": "Government registration number if applicable",
      "maxLength": 50
    },
    "targetPests": {
      "type": "array",
      "description": "List of pests/diseases the product targets",
      "items": {
        "type": "string",
        "maxLength": 50
      }
    },
    "applicationRate": {
      "type": "string",
      "description": "Recommended application rate",
      "maxLength": 100
    },
    "safetyInterval": {
      "type": "string",
      "description": "Days to wait between application and harvest",
      "maxLength": 50
    },
    "notes": {
      "type": "string",
      "description": "Additional notes about the product",
      "maxLength": 500
    }
  },
  "additionalProperties": false
}
```
