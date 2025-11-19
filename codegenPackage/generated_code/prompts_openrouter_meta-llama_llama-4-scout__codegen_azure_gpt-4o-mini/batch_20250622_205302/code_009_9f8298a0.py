"""
Generated Code Metadata:
========================
Original URL: https://bitcoinqr.io
Prompt: Develop a simple Bitcoin QR code generator application using a programming language of your choice, incorporating the technical insights from the bitcoinqr.io website.
Generated: DETERMINISTIC_9f8298a087d10475
Batch ID: 20250622_205302
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

def generate_bitcoin_qr(address, amount=None, label=None, message=None):
    """
    Generate a Bitcoin QR code.

    Parameters:
    - address (str): The Bitcoin address to encode in the QR code.
    - amount (float, optional): The amount of Bitcoin to send.
    - label (str, optional): A label for the transaction.
    - message (str, optional): A message to include with the transaction.

    Returns:
    - str: The file path of the generated QR code image.
    """
    # Validate the Bitcoin address format
    if not is_valid_bitcoin_address(address):
        raise ValueError("Invalid Bitcoin address format.")

    # Construct the Bitcoin URI
    uri = f"bitcoin:{address}"
    if amount:
        uri += f"?amount={amount}"
    if label:
        uri += f"&label={label}"
    if message:
        uri += f"&message={message}"

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

    # Define the output file path
    output_file = os.path.join(os.getcwd(), f"{address}_qr.png")

    # Save the image
    img.save(output_file)

    return output_file

def is_valid_bitcoin_address(address):
    """
    Validate the Bitcoin address format.

    Parameters:
    - address (str): The Bitcoin address to validate.

    Returns:
    - bool: True if the address is valid, False otherwise.
    """
    # Basic validation for Bitcoin address (this is a simplified check)
    if len(address) < 26 or len(address) > 35:
        return False
    if not address.startswith(('1', '3', 'bc1')):
        return False
    return True

if __name__ == "__main__":
    try:
        # Example usage
        bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Replace with a valid Bitcoin address
        amount = 0.01  # Optional: specify the amount
        label = "Test Transaction"  # Optional: specify a label
        message = "Thanks for your support!"  # Optional: specify a message

        qr_file = generate_bitcoin_qr(bitcoin_address, amount, label, message)
        print(f"QR code generated and saved to: {qr_file}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
