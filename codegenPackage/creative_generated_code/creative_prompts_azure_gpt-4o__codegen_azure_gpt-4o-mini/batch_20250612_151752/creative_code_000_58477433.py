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
import os

def generate_qr_code(wallet_address: str, amount: float, currency: str = 'BTC') -> str:
    """
    Generates a QR code for a cryptocurrency wallet address and amount.
    
    Parameters:
    wallet_address (str): The cryptocurrency wallet address.
    amount (float): The amount to be sent.
    currency (str): The cryptocurrency type (default is Bitcoin 'BTC').
    
    Returns:
    str: The file path of the saved QR code image.
    
    Raises:
    ValueError: If wallet_address is invalid or amount is not positive.
    """
    
    # Validate the wallet address
    if not isinstance(wallet_address, str) or len(wallet_address) < 26 or len(wallet_address) > 35:
        raise ValueError("Invalid wallet address.")
    
    # Validate the amount
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Amount must be a positive number.")
    
    # Create the URI for the QR code
    uri = f"{currency}:{wallet_address}?amount={amount}"
    
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Define the output file path
    output_file_path = f"{wallet_address}_qr.png"
    
    # Save the QR code image
    img.save(output_file_path)
    
    return output_file_path

# Example Usage
if __name__ == "__main__":
    try:
        address = "your_wallet_address_here"  # Replace with actual wallet address
        amount = 0.01  # Example amount
        qr_file_path = generate_qr_code(address, amount)
        print(f"QR code generated and saved to: {qr_file_path}")
    except Exception as e:
        print(f"Error: {e}")
```
