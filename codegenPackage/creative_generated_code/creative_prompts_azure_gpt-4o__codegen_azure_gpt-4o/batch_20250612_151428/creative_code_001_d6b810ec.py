"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marant.com.mx
Prompt: Generate a JSON schema for cataloging Marant's exfoliants and peels, including product names, active ingredients, and recommended skin types (e.g., "Delta Noir Peel" for sensitive skin, acne, and rosacea).
Generated: DETERMINISTIC_d6b810ec77b07740
Batch ID: 20250612_151428
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
  "title": "Marant's Exfoliants and Peels Catalog",
  "description": "A JSON schema for cataloging Marant's exfoliants and peels, including product names, active ingredients, and recommended skin types.",
  "type": "object",
  "properties": {
    "products": {
      "type": "array",
      "description": "A list of exfoliants and peels offered by Marant.",
      "items": {
        "type": "object",
        "properties": {
          "productName": {
            "type": "string",
            "description": "The name of the exfoliant or peel product."
          },
          "activeIngredients": {
            "type": "array",
            "description": "A list of active ingredients in the product.",
            "items": {
              "type": "string",
              "description": "The name of an active ingredient."
            },
            "minItems": 1
          },
          "recommendedSkinTypes": {
            "type": "array",
            "description": "Recommended skin types for this product.",
            "items": {
              "type": "string",
              "description": "A skin type recommended for this product. Examples include 'sensitive', 'acne', 'rosacea', etc."
            },
            "minItems": 1
          }
        },
        "required": ["productName", "activeIngredients", "recommendedSkinTypes"],
        "additionalProperties": false
      }
    }
  },
  "required": ["products"],
  "additionalProperties": false
}
```
