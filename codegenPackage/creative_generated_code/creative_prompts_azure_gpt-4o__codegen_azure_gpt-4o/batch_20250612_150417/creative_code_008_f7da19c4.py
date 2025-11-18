"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Create a script to convert customer designs into print-ready formats for large-format printing, following the specifications for vinyl and canvas printing described on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_f7da19c4e94cdc6d
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image

def convert_to_print_ready(input_file, output_dir, material_type):
    """
    Converts a customer design into a print-ready format based on the specified material type.

    Args:
        input_file (str): Path to the input design file.
        output_dir (str): Path to the directory where the output file will be saved.
        material_type (str): The type of material ("vinyl" or "canvas").

    Raises:
        ValueError: If an unsupported material type is provided.
        FileNotFoundError: If the input file does not exist.
    """
    # Validate material type
    if material_type.lower() not in ['vinyl', 'canvas']:
        raise ValueError("Unsupported material type. Use 'vinyl' or 'canvas'.")

    # Ensure the input file exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

    # Create output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # Define specifications for vinyl and canvas
    specifications = {
        'vinyl': {"dpi": 300, "color_mode": "CMYK", "max_size": (15000, 15000)},  # max size in pixels
        'canvas': {"dpi": 150, "color_mode": "RGB", "max_size": (12000, 12000)}
    }

    spec = specifications[material_type.lower()]

    try:
        # Open the input image
        with Image.open(input_file) as img:
            # Convert color mode
            if spec["color_mode"] != img.mode:
                img = img.convert(spec["color_mode"])

            # Resize if necessary
            img.thumbnail(spec["max_size"], Image.ANTIALIAS)

            # Prepare output file path and save
            output_file = os.path.join(
                output_dir,
                f"{os.path.splitext(os.path.basename(input_file))[0]}_{material_type}_print_ready.tif"
            )
            img.save(output_file, dpi=(spec["dpi"], spec["dpi"]), format="TIFF")
            print(f"File successfully converted and saved to: {output_file}")
    except Exception as e:
        print(f"An error occurred during the conversion process: {e}")
        raise


if __name__ == '__main__':
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert design files into print-ready formats.")
    parser.add_argument('input_file', type=str, help='Path to the input design file (e.g., .jpg, .png).')
    parser.add_argument('output_dir', type=str, help='Directory to save the print-ready file.')
    parser.add_argument('material_type', type=str, help='Material type for printing ("vinyl" or "canvas").')

    args = parser.parse_args()

    # Run the conversion process
    try:
        convert_to_print_ready(args.input_file, args.output_dir, args.material_type)
    except Exception as e:
        print(f"Error: {e}")
```
