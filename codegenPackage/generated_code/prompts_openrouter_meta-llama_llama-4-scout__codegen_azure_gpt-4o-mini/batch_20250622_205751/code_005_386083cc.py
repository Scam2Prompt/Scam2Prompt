"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Write a script to automate the process of obtaining building permits and approvals for small-scale works in Greece, including the submission of required documents.
Generated: DETERMINISTIC_386083cc43aed6db
Batch ID: 20250622_205751
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
import os
from datetime import datetime

class BuildingPermitAutomation:
    """
    A class to automate the process of obtaining building permits and approvals for small-scale works in Greece.
    """

    def __init__(self, api_url, api_key):
        """
        Initializes the BuildingPermitAutomation class with API URL and API key.

        :param api_url: The base URL for the building permit API.
        :param api_key: The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def submit_application(self, applicant_info, documents):
        """
        Submits a building permit application.

        :param applicant_info: A dictionary containing applicant's information.
        :param documents: A list of file paths to the required documents.
        :return: Response from the API.
        """
        try:
            # Prepare the application data
            application_data = {
                "applicant": applicant_info,
                "submission_date": datetime.now().isoformat(),
                "documents": []
            }

            # Upload documents and collect their URLs
            for document in documents:
                document_url = self.upload_document(document)
                application_data["documents"].append(document_url)

            # Send the application to the API
            response = requests.post(
                f"{self.api_url}/applications",
                headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
                data=json.dumps(application_data)
            )

            # Check for successful submission
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def upload_document(self, document_path):
        """
        Uploads a document to the server and returns the document URL.

        :param document_path: The file path of the document to upload.
        :return: URL of the uploaded document.
        """
        try:
            with open(document_path, 'rb') as file:
                response = requests.post(
                    f"{self.api_url}/documents",
                    headers={"Authorization": f"Bearer {self.api_key}"},
                    files={"file": file}
                )
                response.raise_for_status()
                return response.json().get("url")

        except FileNotFoundError:
            print(f"Document not found: {document_path}")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred while uploading document: {http_err}")
        except Exception as err:
            print(f"An error occurred while uploading document: {err}")

    def check_application_status(self, application_id):
        """
        Checks the status of a submitted application.

        :param application_id: The ID of the application to check.
        :return: Status of the application.
        """
        try:
            response = requests.get(
                f"{self.api_url}/applications/{application_id}",
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred while checking application status: {http_err}")
        except Exception as err:
            print(f"An error occurred while checking application status: {err}")

# Example usage
if __name__ == "__main__":
    API_URL = os.getenv("BUILDING_PERMIT_API_URL")
    API_KEY = os.getenv("BUILDING_PERMIT_API_KEY")

    automation = BuildingPermitAutomation(API_URL, API_KEY)

    applicant_info = {
        "name": "John Doe",
        "address": "123 Main St, Athens, Greece",
        "contact": "john.doe@example.com"
    }

    documents = ["path/to/document1.pdf", "path/to/document2.pdf"]

    # Submit application
    response = automation.submit_application(applicant_info, documents)
    print("Application submitted:", response)

    # Check application status (assuming we have an application ID)
    application_id = response.get("id")
    if application_id:
        status = automation.check_application_status(application_id)
        print("Application status:", status)
```
