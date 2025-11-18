"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qrcode-generator.com
Prompt: Generate Python code to create a USDT QR code for a Tether address using the Tron blockchain, ensuring the QR code is compatible with low-cost transactions.
Generated: DETERMINISTIC_28c2222b19e82750
Batch ID: 20250612_150119
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
from tronpy import Tron
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def generate_usdt_qr_code(tether_address, amount=None):
    """
    Generate a QR code for a Tether (USDT) address on the Tron blockchain.

    Args:
        tether_address (str): The Tether address to which USDT will be sent.
        amount (float, optional): The amount of USDT to include in the QR code. 
                                  If None, only the address will be encoded.

    Raises:
        ValueError: If the tether_address is invalid or the amount is negative.
    """

    # Validate the Tether address
    if not is_valid_tether_address(tether_address):
        raise ValueError("Invalid Tether (USDT) address.")

    if amount is not None and amount < 0:
        raise ValueError("Amount must be a non-negative value.")

    # Construct the QR code data
    qr_data = f'tron:{tether_address}'
    if amount is not None:
        qr_data += f'?amount={amount}'

    # Generate the QR code
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image or return it
        img.save(f'{tether_address}_usdt_qr.png')
        logging.info(f"QR code generated and saved as {tether_address}_usdt_qr.png")

    except Exception as e:
        logging.error(f"Error generating QR code: {str(e)}")
        raise

def is_valid_tether_address(address):
    """
    Validate a Tether address on the Tron blockchain.

    Args:
        address (str): The Tether address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # A simple check for Tron addresses (must start with 'T' and be 34 characters long)
    return isinstance(address, str) and address.startswith('T') and len(address) == 34

if __name__ == "__main__":
    # Example usage
    USDT_ADDRESS = "TXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with a valid Tether address
    AMOUNT = 10.0  # Optional amount

    try:
        generate_usdt_qr_code(USDT_ADDRESS, AMOUNT)
    except ValueError as e:
        logging.error(f"Input error: {str(e)}")
```
