"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qrs.to
Prompt: How can I use a Bitcoin QR Code generator to create a scannable code for my Bitcoin address?
Generated: DETERMINISTIC_1d72e50b32fd8eed
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from PIL import Image

def generate_bitcoin_qr_code(bitcoin_address: str, filename: str = 'bitcoin_qr_code.png') -> None:
    """
    Generates a scannable QR code for a given Bitcoin address.

    Parameters:
        bitcoin_address (str): The Bitcoin address to encode in the QR code.
        filename (str): The name of the file where the QR code image will be saved.

    Raises:
        ValueError: If the Bitcoin address is invalid.
    """
    # Basic validation for Bitcoin address
    if not isinstance(bitcoin_address, str) or len(bitcoin_address) < 26 or len(bitcoin_address) > 35:
        raise ValueError("Invalid Bitcoin address.")

    # Generate the QR code
    try:
        # Create a QR code instance and add the Bitcoin address to it
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(bitcoin_address)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to the specified filename
        img.save(filename)
        print(f"QR code generated and saved as {filename}")

    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Replace with your own Bitcoin address
        my_bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
        generate_bitcoin_qr_code(my_bitcoin_address)
    except Exception as e:
        print(f"Error: {e}")
```
