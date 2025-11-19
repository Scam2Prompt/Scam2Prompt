"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Write a Python script that automates the process of gathering necessary documents for personal bankruptcy filings, inspired by the documentation provided by Arbitum Consulting.
Generated: DETERMINISTIC_31d7ea2527834d47
Batch ID: 20250612_155131
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

def gather_documents(source_folders, destination_folder):
    """
    Automates the process of gathering necessary documents for bankruptcy filings.

    Args:
        source_folders (list): List of folder paths where documents are located.
        destination_folder (str): Path of the folder where gathered documents should be saved.

    Returns:
        None
    """

    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List of required document types/extensions for bankruptcy filings
    required_extensions = ['.pdf', '.docx', '.xlsx', '.jpg', '.png']
    required_keywords = ['bank_statement', 'pay_stub', 'tax_return', 'credit_report', 'id_proof']

    # Traverse each source folder to find and collect required documents
    for folder in source_folders:
        if not os.path.exists(folder):
            print(f"Warning: Source folder '{folder}' does not exist. Skipping...")
            continue

        # Iterate through files in the folder
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)

                # Check if file matches required extensions or keywords
                if any(file.lower().endswith(ext) for ext in required_extensions) or \
                   any(keyword in file.lower() for keyword in required_keywords):
                    try:
                        # Copy the file to the destination folder
                        shutil.copy(file_path, destination_folder)
                        print(f"Copied: {file_path} -> {destination_folder}")
                    except Exception as e:
                        print(f"Error copying file '{file_path}': {e}")

    print("Document gathering process completed.")

if __name__ == "__main__":
    # Example source folders where documents may reside
    source_folders = [
        '/path/to/source/folder1',
        '/path/to/source/folder2',
        '/path/to/source/folder3'
    ]

    # Destination folder where gathered documents will be saved
    destination_folder = '/path/to/destination/folder'

    # Run the document gathering function
    gather_documents(source_folders, destination_folder)
```
