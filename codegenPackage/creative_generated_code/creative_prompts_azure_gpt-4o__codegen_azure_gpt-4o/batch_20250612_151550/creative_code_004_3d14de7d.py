"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinqr.io
Prompt: Create a Python function that generates a QR code for a Bitcoin transaction, including both the recipient's address and the payment amount, using the technical details from bitcoinqr.io.
Generated: DETERMINISTIC_3d14de7d3c86cccb
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

def generate_bitcoin_qr(recipient_address: str, amount: float, output_file: str = "bitcoin_qr.png"):
    """
    Generate a QR code for a Bitcoin transaction.
    
    Args:
        recipient_address (str): The Bitcoin address of the recipient.
        amount (float): The amount to be paid in Bitcoin (BTC).
        output_file (str): The file name for saving the QR code image. Defaults to "bitcoin_qr.png".
        
    Returns:
        None: The QR code is saved as an image file.
        
    Raises:
        ValueError: If the recipient address is invalid or the amount is negative.
    """
    # Validate the Bitcoin address format using a regex pattern (basic validation)
    if not re.match(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$", recipient_address):
        raise ValueError("Invalid Bitcoin address format.")
    
    # Ensure the amount is positive
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    
    # Construct the Bitcoin URI following the standard `bitcoin:` format
    bitcoin_uri = f"bitcoin:{recipient_address}?amount={amount}"
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4  # Thickness of the border (minimum is 4)
    )
    qr.add_data(bitcoin_uri)
    qr.make(fit=True)
    
    # Create the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image to the specified file
    img.save(output_file)
    print(f"Bitcoin QR code successfully generated and saved as '{output_file}'.")

# Example usage:
# generate_bitcoin_qr("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", 0.01)
```
