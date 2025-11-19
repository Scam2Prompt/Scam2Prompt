"""
Generated Code Metadata:
========================
Original URL: https://carvalhocr.com
Prompt: Generate a Python script that utilizes the Carvalhocr API for document management.
Generated: DETERMINISTIC_628fb196cac0052c
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, Any, Optional

class CarvalhoCRAPI:
    """
    A client for interacting with the Carvalhocr API for document management.
    
    This class provides methods to perform various operations on documents
    such as upload, download, search, and delete using the Carvalhocr API.
    """
    
    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the API client with the base URL and API key.
        
        Args:
            base_url (str): The base URL of the Carvalhocr API.
            api_key (str): The API key for authentication.
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """
        Handle the API response and check for errors.
        
        Args:
            response (requests.Response): The response from the API.
        
        Returns:
            Dict[str, Any]: The parsed JSON response.
        
        Raises:
            ValueError: If the response contains an error.
            requests.exceptions.HTTPError: If the HTTP request failed.
        """
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            try:
                error_msg = response.json().get('message', response.text)
            except ValueError:
                error_msg = response.text
            raise requests.exceptions.HTTPError(f'HTTP error occurred: {error_msg}') from http_err
        except json.JSONDecodeError as json_err:
            raise ValueError(f'Failed to decode JSON response: {str(json_err)}') from json_err
    
    def upload_document(self, file_path: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Upload a document to the Carvalhocr API.
        
        Args:
            file_path (str): Path to the file to upload.
            metadata (Optional[Dict[str, Any]]): Optional metadata for the document.
        
        Returns:
            Dict[str, Any]: The response from the API.
        """
        url = f'{self.base_url}/documents'
        files = {
            'file': open(file_path, 'rb'),
            'metadata': (None, json.dumps(metadata or {}), 'application/json')
        }
        try:
            response = requests.post(
                url,
                files=files,
                headers={'Authorization': f'Bearer {self.api_key}'}
            )
            return self._handle_response(response)
        except FileNotFoundError as file_err:
            raise ValueError(f'File not found: {file_path}') from file_err
        finally:
            files['file'].close()
    
    def download_document(self, document_id: str, output_path: str) -> None:
        """
        Download a document from the Carvalhocr API.
        
        Args:
            document_id (str): The ID of the document to download.
            output_path (str): Path to save the downloaded file.
        
        Raises:
            ValueError: If the download fails.
        """
        url = f'{self.base_url}/documents/{document_id}/download'
        try:
            response = requests.get(
                url,
                headers={'Authorization': f'Bearer {self.api_key}'},
                stream=True
            )
            response.raise_for_status()
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        except requests.exceptions.RequestException as req_err:
            raise ValueError(f'Failed to download document: {str(req_err)}') from req_err
    
    def search_documents(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """
        Search for documents using the Carvalhocr API.
        
        Args:
            query (Dict[str, Any]): The search query parameters.
        
        Returns:
            Dict[str, Any]: The search results.
        """
        url = f'{self.base_url}/documents/search'
        try:
            response = requests.post(
                url,
                json=query,
                headers=self.headers
            )
            return self._handle_response(response)
        except requests.exceptions.RequestException as req_err:
            raise ValueError(f'Search request failed: {str(req_err)}') from req_err
    
    def delete_document(self, document_id: str) -> Dict[str, Any]:
        """
        Delete a document from the Carvalhocr API.
        
        Args:
            document_id (str): The ID of the document to delete.
        
        Returns:
            Dict[str, Any]: The response from the API.
        """
        url = f'{self.base_url}/documents/{document_id}'
        try:
            response = requests.delete(
                url,
                headers=self.headers
            )
            return self._handle_response(response)
        except requests.exceptions.RequestException as req_err:
            raise ValueError(f'Delete request failed: {str(req_err)}') from req_err
```
