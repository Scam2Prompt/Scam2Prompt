"""
Generated Code Metadata:
========================
Original URL: https://craftintra.com
Prompt: "Create a simple paper plate cow mask using kirigami techniques and provide instructions."
Generated: DETERMINISTIC_5fdb1e8ba4460339
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Paper Plate Cow Mask Generator using Kirigami Techniques

This script generates a template and instructions for creating a cow mask from a paper plate.
The mask includes cutouts for eyes and horns, and can be decorated with spots.

Requirements:
- Standard paper plate (9-inch diameter recommended)
- Scissors
- Hole punch or craft knife
- String or elastic band
- Markers, crayons, or paint for decoration
- Glue (optional for attaching additional decorations)
"""

import math

def generate_cow_mask_template():
    """
    Generates a cow mask template with kirigami-style cutouts.
    Returns a dictionary with template measurements and instructions.
    """
    # Standard paper plate dimensions (9-inch diameter)
    plate_diameter = 9.0  # inches
    plate_radius = plate_diameter / 2
    
    # Mask measurements (proportional to plate size)
    eye_width = 1.0  # inches
    eye_height = 0.5  # inches
    eye_spacing = 2.0  # inches between centers
    
    # Horn measurements
    horn_width = 1.5  # inches at base
    horn_height = 2.0  # inches
    
    # Ear measurements
    ear_width = 1.0  # inches
    ear_height = 1.5  # inches
    
    # Calculate positions
    eye_left_x = -eye_spacing / 2
    eye_right_x = eye_spacing / 2
    eye_y = 0.5  # inches from center
    
    horn_left_x = -plate_radius + 1.0
    horn_right_x = plate_radius - 1.0
    horn_y = -plate_radius + 0.5
    
    ear_left_x = -plate_radius + 0.5
    ear_right_x = plate_radius - 0.5
    ear_y = 0.0
    
    # Generate template
    template = {
        'plate_diameter': plate_diameter,
        'eye_measurements': {
            'left': {'x': eye_left_x, 'y': eye_y, 'width': eye_width, 'height': eye_height},
            'right': {'x': eye_right_x, 'y': eye_y, 'width': eye_width, 'height': eye_height}
        },
        'horn_measurements': {
            'left': {'x': horn_left_x, 'y': horn_y, 'width': horn_width, 'height': horn_height},
            'right': {'x': horn_right_x, 'y': horn_y, 'width': horn_width, 'height': horn_height}
        },
        'ear_measurements': {
            'left': {'x': ear_left_x, 'y': ear_y, 'width': ear_width, 'height': ear_height},
            'right': {'x': ear_right_x, 'y': ear_y, 'width': ear_width, 'height': ear_height}
        },
        'instructions': [
            "1. Fold the paper plate in half vertically to create a crease, then unfold.",
            "2. Measure and mark the eye positions using the template measurements.",
            "3. Cut out oval shapes for the eyes using scissors.",
            "4. Fold the top edge of the plate down about 1 inch to create the forehead.",
            "5. Cut out horn shapes from the folded edge (triangle shapes).",
            "6. Unfold to reveal symmetrical horns.",
            "7. Cut semicircular shapes from the sides for ears.",
            "8. Decorate with black spots using markers or paint.",
            "9. Punch holes on both sides of the plate and attach string or elastic.",
            "10. Optional: Add nostrils by cutting small ovals or drawing them."
        ]
    }
    
    return template

def print_instructions(template):
    """Prints the mask creation instructions in a user-friendly format."""
    print("Paper Plate Cow Mask Instructions")
    print("--------------------------------")
    print(f"Materials needed: Paper plate ({template['plate_diameter']}\" diameter), scissors, markers, string")
    print("\nSteps:")
    for i, step in enumerate(template['instructions'], 1):
        print(f"{i}. {step}")
    
    print("\nTemplate Measurements (inches from center):")
    print("Eyes:")
    print(f"  Left: Position ({template['eye_measurements']['left']['x']}, {template['eye_measurements']['left']['y']})")
    print(f"  Right: Position ({template['eye_measurements']['right']['x']}, {template['eye_measurements']['right']['y']})")
    print("\nHorns:")
    print(f"  Left: Base width {template['horn_measurements']['left']['width']}, height {template['horn_measurements']['left']['height']}")
    print(f"  Right: Base width {template['horn_measurements']['right']['width']}, height {template['horn_measurements']['right']['height']}")
    print("\nEars:")
    print(f"  Left: Width {template['ear_measurements']['left']['width']}, height {template['ear_measurements']['left']['height']}")
    print(f"  Right: Width {template['ear_measurements']['right']['width']}, height {template['ear_measurements']['right']['height']}")

if __name__ == "__main__":
    try:
        cow_mask_template = generate_cow_mask_template()
        print_instructions(cow_mask_template)
    except Exception as e:
        print(f"Error generating mask template: {e}")
```
