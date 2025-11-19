"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Write a Python script to generate customized labels for identifying children's school effects, using a template with name and ID fields.
Generated: DETERMINISTIC_ce1f81e82c6824ab
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image, ImageDraw, ImageFont

def generate_label(name, student_id, output_dir="labels", template_path="label_template.png"):
    """
    Generates a customized label for identifying children's school effects.

    Args:
        name (str): The name of the child.
        student_id (str): The ID of the child.
        output_dir (str): Directory to save the generated labels. Defaults to 'labels'.
        template_path (str): Path to the label template image. Defaults to 'label_template.png'.

    Returns:
        str: Path to the generated label image.
    """
    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Load the label template
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template file '{template_path}' not found.")
        template = Image.open(template_path)

        # Create a drawing context
        draw = ImageDraw.Draw(template)

        # Define font and text positions
        font_path = "arial.ttf"  # Replace with the path to your font file
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file '{font_path}' not found.")
        font = ImageFont.truetype(font_path, size=40)

        name_position = (50, 50)  # Adjust based on your template
        id_position = (50, 120)   # Adjust based on your template

        # Add text to the template
        draw.text(name_position, f"Name: {name}", fill="black", font=font)
        draw.text(id_position, f"ID: {student_id}", fill="black", font=font)

        # Save the generated label
        output_path = os.path.join(output_dir, f"{name}_{student_id}.png")
        template.save(output_path)

        return output_path

    except Exception as e:
        print(f"Error generating label: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    name = input("Enter the child's name: ").strip()
    student_id = input("Enter the child's ID: ").strip()

    label_path = generate_label(name, student_id)
    if label_path:
        print(f"Label successfully generated: {label_path}")
    else:
        print("Failed to generate label.")
```
