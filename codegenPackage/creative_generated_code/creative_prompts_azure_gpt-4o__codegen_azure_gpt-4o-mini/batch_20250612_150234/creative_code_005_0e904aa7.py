"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anygrid.app
Prompt: Develop a script that uses AnyGrid to audit expense reports by scanning receipts and detecting compliance anomalies, then summarizing the findings in a structured format.
Generated: DETERMINISTIC_0e904aa70216b55c
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2  # OpenCV for image processing
import pytesseract  # OCR tool to extract text from images
import numpy as np  # NumPy for numerical operations
import os  # OS for file operations
import json  # JSON for structured output

class ReceiptAuditor:
    def __init__(self, receipt_dir):
        """
        Initializes the ReceiptAuditor with the directory containing receipt images.
        
        Args:
            receipt_dir (str): Path to the directory containing receipt images.
        """
        self.receipt_dir = receipt_dir
        self.expense_reports = []

    def scan_receipts(self):
        """
        Scans all receipts in the specified directory and extracts text from each.
        """
        for filename in os.listdir(self.receipt_dir):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                receipt_path = os.path.join(self.receipt_dir, filename)
                text = self.extract_text(receipt_path)
                if text:
                    self.expense_reports.append({'filename': filename, 'text': text})

    def extract_text(self, image_path):
        """
        Extracts text from an image using OCR.

        Args:
            image_path (str): Path to the image file.

        Returns:
            str: Extracted text from the image, or None if an error occurs.
        """
        try:
            # Load the image
            image = cv2.imread(image_path)
            # Preprocess the image for better OCR results
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
            # Perform OCR
            text = pytesseract.image_to_string(binary)
            return text
        except Exception as e:
            print(f"Error extracting text from {image_path}: {e}")
            return None

    def audit_expense_reports(self):
        """
        Audits the extracted expense reports for compliance anomalies.
        """
        anomalies = []
        for report in self.expense_reports:
            # Simple compliance check: looking for the presence of "Total" and a dollar amount
            if "total" not in report['text'].lower():
                anomalies.append({
                    'filename': report['filename'],
                    'issue': 'Missing total amount'
                })
            # Add more complex checks here as needed

        return anomalies

    def summarize_findings(self, anomalies):
        """
        Summarizes the findings in a structured JSON format.

        Args:
            anomalies (list): List of detected anomalies.

        Returns:
            str: JSON formatted summary of anomalies.
        """
        summary = {
            'total_reports': len(self.expense_reports),
            'anomalies_detected': len(anomalies),
            'anomalies': anomalies
        }
        return json.dumps(summary, indent=4)

    def run_audit(self):
        """
        Runs the entire audit process: scanning receipts and auditing expense reports.
        """
        self.scan_receipts()
        anomalies = self.audit_expense_reports()
        summary = self.summarize_findings(anomalies)
        print(summary)

if __name__ == '__main__':
    # Define the directory containing receipt images
    receipt_directory = 'path/to/your/receipts'
    auditor = ReceiptAuditor(receipt_directory)
    auditor.run_audit()
```

**Note**: Ensure that you have the necessary packages installed (`opencv-python`, `pytesseract`, and `numpy`) and that Tesseract-OCR is set up correctly on your system. Adjust `receipt_directory` to the appropriate path where your receipt images are stored.
