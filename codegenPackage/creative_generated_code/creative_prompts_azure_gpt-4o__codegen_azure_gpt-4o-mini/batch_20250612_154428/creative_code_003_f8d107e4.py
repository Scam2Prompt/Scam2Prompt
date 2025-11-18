"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://confinance.info
Prompt: Provide a Python script to convert conservation finance documentation into both .md and .pdf formats, as described on https://confinance.info.
Generated: DETERMINISTIC_f8d107e4e82636bc
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import markdown
from weasyprint import HTML
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_md_to_pdf(md_file_path, pdf_file_path):
    """
    Convert Markdown file to PDF format.

    Args:
        md_file_path (str): The path to the Markdown file.
        pdf_file_path (str): The path where the PDF will be saved.

    Raises:
        FileNotFoundError: If the Markdown file does not exist.
        Exception: If an error occurs during conversion.
    """
    if not os.path.exists(md_file_path):
        logging.error(f"Markdown file not found: {md_file_path}")
        raise FileNotFoundError(f"The specified Markdown file does not exist: {md_file_path}")

    try:
        # Read the Markdown file
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
            logging.info(f"Successfully read Markdown file: {md_file_path}")

        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content)
        logging.info("Converted Markdown to HTML.")

        # Convert HTML to PDF and save it
        HTML(string=html_content).write_pdf(pdf_file_path)
        logging.info(f"Successfully converted to PDF: {pdf_file_path}")

    except Exception as e:
        logging.error(f"Error during conversion: {str(e)}")
        raise

def convert_documentation(md_files):
    """
    Convert a list of Markdown files to both Markdown and PDF formats.

    Args:
        md_files (list): A list of Markdown file paths.

    Raises:
        Exception: If an error occurs during conversion of any file.
    """
    for md_file in md_files:
        # Define the output PDF file name
        pdf_file = f"{os.path.splitext(md_file)[0]}.pdf"
        logging.info(f"Starting conversion for: {md_file}")

        try:
            convert_md_to_pdf(md_file, pdf_file)
            logging.info(f"Completed conversion for: {md_file}")
        except Exception as e:
            logging.error(f"Failed to convert {md_file}: {str(e)}")

if __name__ == "__main__":
    # List of Markdown files to convert
    markdown_files = [
        'conservation_finance_guide.md',
        'case_studies.md',
        'funding_sources.md',
    ]

    # Convert the documentation
    convert_documentation(markdown_files)
```

### Requirements:
- Install required packages:
```bash
pip install markdown weasyprint
``` 

### Note:
- Ensure that the Markdown files exist in the same directory or provide the correct paths.
- This script is designed to be run as a standalone program.
