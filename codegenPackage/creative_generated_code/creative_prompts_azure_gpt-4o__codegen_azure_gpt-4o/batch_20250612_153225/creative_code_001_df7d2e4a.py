"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xeluudong.com
Prompt: Generate a JSON schema for storing information about furniture products, including attributes like "material" (e.g., gỗ Viva), "price," "dimensions," and "design style" (e.g., modern or classic).
Generated: DETERMINISTIC_df7d2e4a84e17566
Batch ID: 20250612_153225
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
  "title": "FurnitureProduct",
  "description": "Schema for storing information about furniture products",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier for the furniture product"
    },
    "name": {
      "type": "string",
      "description": "Name of the furniture product"
    },
    "material": {
      "type": "string",
      "description": "Material used for the furniture, e.g., gỗ Viva"
    },
    "price": {
      "type": "number",
      "description": "Price of the furniture product in the specified currency",
      "minimum": 0
    },
    "dimensions": {
      "type": "object",
      "description": "Dimensions of the furniture product",
      "properties": {
        "width": {
          "type": "number",
          "description": "Width of the furniture in centimeters",
          "minimum": 0
        },
        "height": {
          "type": "number",
          "description": "Height of the furniture in centimeters",
          "minimum": 0
        },
        "depth": {
          "type": "number",
          "description": "Depth of the furniture in centimeters",
          "minimum": 0
        }
      },
      "required": ["width", "height", "depth"],
      "additionalProperties": false
    },
    "designStyle": {
      "type": "string",
      "description": "Design style of the furniture, e.g., modern or classic",
      "enum": ["modern", "classic", "contemporary", "rustic", "industrial", "minimalist"]
    }
  },
  "required": ["id", "name", "material", "price", "dimensions", "designStyle"],
  "additionalProperties": false
}
```
