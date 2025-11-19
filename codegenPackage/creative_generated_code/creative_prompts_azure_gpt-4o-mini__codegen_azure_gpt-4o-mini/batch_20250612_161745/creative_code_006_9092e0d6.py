"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payapayments.com
Prompt: Create a sample code for integrating Paya's e-invoicing capabilities into a B2B platform.
Generated: DETERMINISTIC_9092e0d63b843446
Batch ID: 20250612_161745
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paya.com/v1": {
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
import requests
import json

class PayaEInvoice:
    def __init__(self, api_key, api_url):
        """
        Initializes the PayaEInvoice instance with API key and URL.

        :param api_key: Your API key for authenticating with Paya
        :param api_url: The endpoint URL for Paya's e-invoicing API
        """
        self.api_key = api_key
        self.api_url = api_url

    def create_invoice(self, invoice_data):
        """
        Creates an invoice using Paya's e-invoicing API.

        :param invoice_data: A dictionary containing invoice details
        :return: Response from the API or error message
        """
        try:
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.api_key}'
            }
            response = requests.post(self.api_url + '/invoices', headers=headers, json=invoice_data)

            # Check for HTTP errors
            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as http_err:
            return {'error': f'HTTP error occurred: {http_err}'}
        except Exception as err:
            return {'error': f'An error occurred: {err}'}

    def get_invoice_status(self, invoice_id):
        """
        Retrieves the status of a specific invoice.

        :param invoice_id: The ID of the invoice to check
        :return: Invoice status or error message
        """
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}'
            }
            response = requests.get(self.api_url + f'/invoices/{invoice_id}', headers=headers)

            # Check for HTTP errors
            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as http_err:
            return {'error': f'HTTP error occurred: {http_err}'}
        except Exception as err:
            return {'error': f'An error occurred: {err}'}


if __name__ == "__main__":
    # Replace with your actual API key and URL
    API_KEY = 'your_api_key_here'
    API_URL = 'https://api.paya.com/v1'

    # Create an instance of the PayaEInvoice class
    paya_invoice = PayaEInvoice(api_key=API_KEY, api_url=API_URL)

    # Sample invoice data
    invoice_data = {
        "customer": {
            "name": "ABC Corp",
            "email": "contact@abccorp.com"
        },
        "items": [
            {
                "description": "Consulting Services",
                "amount": 1000.00,
                "quantity": 1
            }
        ],
        "total": 1000.00,
        "currency": "USD"
    }

    # Create an invoice
    create_response = paya_invoice.create_invoice(invoice_data)
    print("Create Invoice Response:", json.dumps(create_response, indent=2))

    # Assuming invoice response contains an ID, check its status
    if 'id' in create_response:
        invoice_id = create_response['id']
        status_response = paya_invoice.get_invoice_status(invoice_id)
        print("Invoice Status Response:", json.dumps(status_response, indent=2))
```
