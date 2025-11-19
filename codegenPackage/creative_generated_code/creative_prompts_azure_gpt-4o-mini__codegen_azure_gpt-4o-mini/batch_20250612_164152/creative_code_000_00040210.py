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
import sys

def generate_monero_qr(amount: float, address: str, label: str = '', message: str = '') -> None:
    """
    Generate a Monero QR Code for the specified amount and address.

    :param amount: The amount of XMR to send.
    :param address: The Monero wallet address to send the XMR to.
    :param label: An optional label for the transaction.
    :param message: An optional message for the transaction.
    """
    # Validate the amount
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    # Validate the address (simple length check, can be enhanced)
    if len(address) != 95:  # Typical length of a Monero address
        raise ValueError("Invalid Monero address length.")

    # Construct the Monero URI
    uri = f'monero:{address}?amount={amount}'
    
    if label:
        uri += f'&label={label}'
    if message:
        uri += f'&message={message}'

    # Generate the QR Code
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(uri)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill='black', back_color='white')

        # Save the QR Code image
        img_file = f'monero_qr_{address}.png'
        img.save(img_file)
        print(f"QR Code generated and saved as {img_file}")

    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")

if __name__ == "__main__":
    # Example usage: python script.py <amount> <address>
    if len(sys.argv) < 3:
        print("Usage: python script.py <amount> <address> [label] [message]")
        sys.exit(1)

    try:
        # Parse command line arguments
        amount = float(sys.argv[1])
        address = sys.argv[2]
        label = sys.argv[3] if len(sys.argv) > 3 else ''
        message = sys.argv[4] if len(sys.argv) > 4 else ''

        # Generate the Monero QR Code
        generate_monero_qr(amount, address, label, message)

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
