"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anygrid.app
Prompt: Create a Python function that leverages AnyGrid's natural language query feature to summarize and compare hundreds of documents in seconds, organizing the results into a grid.
Generated: DETERMINISTIC_a267f6dc0f1a53c5
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import anygrid  # Ensure you have the AnyGrid library installed: pip install anygrid
import os

def summarize_and_compare_documents(documents, api_key):
    """
    Summarizes and compares a list of documents using AnyGrid's natural language query feature.
    Organizes the results into a grid.

    Args:
        documents (list of str): List of document texts to be processed.
        api_key (str): API key for authenticating with AnyGrid.

    Returns:
        dict: Results organized into a grid containing summaries and comparisons.
    """

    # Validate inputs
    if not isinstance(documents, list) or not all(isinstance(doc, str) for doc in documents):
        raise ValueError("Documents must be a list of strings.")

    if not api_key or not isinstance(api_key, str):
        raise ValueError("A valid API key must be provided.")

    # Initialize the AnyGrid client with the provided API key
    client = anygrid.Client(api_key=api_key)

    try:
        # Use the natural language query feature to summarize and compare documents
        query = """
        Summarize each document and provide a comparison highlighting key similarities and differences.
        Organize the results into a structured grid format.
        """
        
        # Pass the documents and query to AnyGrid's API
        response = client.query(input_data=documents, query_text=query)
        
        # Check for successful response
        if response.status_code != 200:
            raise RuntimeError(f"Error querying AnyGrid API: {response.error_message}")

        # Return the structured grid result
        return response.result_grid

    except Exception as e:
        # Handle any errors that may occur and log them appropriately
        print(f"An error occurred: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Replace with actual document texts and your AnyGrid API key
    example_documents = ["Document 1 text here", "Document 2 text here", "Document 3 text here"]
    example_api_key = os.getenv("ANYGRID_API_KEY")  # Fetch API key from environment variable for security

    try:
        results_grid = summarize_and_compare_documents(example_documents, example_api_key)
        print("Results Grid:", results_grid)
    except Exception as error:
        print(f"Failed to process documents: {error}")
```
