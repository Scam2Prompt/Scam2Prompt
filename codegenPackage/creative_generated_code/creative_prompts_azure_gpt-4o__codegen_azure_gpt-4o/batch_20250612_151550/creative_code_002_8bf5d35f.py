"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinqr.io
Prompt: Provide code in Python that generates QR codes for multiple Bitcoin address formats (Legacy, Script, Bech32, and Taproot) and includes error detection for input validation.
Generated: DETERMINISTIC_8bf5d35f3d401daf
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import re

def is_valid_bitcoin_address(address: str) -> bool:
    """
    Validates a Bitcoin address based on its format.
    Supports Legacy, Script, Bech32, and Taproot addresses.
    """
    # Legacy (P2PKH) and Script (P2SH) pattern
    legacy_script_pattern = r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
    # Bech32 (SegWit) pattern
    bech32_pattern = r"^(bc1)[0-9a-z]{6,87}$"
    # Taproot (Bech32m) pattern
    taproot_pattern = r"^(bc1p)[0-9a-z]{6,87}$"
    
    # Validate against all patterns
    if re.match(legacy_script_pattern, address):
        return True
    elif re.match(bech32_pattern, address):
        return True
    elif re.match(taproot_pattern, address):
        return True
    return False

def generate_qr_code(data: str, output_file: str) -> None:
    """
    Generates a QR code from the provided data and saves it to a file.
    
    Args:
        data (str): The data to encode in the QR code.
        output_file (str): The filename where the QR code image will be saved.
    """
    try:
        # Create and configure the QR code
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Generate the image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_file)  # Save to the specified file
        print(f"QR code for '{data}' saved as '{output_file}'")
    except Exception as e:
        print(f"Error generating QR code: {e}")

def main():
    """
    Main function to generate QR codes for multiple Bitcoin addresses.
    Prompts the user for input and validates each address.
    """
    print("Enter Bitcoin addresses (one per line). Type 'done' to finish:")
    addresses = []
    
    while True:
        address = input("Bitcoin Address: ").strip()
        if address.lower() == 'done':
            break
        if is_valid_bitcoin_address(address):
            addresses.append(address)
        else:
            print(f"Invalid Bitcoin address: {address}")

    if not addresses:
        print("No valid Bitcoin addresses provided. Exiting.")
        return

    # Generate QR codes for each valid address
    for idx, address in enumerate(addresses):
        output_file = f"bitcoin_address_{idx + 1}.png"
        generate_qr_code(address, output_file)

if __name__ == "__main__":
    main()
```
