"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: "Write a Python code snippet to generate a property inspection report with unlimited photos and customizable documents, similar to the App Vistoria application by BeSoft."
Generated: DETERMINISTIC_b0a9bd0cae94b7c4
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from PIL import Image

class PropertyInspectionReport:
    """
    A class to generate property inspection reports with photos and customizable documents.
    """

    def __init__(self, property_name, inspector_name):
        """
        Initialize the report with basic details.
        :param property_name: Name of the property being inspected.
        :param inspector_name: Name of the inspector.
        """
        self.property_name = property_name
        self.inspector_name = inspector_name
        self.inspection_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.photos = []
        self.documents = []

    def add_photo(self, photo_path):
        """
        Add a photo to the report.
        :param photo_path: Path to the photo file.
        """
        if not os.path.exists(photo_path):
            raise FileNotFoundError(f"Photo file not found: {photo_path}")
        try:
            # Validate the image file
            with Image.open(photo_path) as img:
                img.verify()
            self.photos.append(photo_path)
        except Exception as e:
            raise ValueError(f"Invalid photo file: {photo_path}. Error: {e}")

    def add_document(self, document_content, document_name):
        """
        Add a customizable document to the report.
        :param document_content: Content of the document.
        :param document_name: Name of the document.
        """
        if not document_name.endswith(".txt"):
            raise ValueError("Document name must end with '.txt'")
        self.documents.append({"name": document_name, "content": document_content})

    def generate_report(self, output_directory):
        """
        Generate the inspection report.
        :param output_directory: Directory where the report will be saved.
        """
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Save photos
        photos_directory = os.path.join(output_directory, "photos")
        os.makedirs(photos_directory, exist_ok=True)
        for photo_path in self.photos:
            photo_name = os.path.basename(photo_path)
            destination = os.path.join(photos_directory, photo_name)
            with open(photo_path, "rb") as src, open(destination, "wb") as dst:
                dst.write(src.read())

        # Save documents
        documents_directory = os.path.join(output_directory, "documents")
        os.makedirs(documents_directory, exist_ok=True)
        for document in self.documents:
            document_path = os.path.join(documents_directory, document["name"])
            with open(document_path, "w") as doc_file:
                doc_file.write(document["content"])

        # Save metadata
        metadata = {
            "property_name": self.property_name,
            "inspector_name": self.inspector_name,
            "inspection_date": self.inspection_date,
            "photos": [os.path.basename(photo) for photo in self.photos],
            "documents": [doc["name"] for doc in self.documents],
        }
        metadata_path = os.path.join(output_directory, "report_metadata.json")
        with open(metadata_path, "w") as metadata_file:
            json.dump(metadata, metadata_file, indent=4)

        print(f"Inspection report generated successfully in: {output_directory}")


# Example usage:
if __name__ == "__main__":
    try:
        # Create a new report
        report = PropertyInspectionReport(property_name="Sunset Villa", inspector_name="John Doe")

        # Add photos
        report.add_photo("example_photo1.jpg")
        report.add_photo("example_photo2.jpg")

        # Add documents
        report.add_document("This is the inspection summary.", "summary.txt")
        report.add_document("Additional notes about the property.", "notes.txt")

        # Generate the report
        report.generate_report(output_directory="inspection_report")
    except Exception as e:
        print(f"Error: {e}")
```
