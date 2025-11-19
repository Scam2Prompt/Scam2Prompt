"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinqr.io
Prompt: How can I generate a QR code for a Bitcoin payment using different address formats like Legacy, SegWit, and Bech32?
Generated: DETERMINISTIC_422aad384d803a11
Batch ID: 20250612_135517
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

def generate_qr_code(address, filename='bitcoin_qr.png'):
    """
    Generate a QR code from the given Bitcoin address and save it to a file.

    Parameters:
        address (str): The Bitcoin address to encode in the QR code.
        filename (str): The filename where the QR code image will be saved.
    """
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,  # controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
            box_size=10,  # controls how many pixels each “box” of the QR code is
            border=4,  # controls how many boxes thick the border should be
        )
        
        # Add the Bitcoin address to the QR code
        qr.add_data(address)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a file
        img.save(filename)
        print(f"QR code generated and saved as {filename}")

    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}", file=sys.stderr)

def main():
    """
    Main function to generate QR codes for different Bitcoin address formats.
    """
    # Example Bitcoin addresses
    addresses = {
        'Legacy': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
        'SegWit': '3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy',
        'Bech32': 'bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kp6q7',
    }

    # Generate QR codes for each address type
    for format_name, address in addresses.items():
        filename = f'bitcoin_qr_{format_name.lower()}.png'
        generate_qr_code(address, filename)

if __name__ == "__main__":
    main()
```
Make sure you have the required library installed. You can install it using:
```bash
pip install qrcode[pil]
```
