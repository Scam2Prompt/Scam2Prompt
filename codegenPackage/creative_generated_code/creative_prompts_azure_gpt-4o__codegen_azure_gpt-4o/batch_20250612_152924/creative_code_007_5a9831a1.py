"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appdevistorias.com.br
Prompt: Provide a code example for integrating remote digital signature functionality into an inspection app, referencing the BeSoft App Vistoria's Autentique integration.
Generated: DETERMINISTIC_5a9831a18dd5fe5d
Batch ID: 20250612_152924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.autentique.com/v2": {
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

class DigitalSignatureIntegration:
    """
    A class to manage the integration with Autentique's digital signature API 
    for BeSoft App Vistoria's inspection app.
    """
    
    def __init__(self, api_key: str, base_url: str = "https://api.autentique.com/v2"):
        """
        Initializes the integration class.

        :param api_key: The API key for authenticating with the Autentique API.
        :param base_url: The base URL of the Autentique API (defaults to the v2 endpoint).
        """
        self.api_key = api_key
        self.base_url = base_url

    def create_document(self, title: str, file_path: str):
        """
        Creates a document in Autentique for digital signing.

        :param title: The title of the document to be created.
        :param file_path: The local path to the document file to upload.
        :return: The API response containing document details or an error message.
        """
        try:
            url = f"{self.base_url}/documents"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            files = {
                "file": (file_path, open(file_path, "rb")),
                "title": (None, title)
            }

            response = requests.post(url, headers=headers, files=files)

            if response.status_code == 201:
                return response.json()  # Successfully created
            else:
                response.raise_for_status()  # Raise an HTTPError if status code is unsuccessful
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def list_documents(self):
        """
        Lists all documents available in Autentique.

        :return: The API response containing the list of documents or an error message.
        """
        try:
            url = f"{self.base_url}/documents"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                return response.json()  # Successfully retrieved list
            else:
                response.raise_for_status()  # Raise an HTTPError if status code is unsuccessful
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def send_signature_request(self, document_id: str, signer_name: str, signer_email: str):
        """
        Sends a signature request to a signer for a specific document.

        :param document_id: The ID of the document to be signed.
        :param signer_name: The name of the signer.
        :param signer_email: The email address of the signer.
        :return: The API response containing signature details or an error message.
        """
        try:
            url = f"{self.base_url}/signers"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            payload = {
                "document_id": document_id,
                "signers": [
                    {"name": signer_name, "email": signer_email}
                ]
            }

            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 201:
                return response.json()  # Successfully sent request
            else:
                response.raise_for_status()  # Raise an HTTPError if status code is unsuccessful
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_autentique_api_key_here"
    integration = DigitalSignatureIntegration(API_KEY)

    # Step 1: Create a new document
    new_document = integration.create_document("Inspection Report", "path/to/report.pdf")
    if "error" in new_document:
        print(f"Error creating document: {new_document['error']}")
    else:
        print(f"Document created: {new_document}")

    # Step 2: List all documents
    documents = integration.list_documents()
    if "error" in documents:
        print(f"Error listing documents: {documents['error']}")
    else:
        print(f"Documents: {documents}")

    # Step 3: Send signature request
    if "data" in new_document and new_document["data"]:
        document_id = new_document["data"]["id"]
        signature_request = integration.send_signature_request(document_id, "John Doe", "john.doe@example.com")
        if "error" in signature_request:
            print(f"Error sending signature request: {signature_request['error']}")
        else:
            print(f"Signature request sent: {signature_request}")
```
