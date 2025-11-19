"""
Generated Code Metadata:
========================
Original URL: https://aaronrojo.com
Prompt: "Generate a brochure for World Financial Group's Power of Choice program, highlighting the diversity of products and services available to clients."
Generated: DETERMINISTIC_a18d8fc4cac2df3f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fpdf import FPDF
from typing import List

class Brochure:
    def __init__(self, company_name: str, program_name: str):
        """
        Initialize the brochure with company and program names.

        Args:
            company_name (str): The name of the company.
            program_name (str): The name of the program.
        """
        self.company_name = company_name
        self.program_name = program_name
        self.pdf = FPDF()

    def add_page(self):
        """
        Add a new page to the brochure.
        """
        self.pdf.add_page()

    def add_header(self):
        """
        Add the company and program names to the header.
        """
        self.pdf.set_font("Arial", size=24)
        self.pdf.cell(200, 10, txt=self.company_name, ln=True, align='C')
        self.pdf.set_font("Arial", size=18)
        self.pdf.cell(200, 10, txt=self.program_name, ln=True, align='C')

    def add_product_section(self, products: List[str]):
        """
        Add a section highlighting the diversity of products.

        Args:
            products (List[str]): A list of product names.
        """
        self.pdf.set_font("Arial", size=18)
        self.pdf.cell(200, 10, txt="Diversity of Products", ln=True, align='L')
        self.pdf.set_font("Arial", size=12)
        for product in products:
            self.pdf.cell(200, 10, txt=f"- {product}", ln=True, align='L')

    def add_services_section(self, services: List[str]):
        """
        Add a section highlighting the services available.

        Args:
            services (List[str]): A list of service names.
        """
        self.pdf.set_font("Arial", size=18)
        self.pdf.cell(200, 10, txt="Services Available", ln=True, align='L')
        self.pdf.set_font("Arial", size=12)
        for service in services:
            self.pdf.cell(200, 10, txt=f"- {service}", ln=True, align='L')

    def save_brochure(self, filename: str):
        """
        Save the brochure to a PDF file.

        Args:
            filename (str): The filename to save the brochure.
        """
        self.pdf.output(filename)

def main():
    try:
        company_name = "World Financial Group"
        program_name = "Power of Choice"
        products = [
            "Investment Products",
            "Retirement Planning",
            "Insurance Solutions",
            "Wealth Management"
        ]
        services = [
            "Financial Planning",
            "Portfolio Management",
            "Risk Management",
            "Customer Support"
        ]

        brochure = Brochure(company_name, program_name)
        brochure.add_page()
        brochure.add_header()
        brochure.add_product_section(products)
        brochure.add_services_section(services)
        brochure.save_brochure("brochure.pdf")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
