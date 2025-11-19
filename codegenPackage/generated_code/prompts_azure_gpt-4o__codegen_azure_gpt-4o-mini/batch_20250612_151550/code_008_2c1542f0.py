"""
Generated Code Metadata:
========================
Original URL: https://bitcoinqr.io
Prompt: Write a Python script to generate QR codes for Bitcoin addresses while ensuring privacy and security by avoiding the storage of logs or cookies, as emphasized by bitcoinqr.io.
Generated: DETERMINISTIC_2c1542f04bbf3069
Batch ID: 20250612_151550
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
import sys

def generate_qr_code(bitcoin_address, output_file):
    """
    Generates a QR code for the given Bitcoin address and saves it to the specified output file.

    Parameters:
    bitcoin_address (str): The Bitcoin address to encode in the QR code.
    output_file (str): The file path where the QR code image will be saved.

    Raises:
    ValueError: If the Bitcoin address is invalid.
    IOError: If there is an error saving the QR code image.
    """
    # Validate the Bitcoin address (basic validation)
    if not isinstance(bitcoin_address, str) or len(bitcoin_address) < 26 or len(bitcoin_address) > 35:
        raise ValueError("Invalid Bitcoin address.")

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the Bitcoin address to the QR code
    qr.add_data(bitcoin_address)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the specified output file
    try:
        img.save(output_file)
    except IOError as e:
        raise IOError(f"Error saving QR code image: {e}")

def main():
    """
    Main function to execute the QR code generation process.
    It reads the Bitcoin address from command line arguments and generates a QR code.
    """
    if len(sys.argv) != 3:
        print("Usage: python generate_qr.py <bitcoin_address> <output_file>")
        sys.exit(1)

    bitcoin_address = sys.argv[1]
    output_file = sys.argv[2]

    try:
        generate_qr_code(bitcoin_address, output_file)
        print(f"QR code generated successfully and saved to {output_file}")
    except (ValueError, IOError) as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### Usage
To run the script, use the following command in your terminal:
```bash
python generate_qr.py <bitcoin_address> <output_file>
```
Replace `<bitcoin_address>` with the actual Bitcoin address and `<output_file>` with the desired output file path (e.g., `qrcode.png`).
