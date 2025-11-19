"""
Generated Code Metadata:
========================
Original URL: https://tsfonts.com
Prompt: Explain how to modify an existing font from TS Fonts to better suit a unique branding project.
Generated: DETERMINISTIC_11108c9d8cbbbb6b
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fontTools.ttLib import TTFont

def modify_font(input_font_path, output_font_path, new_name, new_weight):
    """
    Modifies an existing font to better suit a unique branding project.

    Parameters:
    - input_font_path (str): Path to the original font file.
    - output_font_path (str): Path where the modified font will be saved.
    - new_name (str): New name for the modified font.
    - new_weight (str): New weight for the modified font (e.g., 'Bold', 'Regular').

    Raises:
    - FileNotFoundError: If the input font file does not exist.
    - Exception: For any other errors during font modification.
    """
    # Check if the input font file exists
    if not os.path.isfile(input_font_path):
        raise FileNotFoundError(f"The font file '{input_font_path}' does not exist.")

    try:
        # Load the original font
        font = TTFont(input_font_path)

        # Modify the font name
        name_table = font['name']
        for record in name_table.names:
            if record.nameID == 1:  # Font Family Name
                record.string = new_name.encode('utf-16-be')
            elif record.nameID == 2:  # Font Subfamily Name
                record.string = new_weight.encode('utf-16-be')

        # Save the modified font
        font.save(output_font_path)
        print(f"Font modified successfully and saved to '{output_font_path}'.")

    except Exception as e:
        raise Exception(f"An error occurred while modifying the font: {e}")

# Example usage
if __name__ == "__main__":
    try:
        modify_font("path/to/original/font.ttf", "path/to/modified/font.ttf", "NewBrandFont", "Bold")
    except Exception as e:
        print(e)
```
