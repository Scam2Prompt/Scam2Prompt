"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qr.to
Prompt: Write Python code to generate a Bitcoin QR Code using a static Bitcoin address, referencing the functionality described on the "Bitcoin QR Code Generator" website.
Generated: DETERMINISTIC_89fcceb3dea2b494
Batch ID: 20250612_150440
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

def generate_bitcoin_qr(address: str, filename: str = 'bitcoin_qr.png'):
    """
    Generate a QR code for a given Bitcoin address and save it as an image file.
    
    Args:
        address (str): The Bitcoin address to encode in the QR code.
        filename (str): The filename to save the generated QR code image.
        
    Raises:
        ValueError: If the Bitcoin address is invalid.
        Exception: If there is an issue saving the QR code image.
    """
    
    # Validate the Bitcoin address
    if not is_valid_bitcoin_address(address):
        raise ValueError("Invalid Bitcoin address provided.")
    
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Thickness of the border (minimum is 4)
    )
    
    # Add the Bitcoin URI to the QR code
    qr.add_data(f'bitcoin:{address}')
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    try:
        img.save(filename)
        print(f"QR code generated and saved as '{filename}'")
    except Exception as e:
        raise Exception(f"Failed to save QR code image: {e}")

def is_valid_bitcoin_address(address: str) -> bool:
    """
    Validate a Bitcoin address format.
    
    Args:
        address (str): The Bitcoin address to validate.
        
    Returns:
        bool: True if the address is valid, False otherwise.
    """
    # Basic validation for a Bitcoin address (length and prefix checks)
    if len(address) not in [26, 34]:
        return False
    if not (address.startswith('1') or address.startswith('3') or address.startswith('bc1')):
        return False
    return True

if __name__ == "__main__":
    # Static Bitcoin address for demonstration
    bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Example Bitcoin address
    output_filename = "bitcoin_qr.png"
    
    try:
        generate_bitcoin_qr(bitcoin_address, output_filename)
    except Exception as e:
        print(f"Error: {e}")
```
