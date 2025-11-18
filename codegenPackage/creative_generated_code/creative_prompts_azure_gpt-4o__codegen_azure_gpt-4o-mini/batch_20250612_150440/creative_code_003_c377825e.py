"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qr.to
Prompt: Provide code to create static QR Codes for cryptocurrency addresses that do not expire, as described on the coin-qr.to website.
Generated: DETERMINISTIC_c377825e3362d324
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import os

def generate_qr_code(data: str, file_path: str, image_format: str = 'PNG') -> None:
    """
    Generates a static QR code for a given data string and saves it to the specified file path.

    Parameters:
        data (str): The data to encode in the QR code (e.g., a cryptocurrency address).
        file_path (str): The file path where the QR code image will be saved.
        image_format (str): The format of the saved image (default is 'PNG').

    Raises:
        ValueError: If the data is empty or if the provided image format is not supported.
        IOError: If there is an issue saving the QR code image to the file system.
    """
    # Validate input data
    if not data:
        raise ValueError("Data to encode in QR code must not be empty.")
    
    # Validate image format
    if image_format.upper() not in ['PNG', 'JPEG', 'BMP', 'GIF']:
        raise ValueError(f"Unsupported image format: {image_format}. Please use PNG, JPEG, BMP, or GIF.")

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border (minimum is 4)
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the specified file path
    try:
        img.save(file_path, format=image_format)
    except IOError as e:
        raise IOError(f"Failed to save QR code image: {e}")

def main():
    """
    Main function to generate a QR code for a cryptocurrency address.
    This can be modified to take user input or read from a config.
    """
    # Example cryptocurrency address (replace with actual address)
    crypto_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Bitcoin address
    output_file = "crypto_address_qr.png"  # File name for output QR code image

    try:
        generate_qr_code(crypto_address, output_file)
        print(f"QR code generated successfully and saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
