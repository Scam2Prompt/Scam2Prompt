"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Create a JSON object representing the pricing structure for Playland Kenya’s services, including child packages, bowling, virtual reality, ropes courses, and pool tables.
Generated: DETERMINISTIC_c42de36f6c925d62
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def create_pricing_structure():
    """
    Creates a JSON object representing the pricing structure for Playland Kenya’s services.
    
    Returns:
        str: A JSON-formatted string of the pricing structure.
    """
    
    pricing_structure = {
        "Playland_Kenya": {
            "services": {
                "child_packages": {
                    "basic": {
                        "price": 1000,
                        "description": "Access to all basic play areas.",
                        "age_limit": "3-12 years"
                    },
                    "premium": {
                        "price": 1500,
                        "description": "Access to all areas plus one complimentary snack.",
                        "age_limit": "3-12 years"
                    }
                },
                "bowling": {
                    "per_game": {
                        "price": 300,
                        "description": "Per person, includes shoe rental.",
                        "min_players": 1,
                        "max_players": 6
                    },
                    "group_package": {
                        "price": 1500,
                        "description": "Up to 5 players for 2 games, includes snacks.",
                        "players": 5
                    }
                },
                "virtual_reality": {
                    "per_session": {
                        "price": 500,
                        "description": "30-minute VR experience.",
                        "age_limit": "10+ years"
                    },
                    "group_discount": {
                        "price": 400,
                        "description": "Per person for groups of 4 or more.",
                        "min_group_size": 4
                    }
                },
                "ropes_courses": {
                    "adult_ticket": {
                        "price": 1200,
                        "description": "Full access to ropes courses for adults.",
                        "age_limit": "13+ years"
                    },
                    "child_ticket": {
                        "price": 800,
                        "description": "Full access to ropes courses for children.",
                        "age_limit": "5-12 years"
                    }
                },
                "pool_tables": {
                    "per_hour": {
                        "price": 400,
                        "description": "Per table, includes all equipment.",
                        "max_players": 4
                    },
                    "happy_hour": {
                        "price": 250,
                        "description": "Per table during happy hour (4 PM - 6 PM).",
                        "max_players": 4
                    }
                }
            }
        }
    }

    return json.dumps(pricing_structure, indent=4)

if __name__ == "__main__":
    try:
        pricing_json = create_pricing_structure()
        print(pricing_json)
    except Exception as e:
        print(f"An error occurred while creating the pricing structure: {e}")
```
