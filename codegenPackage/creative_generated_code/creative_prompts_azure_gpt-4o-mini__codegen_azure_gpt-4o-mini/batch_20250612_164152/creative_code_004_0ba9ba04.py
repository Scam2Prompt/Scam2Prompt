"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Provide an example of a Monero QR Code generation API call and explain how it can be used in a web application for cryptocurrency payments.
Generated: DETERMINISTIC_0ba9ba048c06023f
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import qrcode
from PIL import Image

def generate_monero_qr_code(address, payment_id=None, amount=None):
    """
    Generates a QR code for a Monero cryptocurrency payment.

    Args:
        address (str): The Monero wallet address to receive payments.
        payment_id (str, optional): An optional payment ID for the transaction.
        amount (float, optional): An optional amount to request in XMR.

    Returns:
        str: The file path of the generated QR code image.
    """
    try:
        # Base Monero URI
        monero_uri = f"monero:{address}"

        # Add payment_id if provided
        if payment_id:
            monero_uri += f"?tx_payment_id={payment_id}"
        
        # Add amount if provided
        if amount:
            monero_uri += f"&amount={amount:.12f}"

        # Generate the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(monero_uri)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image
        file_path = "monero_payment_qr.png"
        img.save(file_path)

        return file_path

    except Exception as e:
        print(f"Error generating QR code: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace with your Monero wallet address, payment id, and amount
    wallet_address = "44AFFZxD1Z6KzJmZxKg2PTt7c6tB1wTRu2sUo9mrbVvD6dzXKYHgX5gFz8YkJ9hQ6M8Xv5dW8B2dQ1C7S4J2x9VM8Mbqf6fD"
    payment_id = "abcdef1234567890"
    amount = 0.01  # Amount in XMR

    qr_code_path = generate_monero_qr_code(wallet_address, payment_id, amount)
    if qr_code_path:
        print(f"QR Code generated successfully: {qr_code_path}")
```
