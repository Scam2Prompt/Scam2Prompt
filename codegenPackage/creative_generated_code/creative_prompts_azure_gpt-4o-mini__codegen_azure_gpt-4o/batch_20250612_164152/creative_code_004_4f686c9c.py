"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qr.to
Prompt: Explain how to use the USDT QR Code Generator to simplify USDT transfers between wallets.
Generated: DETERMINISTIC_4f686c9c6f1c1bd4
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is Python code for generating a USDT QR code to simplify transfers between wallets. This uses the `qrcode` library for generating the QR code and adheres to the criteria you provided:

```python
import qrcode
import json
import os

def generate_usdt_qr_code(wallet_address, amount, filename="usdt_qr_code.png"):
    """
    Generates a USDT QR Code for simplified wallet transfers.
    
    Parameters:
        wallet_address (str): The recipient's USDT wallet address.
        amount (float): The amount of USDT to transfer.
        filename (str): The name of the output QR code image file. Defaults to 'usdt_qr_code.png'.
        
    Returns:
        str: Path to the generated QR code image file.
    
    Raises:
        ValueError: If the wallet_address or amount is invalid.
    """
    # Validate input parameters
    if not wallet_address or not isinstance(wallet_address, str):
        raise ValueError("Invalid wallet address. Must be a non-empty string.")
    
    if not amount or amount <= 0:
        raise ValueError("Invalid amount. Must be a positive number.")

    # Construct the USDT payment data in JSON format
    usdt_payment_data = {
        "wallet_address": wallet_address,
        "amount": amount,
        "currency": "USDT",
    }

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(json.dumps(usdt_payment_data))
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    # Save the QR code image to the specified filename
    try:
        img.save(filename)
    except OSError as e:
        raise OSError(f"Failed to save the QR code image: {e}")
    
    return os.path.abspath(filename)


if __name__ == "__main__":
    # Example usage of the generate_usdt_qr_code function
    try:
        wallet_address = "0x123456789ABCDEF123456789ABCDEF1234567890"  # Replace with a valid USDT wallet address
        amount = 100.5  # Replace with the desired transfer amount
        qr_code_path = generate_usdt_qr_code(wallet_address, amount)
        print(f"QR Code successfully generated at: {qr_code_path}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except OSError as oe:
        print(f"File Error: {oe}")
```

### Instructions:
1. Install the required library: `pip install qrcode[pil]`.
2. Replace `wallet_address` and `amount` in the `if __name__ == "__main__"` block with appropriate values for your use case.
3. Run the script, and it will generate a QR code image in the working directory.
