"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinqr.io
Prompt: How can I generate a QR code for a Bitcoin payment using different address formats like Legacy, SegWit, and Bech32?
Generated: DETERMINISTIC_422aad384d803a11
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code to generate a QR code for a Bitcoin payment using different address formats:

```python
import qrcode
import re


def validate_bitcoin_address(address: str) -> bool:
    """
    Validate a Bitcoin address for Legacy, SegWit, or Bech32 format.
    
    Args:
        address (str): Bitcoin address to validate.
    
    Returns:
        bool: True if the address is valid, False otherwise.
    """
    # Regex patterns for Bitcoin address formats
    legacy_pattern = r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"  # Legacy format
    segwit_pattern = r"^[3][a-km-zA-HJ-NP-Z1-9]{25,34}$"   # SegWit format
    bech32_pattern = r"^(bc1)[a-z0-9]{39,59}$"             # Bech32 format

    # Validate against the patterns
    if re.match(legacy_pattern, address) or re.match(segwit_pattern, address) or re.match(bech32_pattern, address):
        return True
    return False


def generate_bitcoin_payment_qr(bitcoin_address: str, amount: float, label: str = None, message: str = None) -> None:
    """
    Generate a QR code for Bitcoin payment.
    
    Args:
        bitcoin_address (str): Valid Bitcoin address.
        amount (float): Amount to request in BTC.
        label (str): Optional label for the payment.
        message (str): Optional message for the payment.
    """
    # Validate the Bitcoin address
    if not validate_bitcoin_address(bitcoin_address):
        raise ValueError("Invalid Bitcoin address format.")

    # Construct the Bitcoin URI
    bitcoin_uri = f"bitcoin:{bitcoin_address}?amount={amount}"
    if label:
        bitcoin_uri += f"&label={label}"
    if message:
        bitcoin_uri += f"&message={message}"

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(bitcoin_uri)
    qr.make(fit=True)

    # Save the QR code to a file
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("bitcoin_payment_qr.png")

    print(f"QR code generated and saved as 'bitcoin_payment_qr.png'.")
    print(f"Bitcoin URI: {bitcoin_uri}")


# Example usage:
try:
    generate_bitcoin_payment_qr(
        bitcoin_address="bc1qw4rsh7fxh8p48schlkg6a7ejj9d4hxp8s23k3l",  # Example Bech32 address
        amount=0.01,  # Example BTC amount
        label="Coffee",
        message="Payment for coffee"
    )
except ValueError as e:
    print(f"Error: {e}")
```

This code uses Python's `qrcode` library to generate a QR code for a Bitcoin payment. It validates the Bitcoin address format using regular expressions before creating the QR code. Make sure to install the `qrcode` library (`pip install qrcode[pil]`) before running the script.
