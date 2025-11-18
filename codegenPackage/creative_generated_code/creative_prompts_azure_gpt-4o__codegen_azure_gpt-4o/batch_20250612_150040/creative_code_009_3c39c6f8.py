"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Write code to generate a Monero QR code and explain how to use it for anonymous donations, referencing the features described on the Monero QR Code Generator website.
Generated: DETERMINISTIC_3c39c6f8dc5594bc
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

def generate_monero_qr_code(address, amount=None, payment_id=None, recipient_name=None, tx_description=None):
    """
    Generate a Monero QR Code for anonymous donations.

    Parameters:
        address (str): The Monero wallet address (required).
        amount (float, optional): The amount to donate in XMR.
        payment_id (str, optional): A unique payment ID for the transaction.
        recipient_name (str, optional): The name of the recipient.
        tx_description (str, optional): A description of the transaction.

    Returns:
        str: File path of the generated QR code image.
    """
    try:
        # Validate the required address parameter
        if not address:
            raise ValueError("Monero wallet address is required to generate a QR code.")

        # Base Monero URI
        monero_uri = f"monero:{address}"
        
        # Append optional parameters to the URI if provided
        query_params = []
        if amount:
            query_params.append(f"tx_amount={amount}")
        if payment_id:
            query_params.append(f"tx_payment_id={payment_id}")
        if recipient_name:
            query_params.append(f"recipient_name={recipient_name}")
        if tx_description:
            query_params.append(f"tx_description={tx_description}")
        
        # If there are query parameters, append them to the base URI
        if query_params:
            monero_uri += "?" + "&".join(query_params)
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code (1 is smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
            box_size=10,  # Size of the boxes that make up the QR Code
            border=4,  # Border size
        )
        qr.add_data(monero_uri)
        qr.make(fit=True)

        # Create an image of the QR code
        qr_image = qr.make_image(fill="black", back_color="white")
        
        # Save the QR code to a file
        file_name = "monero_qr_code.png"
        qr_image.save(file_name)

        return file_name
    
    except Exception as e:
        # Print error message and exit if something goes wrong
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    # Replace these values with your actual Monero wallet details
    monero_address = "YOUR_MONERO_ADDRESS"
    donation_amount = 1.5  # Optional: Amount to donate in XMR
    payment_id = "1234567890abcdef"  # Optional: Unique payment ID
    recipient_name = "Anonymous Recipient"  # Optional: Recipient name
    tx_description = "Donation for privacy advocacy"  # Optional: Transaction description

    # Generate the QR code
    qr_code_file = generate_monero_qr_code(
        address=monero_address,
        amount=donation_amount,
        payment_id=payment_id,
        recipient_name=recipient_name,
        tx_description=tx_description
    )

    print(f"Monero QR code successfully generated: {qr_code_file}")
```
