"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinqr.io
Prompt: Provide code in Python that generates QR codes for multiple Bitcoin address formats (Legacy, Script, Bech32, and Taproot) and includes error detection for input validation.
Generated: DETERMINISTIC_8bf5d35f3d401daf
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
import re

# Define a function to validate Bitcoin addresses
def is_valid_bitcoin_address(address):
    """
    Validate Bitcoin addresses for different formats.
    
    Args:
        address (str): The Bitcoin address to validate.
    
    Returns:
        bool: True if the address is valid, False otherwise.
    """
    # Regular expressions for each Bitcoin address format
    legacy_regex = re.compile(r'^[1][A-HJ-NP-Za-km-z1-9]{25,34}$')  # Legacy addresses (starts with 1)
    script_regex = re.compile(r'^[3][A-HJ-NP-Za-km-z1-9]{25,34}$')  # Script addresses (starts with 3)
    bech32_regex = re.compile(r'^[bc][1-9A-HJ-NP-Za-km-z]{25,39}$')   # Bech32 addresses (starts with bc)
    taproot_regex = re.compile(r'^[tb][1-9A-HJ-NP-Za-km-z]{39}$')    # Taproot addresses (starts with tb)
    
    return (legacy_regex.match(address) or 
            script_regex.match(address) or 
            bech32_regex.match(address) or 
            taproot_regex.match(address))

# Define a function to generate QR code from Bitcoin address
def generate_qr_code(address):
    """
    Generate a QR code image from a valid Bitcoin address.
    
    Args:
        address (str): The Bitcoin address to convert into a QR code.
    
    Returns:
        PIL.Image.Image: QR code image.
    """
    # Generate QR Code
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
    return img

def main():
    """
    Main function to execute the QR code generation for multiple Bitcoin addresses.
    """
    # List of Bitcoin addresses to generate QR codes for
    bitcoin_addresses = [
        "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",  # Legacy
        "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy",  # Script
        "bc1qw4xj0gk6ya7j2m56l8z7t4k3k5xwzqk9f8xryh",  # Bech32
        "tb1q9wug0f0q3pt7c5v5u9a8uk9n77k28dj6f6m0w9",  # Taproot
    ]

    for address in bitcoin_addresses:
        if is_valid_bitcoin_address(address):
            try:
                # Generate QR code
                qr_image = generate_qr_code(address)
                # Save the image with the address as the filename
                qr_image.save(f"{address}.png")
                print(f"QR code generated and saved for address: {address}")
            except Exception as e:
                print(f"Error generating QR code for address {address}: {e}")
        else:
            print(f"Invalid Bitcoin address: {address}")

if __name__ == "__main__":
    main()
```
