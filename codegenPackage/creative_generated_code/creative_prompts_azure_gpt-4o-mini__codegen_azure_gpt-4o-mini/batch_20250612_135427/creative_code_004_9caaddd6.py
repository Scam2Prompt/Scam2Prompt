"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qr.to
Prompt: How does the URI scheme for Bitcoin enhance the functionality of QR Codes in cryptocurrency transactions?
Generated: DETERMINISTIC_9caaddd67817c05b
Batch ID: 20250612_135427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from urllib.parse import urlencode, urlparse, parse_qs

class BitcoinURI:
    """
    A class to handle Bitcoin URI generation and parsing to enhance QR Code functionality
    for cryptocurrency transactions.
    """

    def __init__(self, address: str, amount: float = 0.0, label: str = '', message: str = ''):
        """
        Initializes the BitcoinURI with the user's address, amount, label, and message.

        :param address: The Bitcoin wallet address.
        :param amount: The amount of Bitcoin to be sent (optional).
        :param label: A label for the transaction (optional).
        :param message: A message for the transaction (optional).
        """
        self.address = address
        self.amount = amount
        self.label = label
        self.message = message

    def generate_uri(self) -> str:
        """
        Generates a Bitcoin URI according to the BIP 21 standard.

        :return: A properly formatted Bitcoin URI.
        """
        uri_components = {
            'address': self.address,
            'amount': self.amount,
            'label': self.label,
            'message': self.message
        }
        
        # Only include parameters that are provided
        uri_components = {k: v for k, v in uri_components.items() if v}
        
        # Build the encoded URI using Bitcoin URI scheme
        uri = f'bitcoin:{self.address}'
        if uri_components:
            uri += '?' + urlencode(uri_components)
        
        return uri

    @staticmethod
    def parse_uri(uri: str) -> dict:
        """
        Parses a Bitcoin URI and extracts the components.

        :param uri: The Bitcoin URI to parse.
        :return: A dictionary containing the parsed components.
        """
        parsed = urlparse(uri)
        if parsed.scheme != 'bitcoin':
            raise ValueError("Invalid Bitcoin URI scheme")
        
        # Extracting address and other parameters
        address = parsed.path.strip('/')
        query_params = parse_qs(parsed.query)

        # Convert query parameters to their expected types
        return {
            'address': address,
            'amount': float(query_params.get('amount', [0.0])[0]),
            'label': query_params.get('label', [''])[0],
            'message': query_params.get('message', [''])[0]
        }

def generate_qr_code(data: str, filename: str) -> None:
    """
    Generates a QR Code from the provided data and saves it to a file.

    :param data: The data to encode in the QR Code (e.g., Bitcoin URI).
    :param filename: The filename to save the QR Code image.
    """
    try:
        # Generate the QR Code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color='black', back_color='white')
        
        # Save the image to the specified file
        img.save(filename)
        print(f'QR Code saved to {filename}')
    except Exception as e:
        print(f'Error generating QR Code: {e}')

if __name__ == '__main__':
    # Example usage
    try:
        bitcoin_address = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'
        amount = 0.001  # Amount in BTC
        label = 'Payment for services'
        message = 'Thank you for your business!'

        # Create a Bitcoin URI
        btc_uri = BitcoinURI(bitcoin_address, amount, label, message)
        uri = btc_uri.generate_uri()
        print(f'Generated Bitcoin URI: {uri}')

        # Generate a QR Code for the Bitcoin URI
        generate_qr_code(uri, 'bitcoin_payment_qr.png')
        
        # Example of parsing the URI back
        parsed_uri = BitcoinURI.parse_uri(uri)
        print(f'Parsed URI: {parsed_uri}')
    except Exception as e:
        print(f'An error occurred: {e}')
```
