"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Create a script that generates a Monero QR code and explains how to integrate it into a website for donation purposes, referencing the Monero QR Code Generator website.
Generated: DETERMINISTIC_df0be73df3a61283
Batch ID: 20250612_150040
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://moneroaddress.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import qrcode  # Import qrcode library for QR code generation
import os  # Import os for file path operations
from PIL import Image  # Import Image from PIL for image handling

def generate_monero_qr(address: str, amount: float = 0.0, label: str = "", message: str = "") -> str:
    """
    Generate a Monero QR code for receiving donations.

    :param address: The Monero wallet address to receive donations.
    :param amount: Optional amount to request (in XMR).
    :param label: Optional label for the transaction.
    :param message: Optional message for the transaction.
    :return: The file path of the generated QR code image.
    """
    try:
        # Base Monero URI format
        monero_uri = f"monero:{address}"
        
        # Append amount if provided
        if amount > 0:
            monero_uri += f"?tx_amount={amount}"
        
        # Append label if provided
        if label:
            monero_uri += f"&label={label}"
        
        # Append message if provided
        if message:
            monero_uri += f"&message={message}"

        # Generate the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(monero_uri)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Define the file path for saving the QR code
        file_path = os.path.join(os.getcwd(), 'monero_qr_code.png')
        img.save(file_path)

        return file_path

    except Exception as e:
        print(f"Error generating QR code: {e}")
        return None

if __name__ == "__main__":
    # Example usage: Replace with your Monero address and optional parameters as needed.
    wallet_address = "YOUR_MONERO_WALLET_ADDRESS"  # Replace with actual Monero wallet address
    donation_amount = 0.01  # Optional: Specify donation amount in XMR
    donation_label = "Donation"  # Optional: Specify a label for the transaction
    donation_message = "Thank you for your support!"  # Optional: Specify a message

    qr_code_path = generate_monero_qr(wallet_address, donation_amount, donation_label, donation_message)

    if qr_code_path:
        print(f"Monero QR code generated successfully and saved at: {qr_code_path}")
```

### Integration into a Website
1. **Upload the Generated QR Code**: Once you run the script, upload the `monero_qr_code.png` file to your web server.

2. **Embed in HTML**: Use the following HTML code snippet to display the QR code on your donation page:

   ```html
   <img src="path/to/your/monero_qr_code.png" alt="Monero Donation QR Code" />
   ```

   Replace `path/to/your/monero_qr_code.png` with the actual path where you uploaded the QR code image.

3. **Reference the Monero QR Code Generator**: In your webpage’s footer or about section, include a link to the Monero QR Code Generator website for users who might want to generate their own QR codes. 

   ```html
   <footer>
      <p>Generated using the <a href="https://moneroaddress.org/" target="_blank">Monero QR Code Generator</a></p>
   </footer>
   ```

Make sure to test the QR code to ensure it correctly links to your Monero wallet address for donations.
