"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinqr.io
Prompt: Generate Python code to create a Bitcoin QR code using the Bech32 address format, ensuring compatibility with modern wallet apps.
Generated: DETERMINISTIC_0c528044d9168e81
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
import segno

def create_bech32_qr_code(address: str, filename: str) -> None:
    """
    Generates a QR code for a given Bitcoin Bech32 address and saves it as an image file.

    Args:
        address (str): The Bitcoin Bech32 address to encode in the QR code.
        filename (str): The filename (including path) to save the QR code image.

    Raises:
        ValueError: If the provided address is not a valid Bech32 address.
        Exception: For any unexpected errors during QR code generation or file saving.
    """
    # Validate the Bech32 address
    if not is_valid_bech32_address(address):
        raise ValueError("Invalid Bech32 address provided.")

    try:
        # Generate the QR code
        qr = segno.make(address)
        
        # Save the QR code to a file
        qr.save(filename)
        print(f"QR code saved as {filename}")
    except Exception as e:
        raise Exception(f"An error occurred while generating the QR code: {str(e)}")

def is_valid_bech32_address(address: str) -> bool:
    """
    Validates a Bitcoin Bech32 address.

    Args:
        address (str): The Bitcoin Bech32 address to validate.

    Returns:
        bool: True if the address is valid, False otherwise.
    """
    try:
        # Check if the address follows the Bech32 format
        if not (address.startswith('bc1') or address.startswith('tb1')):
            return False
        
        # Decode the address and validate its structure
        # Using segno library for Bech32 verification
        segno.decode_bech32(address)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    # Example usage
    bech32_address = "bc1qw508d6qejxtdg4y5r3zjv0sne5nkh8eeg7d8q3"  # Replace with your Bech32 address
    output_file = "bitcoin_qr_code.png"  # Desired output filename

    try:
        create_bech32_qr_code(bech32_address, output_file)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
