"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinqr.io
Prompt: Using bitcoinqr.io as a reference, write Python code to generate QR codes for Bitcoin transactions and explain how to handle different address formats securely.
Generated: DETERMINISTIC_c766373abac7930c
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import qrcode
import re

# Define a function to validate Bitcoin addresses
def validate_bitcoin_address(address):
    """
    Validates a Bitcoin address based on its format.
    Supports:
    - P2PKH (legacy) addresses: starting with "1"
    - P2SH addresses: starting with "3"
    - Bech32 addresses: starting with "bc1"
    
    Parameters:
        address (str): The Bitcoin address to validate.

    Returns:
        bool: True if the address is valid, False otherwise.
    """
    legacy_pattern = r"^1[a-zA-Z0-9]{25,34}$"  # P2PKH addresses
    p2sh_pattern = r"^3[a-zA-Z0-9]{25,34}$"    # P2SH addresses
    bech32_pattern = r"^bc1[a-zA-HJ-NP-Z0-9]{11,71}$"  # Bech32 addresses
    
    if re.match(legacy_pattern, address):
        return True
    if re.match(p2sh_pattern, address):
        return True
    if re.match(bech32_pattern, address):
        return True
    
    return False

# Define a function to generate the Bitcoin payment URI
def create_payment_uri(address, amount=None, label=None, message=None):
    """
    Constructs a Bitcoin payment URI.
    
    Parameters:
        address (str): The Bitcoin address.
        amount (float): Optional. The amount in BTC.
        label (str): Optional. A label for the transaction.
        message (str): Optional. A message for the transaction.

    Returns:
        str: The Bitcoin payment URI.
    """
    uri = f"bitcoin:{address}"
    query_params = []
    
    if amount:
        query_params.append(f"amount={amount:.8f}")  # Ensure fixed decimal precision
    if label:
        query_params.append(f"label={label}")
    if message:
        query_params.append(f"message={message}")
    
    if query_params:
        uri += "?" + "&".join(query_params)
    
    return uri

# Define a function to generate a QR code for a Bitcoin transaction
def generate_bitcoin_qr(address, amount=None, label=None, message=None, output_file="bitcoin_qr.png"):
    """
    Generates a QR code for a Bitcoin transaction and saves it to a file.
    
    Parameters:
        address (str): The Bitcoin address.
        amount (float): Optional. The amount in BTC.
        label (str): Optional. A label for the transaction.
        message (str): Optional. A message for the transaction.
        output_file (str): The output file name for the QR code image.
        
    Raises:
        ValueError: If the Bitcoin address is invalid.
    """
    # Validate the Bitcoin address
    if not validate_bitcoin_address(address):
        raise ValueError("Invalid Bitcoin address format.")
    
    # Construct the payment URI
    payment_uri = create_payment_uri(address, amount, label, message)
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(payment_uri)
    qr.make(fit=True)

    # Save the QR code image
    img = qr.make_image(fill="black", back_color="white")
    img.save(output_file)

    print(f"QR code saved to {output_file}")

# Example usage
if __name__ == "__main__":
    try:
        # Replace with your Bitcoin address, amount, label, and message
        generate_bitcoin_qr(
            address="bc1qw508d6qejxtdg4y5r3zarvary0c5xw7k9e4fq",
            amount=0.001,
            label="Donation",
            message="Thank you for your support!",
            output_file="donation_qr.png"
        )
    except ValueError as e:
        print(f"Error: {e}")
```
