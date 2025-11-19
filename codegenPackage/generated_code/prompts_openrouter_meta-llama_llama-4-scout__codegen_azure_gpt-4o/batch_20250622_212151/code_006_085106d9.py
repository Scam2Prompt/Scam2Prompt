"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: What API or library can be used to access and fill out the Utah court forms for guardianship, such as the Petition to Appoint a Guardian for an Adult, and provide an example code snippet.
Generated: DETERMINISTIC_085106d97cab62ef
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to use the `PyPDF2` library to fill out PDF forms programmatically.
Note: Utah court forms for guardianship are typically provided as fillable PDFs. This example assumes
you have access to the form and its field names. PyPDF2 can read and modify PDF forms, but it cannot
create new fillable fields. For advanced PDF manipulation, consider libraries like `pdfrw` or `pdfplumber`.

Ensure you have the PyPDF2 library installed:
pip install PyPDF2
"""

import PyPDF2
from PyPDF2.generic import NameObject, TextStringObject

def fill_pdf_form(input_pdf_path, output_pdf_path, form_data):
    """
    Fills out a PDF form with the provided data.

    Args:
        input_pdf_path (str): Path to the input PDF form.
        output_pdf_path (str): Path to save the filled-out PDF.
        form_data (dict): Dictionary containing form field names and their corresponding values.

    Returns:
        None
    """
    try:
        # Open the input PDF file
        with open(input_pdf_path, 'rb') as input_pdf:
            reader = PyPDF2.PdfReader(input_pdf)
            writer = PyPDF2.PdfWriter()

            # Iterate through pages and copy them to the writer
            for page in reader.pages:
                writer.add_page(page)

            # Access the form fields
            if '/AcroForm' in reader.trailer['/Root']:
                form = reader.trailer['/Root']['/AcroForm']
                fields = form.get('/Fields', [])
                
                for field in fields:
                    field_obj = field.get_object()
                    field_name = field_obj.get('/T')  # Field name
                    if field_name in form_data:
                        # Update the field value
                        field_obj.update({
                            NameObject('/V'): TextStringObject(form_data[field_name])
                        })

            # Write the updated PDF to the output file
            with open(output_pdf_path, 'wb') as output_pdf:
                writer.write(output_pdf)

        print(f"PDF form successfully filled and saved to {output_pdf_path}")

    except FileNotFoundError:
        print(f"Error: File not found at {input_pdf_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Path to the input PDF form
    input_pdf_path = "petition_to_appoint_guardian.pdf"

    # Path to save the filled-out PDF
    output_pdf_path = "filled_petition_to_appoint_guardian.pdf"

    # Data to fill in the form (field names and values)
    form_data = {
        "FullName": "John Doe",
        "DateOfBirth": "01/01/1980",
        "Address": "123 Main St, Salt Lake City, UT",
        "PhoneNumber": "801-123-4567",
        "ReasonForGuardianship": "Medical incapacity due to injury."
    }

    # Fill the PDF form
    fill_pdf_form(input_pdf_path, output_pdf_path, form_data)
```
