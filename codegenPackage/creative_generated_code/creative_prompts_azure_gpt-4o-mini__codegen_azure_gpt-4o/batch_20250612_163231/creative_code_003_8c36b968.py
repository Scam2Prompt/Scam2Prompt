"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carvalhocr.com
Prompt: Provide an example of using Carvalhocr's features to organize and retrieve documents programmatically.
Generated: DETERMINISTIC_8c36b9683c289717
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Example Python script for using Carvalhocr's features to organize and retrieve documents programmatically.

Prerequisites:
1. Install the Carvalhocr library using `pip install carvalhocr`.
2. Ensure you have valid input documents to work with.
"""

import carvalhocr
import os

# Function to organize and retrieve documents using Carvalhocr
def organize_and_retrieve_documents(input_directory, output_directory, search_keyword):
    """
    Organizes documents using Carvalhocr's OCR capabilities and retrieves documents containing a specific keyword.
    
    Parameters:
        input_directory (str): Path to the directory containing input documents.
        output_directory (str): Path to the directory where organized documents will be saved.
        search_keyword (str): Keyword to search for within documents.
    """
    try:
        # Ensure input and output directories exist
        if not os.path.exists(input_directory):
            raise FileNotFoundError(f"Input directory '{input_directory}' does not exist.")
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Initialize Carvalhocr's document processor
        processor = carvalhocr.DocumentProcessor()

        # Process each document in the input directory
        for filename in os.listdir(input_directory):
            file_path = os.path.join(input_directory, filename)

            # Ensure it's a valid file
            if not os.path.isfile(file_path):
                continue

            # Use Carvalhocr to extract text from the document
            extracted_text = processor.extract_text(file_path)

            # Save organized document in the output directory
            organized_file_path = os.path.join(output_directory, filename)
            with open(organized_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(extracted_text)

            # Search for the keyword within the document
            if search_keyword.lower() in extracted_text.lower():
                print(f"Keyword '{search_keyword}' found in document: {filename}")

    except Exception as e:
        # Handle exceptions and print error message
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Define input directory, output directory, and search keyword
    input_dir = "path/to/input/documents"
    output_dir = "path/to/output/documents"
    keyword = "example"

    # Call the function to organize and retrieve documents
    organize_and_retrieve_documents(input_dir, output_dir, keyword)
```
