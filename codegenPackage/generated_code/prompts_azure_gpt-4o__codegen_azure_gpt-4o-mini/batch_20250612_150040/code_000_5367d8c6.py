"""
Generated Code Metadata:
========================
Original URL: https://monero-qr-code-generator.com
Prompt: Write Python code to generate a Monero QR code using the functionality described on the Monero QR Code Generator website. Ensure the QR code can be saved locally as an image file.
Generated: DETERMINISTIC_5367d8c6a8cd8a96
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
import os

def generate_monero_qr(address: str, amount: float = 0.0, payment_id: str = None, filename: str = "monero_qr.png") -> None:
    """
    Generate a Monero QR code and save it as an image file.

    Parameters:
    - address (str): The Monero wallet address.
    - amount (float): The amount of Monero to be sent (default is 0.0).
    - payment_id (str): Optional payment ID for the transaction.
    - filename (str): The name of the file to save the QR code image (default is 'monero_qr.png').

    Raises:
    - ValueError: If the address is invalid or if the amount is negative.
    - Exception: For any other errors during QR code generation or file saving.
    """

    # Validate the Monero address
    if not isinstance(address, str) or len(address) == 0:
        raise ValueError("Invalid Monero address provided.")
    
    # Validate the amount
    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    # Construct the Monero URI
    uri = f"monero:{address}"
    if amount > 0:
        uri += f"?amount={amount}"
    if payment_id:
        uri += f"&tx_payment_id={payment_id}"

    try:
        # Generate the QR code
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
        print(f"QR code saved as {filename}")

    except Exception as e:
        raise Exception(f"An error occurred while generating the QR code: {e}")

# Example usage
if __name__ == "__main__":
    try:
        generate_monero_qr(address="43g1...your_monero_address_here...", amount=0.1, payment_id="abcd1234")
    except Exception as e:
        print(f"Error: {e}")
```
