"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qr.to
Prompt: Write a Python script to generate a QR code for a USDT wallet address using libraries like `qrcode`. Ensure the script supports multiple blockchain formats (ERC-20, TRC-20, BEP-20, Omni, BEP-2).
Generated: DETERMINISTIC_6c4865df51ead9a3
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to generate a QR code for a USDT wallet address using the `qrcode` library.
The script supports multiple blockchain formats: ERC-20, TRC-20, BEP-20, Omni, BEP-2.
"""

import qrcode
import os

def generate_qr_code(wallet_address: str, blockchain_format: str, output_file: str):
    """
    Generate a QR code for a given USDT wallet address and blockchain format.

    Args:
        wallet_address (str): The USDT wallet address.
        blockchain_format (str): The blockchain format (ERC-20, TRC-20, BEP-20, Omni, BEP-2).
        output_file (str): The file path to save the generated QR code.

    Raises:
        ValueError: If the blockchain format is not supported.
        Exception: If there are issues during QR code generation or file saving.

    Returns:
        None
    """
    # Validate blockchain format
    supported_formats = {"ERC-20", "TRC-20", "BEP-20", "Omni", "BEP-2"}
    if blockchain_format not in supported_formats:
        raise ValueError(f"Unsupported blockchain format: {blockchain_format}. Supported formats are: {', '.join(supported_formats)}")
    
    # Generate the QR code data payload
    qr_data = {
        "wallet_address": wallet_address,
        "blockchain_format": blockchain_format
    }
    
    try:
        # Create a QR code object
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code (1 is the smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_M,  # Medium error correction
            box_size=10,  # Size of each box in the QR code
            border=4  # Border size (minimum is 4)
        )
        
        # Add data to the QR code
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        # Generate the QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the QR code image to the specified file
        img.save(output_file)
        print(f"QR code has been successfully saved to {output_file}")
    
    except Exception as e:
        raise Exception(f"An error occurred while generating or saving the QR code: {str(e)}")

if __name__ == "__main__":
    # Example usage
    try:
        # Wallet address and blockchain format input
        wallet_address = input("Enter the USDT wallet address: ").strip()
        blockchain_format = input("Enter the blockchain format (ERC-20, TRC-20, BEP-20, Omni, BEP-2): ").strip().upper()
        
        # Output file path
        output_file = "usdt_wallet_qr.png"
        
        # Generate the QR code
        generate_qr_code(wallet_address, blockchain_format, output_file)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Error: {e}")
```
