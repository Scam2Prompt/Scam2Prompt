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
import sys

def generate_bitcoin_qr_code(address, amount=None, label=None, message=None, filename='bitcoin_qr.png'):
    """
    Generate a Bitcoin QR code with a specified amount and label.

    Parameters:
        address (str): The Bitcoin address to encode in the QR code.
        amount (float, optional): The amount of Bitcoin to include in the URI.
        label (str, optional): A label for the transaction.
        message (str, optional): A message to include with the transaction.
        filename (str): The name of the output file for the QR code image.
    
    Raises:
        ValueError: If the address is invalid or if both amount and label are provided without proper formatting.
    """
    # Validate Bitcoin address format (basic check, can be improved)
    if not address.startswith(('1', '3', 'bc1')):
        raise ValueError("Invalid Bitcoin address format.")

    # Construct the base URI
    uri = f"bitcoin:{address}"

    # Append amount if provided
    if amount is not None:
        uri += f"?amount={amount}"

    # Append label if provided
    if label is not None:
        if '?' in uri:
            uri += f"&label={label}"
        else:
            uri += f"?label={label}"

    # Append message if provided
    if message is not None:
        if '?' in uri:
            uri += f"&message={message}"
        else:
            uri += f"?message={message}"

    try:
        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(uri)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill='black', back_color='white')

        # Save the generated QR code to a file
        img.save(filename)
        print(f"QR code generated and saved to '{filename}'.")

    except Exception as e:
        print(f"Error generating QR code: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage with command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python generate_bitcoin_qr.py <address> [amount] [label] [message]")
        sys.exit(1)

    # Read arguments from command line
    bitcoin_address = sys.argv[1]
    bitcoin_amount = float(sys.argv[2]) if len(sys.argv) > 2 else None
    bitcoin_label = sys.argv[3] if len(sys.argv) > 3 else None
    bitcoin_message = sys.argv[4] if len(sys.argv) > 4 else None

    # Generate the QR code
    generate_bitcoin_qr_code(bitcoin_address, bitcoin_amount, bitcoin_label, bitcoin_message)
```

To run this script, save it to a file named `generate_bitcoin_qr.py`, and execute it from the command line with the required arguments. Make sure to have the `qrcode` library installed. You can install it using pip:

```bash
pip install qrcode[pil]
```
