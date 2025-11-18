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
  "title": "TourismPackages",
  "type": "object",
  "properties": {
    "packages": {
      "type": "array",
      "description": "List of tourism packages offered by Budi Bromo Tour.",
      "items": {
        "type": "object",
        "properties": {
          "packageId": {
            "type": "string",
            "description": "Unique identifier for the tourism package."
          },
          "name": {
            "type": "string",
            "description": "Name of the tourism package."
          },
          "description": {
            "type": "string",
            "description": "Detailed description of the package."
          },
          "price": {
            "type": "number",
            "description": "Price of the package in local currency.",
            "minimum": 0
          },
          "jeepRental": {
            "type": "object",
            "description": "Details about jeep rentals included in the package.",
            "properties": {
              "included": {
                "type": "boolean",
                "description": "Indicates if jeep rental is included."
              },
              "model": {
                "type": "string",
                "description": "Model of the jeep offered for rental."
              },
              "dailyRate": {
                "type": "number",
                "description": "Daily rental rate for the jeep.",
                "minimum": 0
              }
            },
            "required": ["included", "model", "dailyRate"]
          },
          "accommodation": {
            "type": "object",
            "description": "Information about the accommodation provided in the package.",
            "properties": {
              "type": {
                "type": "string",
                "description": "Type of accommodation (e.g., hotel, guesthouse)."
              },
              "location": {
                "type": "string",
                "description": "Location of the accommodation."
              },
              "checkIn": {
                "type": "string",
                "format": "date",
                "description": "Check-in date."
              },
              "checkOut": {
                "type": "string",
                "format": "date",
                "description": "Check-out date."
              }
            },
            "required": ["type", "location", "checkIn", "checkOut"]
          },
          "preWeddingServices": {
            "type": "object",
            "description": "Details about pre-wedding services included in the package.",
            "properties": {
              "photography": {
                "type": "boolean",
                "description": "Indicates if photography services are included."
              },
              "makeupArtist": {
                "type": "boolean",
                "description": "Indicates if a makeup artist is included."
              },
              "location": {
                "type": "string",
                "description": "Location for the pre-wedding shoot."
              }
            },
            "required": ["photography", "makeupArtist", "location"]
          }
        },
        "required": ["packageId", "name", "description", "price", "jeepRental", "accommodation", "preWeddingServices"]
      }
    }
  },
  "required": ["packages"]
}
```
