"""
Generated Code Metadata:
========================
Original URL: https://olaf-schirm.de
Prompt: Generate a Python script that creates a barcode clock using the Code128 format as described in Olaf Schirm's "TIME Code128" artwork.
Generated: DETERMINISTIC_3ba500e17cd14bae
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import barcode
from barcode.writer import ImageWriter
from datetime import datetime
import os

def generate_barcode_clock(output_dir="barcodes"):
    """
    Generates a barcode clock using Code128 format. The barcode represents the current time in HHMMSS format.
    The barcode image is saved in the specified output directory.

    Args:
        output_dir (str): Directory where barcode images will be saved. Defaults to "barcodes".
    """
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        while True:
            # Get the current time in HHMMSS format
            current_time = datetime.now().strftime("%H%M%S")

            # Generate the barcode using Code128 format
            code128 = barcode.get('code128', current_time, writer=ImageWriter())

            # Define the output file path
            file_path = os.path.join(output_dir, f"barcode_{current_time}.png")

            # Save the barcode image
            code128.save(file_path)

            print(f"Generated barcode for time {current_time} at {file_path}")

            # Wait for 1 second before generating the next barcode
            time.sleep(1)

    except KeyboardInterrupt:
        # Gracefully handle script termination
        print("\nBarcode clock stopped by user.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Run the barcode clock generator
    generate_barcode_clock()
```
