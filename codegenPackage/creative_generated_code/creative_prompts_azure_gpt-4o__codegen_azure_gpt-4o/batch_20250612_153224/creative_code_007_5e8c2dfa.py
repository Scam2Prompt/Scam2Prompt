"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://printserves.com
Prompt: Create a program that generates branded packaging designs (e.g., paper cups and gift wraps) based on user input and prepares the files for upload to Printserves Nigeria.
Generated: DETERMINISTIC_5e8c2dfad2a20a2a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont

def generate_design(template_type, brand_name, output_folder):
    """
    Generates a branded packaging design based on user input.
    
    Parameters:
        template_type (str): Type of packaging (e.g., 'paper_cup', 'gift_wrap').
        brand_name (str): Name of the brand to include in the design.
        output_folder (str): Folder where generated files will be saved.
    
    Raises:
        ValueError: If template_type is invalid.
        FileNotFoundError: If output_folder does not exist.
    """
    # Validate output folder
    if not os.path.exists(output_folder):
        raise FileNotFoundError(f"Output folder '{output_folder}' does not exist.")
    
    # Validate template type
    supported_templates = ['paper_cup', 'gift_wrap']
    if template_type not in supported_templates:
        raise ValueError(f"Unsupported template type '{template_type}'. Supported types are: {supported_templates}")
    
    # Set design dimensions and other parameters based on template type
    if template_type == 'paper_cup':
        width, height = 400, 300  # Dimensions in pixels
        base_color = (255, 255, 255)  # White background
    elif template_type == 'gift_wrap':
        width, height = 800, 800  # Dimensions in pixels
        base_color = (240, 240, 240)  # Light gray background
    
    # Create a blank image with the specified dimensions and background color
    design = Image.new('RGB', (width, height), base_color)
    draw = ImageDraw.Draw(design)
    
    # Add the brand name to the design
    try:
        font = ImageFont.truetype("arial.ttf", 40)  # Use a predefined font size
    except IOError:
        # Use default font if the specified font is not available
        font = ImageFont.load_default()
    
    text = f"{brand_name}"
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)  # Black text
    
    # Generate filename and save the design
    output_path = os.path.join(output_folder, f"{template_type}_{brand_name}.png")
    design.save(output_path)
    
    print(f"Design successfully generated: {output_path}")

def main():
    """
    Main function to interact with the user and generate branded designs.
    """
    print("Welcome to the branded packaging design generator!")
    try:
        # Gather user input
        template_type = input("Enter template type ('paper_cup' or 'gift_wrap'): ").strip().lower()
        brand_name = input("Enter the brand name: ").strip()
        output_folder = input("Enter the output folder path: ").strip()
        
        # Generate the design
        generate_design(template_type, brand_name, output_folder)
    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
