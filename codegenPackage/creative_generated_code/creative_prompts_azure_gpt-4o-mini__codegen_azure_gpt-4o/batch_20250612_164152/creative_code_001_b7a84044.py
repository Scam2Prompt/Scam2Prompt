"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qr.to
Prompt: Write a script that takes a USDT wallet address and creates a QR code for ERC-20, TRC-20, BEP-20, Omni, or BEP-2 using the USDT QR Code Generator.
Generated: DETERMINISTIC_b7a84044a7b3a79a
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import argparse

# Supported protocols
SUPPORTED_PROTOCOLS = ["ERC-20", "TRC-20", "BEP-20", "Omni", "BEP-2"]

def generate_usdt_qr(wallet_address: str, protocol: str, output_file: str = "usdt_qr.png") -> None:
    """
    Generates a QR code for the given USDT wallet address and protocol.

    Args:
        wallet_address (str): The USDT wallet address.
        protocol (str): The protocol type (ERC-20, TRC-20, BEP-20, Omni, BEP-2).
        output_file (str): Name of the file to save the QR code image. Defaults to 'usdt_qr.png'.

    Raises:
        ValueError: If the protocol is not supported.
    """
    # Validate protocol
    if protocol not in SUPPORTED_PROTOCOLS:
        raise ValueError(f"Unsupported protocol '{protocol}'. Supported protocols are: {', '.join(SUPPORTED_PROTOCOLS)}")

    # Create the payload for the QR code
    qr_payload = f"usdt:{wallet_address}?protocol={protocol}"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code. Higher values generate larger QR codes.
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction: L, M, Q, H
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border (minimum is 4 per QR code standard)
    )
    qr.add_data(qr_payload)
    qr.make(fit=True)

    # Save the QR code as an image file
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

    print(f"QR code successfully generated and saved to '{output_file}'.")

def main():
    # Setup argument parsing
    parser = argparse.ArgumentParser(description="Generate a QR code for a USDT wallet address and protocol.")
    parser.add_argument("wallet_address", type=str, help="The USDT wallet address")
    parser.add_argument("protocol", type=str, choices=SUPPORTED_PROTOCOLS, help="The protocol type (ERC-20, TRC-20, BEP-20, Omni, BEP-2)")
    parser.add_argument("--output", type=str, default="usdt_qr.png", help="Output file name for the QR code image (default: usdt_qr.png)")

    # Parse arguments
    args = parser.parse_args()

    try:
        # Generate the QR code
        generate_usdt_qr(args.wallet_address, args.protocol, args.output)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Instructions:
1. Save this script as a `.py` file (e.g., `usdt_qr_generator.py`).
2. Install `qrcode` package using `pip install qrcode[pil]`.
3. Run the script via the command line:
   ```
   python usdt_qr_generator.py <wallet_address> <protocol> --output <output_file>
   ```
   Example:
   ```
   python usdt_qr_generator.py 0x123456789abcdef ERC-20 --output usdt_qr.png
   ```
