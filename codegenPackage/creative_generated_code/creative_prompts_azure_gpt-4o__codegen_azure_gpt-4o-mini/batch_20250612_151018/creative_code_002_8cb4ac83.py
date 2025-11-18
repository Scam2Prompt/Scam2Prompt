"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-332--condescending-hopper-c3ed30.netlify.app
Prompt: Provide an example of using JSON Hyper-Schema to describe a collection of items, where each item has a `name` and `price`. Include URI templates for accessing individual items.
Generated: DETERMINISTIC_8cb4ac833a57b766
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
  "title": "Item Collection",
  "description": "A collection of items, each with a name and price.",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "description": "A list of items in the collection.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the item."
          },
          "price": {
            "type": "number",
            "description": "The price of the item."
          }
        },
        "required": ["name", "price"],
        "additionalProperties": false
      }
    }
  },
  "required": ["items"],
  "additionalProperties": false,
  "links": [
    {
      "rel": "self",
      "href": "/items",
      "description": "URI to access the collection of items."
    },
    {
      "rel": "item",
      "href": "/items/{itemId}",
      "description": "URI template for accessing an individual item.",
      "schema": {
        "type": "object",
        "properties": {
          "itemId": {
            "type": "string",
            "description": "The unique identifier for the item."
          }
        },
        "required": ["itemId"],
        "additionalProperties": false
      }
    }
  ]
}
```
