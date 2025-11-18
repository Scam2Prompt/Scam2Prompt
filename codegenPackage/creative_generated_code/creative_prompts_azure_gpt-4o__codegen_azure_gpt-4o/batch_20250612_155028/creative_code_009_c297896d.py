"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://validatewalletconnect.vercel.app
Prompt: Create a function to validate wallets during a presale event and generate QR codes for secure transactions using the Wallet Sphere protocol.
Generated: DETERMINISTIC_c297896d3b8d8784
Batch ID: 20250612_155028
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

def validate_wallet_address(wallet_address):
    """
    Validates the given wallet address based on the Wallet Sphere protocol.
    Ensures the wallet address meets the expected format.

    Args:
        wallet_address (str): The wallet address to validate.

    Returns:
        bool: True if the wallet address is valid, otherwise False.
    """
    # Wallet Sphere protocol expects alphanumeric strings of 42 characters starting with '0x'
    wallet_regex = r'^0x[a-fA-F0-9]{40}$'
    if not wallet_address or not re.match(wallet_regex, wallet_address):
        return False
    return True


def generate_qr_code(data, output_file):
    """
    Generates a QR code from the given data and saves it to the specified file.

    Args:
        data (str): The data to encode in the QR code.
        output_file (str): The file path to save the QR code image.

    Raises:
        Exception: If there is an error while generating or saving the QR code.
    """
    try:
        # Create QR code object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Generate QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_file)
    except Exception as e:
        raise Exception(f"Error while generating QR code: {e}")


def process_wallet_for_presale(wallet_address):
    """
    Validates the wallet address and generates a QR code for the presale event.

    Args:
        wallet_address (str): The wallet address to validate.

    Returns:
        str: File path of the generated QR code if the wallet address is valid.

    Raises:
        ValueError: If the wallet address is invalid.
    """
    # Validate the wallet address
    if not validate_wallet_address(wallet_address):
        raise ValueError("Invalid wallet address. Please provide a valid Wallet Sphere address.")

    # Generate QR code and save to file
    qr_code_file = f"{wallet_address}_qr.png"
    try:
        generate_qr_code(wallet_address, qr_code_file)
    except Exception as e:
        raise Exception(f"Failed to generate QR code: {e}")

    return qr_code_file


if __name__ == "__main__":
    # Example usage
    wallet_address = input("Enter wallet address: ").strip()

    try:
        qr_code_path = process_wallet_for_presale(wallet_address)
        print(f"QR code generated successfully: {qr_code_path}")
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
