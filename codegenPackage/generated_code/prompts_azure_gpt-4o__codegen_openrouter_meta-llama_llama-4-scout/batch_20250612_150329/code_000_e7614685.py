"""
Generated Code Metadata:
========================
Original URL: https://ethereum-qr-code-generator.com
Prompt: Generate Python code to create an Ethereum QR code for receiving ETH payments using the functionality described on the Ethereum QR Code Generator website.
Generated: DETERMINISTIC_e76146859a5b805d
Batch ID: 20250612_150329
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
import json

def generate_ethereum_qr_code(address: str, amount: str = "", label: str = "", message: str = "") -> str:
    """
    Generate Ethereum QR code for receiving ETH payments.

    Args:
    - address (str): Ethereum address for receiving ETH payments.
    - amount (str, optional): Amount of ETH to be received. Defaults to "".
    - label (str, optional): Label for the payment. Defaults to "".
    - message (str, optional): Message for the payment. Defaults to "".

    Returns:
    - str: File path of the generated QR code image.
    """

    # Ethereum QR code parameters
    params = {
        "address": address,
        "amount": amount,
        "label": label,
        "message": message
    }

    # Remove empty parameters
    params = {k: v for k, v in params.items() if v}

    # Create Ethereum QR code URI
    ethereum_uri = f"ethereum:{address}"
    if params:
        query_string = urlencode(params)
        ethereum_uri += f"?{query_string}"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(ethereum_uri)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    file_path = "ethereum_qr_code.png"
    img.save(file_path)

    return file_path


def main():
    try:
        address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
        amount = "1.0"
        label = "Payment Label"
        message = "Payment Message"

        file_path = generate_ethereum_qr_code(address, amount, label, message)
        print(f"Ethereum QR code saved to: {file_path}")

    except Exception as e:
        print(f"Error: {json.dumps(str(e), indent=4)}")


if __name__ == "__main__":
    main()
```
