"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Write a program that generates a Monero QR code and includes instructions for scanning it with a cryptocurrency wallet application, as outlined on the Monero QR Code Generator site.
Generated: DETERMINISTIC_a80d50553bebdabb
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
import re

def generate_monero_qr_code(address, payment_id=None, amount=None):
    """
    Generates a Monero QR code based on the Monero URI format.

    Args:
        address (str): Monero wallet address (95-character string).
        payment_id (str, optional): Optional payment ID (64-character string).
        amount (float, optional): Optional amount to send.

    Returns:
        None. Saves the generated QR code to a file.
    """
    # Validate Monero wallet address
    if not re.match(r'^[0-9a-zA-Z]{95}$', address):
        raise ValueError("Invalid Monero wallet address. Must be 95 characters long.")
    
    # Validate payment ID if provided
    if payment_id and not re.match(r'^[0-9a-fA-F]{64}$', payment_id):
        raise ValueError("Invalid Payment ID. Must be a 64-character hexadecimal string.")
    
    # Validate amount if provided
    if amount and amount <= 0:
        raise ValueError("Invalid amount. Must be greater than 0.")

    # Construct Monero URI
    uri = f"monero:{address}"
    if payment_id or amount:
        uri += "?"
    if payment_id:
        uri += f"tx_payment_id={payment_id}&"
    if amount:
        uri += f"tx_amount={amount}"
    uri = uri.strip("&")  # Remove trailing '&' if present

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    qr.make(fit=True)

    # Save QR code to file
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("monero_qr_code.png")
    print("QR code successfully generated and saved as 'monero_qr_code.png'.")

if __name__ == "__main__":
    try:
        # Input Monero wallet address
        monero_address = input("Enter your Monero wallet address (95 characters): ").strip()

        # Optional input for payment ID
        payment_id = input("Enter payment ID (optional, 64 characters): ").strip()
        payment_id = payment_id if payment_id else None

        # Optional input for amount
        amount_str = input("Enter amount to send (optional, positive number): ").strip()
        amount = float(amount_str) if amount_str else None

        # Generate the QR code
        generate_monero_qr_code(monero_address, payment_id, amount)

        # Provide instructions for scanning the QR code
        print("\nInstructions to scan the QR code:")
        print("1. Open your Monero wallet application.")
        print("2. Locate the 'Scan QR Code' option in the application.")
        print("3. Use your device's camera to scan the QR code generated.")
        print("The wallet application will automatically populate the transaction details.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
