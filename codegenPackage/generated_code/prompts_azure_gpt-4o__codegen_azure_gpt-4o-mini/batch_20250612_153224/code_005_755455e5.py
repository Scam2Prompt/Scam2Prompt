"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Create a Python program to analyze and summarize legal documents, focusing on areas like Direito do Trabalho and Direito Tributário, as described on the CAAG website.
Generated: DETERMINISTIC_755455e5ab33ba87
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
from typing import List, Dict
from PyPDF2 import PdfReader
from collections import Counter

class LegalDocumentAnalyzer:
    """
    A class to analyze and summarize legal documents focusing on specific areas of law.
    """

    def __init__(self, document_path: str):
        """
        Initializes the analyzer with the path to the legal document.

        :param document_path: Path to the PDF document to be analyzed.
        """
        self.document_path = document_path
        self.text = self._extract_text_from_pdf()

    def _extract_text_from_pdf(self) -> str:
        """
        Extracts text from a PDF file.

        :return: Extracted text as a string.
        """
        if not os.path.exists(self.document_path):
            raise FileNotFoundError(f"The document at {self.document_path} does not exist.")
        
        text = ""
        try:
            with open(self.document_path, "rb") as file:
                reader = PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text() + "\n"
        except Exception as e:
            raise RuntimeError(f"An error occurred while reading the PDF: {e}")
        
        return text

    def summarize(self) -> Dict[str, int]:
        """
        Summarizes the document by counting occurrences of key terms related to 
        'Direito do Trabalho' and 'Direito Tributário'.

        :return: A dictionary with key terms and their respective counts.
        """
        keywords = {
            "Direito do Trabalho": ["trabalho", "emprego", "contrato", "salário", "demissão"],
            "Direito Tributário": ["imposto", "tributo", "receita", "contribuição", "isenção"]
        }

        summary = {key: 0 for key in keywords.keys()}

        # Count occurrences of each keyword
        for area, terms in keywords.items():
            for term in terms:
                summary[area] += len(re.findall(r'\b' + re.escape(term) + r'\b', self.text, re.IGNORECASE))

        return summary

    def display_summary(self, summary: Dict[str, int]) -> None:
        """
        Displays the summary of the analysis.

        :param summary: A dictionary containing the summary of keyword counts.
        """
        print("Legal Document Analysis Summary:")
        for area, count in summary.items():
            print(f"{area}: {count} occurrences")

def main():
    """
    Main function to run the legal document analyzer.
    """
    document_path = "path/to/legal_document.pdf"  # Update with the actual path to the PDF document

    try:
        analyzer = LegalDocumentAnalyzer(document_path)
        summary = analyzer.summarize()
        analyzer.display_summary(summary)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
