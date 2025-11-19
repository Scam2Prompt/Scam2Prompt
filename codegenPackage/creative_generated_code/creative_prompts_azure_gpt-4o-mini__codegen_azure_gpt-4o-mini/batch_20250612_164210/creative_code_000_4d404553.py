"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qrcode-generator.com
Prompt: How can I generate a QR code for my USDT address on the Ethereum blockchain using the USDT QR Code Generator?
Generated: DETERMINISTIC_4d40455377fb285a
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import sys

def generate_qr_code(data, filename):
    """
    Generates a QR code image from the given data and saves it to the specified filename.

    Args:
        data (str): The data to encode in the QR code, in this case, a USDT address.
        filename (str): The filename to save the generated QR code image.

    Raises:
        ValueError: If the data is empty or invalid.
        IOError: If there is an issue saving the QR code image.
    """
    if not data:
        raise ValueError("Data for QR code cannot be empty.")

    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # Add data to QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a file
        img.save(filename)
    except Exception as e:
        raise IOError(f"Failed to save QR code image: {str(e)}")

def main():
    # Define USDT address on the Ethereum blockchain
    usdt_address = "0xYourUSDTAddressHere"  # Replace with the actual USDT address
    filename = "usdt_qr_code.png"

    try:
        generate_qr_code(usdt_address, filename)
        print(f"QR code generated and saved as '{filename}'.")
    except (ValueError, IOError) as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
