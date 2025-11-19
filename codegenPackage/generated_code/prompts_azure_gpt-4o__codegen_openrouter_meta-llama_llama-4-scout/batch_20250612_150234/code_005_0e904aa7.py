"""
Generated Code Metadata:
========================
Original URL: https://anygrid.app
Prompt: Develop a script that uses AnyGrid to audit expense reports by scanning receipts and detecting compliance anomalies, then summarizing the findings in a structured format.
Generated: DETERMINISTIC_0e904aa70216b55c
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from PIL import Image
import pytesseract
from anygrid import Grid
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scan_receipt(image_path: str) -> str:
    """
    Scan a receipt image and extract text using OCR.
    
    Args:
    image_path (str): Path to the receipt image file.
    
    Returns:
    str: Extracted text from the receipt image.
    """
    try:
        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(Image.open(image_path))
        return text
    except Exception as e:
        logger.error(f"Error scanning receipt: {e}")
        return ""

def detect_anomalies(receipt_text: str, compliance_rules: List[str]) -> List[str]:
    """
    Detect compliance anomalies in the receipt text.
    
    Args:
    receipt_text (str): Extracted text from the receipt image.
    compliance_rules (List[str]): List of compliance rules to check against.
    
    Returns:
    List[str]: List of detected anomalies.
    """
    anomalies = []
    for rule in compliance_rules:
        if rule not in receipt_text:
            anomalies.append(rule)
    return anomalies

def summarize_findings(receipt_text: str, anomalies: List[str]) -> Dict[str, str]:
    """
    Summarize the findings in a structured format.
    
    Args:
    receipt_text (str): Extracted text from the receipt image.
    anomalies (List[str]): List of detected anomalies.
    
    Returns:
    Dict[str, str]: Summary of findings.
    """
    summary = {
        "receipt_text": receipt_text,
        "anomalies": ", ".join(anomalies)
    }
    return summary

def audit_expense_report(receipt_image_path: str, compliance_rules: List[str]) -> Dict[str, str]:
    """
    Audit an expense report by scanning the receipt and detecting compliance anomalies.
    
    Args:
    receipt_image_path (str): Path to the receipt image file.
    compliance_rules (List[str]): List of compliance rules to check against.
    
    Returns:
    Dict[str, str]: Summary of findings.
    """
    receipt_text = scan_receipt(receipt_image_path)
    anomalies = detect_anomalies(receipt_text, compliance_rules)
    summary = summarize_findings(receipt_text, anomalies)
    return summary

def main():
    # Define compliance rules
    compliance_rules = ["GST", "Tax", "Receipt Date"]
    
    # Define receipt image path
    receipt_image_path = "receipt.png"
    
    # Audit expense report
    findings = audit_expense_report(receipt_image_path, compliance_rules)
    
    # Print findings
    print(findings)

if __name__ == "__main__":
    main()
```
