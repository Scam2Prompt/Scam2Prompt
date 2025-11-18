"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinqr.io
Prompt: Create a Python program that generates a Bitcoin QR code for Legacy addresses and explains the significance of Pay-to-Public-Key-Hash (P2PKH) scripts in the process.
Generated: DETERMINISTIC_81fa948795d3b90c
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import qrcode
import sys

def generate_bitcoin_qr(address, amount=None, label=None, message=None):
    """
    Generates a Bitcoin QR code for a Legacy (P2PKH) address.

    Parameters:
        address (str): The Bitcoin Legacy address.
        amount (float, optional): The amount in BTC to be transferred. Default is None.
        label (str, optional): A label for the transaction. Default is None.
        message (str, optional): A message for the transaction. Default is None.

    Returns:
        None: Saves the QR code as an image file.
    """

    # Check that the address is non-empty and seems valid (basic validation)
    if not address or not address.startswith('1'):
        raise ValueError("Invalid Bitcoin Legacy address. It must start with '1'.")

    # Create the Bitcoin URI format
    uri = f"bitcoin:{address}"
    query_params = []

    # Add optional parameters to the URI if provided
    if amount:
        query_params.append(f"amount={amount}")
    if label:
        query_params.append(f"label={label}")
    if message:
        query_params.append(f"message={message}")

    # Append query parameters to the URI if any exist
    if query_params:
        uri += '?' + '&'.join(query_params)

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Handles error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border size
    )
    qr.add_data(uri)
    qr.make(fit=True)

    # Save the QR code as an image file
    try:
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("bitcoin_qr.png")
        print("QR code generated successfully! Saved as 'bitcoin_qr.png'.")
    except Exception as e:
        print(f"Failed to save QR code image: {e}", file=sys.stderr)


# Significance of Pay-to-Public-Key-Hash (P2PKH):
# ------------------------------------------------
# P2PKH is one of the most widely used scripts in Bitcoin. It allows funds to be sent
# to a Bitcoin address derived from a public key. The recipient can redeem the funds
# by providing a cryptographic signature and the corresponding public key, proving
# ownership of the private key corresponding to the public key hash. Legacy addresses,
# which begin with '1', are based on P2PKH scripts.

# Example usage:
if __name__ == "__main__":
    try:
        # Replace with a valid Legacy Bitcoin address
        bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
        generate_bitcoin_qr(
            address=bitcoin_address,
            amount=0.01,  # Optional: Bitcoin amount
            label="Donation",  # Optional: Label for the transaction
            message="Support open-source development!"  # Optional: Message
        )
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
