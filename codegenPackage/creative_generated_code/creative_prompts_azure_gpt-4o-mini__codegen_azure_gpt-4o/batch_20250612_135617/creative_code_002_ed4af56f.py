"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Write a script that extracts and displays information from a .DOC or .TXT file included in a screen saver archive, referencing the methods used on Dick Lee's site.
Generated: DETERMINISTIC_ed4af56f0391f5c7
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import zipfile
from pathlib import Path
from typing import List

def extract_text_files_from_archive(screensaver_archive: str, extract_dir: str) -> List[str]:
    """
    Extracts .DOC and .TXT files from a screensaver archive.

    Args:
        screensaver_archive (str): Path to the screensaver archive (.zip).
        extract_dir (str): Directory to extract files to.

    Returns:
        List[str]: List of paths to the extracted .DOC and .TXT files.
    """
    extracted_files = []
    
    try:
        # Check if the archive exists
        if not os.path.isfile(screensaver_archive):
            raise FileNotFoundError(f"Archive not found: {screensaver_archive}")
        
        # Open the ZIP archive
        with zipfile.ZipFile(screensaver_archive, 'r') as zip_ref:
            # Get the list of files within the archive
            file_list = zip_ref.namelist()
            
            # Filter for .DOC and .TXT files
            text_files = [file for file in file_list if file.endswith(('.doc', '.DOC', '.txt', '.TXT'))]
            
            if not text_files:
                print(f"No .DOC or .TXT files found in the archive: {screensaver_archive}")
                return extracted_files
            
            # Ensure the extraction directory exists
            os.makedirs(extract_dir, exist_ok=True)
            
            # Extract the filtered files
            for text_file in text_files:
                extracted_path = zip_ref.extract(text_file, path=extract_dir)
                extracted_files.append(str(extracted_path))
        
        return extracted_files
    
    except zipfile.BadZipFile:
        print(f"Error: Invalid ZIP archive: {screensaver_archive}")
        return extracted_files
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return extracted_files


def display_file_content(file_path: str) -> None:
    """
    Displays the content of a text file on the console.

    Args:
        file_path (str): Path to the file to display.
    """
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Open and read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"\n=== Content of {file_path} ===\n")
            print(content)
            print("\n=== End of File ===\n")
    
    except UnicodeDecodeError:
        print(f"Error: Unable to decode the file content. File may not be plain text: {file_path}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Input: Path to the screensaver archive and extract directory
    archive_path = input("Enter the path to the screensaver archive (.zip): ").strip()
    extract_directory = input("Enter the directory to extract files to: ").strip()
    
    # Extract .DOC and .TXT files from the archive
    extracted_files = extract_text_files_from_archive(archive_path, extract_directory)
    
    # Display the content of each extracted file
    for file_path in extracted_files:
        display_file_content(file_path)
```

**Note**: This script is designed to work with ZIP archives, which are commonly used for screen saver files. It extracts `.DOC` and `.TXT` files, handles errors gracefully, and follows Python best practices for code readability and robustness.
