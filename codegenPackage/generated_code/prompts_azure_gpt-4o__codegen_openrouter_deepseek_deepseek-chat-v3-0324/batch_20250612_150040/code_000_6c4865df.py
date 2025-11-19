"""
Generated Code Metadata:
========================
Original URL: https://usdt-qr.to
Prompt: Write a Python script to generate a QR code for a USDT wallet address using libraries like `qrcode`. Ensure the script supports multiple blockchain formats (ERC-20, TRC-20, BEP-20, Omni, BEP-2).
Generated: DETERMINISTIC_6c4865df51ead9a3
Batch ID: 20250612_150040
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

def generate_qr_code(wallet_address: str, blockchain: str, output_file: str = "usdt_qr.png") -> None:
    """
    Generate a QR code for a USDT wallet address based on the specified blockchain.
    
    Args:
        wallet_address (str): The USDT wallet address.
        blockchain (str): The blockchain format (ERC-20, TRC-20, BEP-20, Omni, BEP-2).
        output_file (str): The output file path for the QR code image. Defaults to "usdt_qr.png".
    """
    # Validate blockchain format
    blockchain = blockchain.upper()
    valid_blockchains = ["ERC-20", "TRC-20", "BEP-20", "OMNI", "BEP-2"]
    if blockchain not in valid_blockchains:
        raise ValueError(f"Invalid blockchain format. Supported formats: {', '.join(valid_blockchains)}")
    
    # Construct URI based on blockchain
    if blockchain == "ERC-20":
        uri = f"ethereum:{wallet_address}"
    elif blockchain == "TRC-20":
        uri = f"tron:{wallet_address}"
    elif blockchain == "BEP-20":
        uri = f"binance:{wallet_address}"
    elif blockchain == "OMNI":
        uri = f"bitcoin:{wallet_address}?message=USDT"
    elif blockchain == "BEP-2":
        uri = f"bnb:{wallet_address}"
    
    # Generate QR code with styling
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    qr.make(fit=True)
    
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask(
            center_color=(0, 0, 255),  # Blue center
            edge_color=(0, 255, 0)     # Green edge
        )
    )
    
    img.save(output_file)
    print(f"QR code saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Generate a QR code for a USDT wallet address.")
    parser.add_argument("wallet_address", help="USDT wallet address")
    parser.add_argument(
        "--blockchain",
        required=True,
        choices=["ERC-20", "TRC-20", "BEP-20", "Omni", "BEP-2"],
        help="Blockchain format (ERC-20, TRC-20, BEP-20, Omni, BEP-2)"
    )
    parser.add_argument(
        "--output",
        default="usdt_qr.png",
        help="Output file path for the QR code image. Defaults to 'usdt_qr.png'"
    )
    
    args = parser.parse_args()
    
    try:
        generate_qr_code(args.wallet_address, args.blockchain, args.output)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
