"""
Generated Code Metadata:
========================
Original URL: https://anygrid.app
Prompt: How can I use natural language queries to get structured responses from a dataset of hundreds of documents, similar to AnyGrid's features?
Generated: DETERMINISTIC_2438680ef23acc71
Batch ID: 20250622_211918
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
from typing import List, Dict, Any
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.INFO)

class DocumentQueryProcessor:
    def __init__(self, documents: List[str]):
        """
        Initialize the DocumentQueryProcessor with a list of documents.

        :param documents: A list of document strings to be queried.
        """
        self.documents = documents
        self.nlp_model = pipeline("question-answering")

    def query_documents(self, query: str) -> List[Dict[str, Any]]:
        """
        Process a natural language query against the documents and return structured responses.

        :param query: A natural language query string.
        :return: A list of structured responses containing the document index and answer.
        """
        responses = []
        for index, document in enumerate(self.documents):
            try:
                # Use the NLP model to get the answer from the document
                result = self.nlp_model(question=query, context=document)
                responses.append({
                    "document_index": index,
                    "answer": result['answer'],
                    "score": result['score']
                })
            except Exception as e:
                logging.error(f"Error processing document {index}: {e}")
                responses.append({
                    "document_index": index,
                    "error": str(e)
                })
        return responses

def load_documents_from_directory(directory: str) -> List[str]:
    """
    Load documents from a specified directory.

    :param directory: The path to the directory containing document files.
    :return: A list of document strings.
    """
    documents = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    documents.append(file.read())
    except Exception as e:
        logging.error(f"Error loading documents from directory {directory}: {e}")
    return documents

def main():
    # Load documents from a specified directory
    documents_directory = 'path/to/documents'
    documents = load_documents_from_directory(documents_directory)

    if not documents:
        logging.warning("No documents found to process.")
        return

    # Initialize the query processor
    query_processor = DocumentQueryProcessor(documents)

    # Example query
    query = "What is the main topic of the documents?"
    responses = query_processor.query_documents(query)

    # Print structured responses
    print(json.dumps(responses, indent=2))

if __name__ == "__main__":
    main()
```

Make sure to replace `'path/to/documents'` with the actual path to your documents directory. This code uses the Hugging Face Transformers library for natural language processing, so ensure you have it installed in your environment.
