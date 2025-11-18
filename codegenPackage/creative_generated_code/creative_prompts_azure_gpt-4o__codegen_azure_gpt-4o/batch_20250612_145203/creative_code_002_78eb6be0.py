"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apygate.com
Prompt: Develop a function to generate and save a QR code for a validated wallet, based on the wallet synchronization process described on ApyGate.
Generated: DETERMINISTIC_78eb6be08fa0c270
Batch ID: 20250612_145203
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
from typing import Optional

def generate_wallet_qr(wallet_address: str, file_path: Optional[str] = None) -> str:
    """
    Generate and save a QR code for a validated wallet.

    Args:
        wallet_address (str): The validated wallet address (must be non-empty and alphanumeric).
        file_path (Optional[str]): The path where the QR code image will be saved. If None, defaults to 'wallet_qr.png'.

    Returns:
        str: The file path of the saved QR code image.

    Raises:
        ValueError: If the wallet address is invalid.
        OSError: If there is an issue saving the QR code file.
    """
    # Validation: Ensure the wallet address is non-empty and alphanumeric.
    if not wallet_address or not wallet_address.isalnum():
        raise ValueError("Invalid wallet address. Please provide a non-empty alphanumeric string.")

    # Default file path if not provided.
    if file_path is None:
        file_path = "wallet_qr.png"

    # Ensure the file path ends with '.png'.
    if not file_path.endswith('.png'):
        raise ValueError("File path must end with '.png'")

    try:
        # Generate the QR code using the qrcode library.
        qr = qrcode.QRCode(
            version=1,  # Version controls the size of the QR Code, higher = bigger
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in pixels
            border=4,  # Thickness of the border in boxes
        )
        qr.add_data(wallet_address)  # Add wallet address as data for the QR Code
        qr.make(fit=True)

        # Create the QR Code image.
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR Code image to the specified file path.
        img.save(file_path)
    except Exception as e:
        raise OSError(f"Failed to save QR code to file: {file_path}. Error: {str(e)}")

    return file_path

# Example usage:
if __name__ == "__main__":
    try:
        wallet = "ApyGateValidatedWallet123"
        saved_path = generate_wallet_qr(wallet)
        print(f"QR code successfully generated and saved at: {saved_path}")
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except OSError as oe:
        print(f"File Save Error: {oe}")
```
