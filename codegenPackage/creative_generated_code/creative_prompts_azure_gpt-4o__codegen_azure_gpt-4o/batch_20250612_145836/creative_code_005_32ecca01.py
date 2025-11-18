"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Create a Python script to generate edible printing product labels dynamically based on customer input, such as name and design preferences.
Generated: DETERMINISTIC_32ecca019468008a
Batch ID: 20250612_145836
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

def create_label(customer_name, design_preference, output_folder="labels"):
    """
    Generates a printable label with customer name and design preferences.
    
    Args:
        customer_name (str): Name of the customer to appear on the label.
        design_preference (str): Design preference for the label (e.g., 'floral', 'modern').
        output_folder (str): Directory to save the generated label image. Defaults to 'labels'.

    Returns:
        str: File path of the generated label.
    """
    try:
        # Validate input
        if not customer_name.strip():
            raise ValueError("Customer name cannot be empty.")
        if not design_preference.strip():
            raise ValueError("Design preference cannot be empty.")

        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Set label dimensions and colors
        label_width, label_height = 500, 300
        background_color = (255, 255, 255)  # White background
        text_color = (0, 0, 0)  # Black text

        # Initialize the image
        label_image = Image.new("RGB", (label_width, label_height), background_color)
        draw = ImageDraw.Draw(label_image)

        # Load a font (adjust path if necessary)
        try:
            font = ImageFont.truetype("arial.ttf", size=30)
        except IOError:
            raise FileNotFoundError("Font file 'arial.ttf' not found. Ensure the font file is available.")

        # Add customer name to the label
        text = f"Customer: {customer_name}"
        text_width, text_height = draw.textsize(text, font=font)
        text_position = ((label_width - text_width) // 2, (label_height - text_height) // 4)
        draw.text(text_position, text, fill=text_color, font=font)

        # Add design preference
        design_text = f"Design: {design_preference}"
        design_text_width, design_text_height = draw.textsize(design_text, font=font)
        design_text_position = ((label_width - design_text_width) // 2, (label_height - design_text_height) * 3 // 4)
        draw.text(design_text_position, design_text, fill=text_color, font=font)

        # Save the label
        label_path = os.path.join(output_folder, f"{customer_name}_label.png")
        label_image.save(label_path)
        
        return label_path

    except Exception as e:
        # Log error and re-raise
        print(f"Error generating label: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        customer_name = input("Enter customer name: ").strip()
        design_preference = input("Enter design preference (e.g., floral, modern): ").strip()
        output_path = create_label(customer_name, design_preference)
        print(f"Label successfully generated at: {output_path}")
    except Exception as e:
        print(f"Failed to generate label: {e}")
```
