"""
Generated Code Metadata:
========================
Original URL: https://monero-qr-code-generator.com
Prompt: Generate a Python script that creates a Monero QR Code for a specified amount of XMR using the Monero QR Code Generator.
Generated: DETERMINISTIC_000402106e166b2a
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
import sys

def generate_monero_qr_code(address, amount, payment_id=None, recipient_name=None, tx_description=None, output_file="monero_qr.png"):
    """
    Generates a Monero QR Code for a specified amount and saves it as an image file.

    Parameters:
        address (str): The Monero wallet address.
        amount (float): The amount of XMR to be sent.
        payment_id (str, optional): Optional payment ID for the transaction.
        recipient_name (str, optional): Optional recipient name.
        tx_description (str, optional): Optional transaction description.
        output_file (str): The name of the output file for the QR code image.

    Returns:
        None
    """
    try:
        # Validate inputs
        if not address or not isinstance(address, str):
            raise ValueError("Invalid Monero address provided.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")

        # Construct the Monero URI
        monero_uri = f"monero:{address}?amount={amount}"
        if payment_id:
            monero_uri += f"&payment_id={payment_id}"
        if recipient_name:
            monero_uri += f"&recipient_name={recipient_name}"
        if tx_description:
            monero_uri += f"&tx_description={tx_description}"

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(monero_uri)
        qr.make(fit=True)

        # Save the QR code as an image file
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_file)

        print(f"Monero QR Code successfully generated and saved as '{output_file}'.")

    except Exception as e:
        print(f"Error generating Monero QR Code: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Example usage
    # Replace these values with your own Monero address and amount
    monero_address = "YOUR_MONERO_ADDRESS_HERE"
    xmr_amount = 0.5  # Example amount in XMR

    # Optional parameters
    payment_id = None
    recipient_name = None
    tx_description = None

    # Generate the QR code
    generate_monero_qr_code(
        address=monero_address,
        amount=xmr_amount,
        payment_id=payment_id,
        recipient_name=recipient_name,
        tx_description=tx_description,
        output_file="monero_qr.png"
    )
```
