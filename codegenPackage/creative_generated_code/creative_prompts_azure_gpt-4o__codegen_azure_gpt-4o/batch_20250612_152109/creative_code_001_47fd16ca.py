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
  "title": "AgricultureProduct",
  "type": "object",
  "description": "Schema for storing information about pesticides, herbicides, and fertilizers.",
  "properties": {
    "productName": {
      "type": "string",
      "description": "The name of the product, e.g., 'Super Ken 170SC'.",
      "minLength": 1
    },
    "productType": {
      "type": "string",
      "description": "The type of product, such as 'Thuốc trừ bệnh'.",
      "enum": ["Pesticide", "Herbicide", "Fertilizer"]
    },
    "activeIngredients": {
      "type": "array",
      "description": "List of active ingredients in the product.",
      "items": {
        "type": "string",
        "description": "Name of an active ingredient."
      },
      "minItems": 1
    }
  },
  "required": ["productName", "productType", "activeIngredients"],
  "additionalProperties": false,
  "examples": [
    {
      "productName": "Super Ken 170SC",
      "productType": "Pesticide",
      "activeIngredients": ["Active Ingredient A", "Active Ingredient B"]
    },
    {
      "productName": "BI.A 400SC",
      "productType": "Herbicide",
      "activeIngredients": ["Ingredient X", "Ingredient Y"]
    }
  ]
}
```
