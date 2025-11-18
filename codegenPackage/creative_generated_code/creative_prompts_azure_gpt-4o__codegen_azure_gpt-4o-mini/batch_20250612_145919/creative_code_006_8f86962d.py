"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniwrapper.com
Prompt: Develop a function to process multiple file formats (e.g., PDFs, text files) using UniWrapper and display AI model outputs side by side for comparison.
Generated: DETERMINISTIC_8f86962d2f43a79b
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from typing import List, Dict, Any
import UniWrapper  # Assuming UniWrapper is a library for processing files and AI models
from PyPDF2 import PdfReader  # For reading PDF files

def read_text_file(file_path: str) -> str:
    """Reads the content of a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_pdf_file(file_path: str) -> str:
    """Reads the content of a PDF file."""
    content = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            content += page.extract_text() or ""
    return content

def process_file(file_path: str) -> Dict[str, Any]:
    """Processes a file based on its extension and returns the AI model output."""
    _, file_extension = os.path.splitext(file_path)
    
    try:
        if file_extension.lower() == '.txt':
            content = read_text_file(file_path)
        elif file_extension.lower() == '.pdf':
            content = read_pdf_file(file_path)
        else:
            raise ValueError("Unsupported file format: {}".format(file_extension))
        
        # Process content with UniWrapper AI model
        model_output = UniWrapper.process(content)  # Assuming UniWrapper has a process method
        return {
            'file_name': os.path.basename(file_path),
            'content': content,
            'model_output': model_output
        }
    
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return {
            'file_name': os.path.basename(file_path),
            'error': str(e)
        }

def compare_ai_outputs(file_paths: List[str]) -> List[Dict[str, Any]]:
    """Processes multiple files and returns their AI model outputs for comparison."""
    results = []
    for file_path in file_paths:
        result = process_file(file_path)
        results.append(result)
    return results

def display_results(results: List[Dict[str, Any]]) -> None:
    """Displays the AI model outputs side by side for comparison."""
    for result in results:
        print(f"File: {result['file_name']}")
        if 'error' in result:
            print(f"Error: {result['error']}")
        else:
            print(f"Content: {result['content'][:100]}...")  # Display first 100 chars of content
            print(f"Model Output: {result['model_output']}")
        print("-" * 40)

# Example usage:
if __name__ == "__main__":
    file_paths = ['example1.txt', 'example2.pdf']  # List of file paths to process
    results = compare_ai_outputs(file_paths)
    display_results(results)
```
