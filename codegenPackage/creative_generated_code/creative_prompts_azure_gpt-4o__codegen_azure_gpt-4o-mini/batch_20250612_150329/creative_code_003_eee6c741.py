"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-qr-code-generator.com
Prompt: Create a Python script that generates an Ethereum QR code and saves it as an image file, as described on the Ethereum QR Code Generator site.
Generated: DETERMINISTIC_eee6c74194d6e98f
Batch ID: 20250612_150329
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

def generate_ethereum_qr(address: str, file_name: str) -> None:
    """
    Generates a QR code for an Ethereum address and saves it as an image file.

    Parameters:
        address (str): The Ethereum address to encode in the QR code.
        file_name (str): The name of the output image file (should end with .png).

    Raises:
        ValueError: If the address format is incorrect or if the file name is invalid.
    """
    # Validate Ethereum address format
    if not isinstance(address, str) or len(address) != 42 or not address.startswith('0x'):
        raise ValueError("Invalid Ethereum address. It must start with '0x' and be 42 characters long.")
    
    # Validate file name
    if not isinstance(file_name, str) or not file_name.endswith('.png'):
        raise ValueError("Invalid file name. It must be a string ending with '.png'.")

    # Create a QR code instance with the Ethereum URI format
    uri = f'ethereum:{address}'
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10, border=4)
    qr.add_data(uri)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(file_name)
    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    try:
        # Example usage: replace with a valid Ethereum address and desired file name
        eth_address = "0xYourEthereumAddressHere"
        output_file_name = "ethereum_qr_code.png"
        
        generate_ethereum_qr(eth_address, output_file_name)
    except Exception as e:
        print(f"An error occurred: {e}")
```
