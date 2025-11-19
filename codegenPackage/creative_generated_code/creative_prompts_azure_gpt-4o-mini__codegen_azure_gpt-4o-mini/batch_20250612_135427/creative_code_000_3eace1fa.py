"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qr.to
Prompt: How can I use the Bitcoin QR Code Generator to create a QR code for my Bitcoin address and include a specific amount for a transaction?
Generated: DETERMINISTIC_3eace1fa2fa5574e
Batch ID: 20250612_135427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from decimal import Decimal

def generate_bitcoin_qr(address: str, amount: Decimal = None) -> None:
    """
    Generates a QR code for a Bitcoin address, optionally including a transaction amount.

    Parameters:
    address (str): The Bitcoin address to encode in the QR code.
    amount (Decimal, optional): The transaction amount in BTC. Default is None.

    Raises:
    ValueError: If the address is not valid or if the amount is negative.
    """

    # Validate Bitcoin address (basic validation)
    if not isinstance(address, str) or len(address) == 0:
        raise ValueError("Invalid Bitcoin address provided.")
    
    # Validate transaction amount
    if amount is not None:
        if not isinstance(amount, Decimal) or amount < 0:
            raise ValueError("Transaction amount must be a non-negative decimal.")

    # Create the Bitcoin URI
    if amount is not None:
        bitcoin_uri = f'bitcoin:{address}?amount={amount}'
    else:
        bitcoin_uri = f'bitcoin:{address}'

    # Generate the QR code
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
    img_file_name = f'bitcoin_qr_{address}.png'
    img.save(img_file_name)

    print(f"QR code generated and saved as {img_file_name}")

# Example usage
if __name__ == "__main__":
    try:
        btc_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Replace with a valid Bitcoin address
        transaction_amount = Decimal('0.01')  # Example amount in BTC
        generate_bitcoin_qr(btc_address, transaction_amount)
    except Exception as e:
        print(f"An error occurred: {e}")
```
