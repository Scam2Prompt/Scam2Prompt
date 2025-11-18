"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskatiyasgroup.com
Prompt: Create a script to recommend mobile LCDs for smartphones based on user preferences for scratch resistance, light detection, and resolution, using Maskatiyas Group's product specifications.
Generated: DETERMINISTIC_9e32fe64bb4ee6fb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a dictionary of Maskatiyas Group's mobile LCD products and specifications
lcd_products = [
    {
        "name": "LCD Model A",
        "scratch_resistance": 8,  # Scale: 1-10
        "light_detection": True,
        "resolution": "1080x1920"
    },
    {
        "name": "LCD Model B",
        "scratch_resistance": 9,
        "light_detection": False,
        "resolution": "1440x2560"
    },
    {
        "name": "LCD Model C",
        "scratch_resistance": 7,
        "light_detection": True,
        "resolution": "720x1280"
    },
    {
        "name": "LCD Model D",
        "scratch_resistance": 10,
        "light_detection": True,
        "resolution": "2160x3840"
    }
]

# Define a function to recommend LCDs based on user preferences
def recommend_lcds(scratch_resistance, light_detection, resolution):
    """
    Recommend mobile LCDs based on user preferences.

    Parameters:
    - scratch_resistance (int): Minimum scratch resistance (scale 1-10).
    - light_detection (bool): Whether light detection is required.
    - resolution (str): Minimum resolution in the format 'widthxheight'.

    Returns:
    - list: Recommended LCD products matching the criteria.
    """
    try:
        # Validate resolution format
        width, height = map(int, resolution.split('x'))
    except ValueError:
        raise ValueError("Resolution must be in the format 'widthxheight', e.g., '1080x1920'.")

    # Filter products based on user preferences
    recommended = []
    for product in lcd_products:
        product_width, product_height = map(int, product["resolution"].split('x'))

        # Check if all criteria are met
        if (
            product["scratch_resistance"] >= scratch_resistance and
            product["light_detection"] == light_detection and
            product_width >= width and
            product_height >= height
        ):
            recommended.append(product)

    return recommended

# Main script: Get user preferences and recommend LCDs
if __name__ == "__main__":
    try:
        print("Welcome to Maskatiyas Group Mobile LCD Recommender!")
        
        # Collect user preferences
        scratch_resistance = int(input("Enter minimum scratch resistance (1-10): "))
        light_detection = input("Is light detection required? (yes/no): ").strip().lower() == "yes"
        resolution = input("Enter minimum resolution (e.g., '1080x1920'): ").strip()

        # Recommend LCDs
        recommendations = recommend_lcds(scratch_resistance, light_detection, resolution)

        # Display recommendations
        if recommendations:
            print("\nRecommended LCDs:")
            print(json.dumps(recommendations, indent=4))
        else:
            print("\nNo LCDs match your preferences.")
    
    except Exception as e:
        print(f"Error: {e}")
```
