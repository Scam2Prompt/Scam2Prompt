"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Write a Python script to generate a Monero QR code for anonymous cryptocurrency transactions, ensuring compatibility with widely used Monero wallets, as discussed on the Monero QR Code Generator site.
Generated: DETERMINISTIC_b31b755e8f3600f4
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
import sys

def generate_monero_qr(address, amount=None, payment_id=None):
    """
    Generates a Monero QR code as per widely used Monero wallet standards.
    
    Parameters:
        address (str): The Monero public address (required).
        amount (float): Amount to transfer (optional).
        payment_id (str): Payment ID for the transaction (optional).
    
    Returns:
        None: Saves the QR code as an image file.
    """
    try:
        # Validate the address (basic validation, can be expanded as per requirements)
        if not address or len(address) < 95 or len(address) > 106:
            raise ValueError("Invalid Monero address. Please provide a valid address.")

        # Construct the Monero URI
        monero_uri = f"monero:{address}"
        query_params = []

        if amount is not None:
            query_params.append(f"tx_amount={amount:.12f}")  # Monero supports up to 12 decimal places
        if payment_id is not None:
            query_params.append(f"tx_payment_id={payment_id}")

        if query_params:
            monero_uri += "?" + "&".join(query_params)

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(monero_uri)
        qr.make(fit=True)

        # Save the QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        output_file = "monero_qr_code.png"
        img.save(output_file)
        print(f"Monero QR code successfully saved to {output_file}")

    except Exception as e:
        print(f"Error generating Monero QR code: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Example usage
    # Replace with your Monero address, amount, and optional payment ID
    monero_address = "YOUR_MONERO_ADDRESS_HERE"
    transaction_amount = 0.123456789012  # Example amount (max 12 decimal places)
    tx_payment_id = "examplepaymentid1234"  # Optional payment ID

    generate_monero_qr(monero_address, amount=transaction_amount, payment_id=tx_payment_id)
```
