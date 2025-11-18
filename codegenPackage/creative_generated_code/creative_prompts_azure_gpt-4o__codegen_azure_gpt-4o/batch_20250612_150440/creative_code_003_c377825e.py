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

def create_qr_code(data: str, output_file: str) -> None:
    """
    Generates a static QR code for the provided data (e.g., cryptocurrency address).
    The QR code is saved as a PNG file.

    Args:
        data (str): The data to encode in the QR code (e.g., cryptocurrency address).
        output_file (str): The path to save the generated QR code image.

    Raises:
        ValueError: If the data or output_file is invalid.
        IOError: If there is an error while saving the QR code image.
    """
    if not data:
        raise ValueError("The data to encode in the QR code cannot be empty.")

    if not output_file.endswith(".png"):
        raise ValueError("The output file must have a .png extension.")

    try:
        # Create the QR code instance with default settings
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code (1 is the smallest, 40 is the largest)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code grid
            border=4,  # Thickness of the border (minimum is 4)
        )

        # Add the data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to the specified file
        img.save(output_file)
        print(f"QR code successfully generated and saved to: {output_file}")

    except IOError as e:
        raise IOError(f"Error saving QR code image: {e}")

if __name__ == "__main__":
    # Example usage:
    # Replace 'your_crypto_address' with the actual cryptocurrency address to encode.
    cryptocurrency_address = "your_crypto_address_here"  # Replace with actual address
    output_path = "crypto_qr_code.png"  # Path to save the QR code image

    try:
        create_qr_code(cryptocurrency_address, output_path)
    except Exception as e:
        print(f"An error occurred: {e}")
```
