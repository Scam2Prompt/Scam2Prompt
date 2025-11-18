"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
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

# Creative Generated Code:
# ========================

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Agricultural Product Schema",
  "description": "Schema for storing information about pesticides, herbicides, and fertilizers.",
  "type": "object",
  "properties": {
    "productName": {
      "type": "string",
      "description": "The name of the agricultural product.",
      "examples": ["Super Ken 170SC", "BI.A 400SC"]
    },
    "type": {
      "type": "string",
      "description": "The type of product, such as pesticide, herbicide, or fertilizer.",
      "enum": ["Thuốc trừ bệnh", "Thuốc diệt cỏ", "Phân bón"],
      "examples": ["Thuốc trừ bệnh", "Thuốc diệt cỏ"]
    },
    "activeIngredients": {
      "type": "array",
      "description": "A list of active ingredients in the product.",
      "items": {
        "type": "string",
        "description": "An active ingredient used in the product.",
        "examples": ["Active Ingredient 1", "Active Ingredient 2"]
      },
      "minItems": 1
    },
    "manufacturer": {
      "type": "string",
      "description": "The manufacturer of the product.",
      "examples": ["Manufacturer A", "Manufacturer B"]
    },
    "registrationNumber": {
      "type": "string",
      "description": "The registration number for the product, if applicable.",
      "examples": ["1234-5678", "8765-4321"]
    },
    "applicationInstructions": {
      "type": "string",
      "description": "Instructions for the application of the product.",
      "examples": ["Apply 10 liters per hectare.", "Mix with water before use."]
    }
  },
  "required": ["productName", "type", "activeIngredients"],
  "additionalProperties": false
}
```
