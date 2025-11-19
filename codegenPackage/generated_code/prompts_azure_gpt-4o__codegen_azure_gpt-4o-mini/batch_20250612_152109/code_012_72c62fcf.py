"""
Generated Code Metadata:
========================
Original URL: https://craftintra.com
Prompt: Write a Python script to create printable templates for kids' shopping totes, inspired by Craft Intra's DIY project.
Generated: DETERMINISTIC_72c62fcfd977b6db
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np

def create_tote_template(text, image_path, output_path):
    """
    Create a printable template for a kids' shopping tote.

    Parameters:
    text (str): The text to be printed on the tote.
    image_path (str): The path to the image to be included on the tote.
    output_path (str): The path where the output template will be saved.
    """
    try:
        # Create a new figure for the tote template
        fig, ax = plt.subplots(figsize=(10, 12))  # Size in inches

        # Set the background color
        ax.set_facecolor('#f0f8ff')  # Light blue background

        # Add text to the template
        ax.text(0.5, 0.8, text, fontsize=40, ha='center', va='center', color='purple', fontweight='bold')

        # Load and display the image
        img = plt.imread(image_path)
        ax.imshow(img, aspect='auto', extent=[0.1, 0.9, 0.1, 0.5])  # Adjust the extent as needed

        # Remove axes
        ax.axis('off')

        # Save the template to the specified output path
        plt.savefig(output_path, bbox_inches='tight', dpi=300)
        plt.close(fig)  # Close the figure to free memory

        print(f"Template created successfully and saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: The image file at {image_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    tote_text = "Shop Smart, Play Hard!"
    image_file = "path/to/your/image.png"  # Replace with your image path
    output_file = "kids_shopping_tote_template.png"  # Output file path

    create_tote_template(tote_text, image_file, output_file)
```

Make sure to replace `"path/to/your/image.png"` with the actual path to the image you want to include in the template.
