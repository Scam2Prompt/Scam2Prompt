"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Generate a Python script that utilizes EasyDoc's solutions for digital document management and organization in a business context.
Generated: DETERMINISTIC_b9629082d16debf7
Batch ID: 20250612_163647
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.easydoc.com/v1": {
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
"""
Digital Document Management Script using EasyDoc API

This script demonstrates how to utilize EasyDoc's solutions for digital document
management and organization in a business context. It includes functionalities 
for uploading, retrieving, organizing, and deleting documents via EasyDoc's API.

Requirements:
- Install `requests` library: pip install requests
- Obtain an API key from EasyDoc's platform.

Author: Professional Software Developer
"""

import os
import requests

# Constants
EASYDOC_BASE_URL = "https://api.easydoc.com/v1"
API_KEY = os.getenv("EASYDOC_API_KEY")  # Make sure to set your API key as an environment variable

# Helper function to handle API requests
def api_request(endpoint, method="GET", data=None, files=None):
    """
    Makes a request to the EasyDoc API and returns the JSON response.

    Parameters:
    - endpoint (str): API endpoint to target.
    - method (str): HTTP method ('GET', 'POST', 'DELETE').
    - data (dict): Payload for POST/DELETE requests.
    - files (dict): Files for upload.

    Returns:
    - dict: JSON response from the API.
    """
    url = f"{EASYDOC_BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=data, files=files)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, data=data)
        else:
            raise ValueError("Unsupported HTTP method.")
        
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return {"error": str(e)}

# Function to upload a document
def upload_document(file_path, metadata):
    """
    Uploads a document to EasyDoc.

    Parameters:
    - file_path (str): Path to the file to be uploaded.
    - metadata (dict): Metadata associated with the document.

    Returns:
    - dict: Response from EasyDoc API.
    """
    if not os.path.exists(file_path):
        print("File not found. Please provide a valid file path.")
        return {"error": "File not found"}

    endpoint = "documents"
    files = {"file": open(file_path, "rb")}
    data = {"metadata": metadata}

    return api_request(endpoint, method="POST", data=data, files=files)

# Function to retrieve a document
def retrieve_document(document_id):
    """
    Retrieves a document from EasyDoc using its document ID.

    Parameters:
    - document_id (str): ID of the document to retrieve.

    Returns:
    - dict: Response from EasyDoc API.
    """
    endpoint = f"documents/{document_id}"
    return api_request(endpoint, method="GET")

# Function to delete a document
def delete_document(document_id):
    """
    Deletes a document from EasyDoc using its document ID.

    Parameters:
    - document_id (str): ID of the document to delete.

    Returns:
    - dict: Response from EasyDoc API.
    """
    endpoint = f"documents/{document_id}"
    return api_request(endpoint, method="DELETE")

# Function to organize documents into folders
def organize_documents(folder_name, document_ids):
    """
    Organizes documents into a folder in EasyDoc.

    Parameters:
    - folder_name (str): Name of the folder.
    - document_ids (list): List of document IDs to be added to the folder.

    Returns:
    - dict: Response from EasyDoc API.
    """
    endpoint = "folders"
    data = {"name": folder_name, "document_ids": document_ids}
    return api_request(endpoint, method="POST", data=data)

# Example usage
if __name__ == "__main__":
    # Upload a document
    print("Uploading document...")
    upload_response = upload_document("example.pdf", metadata={"title": "Example Document", "category": "Reports"})
    print(upload_response)

    # Retrieve a document
    if "id" in upload_response:
        document_id = upload_response["id"]
        print("Retrieving document...")
        retrieve_response = retrieve_document(document_id)
        print(retrieve_response)

    # Delete the document
    if "id" in upload_response:
        print("Deleting document...")
        delete_response = delete_document(upload_response["id"])
        print(delete_response)

    # Organize documents into a folder
    print("Organizing documents into a folder...")
    organize_response = organize_documents("Business Reports", document_ids=["123", "456", "789"])
    print(organize_response)
```
