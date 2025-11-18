"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniwrapper.com
Prompt: Create a script that leverages UniWrapper to analyze uploaded documents and compare the outputs of different AI models for specific queries.
Generated: DETERMINISTIC_ee4afb0f1333454d
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
import logging
from uniwrapper import UniWrapper, Document

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DocumentAnalyzer:
    def __init__(self, api_key: str):
        """
        Initialize the DocumentAnalyzer with the UniWrapper API key.
        
        :param api_key: Your UniWrapper API key
        """
        self.api_key = api_key
        self.uni_wrapper = UniWrapper(api_key=self.api_key)

    def upload_document(self, file_path: str) -> Document:
        """
        Uploads a document to UniWrapper for analysis.
        
        :param file_path: Path to the document file to upload
        :return: Document object with details of the uploaded document
        :raises FileNotFoundError: If the file does not exist
        :raises Exception: For other errors during upload
        """
        if not os.path.isfile(file_path):
            logging.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        try:
            logging.info(f"Uploading document: {file_path}")
            doc = self.uni_wrapper.upload_document(file_path)
            logging.info("Document uploaded successfully.")
            return doc
        except Exception as e:
            logging.error("Error during document upload", exc_info=True)
            raise Exception("Failed to upload document.") from e

    def analyze_document(self, document: Document, query: str) -> dict:
        """
        Analyzes the uploaded document using different AI models for a specific query.
        
        :param document: The uploaded document object
        :param query: The query string to analyze the document
        :return: Dictionary containing results from different AI models
        """
        results = {}
        models = ['model_a', 'model_b', 'model_c']  # Placeholder for actual model names
        
        for model in models:
            try:
                logging.info(f"Analyzing document with {model} for query: '{query}'")
                result = self.uni_wrapper.analyze(document, model, query)
                results[model] = result
                logging.info(f"Results from {model} obtained successfully.")
            except Exception as e:
                logging.error(f"Error analyzing with {model}", exc_info=True)
                results[model] = f"Error: {str(e)}"
        
        return results

def main():
    """
    Main function to execute the document analysis.
    """
    API_KEY = 'your_uniwrapper_api_key'  # Replace with your actual API key
    FILE_PATH = 'path_to_your_document.pdf'  # Replace with the path to your document
    QUERY = 'Your specific query here'  # Define the query you want to analyze
    
    analyzer = DocumentAnalyzer(api_key=API_KEY)
    
    try:
        document = analyzer.upload_document(FILE_PATH)
        results = analyzer.analyze_document(document, QUERY)
        logging.info(f"Analysis results: {results}")
    except Exception as e:
        logging.error(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    main()
```
