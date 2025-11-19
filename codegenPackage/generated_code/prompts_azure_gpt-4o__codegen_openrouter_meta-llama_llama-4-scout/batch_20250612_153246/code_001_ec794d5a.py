"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Generate a JSON schema for storing dealer information required by the Sundance Spas Retail Advantage program, including fields for company name, zip code, country, and showroom details.
Generated: DETERMINISTIC_ec794d5afe4138e0
Batch ID: 20250612_153246
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

```python
import json

def generate_dealer_info_schema():
    """
    Generates a JSON schema for storing dealer information required by the Sundance Spas Retail Advantage program.

    Returns:
        dict: A dictionary representing the JSON schema.
    """

    # Define the schema
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Sundance Spas Retail Advantage Dealer Information",
        "description": "JSON schema for storing dealer information",
        "type": "object",
        "properties": {
            "company_name": {
                "type": "string",
                "description": "The name of the dealer company",
                "minLength": 1,
                "maxLength": 255
            },
            "zip_code": {
                "type": "string",
                "description": "The zip code of the dealer's location",
                "pattern": "^\\d{5}(-\\d{4})?$",  # US zip code pattern
                "minLength": 5,
                "maxLength": 10
            },
            "country": {
                "type": "string",
                "description": "The country of the dealer's location",
                "minLength": 2,
                "maxLength": 50,
                "enum": ["USA", "Canada", "Mexico"]  # Supported countries
            },
            "showroom": {
                "type": "object",
                "description": "Details about the dealer's showroom",
                "properties": {
                    "address": {
                        "type": "string",
                        "description": "The physical address of the showroom",
                        "minLength": 1,
                        "maxLength": 255
                    },
                    "city": {
                        "type": "string",
                        "description": "The city where the showroom is located",
                        "minLength": 1,
                        "maxLength": 50
                    },
                    "state": {
                        "type": "string",
                        "description": "The state or province where the showroom is located",
                        "minLength": 2,
                        "maxLength": 50
                    },
                    "phone_number": {
                        "type": "string",
                        "description": "The phone number of the showroom",
                        "pattern": "^\\(?([0-9]{3})\\)?[-.\\s]?([0-9]{3})[-.\\s]?([0-9]{4})$",
                        "minLength": 10,
                        "maxLength": 20
                    }
                },
                "required": ["address", "city", "state"]
            }
        },
        "required": ["company_name", "zip_code", "country"]
    }

    return schema

def main():
    try:
        schema = generate_dealer_info_schema()
        print(json.dumps(schema, indent=4))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
