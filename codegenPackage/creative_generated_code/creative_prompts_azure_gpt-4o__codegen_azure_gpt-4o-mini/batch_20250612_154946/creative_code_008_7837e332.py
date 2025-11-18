"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesk.contact
Prompt: Write a Python script to detect and open downloaded files from The Prepper Codex using Adobe Reader or a ZIP extractor like WinZip.
Generated: DETERMINISTIC_7837e33280264301
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import glob
import subprocess
import time
import platform

# Define constants for file types and download directory
DOWNLOAD_DIR = os.path.expanduser("~/Downloads")
PDF_FILE_EXTENSION = "*.pdf"
ZIP_FILE_EXTENSION = "*.zip"

def find_files(file_extension):
    """
    Search for files with the given extension in the download directory.
    
    :param file_extension: The extension of the files to search for.
    :return: List of found file paths.
    """
    search_pattern = os.path.join(DOWNLOAD_DIR, file_extension)
    return glob.glob(search_pattern)

def open_file(file_path):
    """
    Open a file using the appropriate application based on its extension.
    
    :param file_path: The path of the file to be opened.
    """
    if file_path.endswith('.pdf'):
        # Windows, MacOS, and Linux handling for PDF files
        if platform.system() == "Windows":
            subprocess.run(['start', '', file_path], shell=True)
        elif platform.system() == "Darwin":  # MacOS
            subprocess.run(['open', file_path])
        else:  # Assume Linux
            subprocess.run(['xdg-open', file_path])
    elif file_path.endswith('.zip'):
        # Windows, MacOS, and Linux handling for ZIP files
        if platform.system() == "Windows":
            subprocess.run(['start', '', file_path], shell=True)
        elif platform.system() == "Darwin":  # MacOS
            subprocess.run(['open', file_path])
        else:  # Assume Linux
            subprocess.run(['xdg-open', file_path])
    else:
        print(f"Unsupported file type: {file_path}")

def main():
    """
    Main function to find and open downloaded PDF and ZIP files.
    """
    try:
        # Find and open PDF files
        pdf_files = find_files(PDF_FILE_EXTENSION)
        for pdf_file in pdf_files:
            print(f"Opening PDF file: {pdf_file}")
            open_file(pdf_file)
            time.sleep(1)  # Wait to avoid overwhelming the system

        # Find and open ZIP files
        zip_files = find_files(ZIP_FILE_EXTENSION)
        for zip_file in zip_files:
            print(f"Opening ZIP file: {zip_file}")
            open_file(zip_file)
            time.sleep(1)  # Wait to avoid overwhelming the system

        if not pdf_files and not zip_files:
            print("No PDF or ZIP files found in the Downloads directory.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
