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
"""
Script to generate a USDT QR code for the Ethereum blockchain.

Dependencies:
- qrcode: For generating QR codes
- eth_utils: For validating Ethereum addresses

Install dependencies via pip:
pip install qrcode eth_utils
"""

import qrcode
from eth_utils import is_address

def generate_usdt_qr_code(eth_address, amount, output_file="usdt_qr_code.png"):
    """
    Generate a QR code for USDT transfer on Ethereum blockchain.
    
    Parameters:
        eth_address (str): The Ethereum address to send USDT to.
        amount (float): The amount of USDT to be transferred.
        output_file (str): The output filename for the QR code image (default: usdt_qr_code.png).
        
    Returns:
        str: The output file path if successful.
    
    Raises:
        ValueError: If the Ethereum address is invalid or the amount is non-positive.
    """
    # Validate Ethereum address
    if not is_address(eth_address):
        raise ValueError(f"Invalid Ethereum address: {eth_address}")

    # Validate transfer amount
    if amount <= 0:
        raise ValueError(f"Amount must be greater than 0. Given: {amount}")

    # Construct the data string for the QR code
    # Following the format: ethereum:<address>?value=<amount>&token=usdt
    qr_data = f"ethereum:{eth_address}?value={amount}&token=usdt"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Save QR code to file
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

    return output_file


if __name__ == "__main__":
    # Example usage
    try:
        eth_address = input("Enter Ethereum address: ").strip()
        amount = float(input("Enter USDT amount: ").strip())
        output_file = generate_usdt_qr_code(eth_address, amount)
        print(f"QR Code successfully generated and saved as {output_file}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
