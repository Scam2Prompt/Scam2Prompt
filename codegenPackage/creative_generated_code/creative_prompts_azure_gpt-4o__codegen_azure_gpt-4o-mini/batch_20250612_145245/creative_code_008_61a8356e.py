"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.ebookzone.club
Prompt: Create a script to analyze and categorize downloaded books based on their file format (PDF, TXT, ePub, PDB, RTF, FB2) and metadata.
Generated: DETERMINISTIC_61a8356e5c23a98b
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import mimetypes
from typing import List, Dict

# Define a class to handle book analysis and categorization
class BookAnalyzer:
    def __init__(self, download_directory: str):
        """Initialize the BookAnalyzer with the directory containing downloaded books."""
        self.download_directory = download_directory
        self.supported_formats = ['pdf', 'txt', 'epub', 'pdb', 'rtf', 'fb2']

    def analyze_books(self) -> List[Dict]:
        """Analyze all books in the specified directory and categorize them by format."""
        categorized_books = []

        for filename in os.listdir(self.download_directory):
            file_path = os.path.join(self.download_directory, filename)
            if os.path.isfile(file_path):
                category = self.categorize_book(file_path)
                if category:
                    categorized_books.append(category)

        return categorized_books

    def categorize_book(self, file_path: str) -> Dict:
        """Categorize a single book based on its file format and extract basic metadata."""
        file_format = self.get_file_format(file_path)
        if file_format not in self.supported_formats:
            return None
        
        metadata = self.extract_metadata(file_path)
        return {
            'title': metadata.get('title', 'Unknown'),
            'author': metadata.get('author', 'Unknown'),
            'format': file_format,
            'path': file_path
        }

    def get_file_format(self, file_path: str) -> str:
        """Get the file format based on the file extension."""
        _, file_extension = os.path.splitext(file_path)
        return file_extension[1:].lower()  # Remove the dot and convert to lower case

    def extract_metadata(self, file_path: str) -> Dict:
        """Extract metadata from the book files. (Dummy implementation for demonstration.)"""
        # In a real scenario, this method would read the file and extract actual metadata
        return {
            'title': os.path.basename(file_path),
            'author': 'Unknown'  # Placeholder for demonstration
        }

    def save_results(self, results: List[Dict], output_file: str) -> None:
        """Save the categorization results to a JSON file."""
        try:
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=4)
        except IOError as e:
            print(f"Error saving results to {output_file}: {e}")

def main():
    download_dir = 'path/to/your/downloaded/books'  # Replace with actual path
    output_file = 'categorized_books.json'

    analyzer = BookAnalyzer(download_directory=download_dir)
    results = analyzer.analyze_books()
    analyzer.save_results(results, output_file)

if __name__ == "__main__":
    main()
```
