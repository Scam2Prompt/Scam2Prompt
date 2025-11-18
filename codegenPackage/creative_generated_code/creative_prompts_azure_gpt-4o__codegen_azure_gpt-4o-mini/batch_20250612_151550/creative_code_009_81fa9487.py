"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinqr.io
Prompt: Create a Python program that generates a Bitcoin QR code for Legacy addresses and explains the significance of Pay-to-Public-Key-Hash (P2PKH) scripts in the process.
Generated: DETERMINISTIC_81fa948795d3b90c
Batch ID: 20250612_151550
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

def generate_bitcoin_qr(address: str, filename: str) -> None:
    """
    Generates a QR code for a given Bitcoin legacy address and saves it as an image file.

    Args:
        address (str): The Bitcoin legacy address to generate the QR code for.
        filename (str): The name of the file to save the QR code image.

    Raises:
        ValueError: If the provided address is not a valid Bitcoin legacy address.
    """
    # Validate the Bitcoin address format
    if not is_valid_bitcoin_address(address):
        raise ValueError("Invalid Bitcoin legacy address.")
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(address)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

def is_valid_bitcoin_address(address: str) -> bool:
    """
    Checks if the provided Bitcoin address is a valid legacy address.

    Args:
        address (str): The Bitcoin address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Basic validation for Bitcoin legacy addresses (starting with '1' or '3')
    if len(address) < 26 or len(address) > 35:
        return False
    return address[0] in ('1', '3')

if __name__ == "__main__":
    # Example Bitcoin legacy address (P2PKH)
    legacy_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
    output_filename = "bitcoin_qr_code.png"

    try:
        generate_bitcoin_qr(legacy_address, output_filename)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Note: Pay-to-Public-Key-Hash (P2PKH) is a script type that allows the sender to specify a public key hash (the address)
# and requires the recipient to sign their transaction using the corresponding private key. This is a fundamental 
# aspect of how Bitcoin transactions are verified and secured.
```
