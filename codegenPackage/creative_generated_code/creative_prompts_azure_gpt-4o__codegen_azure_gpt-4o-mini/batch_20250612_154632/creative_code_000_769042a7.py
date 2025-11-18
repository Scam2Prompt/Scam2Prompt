"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet2qr.com
Prompt: Write a Python script to generate a Tether (USDT) QR code for secure transactions using the Wallet2QR tool or similar libraries.
Generated: DETERMINISTIC_769042a70aad7b1a
Batch ID: 20250612_154632
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
import sys

def generate_usdt_qr(address, amount=None, message=None):
    """
    Generate a QR code for a Tether (USDT) transaction.

    :param address: The wallet address to which USDT will be sent.
    :param amount: Optional amount of USDT to be included in the QR code.
    :param message: Optional message to be included in the QR code.
    :return: Path to the generated QR code image.
    """
    try:
        # Validate the address
        if not address.startswith("0x") or len(address) != 42:
            raise ValueError("Invalid wallet address. It should start with '0x' and be 42 characters long.")

        # Construct the URI for USDT transactions
        uri = f"ethereum:{address}"
        if amount:
            uri += f"?amount={amount}"
        if message:
            uri += f"&message={message}"

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(uri)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image
        output_file = f"usdt_qr_{address[2:]}.png"
        img.save(output_file)

        return output_file

    except Exception as e:
        print(f"Error generating QR code: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    # Replace with actual address and optional parameters
    usdt_address = "0xYourWalletAddressHere"
    usdt_amount = "10"  # Optional, in USDT
    usdt_message = "Payment for services"  # Optional

    qr_code_file = generate_usdt_qr(usdt_address, usdt_amount, usdt_message)
    print(f"QR code generated and saved as: {qr_code_file}")
```
