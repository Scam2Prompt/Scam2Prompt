"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qr.to
Prompt: Create a script that generates a Bitcoin QR Code with a specified amount and label, following the URI scheme for Bitcoin transactions explained on coin-qr.to.
Generated: DETERMINISTIC_ef1bdaef47d4e7e8
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from qrcode.constants import ERROR_CORRECT_L
import sys

def generate_bitcoin_qr(output_file: str, address: str, amount: float, label: str):
    """
    Generates a Bitcoin QR Code based on the URI scheme.

    Parameters:
        output_file (str): The path to save the generated QR code image.
        address (str): The Bitcoin address.
        amount (float): The amount of Bitcoin to be sent.
        label (str): A label to identify the transaction.
    """
    try:
        # Validate input parameters
        if not address:
            raise ValueError("Bitcoin address must not be empty.")
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if not label:
            raise ValueError("Label must not be empty.")

        # Construct the Bitcoin URI following the Bitcoin URI scheme
        # Format: bitcoin:<address>?amount=<amount>&label=<label>
        bitcoin_uri = f"bitcoin:{address}?amount={amount}&label={label}"

        # Create a QR code generator instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code, 1 is the smallest.
            error_correction=ERROR_CORRECT_L,  # Error correction level.
            box_size=10,  # Size of each box in the QR Code grid.
            border=4,  # Border size (minimum is 4).
        )

        # Add the Bitcoin URI to the QR code
        qr.add_data(bitcoin_uri)
        qr.make(fit=True)

        # Generate the QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to the specified file
        img.save(output_file)
        print(f"QR Code successfully saved to {output_file}")

    except Exception as e:
        # Handle and print any errors that occur during execution
        print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Example usage with user-specified parameters
    # Replace these values with actual inputs for production use
    bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Replace with a valid Bitcoin address
    bitcoin_amount = 0.005  # Replace with the desired amount
    transaction_label = "Donation"  # Replace with the desired label
    qr_output_file = "bitcoin_qr.png"  # Replace with the desired output file name

    # Generate the Bitcoin QR Code
    generate_bitcoin_qr(qr_output_file, bitcoin_address, bitcoin_amount, transaction_label)
```
