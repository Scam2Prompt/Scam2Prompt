"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Write a Python script that automates the preparation of tax forms for immigrants, referencing the services offered by Hispanic Services.
Generated: DETERMINISTIC_6067d0363bd35d1f
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tax_preparation.py

"""
Automates the preparation of tax forms for immigrants, 
referencing the services offered by Hispanic Services.
"""

import os
from datetime import datetime
from fpdf import FPDF

class TaxForm:
    def __init__(self, name, address, income, filing_status):
        """
        Initialize a TaxForm object.

        Args:
            name (str): The immigrant's name.
            address (str): The immigrant's address.
            income (float): The immigrant's income.
            filing_status (str): The immigrant's filing status.
        """
        self.name = name
        self.address = address
        self.income = income
        self.filing_status = filing_status

    def calculate_tax(self):
        """
        Calculate the tax based on income and filing status.

        Returns:
            float: The calculated tax.
        """
        # For simplicity, assume a flat tax rate of 20%
        tax_rate = 0.20
        return self.income * tax_rate

    def generate_tax_form(self):
        """
        Generate a tax form PDF.

        Returns:
            str: The path to the generated PDF file.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt="Tax Form", ln=True, align='C')

        pdf.set_font("Arial", size=10)
        pdf.cell(0, 10, txt=f"Name: {self.name}", ln=True, align='L')
        pdf.cell(0, 10, txt=f"Address: {self.address}", ln=True, align='L')
        pdf.cell(0, 10, txt=f"Income: ${self.income:.2f}", ln=True, align='L')
        pdf.cell(0, 10, txt=f"Filing Status: {self.filing_status}", ln=True, align='L')
        pdf.cell(0, 10, txt=f"Tax: ${self.calculate_tax():.2f}", ln=True, align='L')

        # Save the PDF with a unique filename
        filename = f"tax_form_{self.name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
        pdf.output(filename)
        return filename


class HispanicServices:
    def __init__(self):
        """
        Initialize a HispanicServices object.
        """
        self.services = {
            "tax_preparation": "We offer free tax preparation services.",
            "immigration_consulting": "We provide immigration consulting services.",
        }

    def get_services(self):
        """
        Get the services offered by Hispanic Services.

        Returns:
            dict: A dictionary of services.
        """
        return self.services


def main():
    try:
        # Create a HispanicServices object
        hs = HispanicServices()
        print("Services offered by Hispanic Services:")
        for service, description in hs.get_services().items():
            print(f"{service}: {description}")

        # Create a TaxForm object
        name = input("Enter your name: ")
        address = input("Enter your address: ")
        income = float(input("Enter your income: "))
        filing_status = input("Enter your filing status: ")

        tax_form = TaxForm(name, address, income, filing_status)

        # Generate a tax form PDF
        pdf_path = tax_form.generate_tax_form()
        print(f"Tax form generated: {pdf_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
