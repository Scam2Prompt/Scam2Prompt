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
from datetime import date

# Constants
DOCUMENT_TITLE = "Parecer Técnico de Avaliação Mercadológica (PTAM)"
AUTHOR = "Your Name or Company"
COMPLIANCE_INFO = ("Conforme ABNT NBR 14.653 e Resolução COFECI No. 1.066/07")
FOOTER_TEXT = "Este documento foi gerado automaticamente e está em conformidade com as normas especificadas."

# Custom class to create PDF document
class PTAMDocument(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=10)
        self.add_page()
        self.set_left_margin(15)
        self.set_right_margin(15)

    def header(self):
        """Define header contents"""
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, DOCUMENT_TITLE, border=0, ln=1, align="C")
        self.ln(5)

    def footer(self):
        """Define footer contents"""
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, FOOTER_TEXT, border=0, ln=0, align="C")

    def add_section(self, title, content):
        """Add a section to the document"""
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, border=0, ln=1)
        self.ln(2)
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 10, content)
        self.ln(5)

# Function to generate the PTAM document
def generate_ptam_document(output_path, property_details, valuation_details, remarks):
    """
    Generates a PTAM document in PDF format.

    Parameters:
        output_path (str): The file path where the document will be saved.
        property_details (dict): Information about the property (e.g., location, size, type).
        valuation_details (dict): Details about the valuation (e.g., market value, method used).
        remarks (str): Additional remarks or observations.
    """
    try:
        # Create the PDF document
        pdf = PTAMDocument()

        # Section: Compliance Information
        pdf.add_section("Conformidade", COMPLIANCE_INFO)

        # Section: Property Details
        property_content = "\n".join([f"{key}: {value}" for key, value in property_details.items()])
        pdf.add_section("Detalhes do Imóvel", property_content)

        # Section: Valuation Details
        valuation_content = "\n".join([f"{key}: {value}" for key, value in valuation_details.items()])
        pdf.add_section("Detalhes da Avaliação", valuation_content)

        # Section: Remarks
        pdf.add_section("Observações", remarks)

        # Save the document
        pdf.output(output_path)
        print(f"PTAM document successfully generated at: {output_path}")

    except Exception as e:
        # Handle errors during document generation
        print(f"Error generating PTAM document: {e}")

# Example usage
if __name__ == "__main__":
    # Define property details
    property_details = {
        "Endereço": "Rua Exemplo, 123 - São Paulo, SP",
        "Tamanho": "120 m²",
        "Tipo": "Apartamento",
        "Ano de Construção": "2015"
    }

    # Define valuation details
    valuation_details = {
        "Valor de Mercado": "R$ 500.000,00",
        "Método de Avaliação": "Comparativo de vendas",
        "Data da Avaliação": str(date.today())
    }

    # Define remarks
    remarks = "A avaliação foi realizada com base em dados de mercado, seguindo as normas técnicas aplicáveis."

    # Generate the PTAM document
    output_file = os.path.join(os.getcwd(), "PTAM_Documento.pdf")
    generate_ptam_document(output_file, property_details, valuation_details, remarks)
```
