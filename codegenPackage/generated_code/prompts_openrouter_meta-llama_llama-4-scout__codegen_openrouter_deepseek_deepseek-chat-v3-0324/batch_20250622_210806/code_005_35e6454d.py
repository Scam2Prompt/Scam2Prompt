"""
Generated Code Metadata:
========================
Original URL: https://icestyle.pl
Prompt: "Write a product description for a new line of figure skating dresses inspired by the designs on the IceStyle website."
Generated: DETERMINISTIC_35e6454df1ada7db
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_product_description(dress_name, design_elements, fabric_details, target_audience):
    """
    Generates a professional product description for figure skating dresses.
    
    Args:
        dress_name (str): Name of the skating dress
        design_elements (list): List of design features (e.g., ["crystal embellishments", "floral pattern"])
        fabric_details (dict): Dictionary with fabric properties (e.g., {"material": "stretch mesh", "features": ["breathable", "moisture-wicking"]})
        target_audience (str): Intended skater level (e.g., "competitive", "recreational")
    
    Returns:
        str: Formatted product description
    """
    
    # Validate input types
    if not isinstance(dress_name, str):
        raise ValueError("dress_name must be a string")
    if not isinstance(design_elements, list):
        raise ValueError("design_elements must be a list")
    if not isinstance(fabric_details, dict):
        raise ValueError("fabric_details must be a dictionary")
    if not isinstance(target_audience, str):
        raise ValueError("target_audience must be a string")
    
    # Build design elements string
    design_str = ", ".join(design_elements[:-1]) + f" and {design_elements[-1]}" if len(design_elements) > 1 else design_elements[0]
    
    # Build fabric features string
    fabric_features = ", ".join(fabric_details["features"])
    
    description = f"""
    Introducing the stunning {dress_name} figure skating dress, designed for {target_audience} skaters who demand both elegance and performance.
    
    This exquisite dress features {design_str}, creating a dazzling effect on the ice. 
    Crafted from premium {fabric_details['material']} that's {fabric_features}, ensuring comfort and freedom of movement.
    
    The {dress_name} combines competitive functionality with haute couture styling, making it perfect for:
    - Competition performances
    - Ice shows and exhibitions
    - Special skating events
    
    Available in a range of sizes and customizable colors to match your unique style.
    """
    
    return description.strip()

# Example usage
if __name__ == "__main__":
    example_description = generate_product_description(
        dress_name="Aurora Glide",
        design_elements=["hand-sewn Swarovski crystals", "asymmetrical neckline", "ombré color fade"],
        fabric_details={
            "material": "four-way stretch mesh",
            "features": ["breathable", "moisture-wicking", "shape-retaining"]
        },
        target_audience="competitive"
    )
    print(example_description)
```
