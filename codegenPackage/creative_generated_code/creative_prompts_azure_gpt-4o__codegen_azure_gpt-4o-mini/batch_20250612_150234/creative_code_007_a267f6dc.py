"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anygrid.app
Prompt: Create a Python function that leverages AnyGrid's natural language query feature to summarize and compare hundreds of documents in seconds, organizing the results into a grid.
Generated: DETERMINISTIC_a267f6dc0f1a53c5
Batch ID: 20250612_150234
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.anygrid.com/v1/queries": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd

class AnyGridAPIError(Exception):
    """Custom exception for handling AnyGrid API errors."""
    pass

def summarize_and_compare_documents(documents: list, api_key: str) -> pd.DataFrame:
    """
    Summarize and compare a list of documents using AnyGrid's natural language query feature.

    Parameters:
    documents (list): A list of document strings to be summarized and compared.
    api_key (str): The API key for authenticating with AnyGrid's API.

    Returns:
    pd.DataFrame: A DataFrame containing the summaries and comparisons of the documents.

    Raises:
    AnyGridAPIError: If the API response indicates an error.
    Exception: If there are issues with the API request.
    """
    # Check if the documents list is empty
    if not documents:
        raise ValueError("The documents list cannot be empty.")

    # Prepare the data for the API request
    payload = {
        "query": {
            "type": "summarize_and_compare",
            "documents": documents
        }
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Send the request to AnyGrid's API
        response = requests.post("https://api.anygrid.com/v1/queries", json=payload, headers=headers)
        
        # Raise an exception if the response indicates an error
        response.raise_for_status()
        
    except requests.HTTPError as http_err:
        raise AnyGridAPIError(f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise Exception(f"An error occurred during the API request: {err}")

    # Process the response JSON
    results = response.json()
    
    # Check for expected structure in the response
    if 'results' not in results:
        raise AnyGridAPIError("Unexpected response structure from AnyGrid API.")

    # Create a DataFrame to hold the summaries and comparisons
    summary_data = []
    for result in results['results']:
        summary_data.append({
            "Document": result['document'],
            "Summary": result['summary'],
            "Comparison": result['comparison']
        })

    # Convert to DataFrame
    summary_df = pd.DataFrame(summary_data)

    return summary_df

# Example usage (uncomment and replace with actual data and API key):
# if __name__ == "__main__":
#     documents_list = ["Document 1 content...", "Document 2 content..."]
#     api_key = "your_anygrid_api_key"
#     try:
#         summary_df = summarize_and_compare_documents(documents_list, api_key)
#         print(summary_df)
#     except Exception as e:
#         print(f"An error occurred: {e}")
```
