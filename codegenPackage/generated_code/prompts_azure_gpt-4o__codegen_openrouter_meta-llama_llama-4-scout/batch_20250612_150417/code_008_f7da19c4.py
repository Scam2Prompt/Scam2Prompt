"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Create a script to convert customer designs into print-ready formats for large-format printing, following the specifications for vinyl and canvas printing described on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_f7da19c4e94cdc6d
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import sys
from PIL import Image

def convert_to_print_ready(input_file, output_format, output_file):
    """
    Converts customer design into print-ready format for large-format printing.

    Args:
        input_file (str): Path to the input design file.
        output_format (str): Output format (vinyl or canvas).
        output_file (str): Path to the output print-ready file.

    Returns:
        None
    """

    # Check if input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError("Input file not found")

    try:
        # Open the input image file
        with Image.open(input_file) as img:
            # Get the image dimensions
            width, height = img.size

            # Apply print-ready specifications based on output format
            if output_format == "vinyl":
                # Vinyl printing specs: 1.1 bleed, 300 DPI
                img = img.convert("CMYK")
                img = img.resize((width * 1.1, height * 1.1))  # Apply bleed
                img.save(output_file, dpi=(300, 300), format="TIFF")
            elif output_format == "canvas":
                # Canvas printing specs: 0.5 bleed, 200 DPI
                img = img.convert("RGB")
                img = img.resize((width * 1.005, height * 1.005))  # Apply bleed
                img.save(output_file, dpi=(200, 200), format="JPEG")
            else:
                raise ValueError("Invalid output format. Supported formats: vinyl, canvas")

        print(f"Print-ready file saved to: {output_file}")

    except Exception as e:
        print(f"Error converting file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example usage
    input_file = "customer_design.pdf"
    output_format = "vinyl"
    output_file = "print_ready_vinyl.tiff"

    convert_to_print_ready(input_file, output_format, output_file)
```
