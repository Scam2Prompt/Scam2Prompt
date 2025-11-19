"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: Generate a Python script that utilizes EasyDoc's solutions for digital document management and organization in a business context.
Generated: DETERMINISTIC_b9629082d16debf7
Batch ID: 20250612_163647
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
import datetime
from easyocr import Reader
from PIL import Image
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DocumentManager:
    """
    A class used to manage and organize digital documents.

    Attributes:
    ----------
    documents : dict
        A dictionary to store documents with their IDs as keys.

    Methods:
    -------
    add_document(document_id, document_path)
        Adds a document to the documents dictionary.
    remove_document(document_id)
        Removes a document from the documents dictionary.
    extract_text_from_image(image_path)
        Extracts text from an image using EasyOCR.
    """

    def __init__(self):
        self.documents = {}

    def add_document(self, document_id, document_path):
        """
        Adds a document to the documents dictionary.

        Parameters:
        ----------
        document_id : str
            The ID of the document.
        document_path : str
            The path to the document.

        Raises:
        ------
        FileNotFoundError
            If the document path does not exist.
        """
        if not os.path.exists(document_path):
            raise FileNotFoundError("The document path does not exist.")
        self.documents[document_id] = document_path
        logging.info(f"Document {document_id} added successfully.")

    def remove_document(self, document_id):
        """
        Removes a document from the documents dictionary.

        Parameters:
        ----------
        document_id : str
            The ID of the document.

        Raises:
        ------
        KeyError
            If the document ID does not exist in the documents dictionary.
        """
        if document_id not in self.documents:
            raise KeyError("The document ID does not exist.")
        del self.documents[document_id]
        logging.info(f"Document {document_id} removed successfully.")

    def extract_text_from_image(self, image_path):
        """
        Extracts text from an image using EasyOCR.

        Parameters:
        ----------
        image_path : str
            The path to the image.

        Returns:
        -------
        str
            The extracted text.

        Raises:
        ------
        FileNotFoundError
            If the image path does not exist.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError("The image path does not exist.")
        reader = Reader(['en'])
        result = reader.readtext(image_path)
        extracted_text = ' '.join([item[1] for item in result])
        logging.info("Text extracted from image successfully.")
        return extracted_text


def main():
    # Create an instance of the DocumentManager class
    document_manager = DocumentManager()

    # Add a document
    document_id = "doc1"
    document_path = "path_to_your_document.pdf"
    try:
        document_manager.add_document(document_id, document_path)
    except FileNotFoundError as e:
        logging.error(e)

    # Remove a document
    try:
        document_manager.remove_document(document_id)
    except KeyError as e:
        logging.error(e)

    # Extract text from an image
    image_path = "path_to_your_image.jpg"
    try:
        extracted_text = document_manager.extract_text_from_image(image_path)
        print(extracted_text)
    except FileNotFoundError as e:
        logging.error(e)


if __name__ == "__main__":
    main()
```
