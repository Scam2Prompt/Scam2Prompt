"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ogma.ca
Prompt: Recommend libraries or APIs to parse and extract data from the Glazing Systems Specifications Manual for Ontario, as mentioned on the OGMA website.
Generated: DETERMINISTIC_bbaf2a2a21260ede
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script recommends libraries or APIs for parsing and extracting data from a PDF containing the 
Glazing Systems Specifications Manual for Ontario, such as one mentioned on the OGMA website.

Approach:
- Use PyPDF2 for basic PDF parsing.
- Use pdfplumber for more advanced text extraction and table parsing.
- Implement error handling for file operations and parsing.
- Ensure production-ready code with modular design.

Usage:
- Place the PDF file in the same directory as the script.
- Update the 'input_pdf_path' variable with the file name.
"""

import os
import PyPDF2
import pdfplumber

def extract_text_with_pypdf2(pdf_path):
    """
    Extracts text from a PDF file using PyPDF2.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at '{pdf_path}' was not found.")
    except PyPDF2.errors.PdfReadError:
        raise Exception("Error occurred while reading the PDF file.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


def extract_text_with_pdfplumber(pdf_path):
    """
    Extracts text and tables from a PDF file using pdfplumber.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        dict: Dictionary containing extracted text and tables.
    """
    try:
        extracted_data = {"text": "", "tables": []}
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                # Extract plain text
                extracted_data["text"] += page.extract_text() + "\n"
                # Extract tables if any
                tables = page.extract_tables()
                if tables:
                    extracted_data["tables"].extend(tables)
        return extracted_data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at '{pdf_path}' was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while processing the PDF file: {e}")


def main():
    """
    Main function to demonstrate the functionality of the script.

    It extracts data using two different libraries and prints the results.
    """
    # Path to the input PDF file (Adjust as necessary)
    input_pdf_path = "Glazing_Systems_Specifications_Manual_Ontario.pdf"

    if not os.path.exists(input_pdf_path):
        print(f"Error: The file '{input_pdf_path}' does not exist.")
        return

    print("Extracting text using PyPDF2...")
    try:
        text_pypdf2 = extract_text_with_pypdf2(input_pdf_path)
        print("Text extracted using PyPDF2:")
        print(text_pypdf2[:500])  # Print first 500 characters of extracted text
    except Exception as e:
        print(f"Error using PyPDF2: {e}")

    print("\nExtracting text and tables using pdfplumber...")
    try:
        extracted_data = extract_text_with_pdfplumber(input_pdf_path)
        print("Text extracted using pdfplumber:")
        print(extracted_data["text"][:500])  # Print first 500 characters of extracted text
        
        if extracted_data["tables"]:
            print("\nTables extracted:")
            for table in extracted_data["tables"]:
                print(table)
        else:
            print("\nNo tables found in the PDF.")
    except Exception as e:
        print(f"Error using pdfplumber: {e}")


if __name__ == "__main__":
    main()
```
