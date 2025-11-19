"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Explain how to use the Monero QR Code Generator for creating QR Codes that enhance Monero transactions on social media platforms.
Generated: DETERMINISTIC_66dfc7daaa90afd0
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Monero QR Code Generator
This script generates QR codes for Monero transactions, which can be shared on social media platforms.
It uses the `qrcode` library to create the QR code and saves the image to disk.
"""

import qrcode
import os

def generate_monero_qr(address: str, amount: float, payment_id: str = None, recipient_name: str = None, save_path: str = "monero_qr.png") -> None:
    """
    Generates a QR code for Monero transactions based on provided details.

    Args:
        address (str): The Monero wallet address (required).
        amount (float): The amount to be sent in XMR (required).
        payment_id (str, optional): A unique payment ID for the transaction (optional).
        recipient_name (str, optional): Name of the recipient to include in the QR code metadata (optional).
        save_path (str, optional): Path to save the generated QR code image (defaults to 'monero_qr.png').

    Raises:
        ValueError: If the provided address or amount is invalid.
        IOError: If the QR code image cannot be saved.
    """

    # Validate input
    if not address or len(address) == 0:
        raise ValueError("Invalid Monero address provided.")
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    # Construct the URI following Monero's payment URI scheme
    monero_uri = f"monero:{address}?tx_amount={amount}"
    if payment_id:
        monero_uri += f"&tx_payment_id={payment_id}"
    if recipient_name:
        monero_uri += f"&recipient_name={recipient_name}"

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L is lowest)
        box_size=10,  # Size of each box
        border=4  # Border size
    )
    qr.add_data(monero_uri)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to disk
    try:
        img.save(save_path)
        print(f"QR Code successfully saved to {save_path}")
    except IOError as e:
        raise IOError(f"Failed to save QR code image: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # Replace these values with real data
        monero_address = "4A4zX9w1R9YqH7G8Kv1LJ5F2zR9YksjfkM2Y1z4YH8kwWCMs8J9Fa9ftZ"
        amount_to_send = 0.5  # XMR
        payment_id_example = "123456789abcdef"
        recipient_name_example = "Alice"

        # Generate QR code
        generate_monero_qr(
            address=monero_address,
            amount=amount_to_send,
            payment_id=payment_id_example,
            recipient_name=recipient_name_example,
            save_path="monero_transaction_qr.png"
        )
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes for Deployment:
1. Install the `qrcode` library if not already installed:
   ```
   pip install qrcode[pil]
   ```
2. Replace placeholder variables (`monero_address`, `amount_to_send`, etc.) with actual transaction details when using the script.
3. The generated QR code can be shared on social media platforms to facilitate Monero transactions.
