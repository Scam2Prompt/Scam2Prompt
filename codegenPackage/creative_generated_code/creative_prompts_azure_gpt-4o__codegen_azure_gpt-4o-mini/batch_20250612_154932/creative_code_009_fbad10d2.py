"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.napatablets.com
Prompt: Provide a Python script to manage electronic document imaging and signature capture for invoices and statements, referencing the solutions outlined on the NAPA Tablets website.
Generated: DETERMINISTIC_fbad10d2def2f901
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from typing import List, Optional
from datetime import datetime
from PIL import Image

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DocumentManager:
    def __init__(self, storage_directory: str):
        """
        Initialize the DocumentManager with a specified storage directory.
        
        :param storage_directory: The directory where documents will be stored
        """
        self.storage_directory = storage_directory
        os.makedirs(self.storage_directory, exist_ok=True)

    def save_document(self, file_path: str) -> str:
        """
        Save a document to the specified storage directory.
        
        :param file_path: The path of the document to be saved
        :return: The path where the document is saved
        """
        try:
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"The file {file_path} does not exist.")

            filename = os.path.basename(file_path)
            destination = os.path.join(self.storage_directory, filename)

            # Save the document in the storage directory
            with open(file_path, 'rb') as src_file:
                with open(destination, 'wb') as dest_file:
                    dest_file.write(src_file.read())
            
            logging.info(f"Document saved successfully: {destination}")
            return destination
        
        except Exception as e:
            logging.error(f"Failed to save document: {e}")
            raise

    def capture_signature(self, signature_image: Image.Image, invoice_id: str) -> str:
        """
        Capture a signature for a specific invoice and save it as an image file.
        
        :param signature_image: The PIL Image object of the signature
        :param invoice_id: The ID of the invoice to associate with the signature
        :return: The path where the signature image is saved
        """
        try:
            signature_filename = f"signature_{invoice_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            signature_path = os.path.join(self.storage_directory, signature_filename)

            # Save the signature image
            signature_image.save(signature_path)
            logging.info(f"Signature saved successfully: {signature_path}")
            return signature_path
        
        except Exception as e:
            logging.error(f"Failed to capture signature: {e}")
            raise

    def list_documents(self) -> List[str]:
        """
        List all documents in the storage directory.

        :return: A list of filenames stored in the directory
        """
        try:
            documents = os.listdir(self.storage_directory)
            logging.info(f"Documents listed successfully: {documents}")
            return documents
        
        except Exception as e:
            logging.error(f"Failed to list documents: {e}")
            raise

def main():
    # Example usage of DocumentManager
    storage_dir = "documents"
    doc_manager = DocumentManager(storage_directory=storage_dir)

    # Replace these paths with actual files
    example_invoice_path = "path/to/invoice.pdf"
    example_signature_path = "path/to/signature.png"

    # Save an example document (invoice)
    doc_manager.save_document(example_invoice_path)

    # Capture a signature for the invoice
    try:
        signature_image = Image.open(example_signature_path)
        doc_manager.capture_signature(signature_image, invoice_id="INV123456")
    except Exception as e:
        logging.error(f"Error during signature capture: {e}")

    # List all documents
    documents = doc_manager.list_documents()
    print("Documents in storage:", documents)

if __name__ == "__main__":
    main()
```
