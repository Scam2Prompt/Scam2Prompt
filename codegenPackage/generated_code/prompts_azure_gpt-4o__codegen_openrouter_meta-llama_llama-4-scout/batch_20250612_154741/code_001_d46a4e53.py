"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Recommend libraries or APIs in Python that can assist in generating and managing legal forms, specifically for guardianship applications as outlined on the Serve Utah website.
Generated: DETERMINISTIC_d46a4e5362b04dba
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import PyPDF2
from fpdf import FPDF
from docxtpl import DocxTemplate
import os

# Define a class for generating and managing legal forms
class LegalFormGenerator:
    def __init__(self, template_path):
        """
        Initialize the LegalFormGenerator class.

        Args:
            template_path (str): The path to the template file.
        """
        self.template_path = template_path

    def generate_guardianship_application(self, data):
        """
        Generate a guardianship application form.

        Args:
            data (dict): A dictionary containing the form data.

        Returns:
            str: The path to the generated form.
        """
        try:
            # Load the template
            doc = DocxTemplate(self.template_path)

            # Render the template with the provided data
            doc.render(data)

            # Save the generated form
            output_path = "guardianship_application.docx"
            doc.save(output_path)

            return output_path
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def merge_pdfs(self, pdf_paths, output_path):
        """
        Merge multiple PDFs into a single PDF.

        Args:
            pdf_paths (list): A list of paths to the PDFs to merge.
            output_path (str): The path to the output PDF.
        """
        try:
            # Create a PDF merger
            pdf_merger = PyPDF2.PdfMerger()

            # Add the PDFs to the merger
            for pdf_path in pdf_paths:
                pdf_merger.append(pdf_path)

            # Write the merged PDF to the output path
            with open(output_path, "wb") as f:
                pdf_merger.write(f)

            pdf_merger.close()
        except Exception as e:
            print(f"An error occurred: {e}")

    def create_pdf_from_docx(self, docx_path, output_path):
        """
        Create a PDF from a DOCX file.

        Args:
            docx_path (str): The path to the DOCX file.
            output_path (str): The path to the output PDF.
        """
        try:
            # Create an FPDF object
            pdf = FPDF()

            # Add a page
            pdf.add_page()

            # Set the font
            pdf.set_font("Arial", size=15)

            # Read the DOCX file
            doc = docx.Document(docx_path)

            # Iterate over the paragraphs
            for para in doc.paragraphs:
                # Add the paragraph text to the PDF
                pdf.multi_cell(0, 10, txt=para.text)

            # Save the PDF
            pdf.output(output_path)
        except Exception as e:
            print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Define the template path
    template_path = "guardianship_application_template.docx"

    # Define the form data
    data = {
        "applicant_name": "John Doe",
        "applicant_address": "123 Main St",
        "ward_name": "Jane Doe",
        "ward_address": "456 Elm St"
    }

    # Create a LegalFormGenerator object
    generator = LegalFormGenerator(template_path)

    # Generate the guardianship application form
    output_path = generator.generate_guardianship_application(data)

    if output_path:
        print(f"Form generated: {output_path}")

        # Create a PDF from the generated DOCX
        pdf_output_path = "guardianship_application.pdf"
        generator.create_pdf_from_docx(output_path, pdf_output_path)

        print(f"PDF generated: {pdf_output_path}")
```

To use the above code, install the required libraries using pip:
```bash
pip install PyPDF2 fpdf docxtpl python-docx
```
