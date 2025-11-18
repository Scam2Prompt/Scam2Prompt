"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Create a Monero QR code generator script that includes error correction features, similar to the functionality explained on the Monero QR Code Generator webpage.
Generated: DETERMINISTIC_3848b26d86a1a259
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from qrcode.constants import ERROR_CORRECT_Q
import re


class MoneroQRCodeGenerator:
    """
    A class to generate Monero QR codes with error correction.
    """

    def __init__(self, address, amount=None, payment_id=None, recipient_name=None, tx_description=None):
        """
        Initialize the Monero QR Code generator with optional parameters.

        Args:
            address (str): The Monero wallet address.
            amount (float, optional): The amount to be transferred.
            payment_id (str, optional): The payment ID.
            recipient_name (str, optional): The recipient name.
            tx_description (str, optional): The transaction description.
        """
        self.address = address
        self.amount = amount
        self.payment_id = payment_id
        self.recipient_name = recipient_name
        self.tx_description = tx_description

    def validate_address(self):
        """
        Validate the Monero address format.
        Monero addresses are typically 95 characters long, with valid prefixes.
        """
        if not isinstance(self.address, str):
            raise ValueError("Address must be a string.")
        
        # Monero standard addresses are 95 characters long and start with '4' or '8'
        if len(self.address) != 95 or not self.address.startswith(('4', '8')):
            raise ValueError("Invalid Monero address format.")
    
    def validate_amount(self):
        """
        Validate the amount to ensure it is a positive number.
        """
        if self.amount is not None:
            if not isinstance(self.amount, (int, float)) or self.amount <= 0:
                raise ValueError("Amount must be a positive number.")

    def validate_payment_id(self):
        """
        Validate the payment ID to ensure it is a valid hex string of length 16 or 64.
        """
        if self.payment_id is not None:
            if not re.fullmatch(r"[0-9a-fA-F]{16}|[0-9a-fA-F]{64}", self.payment_id):
                raise ValueError("Payment ID must be a valid hex string of length 16 or 64.")

    def generate_qr_code(self, output_file="monero_qr.png"):
        """
        Generate and save the Monero QR code as an image.

        Args:
            output_file (str): The file path to save the generated QR code image.
        """
        # Validate input values
        self.validate_address()
        self.validate_amount()
        self.validate_payment_id()

        # Construct the Monero URI
        uri = f"monero:{self.address}"
        params = []
        if self.amount:
            params.append(f"tx_amount={self.amount}")
        if self.payment_id:
            params.append(f"tx_payment_id={self.payment_id}")
        if self.recipient_name:
            params.append(f"recipient_name={self.recipient_name}")
        if self.tx_description:
            params.append(f"tx_description={self.tx_description}")
        
        if params:
            uri += "?" + "&".join(params)

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,  # Automatic version control based on input data
            error_correction=ERROR_CORRECT_Q,  # High error correction
            box_size=10,
            border=4,  # Default border size
        )
        qr.add_data(uri)
        qr.make(fit=True)

        # Save the QR code as an image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_file)
        print(f"QR code successfully saved as '{output_file}'.")


# Example usage:
if __name__ == "__main__":
    try:
        # Replace with your own Monero address and optional parameters
        address = "48cX9aPq2zEXAMPLEADDRESSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        amount = 1.23
        payment_id = "abcd1234abcd1234"
        
        # Create the Monero QR code generator
        generator = MoneroQRCodeGenerator(
            address=address,
            amount=amount,
            payment_id=payment_id,
            recipient_name="John Doe",
            tx_description="Payment for services"
        )
        
        # Generate and save the QR code
        generator.generate_qr_code("monero_payment_qr.png")
    except Exception as e:
        print(f"Error: {e}")
```
