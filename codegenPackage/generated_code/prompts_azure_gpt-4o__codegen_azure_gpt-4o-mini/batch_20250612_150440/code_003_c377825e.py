"""
Generated Code Metadata:
========================
Original URL: https://coin-qr.to
Prompt: Provide code to create static QR Codes for cryptocurrency addresses that do not expire, as described on the coin-qr.to website.
Generated: DETERMINISTIC_c377825e3362d324
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
import os

def create_qr_code(data, filename, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4):
    """
    Create a static QR code for the given data and save it as an image file.

    Parameters:
    - data (str): The data to encode in the QR code (e.g., cryptocurrency address).
    - filename (str): The filename to save the QR code image (should end with .png).
    - version (int): Version of the QR code (1 to 40, default is 1).
    - error_correction (int): Error correction level (L, M, Q, H), default is L.
    - box_size (int): Size of each box in the QR code, default is 10.
    - border (int): Thickness of the border (minimum is 4), default is 4.
    
    Raises:
    - ValueError: If the filename does not end with .png or if the data is empty.
    - Exception: For any other unexpected errors during QR code generation.
    """
    # Validate input parameters
    if not filename.endswith('.png'):
        raise ValueError("Filename must end with .png")
    if not data:
        raise ValueError("Data cannot be empty")

    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border,
        )
        
        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to the specified file
        img.save(filename)
        print(f"QR code saved as {filename}")

    except Exception as e:
        print(f"An error occurred while creating the QR code: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # Define the cryptocurrency address and output filename
        crypto_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Example Bitcoin address
        output_filename = "crypto_qr_code.png"

        # Create the QR code
        create_qr_code(crypto_address, output_filename)

    except Exception as e:
        print(f"An error occurred: {e}")
```
