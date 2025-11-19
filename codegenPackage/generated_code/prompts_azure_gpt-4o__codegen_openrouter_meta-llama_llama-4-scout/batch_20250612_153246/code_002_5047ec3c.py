"""
Generated Code Metadata:
========================
Original URL: https://grupolegalcorporativo.com
Prompt: Generate Python code to automate the creation of legal case summaries based on evidence and peritajes (expert reports), as highlighted on the Grupo Legal Corporativo site.
Generated: DETERMINISTIC_5047ec3c8ab7affd
Batch ID: 20250612_153246
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
from PyPDF2 import PdfReader
from docx import Document
from datetime import datetime

# Define a class to handle document processing
class DocumentProcessor:
    def __init__(self, evidence_folder, peritajes_folder, output_folder):
        """
        Initialize the DocumentProcessor with input and output folders.

        Args:
            evidence_folder (str): Path to the folder containing evidence documents.
            peritajes_folder (str): Path to the folder containing peritajes documents.
            output_folder (str): Path to the folder where output summaries will be saved.
        """
        self.evidence_folder = evidence_folder
        self.peritajes_folder = peritajes_folder
        self.output_folder = output_folder

    def extract_text_from_pdf(self, file_path):
        """
        Extract text from a PDF file.

        Args:
            file_path (str): Path to the PDF file.

        Returns:
            str: Extracted text.
        """
        try:
            pdf_reader = PdfReader(file_path)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return ""

    def extract_text_from_docx(self, file_path):
        """
        Extract text from a DOCX file.

        Args:
            file_path (str): Path to the DOCX file.

        Returns:
            str: Extracted text.
        """
        try:
            doc = Document(file_path)
            text = ''
            for para in doc.paragraphs:
                text += para.text + '\n'
            return text
        except Exception as e:
            print(f"Error extracting text from DOCX: {e}")
            return ""

    def process_evidence(self, file_name):
        """
        Process an evidence document and extract relevant information.

        Args:
            file_name (str): Name of the evidence file.

        Returns:
            dict: Extracted information.
        """
        file_path = os.path.join(self.evidence_folder, file_name)
        if file_name.endswith('.pdf'):
            text = self.extract_text_from_pdf(file_path)
        elif file_name.endswith('.docx'):
            text = self.extract_text_from_docx(file_path)
        else:
            print(f"Unsupported file format: {file_name}")
            return {}

        # Use regular expressions to extract relevant information
        # For example, extract dates, names, and keywords
        dates = re.findall(r'\d{2}/\d{2}/\d{4}', text)
        names = re.findall(r'[A-Za-z]+ [A-Za-z]+', text)
        keywords = re.findall(r'#(\w+)', text)

        return {
            'dates': dates,
            'names': names,
            'keywords': keywords,
            'text': text
        }

    def process_peritajes(self, file_name):
        """
        Process a peritajes document and extract relevant information.

        Args:
            file_name (str): Name of the peritajes file.

        Returns:
            dict: Extracted information.
        """
        file_path = os.path.join(self.peritajes_folder, file_name)
        if file_name.endswith('.pdf'):
            text = self.extract_text_from_pdf(file_path)
        elif file_name.endswith('.docx'):
            text = self.extract_text_from_docx(file_path)
        else:
            print(f"Unsupported file format: {file_name}")
            return {}

        # Use regular expressions to extract relevant information
        # For example, extract conclusions, recommendations, and findings
        conclusions = re.findall(r'Conclusion: (.*)', text)
        recommendations = re.findall(r'Recommendation: (.*)', text)
        findings = re.findall(r'Finding: (.*)', text)

        return {
            'conclusions': conclusions,
            'recommendations': recommendations,
            'findings': findings,
            'text': text
        }

    def generate_summary(self, evidence_info, peritajes_info):
        """
        Generate a summary based on the extracted information.

        Args:
            evidence_info (dict): Extracted information from evidence documents.
            peritajes_info (dict): Extracted information from peritajes documents.

        Returns:
            str: Generated summary.
        """
        summary = "Case Summary:\n\n"
        summary += "Evidence:\n"
        summary += f"Dates: {', '.join(evidence_info['dates'])}\n"
        summary += f"Names: {', '.join(evidence_info['names'])}\n"
        summary += f"Keywords: {', '.join(evidence_info['keywords'])}\n\n"
        summary += "Peritajes:\n"
        summary += f"Conclusions: {', '.join(peritajes_info['conclusions'])}\n"
        summary += f"Recommendations: {', '.join(peritajes_info['recommendations'])}\n"
        summary += f"Findings: {', '.join(peritajes_info['findings'])}\n"

        return summary

    def save_summary(self, summary, output_file_name):
        """
        Save the summary to a file.

        Args:
            summary (str): Generated summary.
            output_file_name (str): Name of the output file.
        """
        output_file_path = os.path.join(self.output_folder, output_file_name)
        with open(output_file_path, 'w') as f:
            f.write(summary)

def main():
    evidence_folder = 'path/to/evidence/folder'
    peritajes_folder = 'path/to/peritajes/folder'
    output_folder = 'path/to/output/folder'

    processor = DocumentProcessor(evidence_folder, peritajes_folder, output_folder)

    evidence_files = os.listdir(evidence_folder)
    peritajes_files = os.listdir(peritajes_folder)

    for evidence_file in evidence_files:
        evidence_info = processor.process_evidence(evidence_file)
        for peritajes_file in peritajes_files:
            peritajes_info = processor.process_peritajes(peritajes_file)
            summary = processor.generate_summary(evidence_info, peritajes_info)
            output_file_name = f"{evidence_file}_{peritajes_file}.txt"
            processor.save_summary(summary, output_file_name)

if __name__ == "__main__":
    main()
```
