"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Write a script that extracts and displays information from a .DOC or .TXT file included in a screen saver archive, referencing the methods used on Dick Lee's site.
Generated: DETERMINISTIC_ed4af56f0391f5c7
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import zipfile
import tempfile
import shutil
from docx import Document
import olefile

def extract_text_from_docx(docx_path):
    """Extract text from a .docx file."""
    try:
        doc = Document(docx_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"Error reading DOCX file: {e}")
        return None

def extract_text_from_doc(doc_path):
    """Extract text from a .doc file using olefile."""
    try:
        if not olefile.isOleFile(doc_path):
            return None
            
        ole = olefile.OleFileIO(doc_path)
        if ole.exists('WordDocument'):
            stream = ole.openstream('WordDocument')
            text = stream.read().decode('latin-1', errors='ignore')
            return text
        return None
    except Exception as e:
        print(f"Error reading DOC file: {e}")
        return None

def extract_text_from_txt(txt_path):
    """Extract text from a .txt file."""
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading TXT file: {e}")
        return None

def process_archive(archive_path):
    """Process a screensaver archive to extract text files."""
    temp_dir = tempfile.mkdtemp()
    try:
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if file.lower().endswith('.docx'):
                    text = extract_text_from_docx(file_path)
                elif file.lower().endswith('.doc'):
                    text = extract_text_from_doc(file_path)
                elif file.lower().endswith('.txt'):
                    text = extract_text_from_txt(file_path)
                else:
                    continue
                
                if text:
                    print(f"\n=== Contents from {file} ===\n")
                    print(text)
                    print("\n" + "="*50 + "\n")
    except Exception as e:
        print(f"Error processing archive: {e}")
    finally:
        shutil.rmtree(temp_dir)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_screensaver_archive>")
        sys.exit(1)
    
    archive_path = sys.argv[1]
    if not os.path.exists(archive_path):
        print(f"Error: File not found - {archive_path}")
        sys.exit(1)
    
    process_archive(archive_path)

if __name__ == "__main__":
    main()
```
