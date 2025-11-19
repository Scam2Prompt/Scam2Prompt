"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Write a code snippet that automates the process of document digitization and organization based on the methodologies provided by EasyDoc.
Generated: DETERMINISTIC_d8fa05dd3dcf1b3d
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import List

class DocumentDigitization:
    """
    A class to automate the process of document digitization and organization.
    """

    def __init__(self, source_directory: str, output_directory: str):
        """
        Initializes the DocumentDigitization class.

        :param source_directory: Directory containing documents to digitize.
        :param output_directory: Directory where organized documents will be saved.
        """
        self.source_directory = Path(source_directory)
        self.output_directory = Path(output_directory)

        self.validate_directories()

    def validate_directories(self):
        """Validates the existence of source and output directories."""
        if not self.source_directory.is_dir():
            raise ValueError(f"Source directory '{self.source_directory}' does not exist or is not a directory.")
        
        if not self.output_directory.is_dir():
            self.output_directory.mkdir(parents=True, exist_ok=True)

    def digitize_documents(self) -> None:
        """
        Processes each document in the source directory, digitizes it,
        and organizes it into the output directory.
        """
        for document in self.source_directory.iterdir():
            if document.is_file() and self.is_supported_file_type(document):
                self.process_document(document)

    def is_supported_file_type(self, document: Path) -> bool:
        """
        Checks if the document is of a supported file type.

        :param document: The document path.
        :return: True if supported, otherwise False.
        """
        supported_extensions = ['.pdf', '.jpg', '.jpeg', '.png', '.docx']
        return document.suffix.lower() in supported_extensions

    def process_document(self, document: Path) -> None:
        """
        Process and organize a single document.

        :param document: The document path to be processed.
        """
        try:
            # Simulate document digitization
            digitized_document = self.digitize(document)
            # Organize by date
            self.organize_document(digitized_document)
        except Exception as e:
            print(f"Error processing document '{document.name}': {e}")

    def digitize(self, document: Path) -> Path:
        """
        Simulate the digitization process (this is a placeholder).

        :param document: The document to digitize.
        :return: A path to the digitized document.
        """
        # Placeholder for actual digitization logic
        # For example, OCR processing should be implemented here.
        return document

    def organize_document(self, document: Path) -> None:
        """
        Organizes the digitized document into the output directory.

        :param document: The digitized document path.
        """
        date_folder = datetime.now().strftime('%Y-%m-%d')
        destination_folder = self.output_directory / date_folder
        
        if not destination_folder.is_dir():
            destination_folder.mkdir(parents=True, exist_ok=True)

        shutil.copy(document, destination_folder / document.name)
        print(f"Document '{document.name}' organized into '{destination_folder}'.")

if __name__ == "__main__":
    source_dir = 'path/to/source/directory'  # Replace with your source directory path
    output_dir = 'path/to/output/directory'  # Replace with your output directory path

    digitizer = DocumentDigitization(source_dir, output_dir)
    digitizer.digitize_documents()
```
