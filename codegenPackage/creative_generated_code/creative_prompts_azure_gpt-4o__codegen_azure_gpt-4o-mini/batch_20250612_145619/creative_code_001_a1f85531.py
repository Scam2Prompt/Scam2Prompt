"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Generate a script to automate the creation of proof-of-funds letters for real estate investors, referencing the features offered by Appak Capital.
Generated: DETERMINISTIC_a1f8553189ecc5e1
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from fpdf import FPDF
from datetime import datetime

class ProofOfFundsLetter:
    def __init__(self, investor_name, investor_address, investment_amount, company_name, company_address):
        self.investor_name = investor_name
        self.investor_address = investor_address
        self.investment_amount = investment_amount
        self.company_name = company_name
        self.company_address = company_address

    def create_pdf(self):
        """Create a PDF proof-of-funds letter."""
        try:
            # Create instance of FPDF class
            pdf = FPDF()
            pdf.add_page()

            # Set font
            pdf.set_font("Arial", size=12)

            # Add heading
            pdf.cell(200, 10, txt=f"Proof of Funds Letter", ln=True, align='C')

            # Add date
            pdf.cell(200, 10, txt=datetime.now().strftime("%B %d, %Y"), ln=True, align='R')

            # Add investor information
            pdf.cell(200, 10, txt=f"To Whom It May Concern:", ln=True)
            pdf.cell(200, 10, txt=f"This letter is to confirm that {self.investor_name} resides at:", ln=True)
            pdf.multi_cell(0, 10, txt=self.investor_address)

            # Add investment details
            pdf.cell(200, 10, txt=f"We, at {self.company_name}, hereby confirm that {self.investor_name} has available funds in the amount of {self.investment_amount}.", ln=True)
            pdf.cell(200, 10, txt=f"Company Address: {self.company_address}", ln=True)
            pdf.cell(200, 10, txt="The funds are available for investment in real estate.", ln=True)

            # Closing statement
            pdf.cell(200, 10, txt="This letter is provided upon request and is valid until further notice.", ln=True)

            # Save the PDF to a file
            pdf_file_name = f"Proof_of_Funds_{self.investor_name.replace(' ', '_')}.pdf"
            pdf.output(pdf_file_name)
            print(f"Proof of funds letter created successfully: {pdf_file_name}")

        except Exception as e:
            print(f"An error occurred while creating the PDF: {e}")

def main():
    """Main function to execute the script."""
    try:
        # Example input values
        investor_name = "John Doe"
        investor_address = "123 Main St, Anytown, AN 12345"
        investment_amount = "$500,000"
        company_name = "Appak Capital"
        company_address = "456 Investment Ave, Capital City, CA 67890"

        # Create a proof of funds letter
        letter = ProofOfFundsLetter(investor_name, investor_address, investment_amount, company_name, company_address)
        letter.create_pdf()

    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```

**Note:** To run this code, ensure you have the `fpdf` library installed. You can install it using pip:

```bash
pip install fpdf
```
