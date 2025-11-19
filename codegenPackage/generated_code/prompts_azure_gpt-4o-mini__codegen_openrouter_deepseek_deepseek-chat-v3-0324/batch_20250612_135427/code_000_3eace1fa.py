"""
Generated Code Metadata:
========================
Original URL: https://coin-qr.to
Prompt: How can I use the Bitcoin QR Code Generator to create a QR code for my Bitcoin address and include a specific amount for a transaction?
Generated: DETERMINISTIC_3eace1fa2fa5574e
Batch ID: 20250612_135427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from qrcode.constants import ERROR_CORRECT_L

def generate_bitcoin_qr_code(address: str, amount: float = None, output_file: str = "bitcoin_qr.png") -> None:
    """
    Generates a Bitcoin QR code for a given address and optional amount.
    
    Args:
        address (str): Bitcoin address to encode in the QR code.
        amount (float, optional): Amount in BTC to include in the payment request. Defaults to None.
        output_file (str, optional): Output filename for the QR code image. Defaults to "bitcoin_qr.png".
    
    Raises:
        ValueError: If the Bitcoin address is empty or invalid.
        TypeError: If the amount is not a number when provided.
    """
    if not address or not isinstance(address, str):
        raise ValueError("Bitcoin address must be a non-empty string")
    
    if amount is not None:
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        uri = f"bitcoin:{address}?amount={amount}"
    else:
        uri = f"bitcoin:{address}"

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(uri)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_file)
        print(f"Successfully generated QR code at {output_file}")
    except Exception as e:
        print(f"Error generating QR code: {e}")
        raise

# Example usage:
# generate_bitcoin_qr_code("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", amount=0.001)
```
