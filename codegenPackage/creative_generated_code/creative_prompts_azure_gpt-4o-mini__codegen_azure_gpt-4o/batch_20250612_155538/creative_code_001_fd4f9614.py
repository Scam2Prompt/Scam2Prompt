"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skillchain.io
Prompt: Write a code snippet that demonstrates how to integrate Skillchain's blockchain technology for immutable document storage.
Generated: DETERMINISTIC_fd4f961401882e90
Batch ID: 20250612_155538
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.skillchain.com/v1/documents": {
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
import json

# Constants for Skillchain API integration
SKILLCHAIN_API_URL = "https://api.skillchain.com/v1/documents"
API_KEY = "your_api_key_here"  # Replace with your Skillchain API key

def upload_document_to_skillchain(file_path, metadata):
    """
    Uploads a document to Skillchain for immutable blockchain storage.
    
    Args:
        file_path (str): Path to the document to be uploaded.
        metadata (dict): Metadata associated with the document (e.g., title, description, tags).

    Returns:
        dict: Response from the Skillchain API.
    """
    try:
        # Open the file to be uploaded
        with open(file_path, 'rb') as file:
            # Prepare the payload
            files = {'document': file}
            headers = {'Authorization': f'Bearer {API_KEY}'}
            data = {'metadata': json.dumps(metadata)}

            # Make the POST request to upload the document
            response = requests.post(SKILLCHAIN_API_URL, headers=headers, files=files, data=data)

            # Check for HTTP errors
            response.raise_for_status()

            # Parse and return the JSON response
            return response.json()

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}. Please verify the file path.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
    return None

# Example usage
if __name__ == "__main__":
    # Document file path and metadata
    file_path = "path/to/document.pdf"  # Replace with the actual file path
    metadata = {
        "title": "Sample Document",
        "description": "This is a sample document stored on Skillchain.",
        "tags": ["example", "immutable", "blockchain"]
    }

    # Upload the document
    response = upload_document_to_skillchain(file_path, metadata)

    # Display the response
    if response:
        print("Document successfully uploaded to Skillchain:")
        print(json.dumps(response, indent=4))
    else:
        print("Failed to upload the document to Skillchain.")
```
