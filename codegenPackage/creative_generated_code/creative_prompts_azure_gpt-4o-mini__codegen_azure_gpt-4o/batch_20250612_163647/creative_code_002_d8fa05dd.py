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
from datetime import datetime
from pathlib import Path
from pytesseract import image_to_string
from PIL import Image
import logging

# Configure logging
logging.basicConfig(
    filename="document_organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def setup_directories(output_dir):
    """
    Sets up the necessary directories for organized storage of digitized documents.
    Args:
        output_dir (str): Path to the parent output directory.
    """
    try:
        # Create main output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories for organization
        subdirs = ['Invoices', 'Receipts', 'Letters', 'Miscellaneous']
        for subdir in subdirs:
            Path(os.path.join(output_dir, subdir)).mkdir(parents=True, exist_ok=True)
        
        logging.info(f"Directories initialized successfully under {output_dir}")
    except Exception as e:
        logging.error(f"Error setting up directories: {str(e)}")
        raise

def extract_text_from_image(image_path):
    """
    Extracts text from an image using OCR (Optical Character Recognition).
    Args:
        image_path (str): Path to the image file.
    Returns:
        str: Extracted text.
    """
    try:
        with Image.open(image_path) as img:
            text = image_to_string(img)
        logging.info(f"Text successfully extracted from image: {image_path}")
        return text
    except Exception as e:
        logging.error(f"Error extracting text from {image_path}: {str(e)}")
        raise

def categorize_document(text):
    """
    Categorizes a document based on its content.
    Args:
        text (str): Extracted text content of the document.
    Returns:
        str: Category name.
    """
    if "invoice" in text.lower():
        return 'Invoices'
    elif "receipt" in text.lower():
        return 'Receipts'
    elif "dear" in text.lower() or "sincerely" in text.lower():
        return 'Letters'
    else:
        return 'Miscellaneous'

def digitize_and_organize_documents(input_dir, output_dir):
    """
    Automates the digitization and organization of documents.
    Args:
        input_dir (str): Path to the input directory containing document images.
        output_dir (str): Path to the output directory for organized documents.
    """
    setup_directories(output_dir)

    try:
        for file_name in os.listdir(input_dir):
            file_path = os.path.join(input_dir, file_name)
            
            # Skip non-image files
            if not file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                logging.warning(f"Skipped non-image file: {file_name}")
                continue
            
            # Extract text using OCR
            text = extract_text_from_image(file_path)
            
            # Categorize the document
            category = categorize_document(text)
            
            # Move the file to the corresponding directory
            target_dir = os.path.join(output_dir, category)
            shutil.move(file_path, os.path.join(target_dir, file_name))
            
            logging.info(f"Moved {file_name} to {category} directory")
    except Exception as e:
        logging.error(f"Error during document digitization: {str(e)}")
        raise

if __name__ == "__main__":
    # Paths for input and output directories
    input_directory = "raw_documents"
    output_directory = "organized_documents"

    try:
        digitize_and_organize_documents(input_directory, output_directory)
        logging.info("Document digitization and organization completed successfully.")
    except Exception as e:
        logging.error(f"Process failed: {str(e)}")
```

This script assumes that you have installed the necessary dependencies (`pytesseract`, `Pillow`, etc.) and configured Tesseract OCR appropriately on your system. Replace `raw_documents` and `organized_documents` with the actual paths in your environment.
