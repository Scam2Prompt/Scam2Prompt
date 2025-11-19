"""
Generated Code Metadata:
========================
Original URL: https://monero-qr-code-generator.com
Prompt: Generate a Python script that creates a Monero QR Code for a specified amount of XMR using the Monero QR Code Generator.
Generated: DETERMINISTIC_000402106e166b2a
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
import argparse
import sys

def generate_monero_qr_code(address: str, amount: float, output_file: str = "monero_qr.png") -> None:
    """
    Generates a Monero QR code for a specified address and amount.
    
    Args:
        address (str): Monero wallet address.
        amount (float): Amount of XMR to be sent.
        output_file (str, optional): Output file path for the QR code. Defaults to "monero_qr.png".
    
    Raises:
        ValueError: If address is empty or amount is invalid.
    """
    if not address:
        raise ValueError("Monero address cannot be empty.")
    
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    
    # Construct the Monero URI scheme
    monero_uri = f"monero:{address}?tx_amount={amount}"
    
    # Configure QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(monero_uri)
    qr.make(fit=True)
    
    # Generate styled QR code
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask(
            center_color=(70, 130, 180),  # SteelBlue
            edge_color=(255, 140, 0)     # DarkOrange
        )
    )
    
    # Save the QR code
    img.save(output_file)

def main():
    parser = argparse.ArgumentParser(description="Generate a Monero QR code for a specified amount of XMR.")
    parser.add_argument("address", type=str, help="Monero wallet address")
    parser.add_argument("amount", type=float, help="Amount of XMR to send")
    parser.add_argument("-o", "--output", type=str, default="monero_qr.png", help="Output file path (default: monero_qr.png)")
    
    args = parser.parse_args()
    
    try:
        generate_monero_qr_code(args.address, args.amount, args.output)
        print(f"Successfully generated Monero QR code at: {args.output}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
