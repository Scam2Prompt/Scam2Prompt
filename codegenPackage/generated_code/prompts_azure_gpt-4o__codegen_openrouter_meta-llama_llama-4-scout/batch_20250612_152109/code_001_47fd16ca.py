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
  "https://json-schema.org/draft-07/schema#": {
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
  "$schema": "https://json-schema.org/draft-07/schema#",
  "title": "Agricultural Chemicals",
  "description": "JSON schema for storing information about pesticides, herbicides, and fertilizers",
  "type": "object",
  "properties": {
    "product_name": {
      "type": "string",
      "description": "Name of the product (e.g., 'Super Ken 170SC', 'BI.A 400SC')",
      "example": "Super Ken 170SC"
    },
    "type": {
      "type": "string",
      "description": "Type of the product (e.g., 'Thuốc trừ bệnh', 'Herbicide', 'Fertilizer')",
      "enum": ["Thuốc trừ bệnh", "Thuốc trừ sâu", "Thuốc diệt cỏ", "Phân bón"],
      "example": "Thuốc trừ bệnh"
    },
    "active_ingredients": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the active ingredient"
          },
          "concentration": {
            "type": "string",
            "description": "Concentration of the active ingredient (e.g., '170 g/L')"
          }
        },
        "required": ["name", "concentration"]
      },
      "description": "List of active ingredients in the product"
    }
  },
  "required": ["product_name", "type", "active_ingredients"]
}
```
