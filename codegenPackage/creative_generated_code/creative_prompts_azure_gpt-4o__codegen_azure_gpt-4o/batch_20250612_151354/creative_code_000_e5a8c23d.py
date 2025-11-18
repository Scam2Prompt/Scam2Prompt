"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Write Python code to generate a QR code for certification purposes, ensuring compliance with SERVIR-141-2016 as described on the Enacip website.
Generated: DETERMINISTIC_e5a8c23d9531de30
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from qrcode.constants import ERROR_CORRECT_H
import os

def generate_qr_code(data, output_file):
    """
    Generates a QR code based on the specified data and saves it to a file.

    Parameters:
    - data (str): The information to encode in the QR code.
    - output_file (str): The file path to save the generated QR code image.

    Returns:
    - None

    Raises:
    - ValueError: If the provided data is empty or invalid.
    - IOError: If an error occurs while saving the file.
    """
    try:
        # Validate input data
        if not data or not isinstance(data, str):
            raise ValueError("The data to encode must be a non-empty string.")
        
        # Create a QR code object with high error correction level
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code (1 is the smallest)
            error_correction=ERROR_CORRECT_H,  # High error correction level (up to 30%)
            box_size=10,  # Size of each box in the QR code grid
            border=4  # Minimum border size around the QR code
        )
        
        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)  # Automatically adjust size to fit the data
        
        # Generate the QR code image
        image = qr.make_image(fill_color="black", back_color="white")
        
        # Save the QR code image to the specified output file
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)  # Create directories if they don't exist
        
        image.save(output_file)
        print(f"QR code successfully saved to {output_file}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except IOError as io_err:
        print(f"Error saving file: {io_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    certification_data = "Certification ID: SERVIR-141-2016\nIssued by: Enacip\nValid until: 2023-12-31"
    output_path = "output/certification_qr_code.png"
    
    generate_qr_code(certification_data, output_path)
```
