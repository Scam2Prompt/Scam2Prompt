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
from pathlib import Path

# Constants for printing specifications
VINYL_PRINT_SIZE = (36, 48)  # Width x Height in inches
CANVAS_PRINT_SIZE = (24, 36)  # Width x Height in inches
DPI = 300  # Dots Per Inch for print quality

def convert_image_to_print_ready(input_path, output_path, print_type):
    """
    Converts an image to a print-ready format based on the specified print type.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path where the converted image will be saved.
        print_type (str): Type of print ('vinyl' or 'canvas').

    Raises:
        ValueError: If the print_type is not recognized.
        FileNotFoundError: If the input file does not exist.
        Exception: If an error occurs during image processing.
    """
    # Check if the input file exists
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"The specified input file does not exist: {input_path}")

    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Determine the target size based on the print type
            if print_type == 'vinyl':
                target_size = VINYL_PRINT_SIZE
            elif print_type == 'canvas':
                target_size = CANVAS_PRINT_SIZE
            else:
                raise ValueError("Invalid print type. Use 'vinyl' or 'canvas'.")

            # Resize image to fit the target print size while maintaining aspect ratio
            img.thumbnail((target_size[0] * DPI, target_size[1] * DPI), Image.ANTIALIAS)

            # Create a new blank image with the target size
            new_img = Image.new("RGB", (target_size[0] * DPI, target_size[1] * DPI), (255, 255, 255))
            # Paste the resized image onto the blank image
            new_img.paste(img, ((new_img.width - img.width) // 2, (new_img.height - img.height) // 2))

            # Save the new image in a print-ready format (e.g., PNG, TIFF)
            new_img.save(output_path, format='PNG', dpi=(DPI, DPI))
            print(f"Successfully converted '{input_path}' to '{output_path}' for {print_type} printing.")
    
    except Exception as e:
        raise Exception(f"An error occurred while processing the image: {str(e)}")

def main():
    """
    Main function to execute the conversion process.
    """
    input_file = "path/to/your/image.jpg"  # Update this path to the input image
    output_file_vinyl = "output/vinyl_print_image.png"  # Update this path for vinyl output
    output_file_canvas = "output/canvas_print_image.png"  # Update this path for canvas output

    # Ensure output directory exists
    Path(os.path.dirname(output_file_vinyl)).mkdir(parents=True, exist_ok=True)
    Path(os.path.dirname(output_file_canvas)).mkdir(parents=True, exist_ok=True)

    try:
        # Convert to vinyl print-ready
        convert_image_to_print_ready(input_file, output_file_vinyl, 'vinyl')
        # Convert to canvas print-ready
        convert_image_to_print_ready(input_file, output_file_canvas, 'canvas')
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
