"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrcode-generator.to
Prompt: Write a code snippet that utilizes the LTC QR Code Generator API to generate a QR code for Litecoin transactions.
Generated: DETERMINISTIC_061fcbefb3496876
Batch ID: 20250612_161125
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

def generate_litecoin_qr(address: str, amount: float = 0.0, label: str = None, message: str = None) -> None:
    """
    Generate a QR code for a Litecoin transaction.

    Parameters:
    address (str): The Litecoin address to which the transaction is being sent.
    amount (float): The amount of Litecoin to be sent (default is 0.0).
    label (str): Optional label for the transaction.
    message (str): Optional message for the transaction.

    Raises:
    ValueError: If the address is invalid or if the amount is negative.
    Exception: For any other errors encountered during QR code generation.
    """
    # Validate the Litecoin address
    if not isinstance(address, str) or len(address) < 26 or len(address) > 35:
        raise ValueError("Invalid Litecoin address.")

    # Validate the amount
    if amount < 0:
        raise ValueError("Amount must be a non-negative value.")

    # Construct the Litecoin URI
    uri = f"litecoin:{address}?amount={amount}"
    if label:
        uri += f"&label={label}"
    if message:
        uri += f"&message={message}"

    try:
        # Generate the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(uri)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill='black', back_color='white')

        # Save the QR code as an image file
        img.save(f"litecoin_qr_{address}.png")

        print(f"QR code generated and saved as litecoin_qr_{address}.png")

    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")

# Example usage
if __name__ == "__main__":
    try:
        generate_litecoin_qr("LZ7Z1j5d2YtWo2Lh8qZxLvSyyJ9e9Mvu1N", 0.1, "Donation", "Thanks for your support!")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
