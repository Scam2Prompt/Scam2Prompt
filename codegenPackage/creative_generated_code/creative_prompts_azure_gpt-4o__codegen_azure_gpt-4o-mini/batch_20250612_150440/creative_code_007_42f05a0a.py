"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qr.to
Prompt: Provide an example of how to create a QR Code for Bitcoin transactions that includes both the recipient's address and the requested amount, as explained on coin-qr.to.
Generated: DETERMINISTIC_42f05a0a1ca445f9
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode  # Import the qrcode library
from qrcode.exceptions import QRCodeException

def create_bitcoin_qr_code(recipient_address: str, amount: float, filename: str) -> None:
    """
    Create a QR code for a Bitcoin transaction.

    Parameters:
    recipient_address (str): The Bitcoin address of the recipient.
    amount (float): The amount of Bitcoin to be sent.
    filename (str): The filename for saving the generated QR code image.

    Raises:
    ValueError: If the recipient address or filename is invalid.
    QRCodeException: If there is an error generating the QR code.
    """

    # Validate inputs
    if not isinstance(recipient_address, str) or not recipient_address.strip():
        raise ValueError("Invalid recipient address provided.")
    
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if not isinstance(filename, str) or not filename.strip():
        raise ValueError("Invalid filename provided.")

    # Create the Bitcoin URI
    uri = f"bitcoin:{recipient_address}?amount={amount}"

    try:
        # Generate the QR Code
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code
            border=4,  # Size of the border (minimum is 4)
        )
        
        qr.add_data(uri)
        qr.make(fit=True)  # Fit the QR Code to the data
        
        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image to a file
        img.save(filename)
        print(f"QR code generated and saved as {filename}")

    except QRCodeException as e:
        print(f"Error generating QR code: {e}")

# Example usage
if __name__ == "__main__":
    try:
        create_bitcoin_qr_code("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", 0.01, "bitcoin_qr.png")
    except Exception as e:
        print(f"An error occurred: {e}")
```
