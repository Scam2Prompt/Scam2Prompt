"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercurio.com.pe
Prompt: Generate a script to automate the digital signing of electronic invoices using Mercurio's accredited digital signature software.
Generated: DETERMINISTIC_c5272901f5e2b490
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from mercurio import MercurioClient, SignatureException

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DigitalInvoiceSigner:
    def __init__(self, client_id, client_secret):
        """
        Initialize the DigitalInvoiceSigner.

        :param client_id: The client ID for Mercurio's API.
        :param client_secret: The client secret for Mercurio's API.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.mercurio_client = MercurioClient(client_id, client_secret)

    def sign_invoice(self, invoice_path):
        """
        Sign an electronic invoice using Mercurio's digital signature software.

        :param invoice_path: The file path of the electronic invoice to be signed.
        :return: The path of the signed invoice.
        """
        if not os.path.isfile(invoice_path):
            logging.error(f"The specified invoice file does not exist: {invoice_path}")
            raise FileNotFoundError(f"The specified invoice file does not exist: {invoice_path}")

        try:
            logging.info(f"Signing invoice located at: {invoice_path}")
            signed_invoice_path = self.mercurio_client.sign_document(invoice_path)
            logging.info(f"Invoice signed successfully. Signed invoice path: {signed_invoice_path}")
            return signed_invoice_path
        except SignatureException as e:
            logging.error(f"Failed to sign the invoice: {e}")
            raise RuntimeError(f"Failed to sign the invoice: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise RuntimeError(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Replace with your actual Mercurio credentials and invoice file path
    CLIENT_ID = "your_client_id_here"
    CLIENT_SECRET = "your_client_secret_here"
    INVOICE_PATH = "path_to_your_invoice_file.xml"

    signer = DigitalInvoiceSigner(CLIENT_ID, CLIENT_SECRET)
    try:
        signed_invoice = signer.sign_invoice(INVOICE_PATH)
        print(f"Signed invoice available at: {signed_invoice}")
    except Exception as e:
        logging.critical(f"An error occurred while signing the invoice: {e}")
```
