"""
Generated Code Metadata:
========================
Original URL: https://ethereum-qr-code-generator.com
Prompt: Create a Python script that generates an Ethereum QR code and saves it as an image file, as described on the Ethereum QR Code Generator site.
Generated: DETERMINISTIC_eee6c74194d6e98f
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
import argparse
from PIL import Image

def generate_ethereum_qr_code(address, amount=None, gas=None, filename="ethereum_qr.png"):
    """
    Generate an Ethereum QR code based on the provided parameters.
    
    Args:
        address (str): Ethereum wallet address
        amount (float, optional): Amount of ETH to transfer. Defaults to None.
        gas (int, optional): Gas limit for the transaction. Defaults to None.
        filename (str, optional): Output filename. Defaults to "ethereum_qr.png".
    """
    try:
        # Validate Ethereum address (basic check)
        if not address.startswith('0x') or len(address) != 42:
            raise ValueError("Invalid Ethereum address format")
        
        # Construct the Ethereum URI scheme
        uri = f"ethereum:{address}"
        
        if amount is not None:
            uri += f"?value={amount}"
            if gas is not None:
                uri += f"&gas={gas}"
        elif gas is not None:
            uri += f"?gas={gas}"
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(uri)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        
        print(f"Ethereum QR code successfully saved as {filename}")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Generate an Ethereum QR code.')
    parser.add_argument('address', type=str, help='Ethereum wallet address')
    parser.add_argument('--amount', type=float, help='Amount of ETH to transfer', default=None)
    parser.add_argument('--gas', type=int, help='Gas limit for the transaction', default=None)
    parser.add_argument('--output', type=str, help='Output filename', default="ethereum_qr.png")
    
    args = parser.parse_args()
    
    generate_ethereum_qr_code(
        address=args.address,
        amount=args.amount,
        gas=args.gas,
        filename=args.output
    )

if __name__ == "__main__":
    main()
```
