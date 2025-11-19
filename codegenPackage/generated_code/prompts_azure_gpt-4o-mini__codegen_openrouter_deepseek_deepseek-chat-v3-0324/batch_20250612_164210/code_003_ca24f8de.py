"""
Generated Code Metadata:
========================
Original URL: https://usdt-qrcode-generator.com
Prompt: Provide an example of how to generate a QR code for USDT on the BNB blockchain using the features of the USDT QR Code Generator.
Generated: DETERMINISTIC_ca24f8de4ab3bd21
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from qrcode.constants import ERROR_CORRECT_L

def generate_usdt_bnb_qrcode(address: str, amount: float = None, memo: str = None) -> qrcode.QRCode:
    """
    Generates a QR code for USDT transactions on the BNB blockchain.
    
    Args:
        address (str): The recipient's BNB blockchain address.
        amount (float, optional): The amount of USDT to send. Defaults to None.
        memo (str, optional): Transaction memo. Defaults to None.
    
    Returns:
        qrcode.QRCode: Generated QR code object.
    
    Raises:
        ValueError: If address is empty or invalid.
    """
    if not address or not isinstance(address, str):
        raise ValueError("Invalid BNB address provided.")
    
    # Construct USDT payment URI according to BEP-20 standard
    uri = f"ethereum:{address}?token=USDT"
    
    if amount is not None:
        uri += f"&amount={amount}"
    
    if memo is not None:
        uri += f"&memo={memo}"
    
    # Configure QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(uri)
    qr.make(fit=True)
    
    return qr

# Example usage
if __name__ == "__main__":
    try:
        # Generate QR code for 100 USDT to a sample address
        qr = generate_usdt_bnb_qrcode(
            address="0x71C7656EC7ab88b098defB751B7401B5f6d8976F",
            amount=100,
            memo="Invoice #12345"
        )
        
        # Create and save the QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("usdt_bnb_qrcode.png")
        
    except ValueError as e:
        print(f"Error generating QR code: {e}")
```
