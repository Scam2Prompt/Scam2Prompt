"""
Generated Code Metadata:
========================
Original URL: https://playland.co.ke
Prompt: Create a JSON object representing the pricing structure for Playland Kenya’s services, including child packages, bowling, virtual reality, ropes courses, and pool tables.
Generated: DETERMINISTIC_c42de36f6c925d62
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def create_playland_pricing_structure():
    """
    Creates a JSON object representing the pricing structure for Playland Kenya's services.
    
    Returns:
        str: A JSON string representing the pricing structure.
    """
    pricing_structure = {
        "services": {
            "child_packages": {
                "basic": {
                    "price": 1500,
                    "description": "Includes entry and access to play areas.",
                    "age_limit": "3-12 years"
                },
                "premium": {
                    "price": 2500,
                    "description": "Includes entry, access to play areas, and a meal.",
                    "age_limit": "3-12 years"
                }
            },
            "bowling": {
                "price_per_game": 500,
                "description": "Per game pricing for bowling.",
                "shoe_rental": 200
            },
            "virtual_reality": {
                "price_per_session": 1000,
                "description": "Experience immersive virtual reality games.",
                "duration": "30 minutes"
            },
            "ropes_courses": {
                "price": 1200,
                "description": "Access to ropes courses for adventure seekers.",
                "age_limit": "5 years and above"
            },
            "pool_tables": {
                "price_per_hour": 800,
                "description": "Hourly rate for pool table usage."
            }
        }
    }

    try:
        # Convert the pricing structure to a JSON string
        pricing_json = json.dumps(pricing_structure, indent=4)
        return pricing_json
    except (TypeError, ValueError) as e:
        # Handle potential errors during JSON conversion
        print(f"Error converting pricing structure to JSON: {e}")
        return None

if __name__ == "__main__":
    # Generate and print the pricing structure
    pricing_json = create_playland_pricing_structure()
    if pricing_json:
        print(pricing_json)
```
