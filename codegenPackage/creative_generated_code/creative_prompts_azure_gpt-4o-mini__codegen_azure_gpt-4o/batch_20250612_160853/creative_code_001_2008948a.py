"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: How can I design a neon advertisement display that aligns with the production capabilities outlined by Nova Forma d.o.o.?
Generated: DETERMINISTIC_2008948ac532dc54
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to design a neon advertisement display aligning with production capabilities of Nova Forma d.o.o.

import json

# Define production capabilities and constraints for Nova Forma d.o.o.
PRODUCTION_CAPABILITIES = {
    "max_width": 200,  # Maximum width in cm
    "max_height": 100, # Maximum height in cm
    "max_colors": 5,   # Maximum number of colors allowed
    "font_styles": ["Arial", "NeonTube", "SansSerif"],  # Allowed font styles
    "max_text_length": 50,  # Maximum text length for the display
}

# Function to validate input for neon advertisement design
def validate_design(design):
    """
    Validates the input neon advertisement design against production capabilities.

    Args:
        design (dict): A dictionary containing the neon sign design.

    Returns:
        bool: True if the design is valid, False otherwise.
        str: Validation error message (if any).
    """
    if design["width"] > PRODUCTION_CAPABILITIES["max_width"]:
        return False, "Width exceeds maximum allowable dimensions."
    if design["height"] > PRODUCTION_CAPABILITIES["max_height"]:
        return False, "Height exceeds maximum allowable dimensions."
    if len(design["colors"]) > PRODUCTION_CAPABILITIES["max_colors"]:
        return False, "Exceeds maximum number of allowed colors."
    if design["font_style"] not in PRODUCTION_CAPABILITIES["font_styles"]:
        return False, f"Font style '{design['font_style']}' is not supported."
    if len(design["text"]) > PRODUCTION_CAPABILITIES["max_text_length"]:
        return False, "Text length exceeds the allowable limit."
    return True, "Design is valid."

# Function to generate neon advertisement display
def create_neon_advertisement(design):
    """
    Creates a neon advertisement display based on the provided design.

    Args:
        design (dict): A dictionary containing the neon sign design.

    Returns:
        dict: A dictionary containing the finalized design or error message.
    """
    try:
        # Validate the input design
        is_valid, message = validate_design(design)
        if not is_valid:
            return {"success": False, "error": message}

        # Create the finalized neon display design
        finalized_design = {
            "width": design["width"],
            "height": design["height"],
            "colors": design["colors"],
            "font_style": design["font_style"],
            "text": design["text"]
        }

        # Return the finalized design
        return {"success": True, "design": finalized_design}

    except Exception as e:
        # Handle unexpected errors gracefully
        return {"success": False, "error": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    # Sample design input
    sample_design = {
        "width": 150,
        "height": 80,
        "colors": ["red", "blue", "green"],
        "font_style": "NeonTube",
        "text": "Welcome to Nova Forma!"
    }

    # Create neon advertisement display
    result = create_neon_advertisement(sample_design)

    # Print the result in JSON format for clarity
    print(json.dumps(result, indent=4))
```
