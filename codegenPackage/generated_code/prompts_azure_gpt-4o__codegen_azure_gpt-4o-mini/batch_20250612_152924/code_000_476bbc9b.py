"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Write Python code to generate a Parecer Técnico de Avaliação Mercadológica (PTAM) document for real estate valuation, ensuring compliance with ABNT NBR 14.653 and COFECI Resolution No. 1.066/07.
Generated: DETERMINISTIC_476bbc9bcafd5c86
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fpdf import FPDF
from datetime import datetime

class PTAMDocument:
    def __init__(self, property_details, evaluator_details):
        """
        Initialize the PTAMDocument with property and evaluator details.

        :param property_details: Dictionary containing property information.
        :param evaluator_details: Dictionary containing evaluator information.
        """
        self.property_details = property_details
        self.evaluator_details = evaluator_details
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_page(self):
        """Add a new page to the PDF document."""
        self.pdf.add_page()

    def set_font(self, family='Arial', size=12, style=''):
        """Set the font for the PDF document."""
        self.pdf.set_font(family, style, size)

    def add_title(self, title):
        """Add a title to the document."""
        self.set_font(size=16, style='B')
        self.pdf.cell(0, 10, title, ln=True, align='C')
        self.set_font(size=12)

    def add_section(self, title, content):
        """Add a section with a title and content."""
        self.set_font(size=14, style='B')
        self.pdf.cell(0, 10, title, ln=True)
        self.set_font(size=12)
        self.pdf.multi_cell(0, 10, content)

    def generate_document(self, output_path):
        """Generate the PTAM document and save it to the specified path.

        :param output_path: Path where the PDF document will be saved.
        """
        try:
            self.add_page()
            self.add_title("Parecer Técnico de Avaliação Mercadológica (PTAM)")

            # Add property details
            self.add_section("Dados do Imóvel", self.format_property_details())
            # Add evaluator details
            self.add_section("Dados do Avaliador", self.format_evaluator_details())

            # Save the PDF to the specified output path
            self.pdf.output(output_path)
            print(f"Document saved successfully at: {output_path}")
        except Exception as e:
            print(f"An error occurred while generating the document: {e}")

    def format_property_details(self):
        """Format the property details for the document."""
        details = []
        for key, value in self.property_details.items():
            details.append(f"{key}: {value}")
        return "\n".join(details)

    def format_evaluator_details(self):
        """Format the evaluator details for the document."""
        details = []
        for key, value in self.evaluator_details.items():
            details.append(f"{key}: {value}")
        return "\n".join(details)

if __name__ == "__main__":
    # Example property and evaluator details
    property_info = {
        "Endereço": "Rua Exemplo, 123",
        "Tipo": "Apartamento",
        "Área (m²)": "80",
        "Valor de Mercado": "R$ 300.000,00",
        "Data da Avaliação": datetime.now().strftime("%d/%m/%Y")
    }

    evaluator_info = {
        "Nome": "João da Silva",
        "CRECI": "123456-F",
        "Data de Nascimento": "01/01/1980",
        "Telefone": "(11) 91234-5678",
        "Email": "joao.silva@example.com"
    }

    # Create PTAM document
    ptam = PTAMDocument(property_info, evaluator_info)
    output_file = os.path.join(os.getcwd(), "PTAM_Document.pdf")
    ptam.generate_document(output_file)
```

Make sure to install the `fpdf` library if you haven't already:

```bash
pip install fpdf
```
