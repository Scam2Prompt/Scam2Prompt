"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olavovieira.com.br
Prompt: Write Python code to generate a Parecer Técnico de Avaliação Mercadológica (PTAM) document for real estate valuation, ensuring compliance with ABNT NBR 14.653 and COFECI Resolution No. 1.066/07.
Generated: DETERMINISTIC_476bbc9bcafd5c86
Batch ID: 20250612_152924
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

class PTAMDocument:
    """Class to generate a Parecer Técnico de Avaliação Mercadológica (PTAM) document."""
    
    def __init__(self, property_details, evaluator_details):
        """
        Initialize the PTAMDocument with property and evaluator details.

        Args:
            property_details (dict): Information about the property being evaluated.
            evaluator_details (dict): Information about the evaluator.
        """
        self.property_details = property_details
        self.evaluator_details = evaluator_details
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_page(self):
        """Add a new page to the PDF document."""
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)

    def header(self):
        """Add header to the document."""
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, 'Parecer Técnico de Avaliação Mercadológica (PTAM)', ln=True, align='C')
        self.pdf.ln(10)

    def add_property_info(self):
        """Add property information to the document."""
        self.pdf.set_font("Arial", 'B', 14)
        self.pdf.cell(0, 10, 'Dados do Imóvel', ln=True)

        self.pdf.set_font("Arial", size=12)
        for key, value in self.property_details.items():
            self.pdf.cell(0, 10, f"{key}: {value}", ln=True)

        self.pdf.ln(10)

    def add_evaluator_info(self):
        """Add evaluator information to the document."""
        self.pdf.set_font("Arial", 'B', 14)
        self.pdf.cell(0, 10, 'Dados do Avaliador', ln=True)

        self.pdf.set_font("Arial", size=12)
        for key, value in self.evaluator_details.items():
            self.pdf.cell(0, 10, f"{key}: {value}", ln=True)

        self.pdf.ln(10)

    def add_compliance_info(self):
        """Add compliance information to the document."""
        self.pdf.set_font("Arial", 'B', 14)
        self.pdf.cell(0, 10, 'Conformidade', ln=True)
        
        self.pdf.set_font("Arial", size=12)
        compliance_statement = (
            "Este parecer técnico foi elaborado em conformidade com a ABNT NBR 14.653 "
            "e a Resolução COFECI nº 1.066/07."
        )
        self.pdf.multi_cell(0, 10, compliance_statement)
        self.pdf.ln(10)

    def save_document(self, filename):
        """Save the generated PDF document to a file.

        Args:
            filename (str): The file path to save the PDF document.
        """
        try:
            self.pdf.output(filename)
            print(f"Document saved successfully: {filename}")
        except Exception as e:
            print(f"An error occurred while saving the document: {e}")

    def generate_ptam(self, filename):
        """Generate the PTAM document.

        Args:
            filename (str): The file path for the output PDF document.
        """
        self.add_page()
        self.header()
        self.add_property_info()
        self.add_evaluator_info()
        self.add_compliance_info()
        self.save_document(filename)

# Example usage
def main():
    property_details = {
        "Endereço": "Rua das Flores, 123",
        "Tipo": "Apartamento",
        "Área útil": "80 m²",
        "Valor de mercado": "R$ 500.000,00",
    }

    evaluator_details = {
        "Nome": "João da Silva",
        "CRECI": "12345",
        "Data de Avaliação": datetime.now().strftime("%d/%m/%Y"),
    }

    ptam = PTAMDocument(property_details, evaluator_details)
    ptam.generate_ptam("PTAM_Avaliacao.pdf")

if __name__ == "__main__":
    main()
```
