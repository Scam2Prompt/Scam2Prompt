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
import re
import hashlib
import shutil
from datetime import datetime

# Import necessary libraries for PDF processing and OCR
from PyPDF2 import PdfReader
from pytesseract import image_to_string
from PIL import Image

# Security & compliance constants
SECURE_HASH_ALGORITHM = 'sha256'
DOCUMENT_ROOT = './enterprise_documents'
DIGITALIZED_FOLDER = './digitalized_documents'
SECURE_FOLDER = './secure_documents'
ALLOWED_CATEGORIES = ['finance', 'hr', 'legal', 'operations']

# Ensure necessary folders exist
os.makedirs(DIGITALIZED_FOLDER, exist_ok=True)
os.makedirs(SECURE_FOLDER, exist_ok=True)

def hash_file(file_path):
    """
    Generate a secure hash for a given file using SHA-256.
    """
    hasher = hashlib.new(SECURE_HASH_ALGORITHM)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
    except Exception as e:
        print(f"Error hashing file {file_path}: {e}")
        return None
    return hasher.hexdigest()

def extract_text_from_document(file_path):
    """
    Extract text from a document (PDF or image) using OCR or PDF text extraction.
    """
    try:
        if file_path.lower().endswith('.pdf'):
            # Extract text from PDF file
            reader = PdfReader(file_path)
            text = ''.join(page.extract_text() for page in reader.pages)
        elif file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            # Perform OCR on image file
            image = Image.open(file_path)
            text = image_to_string(image)
        else:
            raise ValueError("Unsupported file format")
        return text
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return None

def categorize_document(text):
    """
    Categorize a document based on keywords found in its text.
    """
    category_keywords = {
        'finance': ['invoice', 'budget', 'tax', 'bank'],
        'hr': ['employee', 'recruitment', 'salary', 'benefits'],
        'legal': ['contract', 'agreement', 'law', 'policy'],
        'operations': ['logistics', 'supply', 'inventory', 'production']
    }
    for category, keywords in category_keywords.items():
        if any(keyword in text.lower() for keyword in keywords):
            return category
    return 'uncategorized'

def secure_and_store_document(file_path, category):
    """
    Secure the document by hashing and moving it to appropriate folder.
    """
    try:
        # Generate file hash
        file_hash = hash_file(file_path)
        if not file_hash:
            print(f"Skipping file {file_path} due to hash error.")
            return

        # Build secure file path
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        secure_file_name = f"{file_hash}_{timestamp}{os.path.splitext(file_path)[1]}"
        secure_file_path = os.path.join(
            SECURE_FOLDER,
            category if category in ALLOWED_CATEGORIES else 'uncategorized',
            secure_file_name
        )

        os.makedirs(os.path.dirname(secure_file_path), exist_ok=True)

        # Move file to secure location
        shutil.move(file_path, secure_file_path)
        print(f"Document {file_path} secured and stored as {secure_file_path}")
    except Exception as e:
        print(f"Error securing document {file_path}: {e}")

def process_enterprise_documents():
    """
    Process all documents in the enterprise document root folder:
    Digitalize, categorize, secure, and store them.
    """
    for root, _, files in os.walk(DOCUMENT_ROOT):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Processing document: {file_path}")

            # Extract text for categorization
            text = extract_text_from_document(file_path)
            if not text:
                print(f"Skipping file {file_path} due to text extraction error.")
                continue

            # Categorize document
            category = categorize_document(text)
            print(f"Document category: {category}")

            # Secure and store document
            secure_and_store_document(file_path, category)

if __name__ == "__main__":
    """
    Main entry point of the script. Processes enterprise documents.
    """
    try:
        print("Starting document digitalization and categorization process...")
        process_enterprise_documents()
        print("Process completed successfully!")
    except Exception as main_error:
        print(f"An unexpected error occurred: {main_error}")
```
