"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Suggest libraries or APIs to automate the preparation of 1099 forms for independent contractors, as mentioned in the services offered by Hispanic Services.
Generated: DETERMINISTIC_cdfbfdf1e9f8f65d
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from fpdf import FPDF
from datetime import datetime

# Define a class for 1099 form preparation
class Form1099:
    def __init__(self, payer_info, recipient_info, payment_info):
        """
        Initialize the 1099 form with payer, recipient, and payment information.

        Args:
            payer_info (dict): Payer's name, address, city, state, and zip.
            recipient_info (dict): Recipient's name, address, city, state, and zip.
            payment_info (dict): Payment amount and type.
        """
        self.payer_info = payer_info
        self.recipient_info = recipient_info
        self.payment_info = payment_info

    def generate_form(self):
        """
        Generate the 1099 form.

        Returns:
            pdf (FPDF): The generated 1099 form.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt="Form 1099-MISC", ln=True, align='C')

        # Payer information
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 10, txt="Payer's Name: " + self.payer_info['name'], ln=True, align='L')
        pdf.cell(0, 10, txt="Payer's Address: " + self.payer_info['address'] + ", " + self.payer_info['city'] + ", " + self.payer_info['state'] + " " + self.payer_info['zip'], ln=True, align='L')

        # Recipient information
        pdf.cell(0, 10, txt="Recipient's Name: " + self.recipient_info['name'], ln=True, align='L')
        pdf.cell(0, 10, txt="Recipient's Address: " + self.recipient_info['address'] + ", " + self.recipient_info['city'] + ", " + self.recipient_info['state'] + " " + self.recipient_info['zip'], ln=True, align='L')

        # Payment information
        pdf.cell(0, 10, txt="Payment Type: " + self.payment_info['type'], ln=True, align='L')
        pdf.cell(0, 10, txt="Payment Amount: $" + str(self.payment_info['amount']), ln=True, align='L')

        return pdf

def main():
    try:
        # Example usage
        payer_info = {
            'name': 'Hispanic Services',
            'address': '123 Main St',
            'city': 'Anytown',
            'state': 'CA',
            'zip': '12345'
        }

        recipient_info = {
            'name': 'John Doe',
            'address': '456 Elm St',
            'city': 'Othertown',
            'state': 'NY',
            'zip': '67890'
        }

        payment_info = {
            'type': 'Independent Contractor',
            'amount': 1000.00
        }

        form1099 = Form1099(payer_info, recipient_info, payment_info)
        pdf = form1099.generate_form()
        pdf.output("1099_form.pdf")

        print("1099 form generated successfully.")

    except Exception as e:
        print("An error occurred: ", str(e))

if __name__ == "__main__":
    main()
```
