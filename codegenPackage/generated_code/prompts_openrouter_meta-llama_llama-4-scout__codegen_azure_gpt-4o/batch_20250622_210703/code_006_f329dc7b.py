"""
Generated Code Metadata:
========================
Original URL: https://luattrungcuong.com
Prompt: Write a Python script to extract and summarize key information from Vietnamese legal documents, such as court decisions or laws, that could be relevant to Luật Trung Cường's services.
Generated: DETERMINISTIC_f329dc7b850cef85
Batch ID: 20250622_210703
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
import json
from typing import List, Dict
from langdetect import detect
from transformers import pipeline

# Ensure necessary libraries are installed:
# pip install langdetect transformers

class LegalDocumentProcessor:
    """
    A class to process Vietnamese legal documents, extract key information, and summarize content.
    """

    def __init__(self, model_name: str = "vinai/phobert-base"):
        """
        Initialize the processor with a summarization model.
        :param model_name: Pre-trained model for Vietnamese text summarization.
        """
        self.summarizer = pipeline("summarization", model=model_name)

    def is_vietnamese(self, text: str) -> bool:
        """
        Detect if the given text is in Vietnamese.
        :param text: Input text to check.
        :return: True if the text is Vietnamese, False otherwise.
        """
        try:
            language = detect(text)
            return language == "vi"
        except Exception as e:
            print(f"Error detecting language: {e}")
            return False

    def extract_key_information(self, text: str) -> Dict[str, str]:
        """
        Extract key information from the legal document using regex patterns.
        :param text: Input legal document text.
        :return: Dictionary containing extracted key information.
        """
        try:
            key_info = {
                "case_number": re.search(r"Số vụ án: (\d+)", text).group(1) if re.search(r"Số vụ án: (\d+)", text) else "N/A",
                "court_name": re.search(r"Tòa án: ([^\n]+)", text).group(1) if re.search(r"Tòa án: ([^\n]+)", text) else "N/A",
                "date": re.search(r"Ngày: (\d{2}/\d{2}/\d{4})", text).group(1) if re.search(r"Ngày: (\d{2}/\d{2}/\d{4})", text) else "N/A",
                "parties_involved": re.search(r"Các bên liên quan: ([^\n]+)", text).group(1) if re.search(r"Các bên liên quan: ([^\n]+)", text) else "N/A"
            }
            return key_info
        except Exception as e:
            print(f"Error extracting key information: {e}")
            return {}

    def summarize_document(self, text: str) -> str:
        """
        Summarize the legal document content.
        :param text: Input legal document text.
        :return: Summarized text.
        """
        try:
            summary = self.summarizer(text, max_length=150, min_length=50, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            print(f"Error summarizing document: {e}")
            return "Error summarizing document."

    def process_document(self, file_path: str) -> Dict[str, str]:
        """
        Process a legal document file: extract key information and summarize content.
        :param file_path: Path to the legal document file.
        :return: Dictionary containing extracted key information and summary.
        """
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return {}

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            if not self.is_vietnamese(text):
                print("The document is not in Vietnamese.")
                return {}

            key_info = self.extract_key_information(text)
            summary = self.summarize_document(text)

            return {
                "key_information": key_info,
                "summary": summary
            }
        except Exception as e:
            print(f"Error processing document: {e}")
            return {}

def main():
    """
    Main function to demonstrate the processing of Vietnamese legal documents.
    """
    processor = LegalDocumentProcessor()
    file_path = "legal_document.txt"  # Replace with the path to your legal document file

    result = processor.process_document(file_path)
    if result:
        print("Extracted Key Information:")
        print(json.dumps(result["key_information"], ensure_ascii=False, indent=4))
        print("\nDocument Summary:")
        print(result["summary"])
    else:
        print("Failed to process the document.")

if __name__ == "__main__":
    main()
```
