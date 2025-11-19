"""
Generated Code Metadata:
========================
Original URL: https://nabberx.com
Prompt: Write a Python script that automates data management tasks, including document digitization and record-keeping, based on the solutions offered by NabberX.
Generated: DETERMINISTIC_53fdd7c5d4994aa4
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import datetime
import logging
from typing import List, Optional
from pathlib import Path
import pytesseract
from PIL import Image
import PyPDF2
import csv
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_management.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DocumentProcessor:
    """Handles document digitization and processing."""
    
    def __init__(self, output_dir: str = 'processed_documents'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def _validate_input_file(self, file_path: str) -> bool:
        """Validate if file exists and is supported."""
        path = Path(file_path)
        if not path.exists():
            logger.error(f"File not found: {file_path}")
            return False
        if path.suffix.lower() not in ['.pdf', '.jpg', '.jpeg', '.png']:
            logger.error(f"Unsupported file format: {file_path}")
            return False
        return True
    
    def digitize_document(self, file_path: str) -> Optional[str]:
        """Convert document to text using OCR."""
        if not self._validate_input_file(file_path):
            return None
            
        path = Path(file_path)
        try:
            if path.suffix.lower() == '.pdf':
                text = self._extract_text_from_pdf(path)
            else:
                text = self._extract_text_from_image(path)
                
            output_file = self.output_dir / f"{path.stem}_digitized.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text)
                
            logger.info(f"Successfully digitized: {file_path}")
            return str(output_file)
        except Exception as e:
            logger.error(f"Error digitizing {file_path}: {str(e)}")
            return None
    
    def _extract_text_from_pdf(self, pdf_path: Path) -> str:
        """Extract text from PDF file."""
        text = ""
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()
        return text
    
    def _extract_text_from_image(self, image_path: Path) -> str:
        """Extract text from image using Tesseract OCR."""
        image = Image.open(image_path)
        return pytesseract.image_to_string(image)

class RecordKeeper:
    """Manages record-keeping operations."""
    
    def __init__(self, database_dir: str = 'database'):
        self.database_dir = Path(database_dir)
        self.database_dir.mkdir(exist_ok=True)
        
    def create_record(self, record_data: dict, record_type: str) -> bool:
        """Create a new record in the database."""
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{record_type}_{timestamp}.json"
            filepath = self.database_dir / filename
            
            with open(filepath, 'w') as f:
                json.dump(record_data, f, indent=2)
                
            logger.info(f"Created record: {filename}")
            return True
        except Exception as e:
            logger.error(f"Error creating record: {str(e)}")
            return False
    
    def search_records(self, record_type: str, search_criteria: dict) -> List[dict]:
        """Search records matching criteria."""
        results = []
        try:
            for file in self.database_dir.glob(f"{record_type}_*.json"):
                with open(file, 'r') as f:
                    data = json.load(f)
                    if all(data.get(k) == v for k, v in search_criteria.items()):
                        results.append(data)
            return results
        except Exception as e:
            logger.error(f"Error searching records: {str(e)}")
            return []

class DataManager:
    """Main class for data management tasks."""
    
    def __init__(self):
        self.document_processor = DocumentProcessor()
        self.record_keeper = RecordKeeper()
        
    def process_documents(self, files: List[str]) -> List[str]:
        """Process multiple documents."""
        results = []
        for file in files:
            result = self.document_processor.digitize_document(file)
            if result:
                results.append(result)
        return results
    
    def export_to_csv(self, records: List[dict], output_file: str) -> bool:
        """Export records to CSV file."""
        if not records:
            logger.error("No records to export")
            return False
            
        try:
            keys = records[0].keys()
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(records)
            logger.info(f"Exported {len(records)} records to {output_file}")
            return True
        except Exception as e:
            logger.error(f"Error exporting to CSV: {str(e)}")
            return False

def main():
    """Example usage of the data management system."""
    manager = DataManager()
    
    # Example document processing
    documents = ['sample.pdf', 'receipt.jpg']
    processed_files = manager.process_documents(documents)
    print(f"Processed files: {processed_files}")
    
    # Example record keeping
    record_data = {
        'document_id': '12345',
        'type': 'invoice',
        'amount': 100.50,
        'date': '2023-01-15'
    }
    manager.record_keeper.create_record(record_data, 'invoice')
    
    # Example search
    results = manager.record_keeper.search_records('invoice', {'amount': 100.50})
    print(f"Search results: {results}")
    
    # Example export
    if results:
        manager.export_to_csv(results, 'invoices.csv')

if __name__ == '__main__':
    main()
```
