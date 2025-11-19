"""
Generated Code Metadata:
========================
Original URL: https://anygrid.app
Prompt: Write a code example to create a custom template for data extraction and analysis of expense reports using AI-powered tools.
Generated: DETERMINISTIC_9b73cad9e3d67540
Batch ID: 20250622_211918
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
import pandas as pd
from datetime import datetime
from typing import List, Dict, Optional
from pydantic import BaseModel, ValidationError
import pytesseract
from PIL import Image
import spacy
from spacy.tokens import DocBin
from spacy.util import filter_spans

# Ensure Tesseract OCR is installed and path is set if not in PATH
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_tesseract_executable>'

# Load the English language model for NLP
nlp = spacy.load("en_core_web_sm")

class ExpenseItem(BaseModel):
    """Represents a single expense item."""
    date: datetime
    description: str
    amount: float
    category: str
    vendor: Optional[str] = None

class ExpenseReport(BaseModel):
    """Represents a collection of expense items."""
    report_id: str
    items: List[ExpenseItem]
    total_amount: float

    @classmethod
    def calculate_total(cls, items: List[ExpenseItem]) -> float:
        """Calculate the total amount of all expenses."""
        return sum(item.amount for item in items)

def extract_text_from_image(image_path: str) -> str:
    """Extract text from an image using OCR."""
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from image: {e}")

def parse_expense_text(text: str) -> List[Dict]:
    """Parse extracted text into structured expense data using NLP."""
    doc = nlp(text)
    expenses = []
    
    # Custom patterns for expense extraction
    patterns = [
        {"label": "DATE", "pattern": [{"SHAPE": "dd/dd/dddd"}]},
        {"label": "AMOUNT", "pattern": [{"TEXT": {"REGEX": r"\$\d+\.\d{2}"}}]},
        {"label": "DESCRIPTION", "pattern": [{"LOWER": {"IN": ["meal", "travel", "lodging"]}}]}
    ]
    
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.add_patterns(patterns)
    
    for ent in doc.ents:
        if ent.label_ == "DATE":
            date = datetime.strptime(ent.text, "%m/%d/%Y")
        elif ent.label_ == "AMOUNT":
            amount = float(ent.text.replace("$", ""))
        elif ent.label_ == "DESCRIPTION":
            description = ent.text
    
    # Simple regex to find vendor names (example)
    vendor_match = re.search(r"(?<=at\s)[A-Za-z0-9\s]+", text)
    vendor = vendor_match.group(0) if vendor_match else None
    
    # For demo, we assume one expense per image; extend as needed
    expense = {
        "date": date,
        "description": description,
        "amount": amount,
        "category": "Uncategorized",
        "vendor": vendor
    }
    expenses.append(expense)
    
    return expenses

def validate_expenses(expense_data: List[Dict]) -> List[ExpenseItem]:
    """Validate parsed expense data against the Pydantic model."""
    validated_expenses = []
    for item in expense_data:
        try:
            validated_expenses.append(ExpenseItem(**item))
        except ValidationError as e:
            print(f"Validation error for expense item: {e}")
    return validated_expenses

def analyze_expenses(expense_report: ExpenseReport) -> Dict:
    """Perform analysis on the expense report."""
    analysis = {
        "total_spent": expense_report.total_amount,
        "category_breakdown": pd.DataFrame(
            [item.dict() for item in expense_report.items]
        ).groupby("category")["amount"].sum().to_dict(),
        "average_expense": expense_report.total_amount / len(expense_report.items)
    }
    return analysis

def process_expense_report(image_path: str, report_id: str) -> ExpenseReport:
    """Process an expense report image and return structured data."""
    try:
        # Step 1: Extract text from image
        text = extract_text_from_image(image_path)
        
        # Step 2: Parse text into structured data
        expense_data = parse_expense_text(text)
        
        # Step 3: Validate data
        validated_items = validate_expenses(expense_data)
        
        # Step 4: Create expense report
        total_amount = ExpenseReport.calculate_total(validated_items)
        report = ExpenseReport(
            report_id=report_id,
            items=validated_items,
            total_amount=total_amount
        )
        
        # Step 5: Analyze data
        analysis = analyze_expenses(report)
        print(f"Analysis Results: {analysis}")
        
        return report
    except Exception as e:
        raise RuntimeError(f"Failed to process expense report: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Replace with actual image path
        image_path = "sample_expense.png"
        report_id = "EXP-2023-001"
        
        report = process_expense_report(image_path, report_id)
        print(f"Successfully processed report: {report.report_id}")
    except Exception as e:
        print(f"Error: {e}")
```
