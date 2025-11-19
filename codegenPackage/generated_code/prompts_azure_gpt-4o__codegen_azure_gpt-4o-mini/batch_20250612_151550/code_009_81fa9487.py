"""
Generated Code Metadata:
========================
Original URL: https://bitcoinqr.io
Prompt: Create a Python program that generates a Bitcoin QR code for Legacy addresses and explains the significance of Pay-to-Public-Key-Hash (P2PKH) scripts in the process.
Generated: DETERMINISTIC_81fa948795d3b90c
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

def generate_bitcoin_qr(address: str, filename: str) -> None:
    """
    Generates a QR code for a given Bitcoin address and saves it as an image file.

    Parameters:
    address (str): The Bitcoin address to encode in the QR code.
    filename (str): The filename (with extension) to save the QR code image.

    Raises:
    ValueError: If the address is not a valid Bitcoin address.
    IOError: If there is an error saving the QR code image.
    """
    # Validate the Bitcoin address (basic validation)
    if not is_valid_bitcoin_address(address):
        raise ValueError("Invalid Bitcoin address provided.")

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the Bitcoin address to the QR code
    qr.add_data(address)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    try:
        img.save(filename)
    except IOError as e:
        raise IOError(f"Error saving QR code image: {e}")

def is_valid_bitcoin_address(address: str) -> bool:
    """
    Validates a Bitcoin address (basic validation).

    Parameters:
    address (str): The Bitcoin address to validate.

    Returns:
    bool: True if the address is valid, False otherwise.
    """
    # Basic validation for Bitcoin addresses (P2PKH)
    if len(address) == 34 and (address.startswith('1') or address.startswith('3')):
        return True
    return False

if __name__ == "__main__":
    # Example Bitcoin address (P2PKH)
    bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Replace with a valid address
    output_filename = "bitcoin_qr_code.png"

    try:
        generate_bitcoin_qr(bitcoin_address, output_filename)
        print(f"QR code generated and saved as {output_filename}")
    except (ValueError, IOError) as e:
        print(f"An error occurred: {e}")

# Significance of Pay-to-Public-Key-Hash (P2PKH):
# P2PKH is a type of Bitcoin transaction that allows users to send Bitcoin to a public key hash.
# This is the most common type of Bitcoin address, starting with '1'. 
# It ensures that only the owner of the private key corresponding to the public key can spend the funds.
# The QR code generated in this program encodes the P2PKH address, making it easy to share and receive Bitcoin.
```
