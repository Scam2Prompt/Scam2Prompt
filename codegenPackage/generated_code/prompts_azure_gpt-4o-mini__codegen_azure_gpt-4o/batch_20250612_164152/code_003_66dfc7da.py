"""
Generated Code Metadata:
========================
Original URL: https://monero-qr-code-generator.com
Prompt: Explain how to use the Monero QR Code Generator for creating QR Codes that enhance Monero transactions on social media platforms.
Generated: DETERMINISTIC_66dfc7daaa90afd0
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Monero QR Code Generator Script

This script generates QR codes for Monero transactions, which can be shared on social media platforms.
The QR code encodes the Monero payment URI format, allowing users to easily scan and initiate transactions.

Requirements:
- Install the `qrcode` library: pip install qrcode
- Install the `Pillow` library: pip install pillow

Usage:
- Update the Monero address, amount, and optional fields as needed.
- Run the script to generate a QR code image file.
"""

import qrcode
import os

def generate_monero_qr_code(address, amount=None, payment_id=None, recipient_name=None, tx_description=None, output_file="monero_qr.png"):
    """
    Generates a Monero QR code based on the provided parameters.

    Parameters:
        address (str): The Monero wallet address (required).
        amount (float, optional): The amount to be transferred (optional).
        payment_id (str, optional): A unique payment ID for the transaction (optional).
        recipient_name (str, optional): The recipient's name (optional).
        tx_description (str, optional): A description for the transaction (optional).
        output_file (str): The name of the output file for the QR code image (default: "monero_qr.png").

    Returns:
        None: Saves the QR code image to the specified file.
    """
    try:
        # Validate the Monero address
        if not address or len(address) < 95:
            raise ValueError("Invalid Monero address. Please provide a valid address.")

        # Construct the Monero payment URI
        uri = f"monero:{address}"
        query_params = []

        if amount:
            query_params.append(f"tx_amount={amount}")
        if payment_id:
            query_params.append(f"tx_payment_id={payment_id}")
        if recipient_name:
            query_params.append(f"recipient_name={recipient_name}")
        if tx_description:
            query_params.append(f"tx_description={tx_description}")

        if query_params:
            uri += "?" + "&".join(query_params)

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(uri)
        qr.make(fit=True)

        # Create the QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to the specified file
        img.save(output_file)
        print(f"QR code successfully generated and saved to {output_file}")

    except Exception as e:
        print(f"Error generating QR code: {e}")

if __name__ == "__main__":
    # Example usage
    monero_address = "48zTzK1X9Xz2X3XzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzXzX
