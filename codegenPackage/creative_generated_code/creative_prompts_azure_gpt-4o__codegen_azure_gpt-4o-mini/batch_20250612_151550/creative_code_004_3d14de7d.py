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
from qrcode.exceptions import QRCodeError

def generate_bitcoin_qr(recipient_address: str, amount: float, filename: str) -> None:
    """
    Generates a QR code for a Bitcoin transaction.

    Parameters:
    recipient_address (str): The Bitcoin wallet address of the recipient.
    amount (float): The amount of Bitcoin to send.
    filename (str): The name of the file where the QR code image will be saved.

    Raises:
    ValueError: If the recipient address is invalid or if the amount is negative.
    QRCodeError: If there is an error generating the QR code.
    """

    # Validate the recipient address
    if not isinstance(recipient_address, str) or len(recipient_address) < 26 or len(recipient_address) > 35:
        raise ValueError("Invalid Bitcoin address. Address must be a string between 26 and 35 characters.")
    
    # Validate the amount
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Amount must be a positive number.")

    # Construct the Bitcoin URI
    bitcoin_uri = f"bitcoin:{recipient_address}?amount={amount}"

    try:
        # Create a QR code from the Bitcoin URI
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(bitcoin_uri)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a file
        img.save(filename)
        print(f"QR code generated successfully and saved as {filename}")

    except QRCodeError as e:
        raise RuntimeError(f"Error generating QR code: {e}")

# Example usage:
# generate_bitcoin_qr("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", 0.01, "bitcoin_qr.png")
```
