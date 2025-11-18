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
import qrcode
import re

class BitcoinQRCodeGenerator:
    """
    A class to generate QR codes for Bitcoin transactions.
    """

    def __init__(self):
        # Supported Bitcoin address formats
        self.address_formats = {
            'P2PKH': r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',  # Legacy addresses
            'P2SH': r'^[3][a-km-zA-HJ-NP-Z1-9]{25,34}$',  # Pay-to-script hash addresses
            'Bech32': r'^(bc1)[0-9a-z]{39,59}$',             # SegWit addresses
        }

    def is_valid_address(self, address):
        """
        Validate the Bitcoin address format.

        :param address: str, Bitcoin address to validate
        :return: bool, True if valid, False otherwise
        """
        for format_type, pattern in self.address_formats.items():
            if re.match(pattern, address):
                return True
        return False

    def generate_qr_code(self, address, amount=None, label=None, message=None):
        """
        Generate a QR code for a Bitcoin transaction.

        :param address: str, Bitcoin address
        :param amount: float, optional, amount of Bitcoin to send
        :param label: str, optional, label for the transaction
        :param message: str, optional, message for the transaction
        :return: None
        """
        # Validate the Bitcoin address
        if not self.is_valid_address(address):
            raise ValueError("Invalid Bitcoin address format")

        # Base URI for Bitcoin payments
        uri = f"bitcoin:{address}"

        # Append amount, label, and message if provided
        if amount:
            uri += f"?amount={amount}"
        if label:
            uri += f"&label={label}"
        if message:
            uri += f"&message={message}"

        # Generate QR code
        try:
            qr = qrcode.make(uri)
            qr_file_path = f"bitcoin_qr_{address}.png"
            qr.save(qr_file_path)
            print(f"QR code generated and saved to {qr_file_path}")
        except Exception as e:
            raise RuntimeError(f"Error generating QR code: {str(e)}")

if __name__ == "__main__":
    # Example usage
    generator = BitcoinQRCodeGenerator()
    try:
        generator.generate_qr_code(
            address="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", 
            amount=0.01, 
            label="Example Transaction", 
            message="Thanks for your support!"
        )
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RuntimeError as re:
        print(f"RuntimeError: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
