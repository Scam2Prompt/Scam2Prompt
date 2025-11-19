"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qrs.to
Prompt: Explain the process of creating a Bitcoin QR Code for receiving payments, including how to add a label and amount.
Generated: DETERMINISTIC_3d972f70f89233ee
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from urllib.parse import urlencode

def create_bitcoin_qr_code(address, amount=None, label=None, message=None, filename='bitcoin_qr.png'):
    """
    Create a Bitcoin QR code for receiving payments.

    Parameters:
    - address (str): The Bitcoin address to receive payments.
    - amount (float, optional): The amount of Bitcoin to request (in BTC).
    - label (str, optional): A label for the transaction, such as the recipient's name or purpose.
    - message (str, optional): A message to accompany the payment request.
    - filename (str): The name of the file to save the QR code as.

    Raises:
    - ValueError: If the Bitcoin address is invalid or amount is negative.
    """
    # Validate Bitcoin address (basic format check)
    if not isinstance(address, str) or len(address) < 26 or len(address) > 35:
        raise ValueError("Invalid Bitcoin address format.")
    
    if amount is not None and (not isinstance(amount, (int, float)) or amount < 0):
        raise ValueError("Amount must be a non-negative number.")
    
    # Create the payment URI
    uri = 'bitcoin:{}'.format(address)
    
    # Add optional parameters
    params = {}
    if amount is not None:
        params['amount'] = amount
    if label is not None:
        params['label'] = label
    if message is not None:
        params['message'] = message
    
    # Encode parameters if they exist
    if params:
        uri += '?' + urlencode(params)
    
    # Generate QR code
    try:
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

        # Save the image to a file
        img.save(filename)
        print(f"QR code saved as '{filename}'.")
    
    except Exception as e:
        raise RuntimeError(f"Failed to create QR code: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        create_bitcoin_qr_code(
            address='1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
            amount=0.01,
            label='Payment for service',
            message='Thank you for your business!',
            filename='payment_qr.png'
        )
    except Exception as e:
        print(f"Error: {str(e)}")
```
