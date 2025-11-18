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
  "http://json-schema.org/draft-04/hyper-schema": {
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
  "$schema": "http://json-schema.org/draft-04/hyper-schema",
  "title": "ItemCollection",
  "description": "A collection of items where each item has a name and price.",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the item."
          },
          "price": {
            "type": "number",
            "description": "Price of the item."
          }
        },
        "required": ["name", "price"],
        "links": [
          {
            "rel": "self",
            "href": "/items/{name}",
            "title": "Get individual item by name",
            "description": "Provides the URI template for accessing an individual item by its name."
          }
        ]
      }
    }
  },
  "required": ["items"],
  "links": [
    {
      "rel": "self",
      "href": "/items",
      "title": "Get all items",
      "description": "Provides the URI template for accessing the entire item collection."
    },
    {
      "rel": "create",
      "href": "/items",
      "method": "POST",
      "title": "Create a new item",
      "description": "Allows the creation of a new item in the collection."
    },
    {
      "rel": "delete",
      "href": "/items/{name}",
      "method": "DELETE",
      "title": "Delete an item",
      "description": "Allows the deletion of a specific item by its name."
    }
  ]
}
```
