"""
Generated Code Metadata:
========================
Original URL: https://bitcoinqr.io
Prompt: Develop a simple Bitcoin QR code generator application using a programming language of your choice, incorporating the technical insights from the bitcoinqr.io website.
Generated: DETERMINISTIC_9f8298a087d10475
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from urllib.parse import urlencode
import hashlib

def generate_qr_code(bitcoin_address, amount=0, label="", message=""):
    """
    Generate a Bitcoin QR code.

    Args:
        bitcoin_address (str): The Bitcoin address to encode in the QR code.
        amount (float, optional): The amount of Bitcoin to encode. Defaults to 0.
        label (str, optional): The label to encode. Defaults to "".
        message (str, optional): The message to encode. Defaults to "".

    Returns:
        str: The path to the generated QR code image.
    """

    # Create the Bitcoin URI
    bitcoin_uri = "bitcoin:"
    bitcoin_uri += bitcoin_address

    # Add parameters to the URI
    params = {}
    if amount > 0:
        params["amount"] = amount
    if label:
        params["label"] = label
    if message:
        hashed_message = hashlib.sha256(message.encode()).hexdigest()
        params["message"] = message
        params["hash"] = hashed_message

    # Encode the parameters
    query_string = urlencode(params)

    # Append the query string to the URI
    if query_string:
        bitcoin_uri += "?" + query_string

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
    img.save("bitcoin_qr_code.png")

    return "bitcoin_qr_code.png"

def main():
    try:
        bitcoin_address = input("Enter the Bitcoin address: ")
        amount = float(input("Enter the amount (optional): ") or 0)
        label = input("Enter the label (optional): ")
        message = input("Enter the message (optional): ")

        generate_qr_code(bitcoin_address, amount, label, message)
        print("QR code generated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
