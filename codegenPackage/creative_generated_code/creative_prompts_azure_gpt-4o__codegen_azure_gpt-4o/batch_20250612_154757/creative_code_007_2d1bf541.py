"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrcode-generator.to
Prompt: Generate a Python script to batch-create QR codes for multiple cryptocurrency wallet addresses (e.g., BTC, ETH, LTC), referencing the multi-crypto QR code generation features on https://qrcode-generator.to.
Generated: DETERMINISTIC_2d1bf5414c31a74c
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import os

# Define a dictionary containing cryptocurrency wallet addresses
wallet_addresses = {
    "BTC": "your-bitcoin-wallet-address",
    "ETH": "your-ethereum-wallet-address",
    "LTC": "your-litecoin-wallet-address",
    # Add more cryptocurrencies and wallet addresses as needed
}

# Directory to save generated QR codes
output_directory = "crypto_qr_codes"

def generate_qr_code(data, output_path):
    """
    Generate a QR code for the given data and save it to the specified path.

    :param data: The data to encode in the QR code.
    :param output_path: File path to save the generated QR code.
    """
    try:
        # Create a QR code object with default settings
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code (1 is smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code
            border=4,  # Border size (minimum is 4)
        )
        qr.add_data(data)  # Add data to the QR code
        qr.make(fit=True)  # Generate the QR code

        # Create an image from the QR code object
        img = qr.make_image(fill_color="black", back_color="white")
        # Save the image to the specified path
        img.save(output_path)
    except Exception as e:
        print(f"Error generating QR code for data '{data}': {e}")

def main():
    """
    Main function to batch-generate QR codes for cryptocurrency wallet addresses.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate through the wallet addresses and generate QR codes
    for crypto, address in wallet_addresses.items():
        # Define the output path for the QR code image
        output_path = os.path.join(output_directory, f"{crypto}_wallet_qr.png")
        print(f"Generating QR code for {crypto} wallet address...")
        generate_qr_code(address, output_path)
        print(f"QR code saved to: {output_path}")

    print("QR code generation completed.")

if __name__ == "__main__":
    main()
```

This script generates QR codes for multiple cryptocurrency wallet addresses and saves them to a specified directory, following best practices for error handling, readability, and maintainability.
