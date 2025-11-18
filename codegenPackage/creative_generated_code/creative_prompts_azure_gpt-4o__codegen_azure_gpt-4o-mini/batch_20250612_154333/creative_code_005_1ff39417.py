"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ferramentaspremimum.shop
Prompt: Provide a tutorial for using Canva Pro to design a branded infographic, emphasizing the use of templates and advanced customization options.
Generated: DETERMINISTIC_1ff39417383f18d7
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import canva
import sys

def create_branded_infographic(api_key, template_id, brand_colors):
    """
    Create a branded infographic using Canva Pro.

    Parameters:
    api_key (str): Your Canva API key.
    template_id (str): The ID of the Canva template to use.
    brand_colors (list): A list of brand colors in HEX format.

    Returns:
    None
    """

    # Initialize the Canva client
    try:
        client = canva.Client(api_key)
    except Exception as e:
        print(f"Error initializing Canva client: {e}")
        sys.exit(1)

    # Retrieve the template
    try:
        template = client.get_template(template_id)
    except Exception as e:
        print(f"Error retrieving template: {e}")
        sys.exit(1)

    # Create a new design from the template
    try:
        design = client.create_design(template)
    except Exception as e:
        print(f"Error creating design from template: {e}")
        sys.exit(1)

    # Customize the design with brand colors
    try:
        for color in brand_colors:
            design.add_color(color)
    except Exception as e:
        print(f"Error adding brand colors to design: {e}")
        sys.exit(1)

    # Finalize the design
    try:
        design.finalize()
        print(f"Branded infographic created successfully: {design.url}")
    except Exception as e:
        print(f"Error finalizing design: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    API_KEY = 'your_canva_api_key_here'
    TEMPLATE_ID = 'your_template_id_here'
    BRAND_COLORS = ['#FF5733', '#33C1FF', '#FF33A6']  # Example colors

    create_branded_infographic(API_KEY, TEMPLATE_ID, BRAND_COLORS)
```

**Note:** This is a hypothetical script assuming a `canva` library exists, which may not reflect actual Canva API usage. Ensure to replace `'your_canva_api_key_here'` and `'your_template_id_here'` with your actual credentials.
