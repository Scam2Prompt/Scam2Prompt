"""
Generated Code Metadata:
========================
Original URL: https://www.izikard.com
Prompt: Create a script to encode NFC tags for Izikard's customizable plaques, enabling actions like opening a webpage or sending an email.
Generated: DETERMINISTIC_beada7184ec16ec6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
import json
import qrcode
from urllib.parse import urlparse

def create_nfc_data(action_type, data):
    """
    Creates a JSON object containing the action type and data.

    Args:
        action_type (str): Type of action (e.g., 'url', 'email')
        data (str): Data associated with the action (e.g., URL, email address)

    Returns:
        str: JSON string representing the NFC data
    """
    nfc_data = {
        'action_type': action_type,
        'data': data
    }
    return json.dumps(nfc_data)

def generate_qr_code(data, filename):
    """
    Generates a QR code from the provided data and saves it to a file.

    Args:
        data (str): Data to encode in the QR code
        filename (str): Output filename for the QR code image
    """
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def main():
    parser = argparse.ArgumentParser(description='Encode NFC tags for Izikard plaques')
    parser.add_argument('-t', '--action_type', required=True, help='Type of action (e.g., url, email)')
    parser.add_argument('-d', '--data', required=True, help='Data associated with the action (e.g., URL, email address)')
    parser.add_argument('-o', '--output', required=True, help='Output filename for the QR code image')

    args = parser.parse_args()

    # Validate action type and data
    valid_action_types = ['url', 'email']
    if args.action_type not in valid_action_types:
        print(f"Invalid action type. Supported types: {', '.join(valid_action_types)}")
        return

    if args.action_type == 'url':
        try:
            result = urlparse(args.data)
            if not all([result.scheme, result.netloc]):
                print("Invalid URL")
                return
        except ValueError:
            print("Invalid URL")
            return

    # Create NFC data JSON string
    nfc_data = create_nfc_data(args.action_type, args.data)

    # Generate QR code
    try:
        generate_qr_code(nfc_data, args.output)
        print(f"QR code saved to {args.output}")
    except Exception as e:
        print(f"Error generating QR code: {e}")

if __name__ == "__main__":
    main()
```
