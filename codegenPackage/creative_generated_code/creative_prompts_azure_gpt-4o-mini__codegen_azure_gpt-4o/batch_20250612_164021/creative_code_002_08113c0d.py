"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Create a code snippet for a digital illustration project that incorporates elements of color theory, as taught in the painting courses at Ânima.
Generated: DETERMINISTIC_08113c0d965175f2
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import colorsys
import random

# Function to generate a harmonious color palette
def generate_color_palette(base_color, harmony_type="analogous", num_colors=5):
    """
    Generate a harmonious color palette based on the given base color and color theory principles.
    
    Parameters:
        base_color (tuple): The base color as an RGB tuple (R, G, B), values in range 0–255.
        harmony_type (str): Type of color harmony to apply. Options: 'analogous', 'complementary', or 'triadic'.
        num_colors (int): Number of colors to generate in the palette.
        
    Returns:
        List[Tuple]: A list of RGB tuples representing the harmonious color palette.
    """
    try:
        # Validate input
        if not isinstance(base_color, tuple) or len(base_color) != 3 or not all(0 <= c <= 255 for c in base_color):
            raise ValueError("base_color must be a tuple of three integers in the range 0–255.")
        
        if harmony_type not in ("analogous", "complementary", "triadic"):
            raise ValueError("harmony_type must be one of 'analogous', 'complementary', or 'triadic'.")
        
        if num_colors <= 0:
            raise ValueError("num_colors must be a positive integer.")
        
        # Convert base color to HLS (Hue, Lightness, Saturation)
        base_color_hls = colorsys.rgb_to_hls(base_color[0] / 255, base_color[1] / 255, base_color[2] / 255)
        hue, lightness, saturation = base_color_hls
        
        palette = []
        for i in range(num_colors):
            if harmony_type == "analogous":
                # Analogous colors are adjacent on the color wheel
                offset = (i - num_colors // 2) * 0.1  # Adjust hue offset
                new_hue = (hue + offset) % 1  # Ensure hue stays within [0, 1]
            elif harmony_type == "complementary":
                # Complementary colors are opposite on the color wheel
                new_hue = (hue + 0.5) % 1  # Shift hue by 180 degrees (0.5 in HLS space)
            elif harmony_type == "triadic":
                # Triadic colors are evenly spaced around the color wheel
                offset = (i * 0.333) % 1  # Divide the hue space into thirds
                new_hue = (hue + offset) % 1
            
            # Convert HLS back to RGB
            new_color_rgb = colorsys.hls_to_rgb(new_hue, lightness, saturation)
            # Scale RGB values back to 0–255
            palette.append(tuple(int(c * 255) for c in new_color_rgb))
        
        return palette
    except Exception as e:
        print(f"Error generating color palette: {e}")
        return []

# Function to display the color palette
def display_palette(palette):
    """
    Display the color palette in a user-friendly way.
    
    Parameters:
        palette (List[Tuple]): A list of RGB tuples representing the colors.
    """
    try:
        if not palette:
            raise ValueError("Palette is empty or invalid.")
        
        print("Generated Color Palette:")
        for i, color in enumerate(palette, start=1):
            print(f"Color {i}: RGB{color}")
    except Exception as e:
        print(f"Error displaying palette: {e}")

# Example usage
if __name__ == "__main__":
    # Base color (a shade of blue)
    base_color = (60, 120, 200)
    
    # Generate a palette with 'analogous' harmony
    palette = generate_color_palette(base_color, harmony_type="analogous", num_colors=5)
    
    # Display the generated palette
    display_palette(palette)
```
