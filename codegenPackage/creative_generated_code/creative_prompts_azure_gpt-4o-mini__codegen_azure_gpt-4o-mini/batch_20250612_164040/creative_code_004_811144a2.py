"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://confinance.info
Prompt: Suggest a library for handling PDF documents that can be used to extract information from the appendices of the Conservation Finance resource.
Generated: DETERMINISTIC_811144a234580783
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import PyPDF2
import os

def extract_pdf_text(pdf_path, start_page=0, end_page=None):
    """
    Extracts text from a PDF file between specified page numbers.

    Args:
        pdf_path (str): The path to the PDF file.
        start_page (int): The page number to start extraction (zero-indexed).
        end_page (int): The page number to end extraction (zero-indexed, inclusive).
        
    Returns:
        str: The extracted text from the specified pages.
        
    Raises:
        FileNotFoundError: If the PDF file does not exist.
        PyPDF2.utils.PdfReadError: If there is an error reading the PDF file.
    """
    # Check if the PDF file exists
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"The PDF file '{pdf_path}' does not exist.")
    
    extracted_text = ''

    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        # Check if end_page is specified, if not set it to the last page
        if end_page is None or end_page >= len(reader.pages):
            end_page = len(reader.pages) - 1

        # Extract text from the specified pages
        for page_number in range(start_page, end_page + 1):
            page = reader.pages[page_number]
            extracted_text += page.extract_text() + '\n'  # Append page text

    return extracted_text.strip()  # Remove any extra newlines

# Example usage:
if __name__ == "__main__":
    pdf_file_path = "Conservation_Finance_Resource.pdf"
    
    try:
        # Change the page numbers as necessary for appending extraction
        text = extract_pdf_text(pdf_file_path, start_page=10, end_page=15)
        print(text)
    except Exception as e:
        print(f"An error occurred: {e}")
```
