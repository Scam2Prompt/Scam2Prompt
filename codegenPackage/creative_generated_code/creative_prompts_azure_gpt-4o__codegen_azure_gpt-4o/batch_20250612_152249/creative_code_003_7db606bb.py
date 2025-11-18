"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budibromotour.ilmaweb.com
Prompt: Create a JSON schema to represent the tourism packages offered by Budi Bromo Tour, including jeep rentals, accommodations, and pre-wedding services.
Generated: DETERMINISTIC_7db606bb9dc2b351
Batch ID: 20250612_152249
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
  "title": "Budi Bromo Tour Packages",
  "description": "JSON schema representing tourism packages offered by Budi Bromo Tour, including jeep rentals, accommodations, and pre-wedding services.",
  "type": "object",
  "properties": {
    "packageName": {
      "type": "string",
      "description": "Name of the tourism package."
    },
    "price": {
      "type": "number",
      "description": "Total price of the package in USD.",
      "minimum": 0
    },
    "jeepRental": {
      "type": "object",
      "description": "Details about jeep rental services.",
      "properties": {
        "included": {
          "type": "boolean",
          "description": "Indicates whether jeep rental is included in the package."
        },
        "vehicleType": {
          "type": "string",
          "description": "Type of jeep vehicle provided. Example: '4x4 SUV'.",
          "enum": ["4x4 SUV", "Compact Jeep", "Luxury Jeep"]
        },
        "durationHours": {
          "type": "integer",
          "description": "Duration of the jeep rental in hours.",
          "minimum": 1
        }
      },
      "required": ["included"]
    },
    "accommodation": {
      "type": "object",
      "description": "Accommodation details for the package.",
      "properties": {
        "included": {
          "type": "boolean",
          "description": "Indicates whether accommodation is included."
        },
        "hotelName": {
          "type": "string",
          "description": "Name of the hotel where accommodation is provided."
        },
        "roomType": {
          "type": "string",
          "description": "Type of room provided in the hotel.",
          "enum": ["Single", "Double", "Suite"]
        },
        "nights": {
          "type": "integer",
          "description": "Number of nights of accommodation.",
          "minimum": 1
        }
      },
      "required": ["included"]
    },
    "preWeddingServices": {
      "type": "object",
      "description": "Details about pre-wedding services.",
      "properties": {
        "included": {
          "type": "boolean",
          "description": "Indicates whether pre-wedding services are included."
        },
        "photography": {
          "type": "boolean",
          "description": "Indicates whether photography services are provided."
        },
        "videography": {
          "type": "boolean",
          "description": "Indicates whether videography services are provided."
        },
        "makeupArtist": {
          "type": "boolean",
          "description": "Indicates whether a makeup artist is provided."
        },
        "locations": {
          "type": "array",
          "description": "List of locations for pre-wedding photoshoots.",
          "items": {
            "type": "string"
          }
        }
      },
      "required": ["included"]
    }
  },
  "required": ["packageName", "price", "jeepRental", "accommodation", "preWeddingServices"],
  "additionalProperties": false
}
```
