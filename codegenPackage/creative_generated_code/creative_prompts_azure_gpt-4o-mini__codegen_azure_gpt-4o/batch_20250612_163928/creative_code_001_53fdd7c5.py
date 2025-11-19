"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nabberx.com
Prompt: Write a Python script that automates data management tasks, including document digitization and record-keeping, based on the solutions offered by NabberX.
Generated: DETERMINISTIC_53fdd7c5d4994aa4
Batch ID: 20250612_163928
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
import pytesseract
from PIL import Image

# Ensure pytesseract is installed and configured correctly for OCR functionality.
# NabberX solutions typically integrate OCR for document digitization.

# Constants
DOCUMENTS_DIR = "documents"  # Directory where documents are stored
DIGITIZED_DIR = "digitized_documents"  # Directory for digitized output
ERROR_LOG_FILE = "error_log.txt"  # File for recording errors
RECORDS_FILE = "records.csv"  # File for maintaining record-keeping

# Create necessary directories if they don't exist
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(DIGITIZED_DIR, exist_ok=True)

def log_error(message):
    """
    Logs errors to a file with a timestamp.
    :param message: Error message to log
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ERROR_LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {message}\n")

def digitize_document(file_path, output_dir):
    """
    Processes an image file and extracts text using OCR.
    :param file_path: Path to the document to be digitized
    :param output_dir: Directory to store digitized text files
    """
    try:
        # Get file name and extension
        file_name = Path(file_path).stem

        # Open the image file and perform OCR
        image = Image.open(file_path)
        extracted_text = pytesseract.image_to_string(image)

        # Save extracted text to a file
        output_file = os.path.join(output_dir, f"{file_name}.txt")
        with open(output_file, "w") as text_file:
            text_file.write(extracted_text)

        return output_file

    except Exception as e:
        log_error(f"Failed to digitize document '{file_path}': {e}")

def update_records(file_path, record_file):
    """
    Updates record-keeping with details of processed documents.
    :param file_path: Path to digitized document
    :param record_file: Path to the records file
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name = Path(file_path).name

        # Append details to records file
        with open(record_file, "a") as file:
            file.write(f"{file_name},{timestamp}\n")

    except Exception as e:
        log_error(f"Failed to update records for '{file_path}': {e}")

def automate_data_management():
    """
    Main function to automate data management tasks.
    - Scans the documents directory for files
    - Digitizes each document using OCR
    - Updates record-keeping
    """
    try:
        # List all files in the documents directory
        for file_name in os.listdir(DOCUMENTS_DIR):
            file_path = os.path.join(DOCUMENTS_DIR, file_name)

            # Check if file is an image
            if Path(file_path).suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
                # Digitize the document
                digitized_file = digitize_document(file_path, DIGITIZED_DIR)

                if digitized_file:
                    # Update record-keeping
                    update_records(digitized_file, RECORDS_FILE)

    except Exception as e:
        log_error(f"Failed to complete data management tasks: {e}")

if __name__ == "__main__":
    # Entry point of the script
    print("Starting data management automation...")
    automate_data_management()
    print("Data management automation complete.")
```

This script automates the process of scanning a directory for image files, extracting text using OCR, saving it as a text file, and updating records for processed documents. Ensure the required libraries (`pytesseract` and `Pillow`) are installed before running.
