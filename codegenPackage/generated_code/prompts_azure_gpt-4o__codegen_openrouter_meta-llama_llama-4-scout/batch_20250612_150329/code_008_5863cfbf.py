"""
Generated Code Metadata:
========================
Original URL: https://ethereum-qr-code-generator.com
Prompt: Write Python code to generate Ethereum QR codes for decentralized finance (DeFi) applications, referencing the Ethereum QR Code Generator tool's features.
Generated: DETERMINISTIC_5863cfbf6ec93e93
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
from urllib.parse import urlparse
from typing import Optional

def generate_ethereum_qr_code(
    address: str, 
    value: Optional[str] = None, 
    label: Optional[str] = None, 
    message: Optional[str] = None
) -> str:
    """
    Generate Ethereum QR code.

    Args:
    - address (str): Ethereum address.
    - value (str, optional): Ether value to send. Defaults to None.
    - label (str, optional): Label for the recipient. Defaults to None.
    - message (str, optional): Message to include in the QR code. Defaults to None.

    Returns:
    - str: Path to the generated QR code image.
    """

    # Validate Ethereum address
    if not isinstance(address, str) or not address.startswith("0x") or len(address) != 42:
        raise ValueError("Invalid Ethereum address")

    # Construct Ethereum QR code data
    qr_data = f"ethereum:{address}"
    if value:
        qr_data += f"?value={value}"
    if label:
        qr_data += f"&label={label}"
    if message:
        qr_data += f"&message={message}"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img_path = "ethereum_qr_code.png"
    img.save(img_path)

    return img_path


def main():
    try:
        address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
        value = "1.0"
        label = "John Doe"
        message = "Test transaction"

        img_path = generate_ethereum_qr_code(address, value, label, message)
        print(f"QR code saved to: {img_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
