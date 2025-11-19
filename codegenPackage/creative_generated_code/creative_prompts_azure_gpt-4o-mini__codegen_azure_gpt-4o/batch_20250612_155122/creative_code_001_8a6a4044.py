"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-qr-code-generator.com
Prompt: Write a code snippet to generate an Ethereum QR Code that can be scanned for ETH payments.
Generated: DETERMINISTIC_8a6a40446c90bcb1
Batch ID: 20250612_155122
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

def generate_eth_qr_code(eth_address, amount=None, output_file="eth_qr_code.png"):
    """
    Generates a QR code for Ethereum payments.

    Parameters:
        eth_address (str): The Ethereum wallet address (must be a valid address).
        amount (float, optional): The amount of ETH to be requested (default is None).
        output_file (str): The filename to save the generated QR code image (default is 'eth_qr_code.png').

    Returns:
        None: Saves the QR code to the specified file.
    """
    try:
        # Validate Ethereum address format
        if not eth_address.startswith("0x") or len(eth_address) != 42:
            raise ValueError("Invalid Ethereum address. Must start with '0x' and be 42 characters long.")

        # Construct the Ethereum payment URI
        eth_uri = f"ethereum:{eth_address}"
        if amount:
            eth_uri += f"?value={amount}"

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(eth_uri)
        qr.make(fit=True)

        # Create the QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_file)

        print(f"QR code successfully generated and saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


# Example usage
if __name__ == "__main__":
    eth_wallet_address = "0x1234567890abcdef1234567890abcdef12345678"  # Replace with a valid Ethereum address
    eth_amount = 0.05  # ETH amount to request (optional)
    generate_eth_qr_code(eth_wallet_address, eth_amount)
```
