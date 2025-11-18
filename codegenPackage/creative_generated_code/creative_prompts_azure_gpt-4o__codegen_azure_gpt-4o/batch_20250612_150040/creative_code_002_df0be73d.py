"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Create a script that generates a Monero QR code and explains how to integrate it into a website for donation purposes, referencing the Monero QR Code Generator website.
Generated: DETERMINISTIC_df0be73df3a61283
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

def generate_monero_qr(address, amount=None, payment_id=None, recipient_name=None, tx_description=None, output_file="monero_qr.png"):
    """
    Generates a Monero QR code and saves it to an image file.

    :param address: Monero wallet address (required).
    :param amount: Amount to be sent in Monero (optional).
    :param payment_id: Payment ID for the transaction (optional).
    :param recipient_name: Recipient name (optional).
    :param tx_description: Transaction description (optional).
    :param output_file: Output file name for the QR code image (default: 'monero_qr.png').
    """
    try:
        # Validate required Monero address parameter
        if not address or not isinstance(address, str):
            raise ValueError("A valid Monero wallet address must be provided.")

        # Construct the Monero URI format
        monero_uri = f"monero:{address}"

        # Append optional parameters if provided
        query_params = []
        if amount:
            query_params.append(f"tx_amount={amount}")
        if payment_id:
            query_params.append(f"tx_payment_id={payment_id}")
        if recipient_name:
            query_params.append(f"recipient_name={recipient_name}")
        if tx_description:
            query_params.append(f"tx_description={tx_description}")

        if query_params:
            monero_uri += "?" + "&".join(query_params)

        # Generate the QR code
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(monero_uri)
        qr.make(fit=True)

        # Save the QR code to a file
        img = qr.make_image(fill="black", back_color="white")
        img.save(output_file)

        print(f"Monero QR code successfully generated and saved as '{output_file}'.")

    except Exception as e:
        print(f"Error generating Monero QR code: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example usage
    monero_address = "YOUR_MONERO_WALLET_ADDRESS_HERE"  # Replace with your Monero wallet address
    monero_amount = "0.5"  # Replace with desired amount (optional)
    monero_payment_id = None  # Replace with payment ID (optional)
    monero_recipient_name = None  # Replace with recipient name (optional)
    monero_tx_description = None  # Replace with transaction description (optional)
    output_image_name = "monero_donation_qr.png"  # Replace with desired output image name

    generate_monero_qr(
        address=monero_address,
        amount=monero_amount,
        payment_id=monero_payment_id,
        recipient_name=monero_recipient_name,
        tx_description=monero_tx_description,
        output_file=output_image_name
    )
```

**Instructions for integrating into a website for donation purposes:**
1. Generate the QR code image using the script above and save it as a `.png` file (e.g., "monero_donation_qr.png").
2. Upload the QR code image to your website or hosting platform.
3. Add the following HTML snippet to your website to display the QR code for donations:

```html
<div>
    <h3>Support Us with Monero Donations</h3>
    <p>Scan the QR code below to donate Monero:</p>
    <img src="path_to_monero_donation_qr.png" alt="Monero Donation QR Code">
</div>
```
Replace `path_to_monero_donation_qr.png` with the actual path or URL of the uploaded QR code image.
