"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munimala.gob.pe
Prompt: What are the legal documents required for the extemporaneous registration of births in Mala, and how can I automate their submission?
Generated: DETERMINISTIC_c92c4f4f769af831
Batch ID: 20250612_162508
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/register_birth": {
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
import os
import requests
from datetime import datetime

class BirthRegistrationAutomation:
    """
    A class to automate the submission of legal documents for the extemporaneous registration of births in Mala.
    """

    def __init__(self, api_endpoint, api_key):
        """
        Initialize the automation class with the necessary API details.

        Parameters:
        - api_endpoint: str, the API endpoint for submitting documents.
        - api_key: str, the API key for authentication.
        """
        self.api_endpoint = api_endpoint
        self.api_key = api_key

    def validate_documents(self, document_paths):
        """
        Validate the presence and format of the required documents.

        Parameters:
        - document_paths: list of str, paths to the documents to be validated.

        Returns:
        - bool: True if all documents are valid, False otherwise.
        """
        required_formats = ['pdf', 'jpg', 'png']
        valid = True
        for path in document_paths:
            if not os.path.isfile(path):
                print(f"Error: Document {path} does not exist.")
                valid = False
                continue
            if not path.split('.')[-1].lower() in required_formats:
                print(f"Error: Document {path} has an invalid format.")
                valid = False
        return valid

    def submit_documents(self, document_paths):
        """
        Submit the documents to the specified API endpoint.

        Parameters:
        - document_paths: list of str, paths to the documents to be submitted.

        Returns:
        - response: dict, the response from the API call.
        """
        try:
            with open(document_paths[0], 'rb') as file:
                files = {'file': file}
                headers = {'Authorization': f'Bearer {self.api_key}'}
                response = requests.post(self.api_endpoint, files=files, headers=headers)

                # Check for successful response
                response.raise_for_status()
                return response.json()
        
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

    def automate_registration(self, document_paths):
        """
        Automate the registration process by validating and submitting the documents.

        Parameters:
        - document_paths: list of str, paths to the documents to be submitted.
        """
        if self.validate_documents(document_paths):
            print("All documents are valid. Submitting...")
            response = self.submit_documents(document_paths)
            if response:
                print("Documents submitted successfully:", response)
            else:
                print("Failed to submit documents.")
        else:
            print("Document validation failed. Please fix the errors and try again.")

# Example of how to use the BirthRegistrationAutomation class
if __name__ == "__main__":
    # Replace with your actual API endpoint and API key
    API_ENDPOINT = "https://api.example.com/register_birth"
    API_KEY = "your_api_key_here"

    # Paths to the required legal documents
    documents = [
        "/path/to/birth_certificate.pdf",
        "/path/to/parent_id.jpg"
    ]

    # Create an instance of the automation class
    birth_registration = BirthRegistrationAutomation(API_ENDPOINT, API_KEY)

    # Automate the registration process
    birth_registration.automate_registration(documents)
```
