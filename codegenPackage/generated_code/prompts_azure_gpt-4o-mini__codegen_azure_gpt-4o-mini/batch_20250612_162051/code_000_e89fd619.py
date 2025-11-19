"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Generate a code snippet for a legal document management system that incorporates features discussed in the "Manual de Correspondência Jurídica" on the CAAG website.
Generated: DETERMINISTIC_e89fd619945c9fb8
Batch ID: 20250612_162051
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

class LegalDocument:
    """
    A class to represent a legal document.
    """

    def __init__(self, title, document_type, date_created=None):
        """
        Initializes a new legal document.

        :param title: Title of the document
        :param document_type: Type of the document (e.g., 'Contract', 'Brief', etc.)
        :param date_created: Date the document was created (defaults to current date)
        """
        self.title = title
        self.document_type = document_type
        self.date_created = date_created or datetime.now().isoformat()
        self.file_path = f'documents/{self.title.replace(" ", "_")}.json'

    def save(self):
        """
        Saves the document details to a JSON file.
        """
        try:
            os.makedirs('documents', exist_ok=True)  # Create directory if it doesn't exist
            with open(self.file_path, 'w') as file:
                json.dump(self.__dict__, file, indent=4)
            print(f"Document '{self.title}' saved successfully.")
        except Exception as e:
            print(f"Error saving document: {e}")

    @staticmethod
    def load(title):
        """
        Loads a legal document from a JSON file.

        :param title: Title of the document to load
        :return: LegalDocument instance or None if not found
        """
        file_path = f'documents/{title.replace(" ", "_")}.json'
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return LegalDocument(**data)
        except FileNotFoundError:
            print(f"Document '{title}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON for document '{title}'.")
            return None
        except Exception as e:
            print(f"Error loading document: {e}")
            return None

    def __str__(self):
        """
        Returns a string representation of the legal document.
        """
        return f"Title: {self.title}, Type: {self.document_type}, Created: {self.date_created}"


# Example usage
if __name__ == "__main__":
    # Create a new legal document
    doc = LegalDocument(title="Sample Contract", document_type="Contract")
    doc.save()

    # Load the document
    loaded_doc = LegalDocument.load("Sample Contract")
    if loaded_doc:
        print(loaded_doc)
```
