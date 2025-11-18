"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qr.to
Prompt: Provide an example of how to use the `qrcode` Python library to generate a QR code for a Tether (USDT) wallet address and explain how to ensure the QR code works across blockchain formats like ERC-20, TRC-20, BEP-20, Omni, and BEP-2.
Generated: DETERMINISTIC_6619341d74e603f8
Batch ID: 20250612_150040
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

def generate_qr_code(wallet_address: str, output_file: str) -> None:
    """
    Generates a QR code for a given wallet address and saves it to a file.

    Parameters:
    wallet_address (str): The wallet address for which to generate the QR code.
    output_file (str): The file path where the QR code image will be saved.

    Raises:
    ValueError: If the wallet_address is empty or invalid.
    """

    # Validate the wallet address
    if not wallet_address:
        raise ValueError("The wallet address cannot be empty.")
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # Size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(wallet_address)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Check if the output directory exists, if not, create it
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the QR code image
    img.save(output_file)
    print(f"QR code generated and saved to {output_file}")

if __name__ == "__main__":
    # Example usage
    try:
        # Replace with your actual USDT wallet address (ERC-20, TRC-20, BEP-20, Omni, BEP-2)
        wallet_address = "your_usdt_wallet_address_here"
        output_file = "usdt_wallet_qr.png"

        generate_qr_code(wallet_address, output_file)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
