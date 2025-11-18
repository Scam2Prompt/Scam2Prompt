"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qrcode-generator.com
Prompt: Write a script to generate a USDT QR code for the Ethereum blockchain, referencing the security and reliability features discussed on the USDT QR Code Generator website.
Generated: DETERMINISTIC_3b573a6b1f9db998
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode  # Import the qrcode library to generate QR codes
import os

def generate_usdt_qr_code(address: str, amount: float, filename: str) -> None:
    """
    Generates a QR code for sending USDT on the Ethereum blockchain.

    Parameters:
    - address (str): The Ethereum address to which USDT will be sent.
    - amount (float): The amount of USDT to send.
    - filename (str): The filename to save the generated QR code image.

    Raises:
    - ValueError: If the address is invalid or the amount is non-positive.
    """

    # Basic validation of the Ethereum address
    if not is_valid_ethereum_address(address):
        raise ValueError("Invalid Ethereum address provided.")

    if amount <= 0:
        raise ValueError("The amount must be greater than zero.")

    # Construct the USDT URI
    usdt_uri = f"ethereum:{address}?value={amount}"

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(usdt_uri)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the specified filename
    img.save(filename)

    print(f"QR code generated and saved as {filename}")

def is_valid_ethereum_address(address: str) -> bool:
    """
    Validates an Ethereum address.

    Parameters:
    - address (str): The Ethereum address to validate.

    Returns:
    - bool: True if the address is valid, False otherwise.
    """
    # Ethereum address must be 42 characters long (0x + 40 hex characters)
    if len(address) != 42:
        return False
    
    # Check if the address starts with '0x' and contains valid hex characters
    if not address.startswith('0x') or not all(c in '0123456789abcdefABCDEF' for c in address[2:]):
        return False

    return True

if __name__ == "__main__":
    # Example usage
    eth_address = "0xYourEthereumAddressHere"  # Replace with the actual Ethereum address
    amount_to_send = 10.0  # Define the amount of USDT to send
    output_filename = "usdt_qr_code.png"  # Specify the output filename

    try:
        generate_usdt_qr_code(eth_address, amount_to_send, output_filename)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
