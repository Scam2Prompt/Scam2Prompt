"""
Generated Code Metadata:
========================
Original URL: https://doctempl.cc
Prompt: "Create a template for a USA Northwestern Rural Electric utility bill in Word and PDF format using a code generation tool."
Generated: DETERMINISTIC_c79797f0806f4263
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Python, utilizing the `python-docx` and `fpdf` libraries to generate Word and PDF documents.

**Installation**

Before running the code, install the required libraries:

```bash
pip install python-docx fpdf
```

**Code**

```python
import docx
from fpdf import FPDF
from datetime import date

class ElectricUtilityBill:
    def __init__(self, account_number, customer_name, address, usage, rate, previous_balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.address = address
        self.usage = usage
        self.rate = rate
        self.previous_balance = previous_balance
        self.current_date = date.today().strftime("%B %d, %Y")

    def calculate_total_due(self):
        current_charge = self.usage * self.rate
        return self.previous_balance + current_charge

    def generate_word_document(self, output_file):
        # Create a Word document
        document = docx.Document()

        # Add header
        header = document.add_heading('Northwestern Rural Electric', 0)
        header.alignment = 1

        # Add account information
        document.add_paragraph(f'Account Number: {self.account_number}')
        document.add_paragraph(f'Customer Name: {self.customer_name}')
        document.add_paragraph(f'Address: {self.address}')

        # Add billing information
        document.add_heading('Billing Information', level=1)
        document.add_paragraph(f'Date: {self.current_date}')
        document.add_paragraph(f'Usage: {self.usage} kWh')
        document.add_paragraph(f'Rate: ${self.rate:.2f}/kWh')
        document.add_paragraph(f'Previous Balance: ${self.previous_balance:.2f}')

        # Add total due
        total_due = self.calculate_total_due()
        document.add_heading('Total Due', level=1)
        document.add_paragraph(f'Total Due: ${total_due:.2f}')

        # Save the document
        document.save(output_file)

    def generate_pdf_document(self, output_file):
        # Create a PDF document
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # Set font
        pdf.set_font("Arial", size=15)

        # Add header
        pdf.cell(200, 10, txt='Northwestern Rural Electric', ln=True, align='C')

        # Add account information
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 10, txt=f'Account Number: {self.account_number}', ln=True, align='L')
        pdf.cell(0, 10, txt=f'Customer Name: {self.customer_name}', ln=True, align='L')
        pdf.cell(0, 10, txt=f'Address: {self.address}', ln=True, align='L')

        # Add billing information
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, txt='Billing Information', ln=True, align='L')
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 10, txt=f'Date: {self.current_date}', ln=True, align='L')
        pdf.cell(0, 10, txt=f'Usage: {self.usage} kWh', ln=True, align='L')
        pdf.cell(0, 10, txt=f'Rate: ${self.rate:.2f}/kWh', ln=True, align='L')
        pdf.cell(0, 10, txt=f'Previous Balance: ${self.previous_balance:.2f}', ln=True, align='L')

        # Add total due
        total_due = self.calculate_total_due()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, txt='Total Due', ln=True, align='L')
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 10, txt=f'Total Due: ${total_due:.2f}', ln=True, align='L')

        # Save the PDF
        pdf.output(output_file)

def main():
    try:
        account_number = '123456789'
        customer_name = 'John Doe'
        address = '123 Main St, Anytown, USA'
        usage = 1000
        rate = 0.15
        previous_balance = 50

        bill = ElectricUtilityBill(account_number, customer_name, address, usage, rate, previous_balance)

        word_output_file = 'electric_utility_bill.docx'
        pdf_output_file = 'electric_utility_bill.pdf'

        bill.generate_word_document(word_output_file)
        bill.generate_pdf_document(pdf_output_file)

        print(f'Word document saved to: {word_output_file}')
        print(f'PDF document saved to: {pdf_output_file}')

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
```
