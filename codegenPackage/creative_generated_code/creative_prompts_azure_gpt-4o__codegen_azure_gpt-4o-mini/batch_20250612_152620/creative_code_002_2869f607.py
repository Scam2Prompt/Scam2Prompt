"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercurio.com.pe
Prompt: Provide a code example for querying the status of electronic documents using Mercurio's platform, including handling responses for SUNAT compliance.
Generated: DETERMINISTIC_2869f6072d91aa21
Batch ID: 20250612_152620
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mercurio.com": {
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

class DocumentStatusQuery:
    """
    Class to handle querying the status of electronic documents from Mercurio's platform.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the DocumentStatusQuery class.

        :param base_url: Base URL for the Mercurio API.
        :param api_key: API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def query_status(self, document_id: str) -> dict:
        """
        Queries the status of a specified electronic document.

        :param document_id: The unique identifier of the document to query.
        :return: Response containing document status or error message.
        """
        url = f"{self.base_url}/api/documents/{document_id}/status"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request error occurred: {req_err}"}

        # Check for SUNAT compliance in the response
        data = response.json()
        if 'status' in data:
            return data  # Return the document status information
        else:
            return {"error": "Unexpected response format", "data": data}

# Example usage
if __name__ == "__main__":
    # Replace with actual base URL and API key
    BASE_URL = "https://api.mercurio.com"
    API_KEY = "your_api_key_here"
    
    document_id = "1234567890"  # Replace with actual document ID

    # Create an instance of DocumentStatusQuery
    status_query = DocumentStatusQuery(BASE_URL, API_KEY)
    
    # Query the document status
    result = status_query.query_status(document_id)
    
    # Print the result
    print(result)
```
