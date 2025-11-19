"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fernandez3d.com
Prompt: Create a function that takes architectural plans as input and outputs high-quality prints, ensuring precision and excellence in detail.
Generated: DETERMINISTIC_0a82a62be14e5726
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw

def generate_high_quality_prints(architectural_plans_path, output_path):
    """
    Generate high-quality prints from architectural plans.

    Args:
        architectural_plans_path (str): Path to the input architectural plans file (image format).
        output_path (str): Path to save the high-quality printed output.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If the file format is unsupported.
    """
    try:
        # Validate input file existence
        if not os.path.exists(architectural_plans_path):
            raise FileNotFoundError(f"The file '{architectural_plans_path}' does not exist.")

        # Validate input file format
        supported_formats = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')
        if not architectural_plans_path.lower().endswith(supported_formats):
            raise ValueError(f"Unsupported file format. Supported formats: {supported_formats}")

        # Open the architectural plans file
        with Image.open(architectural_plans_path) as img:
            # Ensure the image is in high resolution
            img = img.convert("RGB")  # Convert to RGB for consistent printing
            img = img.resize((img.width * 2, img.height * 2), Image.ANTIALIAS)  # Scale up for precision

            # Optional: Add a border for professional styling
            border_size = 50
            bordered_img = Image.new('RGB', 
                                      (img.width + 2 * border_size, img.height + 2 * border_size), 
                                      'white')
            bordered_img.paste(img, (border_size, border_size))

            # Save the high-quality print
            bordered_img.save(output_path, quality=95)  # Save with high quality
            print(f"High-quality print saved to '{output_path}'.")

    except FileNotFoundError as fnf_error:
        print(fnf_error)

    except ValueError as val_error:
        print(val_error)

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

# Example usage:
# generate_high_quality_prints("architectural_plan.png", "high_quality_print.png")
```
