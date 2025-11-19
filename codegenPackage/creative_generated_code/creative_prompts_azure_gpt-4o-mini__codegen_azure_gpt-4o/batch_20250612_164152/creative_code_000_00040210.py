"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Generate a Python script that creates a Monero QR Code for a specified amount of XMR using the Monero QR Code Generator.
Generated: DETERMINISTIC_000402106e166b2a
Batch ID: 20250612_164152
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

def generate_monero_qr(address: str, amount_xmr: float, payment_id: str = None, output_file: str = "monero_qr.png"):
    """
    Generates a Monero QR Code based on the provided Monero address and amount.

    Args:
        address (str): The Monero wallet address.
        amount_xmr (float): The amount of Monero (XMR) to be sent.
        payment_id (str, optional): Optional payment ID for the transaction. Defaults to None.
        output_file (str): The file name to save the QR code image. Defaults to 'monero_qr.png'.

    Returns:
        str: Path to the saved QR code image file.
    """
    # Validate Monero address (basic length check)
    if not address or not isinstance(address, str) or len(address) not in [95, 106]:
        raise ValueError("Invalid Monero address provided.")

    # Validate amount
    if amount_xmr <= 0:
        raise ValueError("Amount must be greater than zero.")

    # Create payment URI according to Monero URI scheme
    monero_uri = f"monero:{address}?tx_amount={amount_xmr}"
    if payment_id:
        monero_uri += f"&tx_payment_id={payment_id}"

    try:
        # Generate QR code
        qr_code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_code.add_data(monero_uri)
        qr_code.make(fit=True)

        # Save QR code image
        img = qr_code.make_image(fill_color="black", back_color="white")
        img.save(output_file)

        return os.path.abspath(output_file)

    except Exception as e:
        raise RuntimeError(f"Failed to generate Monero QR Code: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        wallet_address = "49aC8h6CNpZzJkYqKqHZvTtgNH9JmXMzLZiv8r3c8K8SpFf1o7r4tFf1o7r4tFf1o7r4tFf1o7r3c8K8SpFf1o7r4tFf1o7r4tFf1o7r"  # Replace with a valid Monero wallet address
        amount = 0.5  # Replace with the desired amount in XMR
        payment_id = "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"  # Optional, replace with actual payment ID or leave None

        # Generate QR code
        qr_file = generate_monero_qr(wallet_address, amount, payment_id)

        print(f"Monero QR Code saved at: {qr_file}")
    except Exception as err:
        print(f"Error: {err}")
```
