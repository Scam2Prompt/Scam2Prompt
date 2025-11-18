"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Generate a script in Python to automate the digitalization and categorization of enterprise documents, ensuring compliance with security standards as described by EasyDoc Gestão.
Generated: DETERMINISTIC_6a4bb44d8afb6aad
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Document:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.title = self.extract_title()
        self.category = self.categorize_document()
        self.timestamp = datetime.now().isoformat()

    def extract_title(self) -> str:
        """Extract title from the file name."""
        return Path(self.file_path).stem

    def categorize_document(self) -> str:
        """Categorize the document based on its extension."""
        ext_to_category = {
            '.pdf': 'PDF Document',
            '.docx': 'Word Document',
            '.xlsx': 'Excel Spreadsheet',
            '.jpg': 'Image',
            '.png': 'Image'
        }
        file_extension = Path(self.file_path).suffix.lower()
        return ext_to_category.get(file_extension, 'Other')

    def to_dict(self) -> Dict:
        """Convert Document instance to dictionary for JSON serialization."""
        return {
            'title': self.title,
            'category': self.category,
            'file_path': self.file_path,
            'timestamp': self.timestamp
        }

class DocumentProcessor:
    def __init__(self, input_directory: str, output_file: str):
        self.input_directory = input_directory
        self.output_file = output_file
        self.documents: List[Document] = []

    def process_documents(self) -> None:
        """Process all documents in the input directory."""
        try:
            for file_name in os.listdir(self.input_directory):
                file_path = os.path.join(self.input_directory, file_name)
                if os.path.isfile(file_path):
                    document = Document(file_path)
                    self.documents.append(document)
                    logging.info(f'Processed document: {document.title}')
            self.save_documents()
        except Exception as e:
            logging.error(f"An error occurred while processing documents: {str(e)}")

    def save_documents(self) -> None:
        """Save the processed documents' metadata to a JSON file."""
        try:
            with open(self.output_file, 'w') as json_file:
                json.dump([doc.to_dict() for doc in self.documents], json_file, indent=4)
            logging.info(f'Documents metadata saved to {self.output_file}')
        except Exception as e:
            logging.error(f"An error occurred while saving documents: {str(e)}")

def main():
    input_directory = 'path/to/your/input/directory'  # Update with your input directory
    output_file = 'output/documents_metadata.json'      # Update with your desired output file path

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    processor = DocumentProcessor(input_directory, output_file)
    processor.process_documents()

if __name__ == '__main__':
    main()
```
