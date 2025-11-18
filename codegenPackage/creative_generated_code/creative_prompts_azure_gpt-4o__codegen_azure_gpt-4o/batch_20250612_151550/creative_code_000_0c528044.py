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
import re

def is_valid_bech32_address(address: str) -> bool:
    """
    Validate a Bech32 Bitcoin address using regex.
    Bech32 addresses start with 'bc1' and can contain alphanumeric characters.
    Returns True if valid, False otherwise.
    """
    bech32_regex = r'^bc1[0-9a-z]{6,87}$'  # Matches Bech32 address format.
    return re.match(bech32_regex, address) is not None

def generate_bitcoin_qr(bech32_address: str, amount: float = None) -> None:
    """
    Generate a Bitcoin QR code using a Bech32 address.
    
    Parameters:
      bech32_address (str): Bech32 formatted Bitcoin address.
      amount (float): Optional transaction amount to include in the QR code.
    """
    try:
        # Validate the Bech32 Bitcoin address.
        if not is_valid_bech32_address(bech32_address):
            raise ValueError("Invalid Bech32 Bitcoin address.")

        # Construct the Bitcoin URI scheme.
        bitcoin_uri = f"bitcoin:{bech32_address}"
        if amount:
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            bitcoin_uri += f"?amount={amount}"

        # Generate the QR code.
        qr_code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_code.add_data(bitcoin_uri)
        qr_code.make(fit=True)

        # Save the QR code as an image file.
        img = qr_code.make_image(fill_color="black", back_color="white")
        img_filename = "bitcoin_qr_code.png"
        img.save(img_filename)

        print(f"QR code successfully generated and saved as '{img_filename}'.")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Replace with a valid Bech32 Bitcoin address
    example_address = "bc1qy8e3mt5whuy4lhq9m9h5v8x2kegx6r4wyqs5fe"
    example_amount = 0.001  # Example transaction amount (optional)
    generate_bitcoin_qr(example_address, example_amount)
```
