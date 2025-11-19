"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-qr-code-generator.com
Prompt: How can I create a free Ethereum QR Code for receiving ETH donations on my website?
Generated: DETERMINISTIC_452caf653e8812f0
Batch ID: 20250612_155122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the required libraries
import qrcode
import sys

def generate_eth_qr_code(wallet_address, filepath="eth_qr_code.png"):
    """
    Generates a QR code for an Ethereum wallet address.

    Parameters:
    wallet_address (str): The Ethereum wallet address where donations will be sent.
    filepath (str): The file path to save the generated QR code image. Defaults to 'eth_qr_code.png'.

    Returns:
    None
    """
    try:
        # Validate the wallet address
        if not wallet_address.startswith("0x") or len(wallet_address) != 42:
            raise ValueError("Invalid Ethereum wallet address. It must start with '0x' and be 42 characters long.")

        # Create the Ethereum QR Code URI (EIP-67 format)
        eth_uri = f"ethereum:{wallet_address}"

        # Generate the QR Code
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code (1 is smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
            box_size=10,  # Size of each box in the QR Code grid
            border=4  # Thickness of the border
        )
        qr.add_data(eth_uri)
        qr.make(fit=True)

        # Create the image and save it to the specified file path
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filepath)

        print(f"QR Code successfully generated and saved to: {filepath}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # Prompt the user to enter their Ethereum wallet address
        wallet_address = input("Enter your Ethereum wallet address: ").strip()
        
        # Generate the QR code
        generate_eth_qr_code(wallet_address)
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
        sys.exit(1)
```

This Python script generates a QR code for an Ethereum wallet address and saves it as an image file.
