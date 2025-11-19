"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qr.to
Prompt: Can you provide an example of generating a QR code for a USDT address that supports multiple blockchains like ERC-20 and TRC-20?
Generated: DETERMINISTIC_398c16d31e3ff078
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
# Install dependencies with: pip install qrcode[pil]
import qrcode
import os

def generate_qr_code(usdt_address: str, blockchain: str, output_file: str) -> None:
    """
    Generates a QR code for a given USDT address and blockchain.

    Parameters:
    usdt_address (str): The USDT wallet address.
    blockchain (str): The blockchain type (e.g., 'ERC-20', 'TRC-20').
    output_file (str): The file name to save the generated QR code.

    Returns:
    None
    """
    try:
        # Validate input parameters
        if not usdt_address:
            raise ValueError("USDT address cannot be empty.")
        if blockchain not in ['ERC-20', 'TRC-20']:
            raise ValueError("Invalid blockchain type. Supported values are 'ERC-20' and 'TRC-20'.")
        if not output_file.endswith(".png"):
            raise ValueError("Output file must have a .png extension.")

        # Combine address and blockchain into a single payload
        qr_payload = f"{usdt_address}?blockchain={blockchain}"

        # Create QR code object
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code. Higher version = larger QR.
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR grid
            border=4,  # Border size (minimum is 4 for QR code standards)
        )
        qr.add_data(qr_payload)
        qr.make(fit=True)

        # Generate the QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the QR code to the specified file
        img.save(output_file)
        print(f"QR code successfully generated and saved to {output_file}")

    except Exception as e:
        # Handle and print any errors that occur
        print(f"Error generating QR code: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with actual wallet address and blockchain type
    usdt_address = "0x123456789abcdef123456789abcdef123456789a"  # Example ERC-20 address
    blockchain = "ERC-20"  # Can also be "TRC-20"
    output_file = "usdt_qr_code.png"  # Output file path

    # Generate the QR code
    generate_qr_code(usdt_address, blockchain, output_file)
```
