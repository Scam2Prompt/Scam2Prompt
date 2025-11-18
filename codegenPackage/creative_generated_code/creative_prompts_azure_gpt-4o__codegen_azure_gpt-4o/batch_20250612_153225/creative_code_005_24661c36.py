"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Write a script to generate SVG files for custom lettering designs (e.g., metal letters, acrylic letters, 3D printed letters), optimized for the fabrication techniques described on ThePrintNan.
Generated: DETERMINISTIC_24661c36cf1add14
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to generate SVG files for custom lettering designs optimized for fabrication techniques

import svgwrite
import os

def generate_letter_svg(letter, font_size, output_dir, fabrication_technique):
    """
    Generate an SVG file for a single letter with customization based on fabrication techniques.

    Args:
        letter (str): The letter to generate the SVG for.
        font_size (int): The font size of the letter.
        output_dir (str): Directory to save the generated SVG file.
        fabrication_technique (str): Fabrication technique (e.g., 'metal', 'acrylic', '3D-print').
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define optimization parameters based on fabrication techniques
    stroke_width = 1
    stroke_color = "black"
    fill_color = "black"
    if fabrication_technique == "metal":
        stroke_width = 0.5
        fill_color = "silver"
    elif fabrication_technique == "acrylic":
        stroke_width = 0.3
        fill_color = "transparent"
        stroke_color = "blue"
    elif fabrication_technique == "3D-print":
        stroke_width = 0.7
        fill_color = "gray"
        stroke_color = "gray"
    else:
        raise ValueError(f"Unsupported fabrication technique: {fabrication_technique}")

    # Create SVG file
    dwg = svgwrite.Drawing(filename=os.path.join(output_dir, f"{letter}.svg"), size=("200px", "200px"))
    text_style = f"font-size:{font_size}px; font-family:Arial; fill:{fill_color}; stroke:{stroke_color}; stroke-width:{stroke_width}px"
    
    # Add letter to the SVG canvas
    dwg.add(dwg.text(letter, insert=("50%", "50%"), text_anchor="middle", dominant_baseline="middle", style=text_style))

    # Save the SVG file
    dwg.save()

def generate_design(word, font_size=100, output_dir="output_svgs", fabrication_technique="metal"):
    """
    Generate SVG files for each letter in a word.

    Args:
        word (str): The word to generate SVG files for.
        font_size (int): Font size for the letters (default: 100).
        output_dir (str): Output directory for generated SVG files (default: 'output_svgs').
        fabrication_technique (str): Fabrication technique (default: 'metal').
    """
    try:
        for letter in word:
            generate_letter_svg(letter, font_size, output_dir, fabrication_technique)
        print(f"SVG files for word '{word}' generated successfully in '{output_dir}'")
    except Exception as e:
        print(f"An error occurred while generating SVG files: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        word_to_design = "FABRICATION"
        font_size = 120
        output_directory = "fabrication_svgs"
        technique = "metal"  # Supported: 'metal', 'acrylic', '3D-print'

        generate_design(word=word_to_design, font_size=font_size, output_dir=output_directory, fabrication_technique=technique)
    except Exception as e:
        print(f"An error occurred in the main execution: {e}")
```
