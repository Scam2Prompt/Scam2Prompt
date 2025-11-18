"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Create a Python function to generate structured interior design plans based on client preferences, referencing the structure interior designing services provided by Remas Engineering Consultants.
Generated: DETERMINISTIC_14f6801e6ac7413b
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, Any, List

class InteriorDesignPlan:
    def __init__(self, style: str, color_scheme: List[str], layout: Dict[str, Any]):
        """
        Initializes the InteriorDesignPlan with style, color scheme, and layout.

        :param style: The design style (e.g., Modern, Rustic).
        :param color_scheme: A list of colors for the design.
        :param layout: A dictionary representing the layout of the design.
        """
        self.style = style
        self.color_scheme = color_scheme
        self.layout = layout

    def to_dict(self) -> Dict[str, Any]:
        """Converts the design plan to a dictionary format."""
        return {
            'style': self.style,
            'color_scheme': self.color_scheme,
            'layout': self.layout
        }

def generate_design_plan(client_preferences: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates a structured interior design plan based on client preferences.

    :param client_preferences: A dictionary containing client preferences,
                              such as style, color_scheme, and layout.
    :return: A dictionary representing the generated interior design plan.
    :raises ValueError: If any required preference is missing.
    """
    try:
        # Extract preferences from the client input
        style = client_preferences.get('style')
        color_scheme = client_preferences.get('color_scheme')
        layout = client_preferences.get('layout')

        # Validate the input preferences
        if not style or not color_scheme or not layout:
            raise ValueError("Missing required client preferences: style, color_scheme, and layout must be provided.")

        # Create an interior design plan object
        design_plan = InteriorDesignPlan(style, color_scheme, layout)

        # Return the design plan as a dictionary
        return design_plan.to_dict()
    
    except Exception as e:
        # Handle unexpected errors
        return {"error": str(e)}

# Example client preferences input
client_preferences_example = {
    'style': 'Modern',
    'color_scheme': ['White', 'Gray', 'Black'],
    'layout': {
        'living_room': {
            'dimensions': '20x15',
            'furniture': ['sofa', 'coffee table', 'TV stand']
        },
        'bedroom': {
            'dimensions': '15x15',
            'furniture': ['bed', 'nightstand', 'wardrobe']
        }
    }
}

# Generate the interior design plan
design_plan = generate_design_plan(client_preferences_example)

# Output the generated design plan
print(json.dumps(design_plan, indent=4))
```
