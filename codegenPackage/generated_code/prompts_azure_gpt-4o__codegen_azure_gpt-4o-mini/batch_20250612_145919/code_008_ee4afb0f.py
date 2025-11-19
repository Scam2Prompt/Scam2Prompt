"""
Generated Code Metadata:
========================
Original URL: https://uniwrapper.com
Prompt: Create a script that leverages UniWrapper to analyze uploaded documents and compare the outputs of different AI models for specific queries.
Generated: DETERMINISTIC_ee4afb0f1333454d
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from uni_wrapper import UniWrapper  # Assuming UniWrapper is a valid library for document analysis

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DocumentAnalyzer:
    def __init__(self, models):
        """
        Initialize the DocumentAnalyzer with a list of AI models.

        :param models: List of AI model names to be used for analysis.
        """
        self.models = models
        self.uni_wrapper = UniWrapper()

    def analyze_document(self, document_path):
        """
        Analyze the uploaded document using the specified AI models.

        :param document_path: Path to the document to be analyzed.
        :return: Dictionary containing the analysis results from each model.
        """
        if not os.path.isfile(document_path):
            logging.error(f"Document not found: {document_path}")
            raise FileNotFoundError(f"Document not found: {document_path}")

        results = {}
        for model in self.models:
            try:
                logging.info(f"Analyzing document with model: {model}")
                analysis_result = self.uni_wrapper.analyze(document_path, model)
                results[model] = analysis_result
            except Exception as e:
                logging.error(f"Error analyzing document with model {model}: {e}")
                results[model] = None  # Store None if an error occurs

        return results

    def compare_results(self, results):
        """
        Compare the analysis results from different models.

        :param results: Dictionary containing analysis results from each model.
        :return: Comparison summary.
        """
        comparison_summary = {}
        for model, result in results.items():
            if result is not None:
                comparison_summary[model] = {
                    'summary': result.get('summary', 'No summary available'),
                    'details': result.get('details', 'No details available')
                }
            else:
                comparison_summary[model] = 'Analysis failed'

        return comparison_summary

def main():
    # List of AI models to be used for analysis
    models = ['model_a', 'model_b', 'model_c']  # Replace with actual model names

    # Create an instance of DocumentAnalyzer
    analyzer = DocumentAnalyzer(models)

    # Path to the document to be analyzed
    document_path = 'path/to/your/document.pdf'  # Replace with the actual document path

    try:
        # Analyze the document
        results = analyzer.analyze_document(document_path)

        # Compare the results
        comparison = analyzer.compare_results(results)

        # Output the comparison summary
        print(json.dumps(comparison, indent=4))
    except Exception as e:
        logging.error(f"An error occurred during document analysis: {e}")

if __name__ == "__main__":
    main()
```
