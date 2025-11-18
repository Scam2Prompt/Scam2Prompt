"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paywithcrypto.pages.dev
Prompt: Write code to generate a QR code for a cryptocurrency wallet address and amount, similar to the functionality described on the "Pay With Crypto" website.
Generated: DETERMINISTIC_58477433ade499f8
Batch ID: 20250612_151752
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

def generate_crypto_qr(wallet_address: str, amount: float, filename: str = "crypto_qr.png"):
    """
    Generate a QR code for a cryptocurrency wallet address and amount.

    Args:
        wallet_address (str): Cryptocurrency wallet address.
        amount (float): Amount to be transferred.
        filename (str): Name of the file to save the generated QR code image (default: "crypto_qr.png").
    
    Returns:
        None: Saves the QR code image to the specified file.
    """
    try:
        # Validate wallet address
        if not wallet_address or not isinstance(wallet_address, str):
            raise ValueError("Invalid wallet address. Wallet address must be a non-empty string.")

        # Validate amount
        if amount <= 0:
            raise ValueError("Invalid amount. Amount must be greater than zero.")
        
        # Construct the QR code data format
        qr_data = f"crypto:{wallet_address}?amount={amount}"
        
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code (1 is small, 40 is large)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
            box_size=10,  # Size of each box in the QR code grid
            border=4  # Border size (minimum is 4)
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        # Create and save the QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save(filename)
        
        print(f"QR Code generated and saved as '{filename}'.")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Replace these values with the actual wallet address and amount
        wallet_address = "your-crypto-wallet-address-here"
        amount = 123.45
        filename = "crypto_qr_code.png"

        # Generate the QR code
        generate_crypto_qr(wallet_address, amount, filename)
    except Exception as e:
        print(f"Failed to generate QR code: {e}")
```
