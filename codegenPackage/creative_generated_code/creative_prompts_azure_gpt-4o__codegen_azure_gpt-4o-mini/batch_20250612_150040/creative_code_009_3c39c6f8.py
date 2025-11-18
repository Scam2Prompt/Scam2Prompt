"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Write code to generate a Monero QR code and explain how to use it for anonymous donations, referencing the features described on the Monero QR Code Generator website.
Generated: DETERMINISTIC_3c39c6f8dc5594bc
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
import os
import sys

def generate_monero_qr(wallet_address, amount=None, tx_note=None):
    """
    Generates a QR code for a Monero donation.

    Parameters:
    wallet_address (str): The Monero wallet address to which donations will be sent.
    amount (float, optional): The amount of Monero to request (if any).
    tx_note (str, optional): A note or message to include with the transaction.

    Returns:
    str: The file path of the generated QR code image.
    """
    
    # Validate wallet address
    if not isinstance(wallet_address, str) or len(wallet_address) == 0:
        raise ValueError("Invalid wallet address provided.")

    # Create the Monero payment URI
    payment_uri = f"monero:{wallet_address}"
    if amount is not None:
        payment_uri += f"?tx_amount={amount}"
    if tx_note is not None:
        payment_uri += f"&tx_notes={tx_note}"

    # Generate QR Code
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(payment_uri)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill='black', back_color='white')

        # Define the output path
        output_path = 'monero_donation_qr.png'
        img.save(output_path)

        print(f"QR Code generated successfully: {output_path}")
        return output_path

    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        # Example usage
        wallet_address = "YOUR_MONERO_WALLET_ADDRESS"  # Replace with your Monero wallet address
        amount = 0.1  # Optional: specify the desired amount in Monero
        tx_note = "Thank you for your support!"  # Optional: specify a transaction note

        # Generate the QR code for donations
        generate_monero_qr(wallet_address, amount, tx_note)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
```

### Usage Instructions:
1. Replace `YOUR_MONERO_WALLET_ADDRESS` in the code with your actual Monero wallet address.
2. Optionally specify the donation amount and transaction note.
3. Run the script. A QR code image (`monero_donation_qr.png`) will be generated in the current directory.
4. Share the generated QR code with potential donors for anonymous donations. Donors can scan the QR code to send funds directly to your Monero wallet.
