"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinqr.io
Prompt: What are the steps to implement a QR code generation feature for Bitcoin transactions that includes error detection for Bech32 addresses?
Generated: DETERMINISTIC_d5c4dd14ddc25f57
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
import re
from typing import Tuple


def validate_bech32_address(address: str) -> Tuple[bool, str]:
    """
    Validate a Bech32 Bitcoin address.
    
    Args:
        address (str): Bitcoin address to validate.
    
    Returns:
        Tuple[bool, str]: A tuple containing a boolean indicating validity 
                          and an error message if invalid.
    """
    # Bech32 addresses start with "bc1" and are case-insensitive
    if not address.lower().startswith("bc1"):
        return False, "Address must start with 'bc1'."
    
    # Bech32 addresses can only contain alphanumeric characters excluding '1', 'b', 'i', 'o'
    if re.search(r"[^023456789acdefghjklmnpqrstuvwxyz]", address.lower()):
        return False, "Invalid character detected in address."
    
    # Bech32 addresses have a maximum length of 90 characters
    if len(address) > 90:
        return False, "Address length exceeds the maximum of 90 characters."
    
    return True, ""


def generate_qr_code(data: str, output_file: str) -> None:
    """
    Generate a QR code for the given data and save it to a file.
    
    Args:
        data (str): The data to encode in the QR code.
        output_file (str): The file path to save the QR code image.
    
    Raises:
        ValueError: If the provided data is empty.
    """
    if not data:
        raise ValueError("Data for QR code generation cannot be empty.")
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Border thickness (minimum is 4)
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create and save the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)


def main():
    """
    Main function to generate a QR code for a Bitcoin transaction.
    """
    # Example Bech32 Bitcoin address
    bitcoin_address = input("Enter a Bech32 Bitcoin address: ")

    # Validate the Bitcoin address
    is_valid, error_message = validate_bech32_address(bitcoin_address)
    if not is_valid:
        print(f"Invalid Bitcoin address: {error_message}")
        return

    # Generate QR code
    try:
        output_file = "bitcoin_transaction_qr.png"
        generate_qr_code(bitcoin_address, output_file)
        print(f"QR code saved successfully to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")


if __name__ == "__main__":
    main()
```
