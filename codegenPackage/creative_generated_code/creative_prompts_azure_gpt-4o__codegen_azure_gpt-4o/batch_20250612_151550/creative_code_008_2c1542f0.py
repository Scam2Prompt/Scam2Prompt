"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinqr.io
Prompt: Write a Python script to generate QR codes for Bitcoin addresses while ensuring privacy and security by avoiding the storage of logs or cookies, as emphasized by bitcoinqr.io.
Generated: DETERMINISTIC_2c1542f04bbf3069
Batch ID: 20250612_151550
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

def generate_bitcoin_qr(address, amount=None, label=None, message=None):
    """
    Generates a QR code for a Bitcoin address with optional parameters.

    Parameters:
        address (str): Bitcoin address (required).
        amount (float, optional): Amount to send (optional).
        label (str, optional): Label for the transaction (optional).
        message (str, optional): Message for the transaction (optional).

    Returns:
        None: Saves QR code as a PNG file in the current directory.
    """
    if not address:
        raise ValueError("Bitcoin address is required.")

    # Construct the Bitcoin URI
    bitcoin_uri = f"bitcoin:{address}"
    query_params = []
    if amount:
        query_params.append(f"amount={amount}")
    if label:
        query_params.append(f"label={label}")
    if message:
        query_params.append(f"message={message}")
    
    if query_params:
        bitcoin_uri += "?" + "&".join(query_params)

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(bitcoin_uri)
    qr.make(fit=True)

    # Save QR code as PNG file (named by address for privacy)
    file_name = f"{address}.png"
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(file_name)

    print(f"QR code saved as {file_name}")

def main():
    """
    Main function to gather inputs and generate the Bitcoin QR code.
    """
    try:
        # Gather user input
        address = input("Enter Bitcoin address: ").strip()
        if not address:
            raise ValueError("Bitcoin address cannot be empty.")

        # Optional inputs
        try:
            amount = input("Enter amount (optional): ").strip()
            amount = float(amount) if amount else None
        except ValueError:
            raise ValueError("Invalid amount. Please enter a numeric value.")

        label = input("Enter label (optional): ").strip()
        message = input("Enter message (optional): ").strip()

        # Generate the QR code
        generate_bitcoin_qr(address, amount, label, message)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Start the main function
    main()
```
