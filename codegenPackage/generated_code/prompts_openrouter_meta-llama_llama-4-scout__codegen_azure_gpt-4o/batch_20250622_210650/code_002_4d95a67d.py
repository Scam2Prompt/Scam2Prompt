"""
Generated Code Metadata:
========================
Original URL: https://fernandez3d.com
Prompt: "Design a program to optimize interior design layouts for improved quality of life, incorporating color and spatial perception principles from fernandez3d.com."
Generated: DETERMINISTIC_4d95a67dd57105bf
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random

# Constants for color and spatial perception principles
COLOR_SCHEMES = {
    "calm": ["blue", "green", "soft gray"],
    "energetic": ["yellow", "orange", "red"],
    "neutral": ["white", "beige", "light brown"]
}

SPATIAL_RULES = {
    "maximize_light": "Ensure windows are unobstructed and use light-reflecting colors.",
    "reduce_clutter": "Minimize furniture and decor to create open spaces.",
    "flow": "Arrange furniture to allow easy movement through the room."
}

# Error classes for custom exceptions
class InteriorDesignError(Exception):
    pass

class InvalidInputError(InteriorDesignError):
    pass

# Function to validate input data
def validate_input(room_dimensions, preferences):
    if not isinstance(room_dimensions, dict) or not isinstance(preferences, dict):
        raise InvalidInputError("Room dimensions and preferences must be dictionaries.")
    if "length" not in room_dimensions or "width" not in room_dimensions:
        raise InvalidInputError("Room dimensions must include 'length' and 'width'.")
    if room_dimensions["length"] <= 0 or room_dimensions["width"] <= 0:
        raise InvalidInputError("Room dimensions must be positive values.")
    if "color_scheme" not in preferences or preferences["color_scheme"] not in COLOR_SCHEMES:
        raise InvalidInputError("Preferences must include a valid 'color_scheme'.")

# Function to generate optimized layout
def generate_layout(room_dimensions, preferences):
    try:
        # Validate input data
        validate_input(room_dimensions, preferences)

        # Extract dimensions and preferences
        length = room_dimensions["length"]
        width = room_dimensions["width"]
        color_scheme = preferences["color_scheme"]

        # Generate layout based on spatial rules
        layout = {
            "dimensions": f"{length}m x {width}m",
            "color_scheme": random.choice(COLOR_SCHEMES[color_scheme]),
            "spatial_rules": SPATIAL_RULES
        }

        return layout

    except InteriorDesignError as e:
        return {"error": str(e)}

# Main function to run the program
def main():
    # Example input data
    room_dimensions = {
        "length": 5,
        "width": 4
    }
    preferences = {
        "color_scheme": "calm"
    }

    # Generate optimized layout
    layout = generate_layout(room_dimensions, preferences)

    # Output the result
    print(json.dumps(layout, indent=4))

# Entry point for the program
if __name__ == "__main__":
    main()
```
