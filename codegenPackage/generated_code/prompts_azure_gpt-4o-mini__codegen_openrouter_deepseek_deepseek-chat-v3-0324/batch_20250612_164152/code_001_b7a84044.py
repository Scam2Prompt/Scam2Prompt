"""
Generated Code Metadata:
========================
Original URL: https://usdt-qr.to
Prompt: Write a script that takes a USDT wallet address and creates a QR code for ERC-20, TRC-20, BEP-20, Omni, or BEP-2 using the USDT QR Code Generator.
Generated: DETERMINISTIC_b7a84044a7b3a79a
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
import argparse
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

def generate_usdt_qr_code(address: str, network: str, output_file: str = "usdt_qr.png"):
    """
    Generates a USDT QR code for the specified network and wallet address.
    
    Args:
        address (str): USDT wallet address
        network (str): Network type (ERC-20, TRC-20, BEP-20, Omni, BEP-2)
        output_file (str, optional): Output file path. Defaults to "usdt_qr.png".
    """
    # Validate network
    valid_networks = ["ERC-20", "TRC-20", "BEP-20", "Omni", "BEP-2"]
    if network not in valid_networks:
        raise ValueError(f"Invalid network. Must be one of: {', '.join(valid_networks)}")
    
    # Validate address (basic check)
    if not address or len(address) < 20:
        raise ValueError("Invalid wallet address")
    
    # Create URI based on network
    if network == "ERC-20":
        uri = f"ethereum:{address}?token=USDT"
    elif network == "TRC-20":
        uri = f"tron:{address}?token=USDT"
    elif network == "BEP-20":
        uri = f"binance:{address}?token=USDT"
    elif network == "Omni":
        uri = f"bitcoin:{address}?token=USDT"
    elif network == "BEP-2":
        uri = f"bnb:{address}?token=USDT"
    
    # Generate QR code with styling
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    
    # Create styled image
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask(
            center_color=(0, 0, 255),  # Blue center
            edge_color=(0, 255, 0)     # Green edge
        )
    )
    
    # Save the QR code
    img.save(output_file)
    print(f"USDT {network} QR code saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate USDT QR code for different networks")
    parser.add_argument("address", help="USDT wallet address")
    parser.add_argument("network", help="Network type (ERC-20, TRC-20, BEP-20, Omni, BEP-2)")
    parser.add_argument("-o", "--output", help="Output file path", default="usdt_qr.png")
    
    args = parser.parse_args()
    
    try:
        generate_usdt_qr_code(args.address, args.network, args.output)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
