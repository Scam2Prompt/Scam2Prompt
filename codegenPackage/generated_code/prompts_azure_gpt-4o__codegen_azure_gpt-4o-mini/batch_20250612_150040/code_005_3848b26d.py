"""
Generated Code Metadata:
========================
Original URL: https://monero-qr-code-generator.com
Prompt: Create a Monero QR code generator script that includes error correction features, similar to the functionality explained on the Monero QR Code Generator webpage.
Generated: DETERMINISTIC_3848b26d86a1a259
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from qrcode.exceptions import QRCodeException
import sys

def generate_monero_qr(address, amount=None, payment_id=None, extra=None, filename='monero_qr.png'):
    """
    Generate a Monero QR code with optional parameters.

    Parameters:
    - address (str): The Monero wallet address.
    - amount (float, optional): The amount of Monero to send.
    - payment_id (str, optional): The payment ID for the transaction.
    - extra (str, optional): Any extra data to include in the QR code.
    - filename (str): The filename to save the QR code image.

    Raises:
    - ValueError: If the address is invalid or if the amount is negative.
    - QRCodeException: If there is an error generating the QR code.
    """
    
    # Validate the Monero address
    if not isinstance(address, str) or len(address) == 0:
        raise ValueError("Invalid Monero address provided.")
    
    # Validate the amount if provided
    if amount is not None:
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be a non-negative number.")
    
    # Validate the payment ID if provided
    if payment_id is not None and (not isinstance(payment_id, str) or len(payment_id) != 16):
        raise ValueError("Payment ID must be a 16-character string.")
    
    # Construct the Monero URI
    uri = f"monero:{address}"
    if amount is not None:
        uri += f"?amount={amount}"
    if payment_id is not None:
        uri += f"&tx_payment_id={payment_id}"
    if extra is not None:
        uri += f"&extra={extra}"

    # Generate the QR code
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(uri)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"QR code generated and saved as {filename}")

    except QRCodeException as e:
        print(f"Error generating QR code: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    try:
        generate_monero_qr(
            address="43A1...your_monero_address_here...",
            amount=0.5,
            payment_id="4c3d...your_payment_id_here...",
            filename="monero_qr_example.png"
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
```
