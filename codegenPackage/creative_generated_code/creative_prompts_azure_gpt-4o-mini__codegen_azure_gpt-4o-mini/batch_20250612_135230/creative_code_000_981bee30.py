"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graphpool.net
Prompt: Generate a code snippet to integrate with the GraphPool API for uploading user-generated content.
Generated: DETERMINISTIC_981bee30bbb38ff8
Batch ID: 20250612_135230
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.graphpool.com/v1": {
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

class GraphPoolAPI:
    """
    A class to interact with the GraphPool API for uploading user-generated content.
    """
    
    BASE_URL = "https://api.graphpool.com/v1"  # Base URL for the GraphPool API
    
    def __init__(self, api_key):
        """
        Initializes the GraphPoolAPI with the provided API key.

        Parameters:
        api_key (str): The API key for authenticating requests to the GraphPool API.
        """
        self.api_key = api_key

    def upload_content(self, file_path, content_metadata):
        """
        Uploads user-generated content to the GraphPool API.

        Parameters:
        file_path (str): The local path to the file to be uploaded.
        content_metadata (dict): A dictionary containing metadata about the content.

        Returns:
        dict: The response from the API, parsed as JSON.

        Raises:
        ValueError: If the file does not exist or the content metadata is invalid.
        Exception: For any other errors encountered during the upload process.
        """
        # Validate the file path
        if not os.path.isfile(file_path):
            raise ValueError(f"File not found: {file_path}")
        
        # Validate content metadata
        if not isinstance(content_metadata, dict) or not content_metadata:
            raise ValueError("Content metadata must be a non-empty dictionary.")

        # Prepare headers for authentication and content type
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # Prepare the file for upload
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(f"{self.BASE_URL}/upload", headers=headers, files=files, data=json.dumps(content_metadata))

        # Check for successful response
        if response.status_code != 200:
            raise Exception(f"Failed to upload content: {response.status_code} {response.text}")

        # Return the response as a JSON dictionary
        return response.json()

# Example usage
if __name__ == "__main__":
    import os
    import json

    API_KEY = "your_api_key_here"  # Replace with your actual API key
    file_path = "path/to/your/file.jpg"  # Replace with the path to your file
    content_metadata = {
        "title": "My User-Generated Content",
        "description": "A description of my content",
        "tags": ["example", "upload"]
    }

    try:
        graph_pool_api = GraphPoolAPI(API_KEY)
        response = graph_pool_api.upload_content(file_path, content_metadata)
        print("Upload successful:", response)
    except Exception as e:
        print("An error occurred:", str(e))
```
