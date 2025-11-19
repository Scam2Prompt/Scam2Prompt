"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qrcode-generator.com
Prompt: Write a script that utilizes the USDT QR Code Generator to create a QR code for USDT transactions on the Tron network.
Generated: DETERMINISTIC_0a5121a082b1f6b2
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import sys

def generate_usdt_qr(address: str, amount: float) -> str:
    """
    Generates a QR code for a USDT transaction on the Tron network.

    Parameters:
    address (str): The recipient's wallet address (Tron network).
    amount (float): The amount of USDT to transfer.

    Returns:
    str: The file path of the generated QR code image.
    """
    try:
        # Validate inputs
        if not address or not isinstance(address, str):
            raise ValueError("Invalid wallet address provided.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Format the payment URI (Tron network USDT)
        payment_uri = f"tron:{address}?amount={amount}"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,  # QR code version (adjusts the size)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code
            border=4  # Border size
        )
        qr.add_data(payment_uri)
        qr.make(fit=True)

        # Create an image of the QR code
        image = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image
        file_path = f"usdt_qr_{address[:10]}_{amount}.png"  # Unique file name
        image.save(file_path)

        return file_path

    except Exception as e:
        print(f"Error generating QR code: {e}", file=sys.stderr)
        raise


if __name__ == "__main__":
    try:
        # Example usage
        wallet_address = input("Enter the recipient's Tron wallet address: ").strip()
        usdt_amount = float(input("Enter the amount of USDT to transfer: ").strip())

        # Generate the QR code
        qr_file_path = generate_usdt_qr(wallet_address, usdt_amount)
        print(f"QR code successfully generated and saved to: {qr_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
```
