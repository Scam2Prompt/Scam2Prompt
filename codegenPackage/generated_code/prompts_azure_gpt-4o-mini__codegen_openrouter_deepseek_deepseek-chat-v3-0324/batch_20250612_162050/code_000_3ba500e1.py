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
import barcode
from barcode.writer import ImageWriter
from datetime import datetime
import time
import os

def generate_barcode_clock(output_dir="barcode_clocks"):
    """
    Generates a barcode clock using Code128 format with the current time.
    The barcode is saved as a PNG image in the specified directory.
    
    Args:
        output_dir (str): Directory to save the barcode images. Defaults to "barcode_clocks".
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        while True:
            # Get current time in HH:MM:SS format
            current_time = datetime.now().strftime("%H:%M:%S")
            
            # Generate barcode
            code128 = barcode.get_barcode_class('code128')
            barcode_instance = code128(current_time, writer=ImageWriter())
            
            # Save barcode with timestamp as filename
            filename = f"barcode_clock_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            filepath = os.path.join(output_dir, filename)
            barcode_instance.save(filepath)
            
            print(f"Generated barcode clock: {current_time} - Saved to {filepath}.png")
            
            # Wait for 1 second before generating the next barcode
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nBarcode clock generation stopped by user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    generate_barcode_clock()
```
