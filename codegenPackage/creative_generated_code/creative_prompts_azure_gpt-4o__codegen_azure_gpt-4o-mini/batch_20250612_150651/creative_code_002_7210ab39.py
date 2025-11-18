"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globallinknext.com
Prompt: Generate code to automate translation workflows using features highlighted in TransPerfect's GlobalLink technology.
Generated: DETERMINISTIC_7210ab3947b0d33e
Batch ID: 20250612_150651
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.transperfect.com/globallink/v1": {
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

class TransPerfectGlobalLink:
    """
    A class to automate translation workflows using TransPerfect's GlobalLink technology.
    """

    def __init__(self, api_key, api_url):
        """
        Initializes the TransPerfectGlobalLink class with API key and URL.

        :param api_key: API key for authentication
        :param api_url: Base URL for TransPerfect GlobalLink API
        """
        self.api_key = api_key
        self.api_url = api_url

    def create_project(self, project_data):
        """
        Creates a new translation project.

        :param project_data: Dictionary containing project details
        :return: Response from the API call
        """
        endpoint = f"{self.api_url}/projects"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        try:
            response = requests.post(endpoint, headers=headers, data=json.dumps(project_data))
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors

    def get_project_status(self, project_id):
        """
        Retrieves the status of a given translation project.

        :param project_id: The ID of the project to check
        :return: Response from the API call
        """
        endpoint = f"{self.api_url}/projects/{project_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors

    def upload_file(self, project_id, file_path):
        """
        Uploads a file for translation in the specified project.

        :param project_id: The ID of the project to upload the file to
        :param file_path: Path to the file to be uploaded
        :return: Response from the API call
        """
        endpoint = f"{self.api_url}/projects/{project_id}/files"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            with open(file_path, 'rb') as file:
                files = {'file': file}
                response = requests.post(endpoint, headers=headers, files=files)
                response.raise_for_status()  # Raises an HTTPError for bad responses
                return response.json()
        except FileNotFoundError:
            print(f"The file {file_path} was not found. Please provide a valid file path.")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    API_URL = "https://api.transperfect.com/globallink/v1"
    
    # Initialize the GlobalLink client
    gl_client = TransPerfectGlobalLink(API_KEY, API_URL)
    
    # Create a project
    project_data = {
        "name": "New Translation Project",
        "sourceLanguage": "en",
        "targetLanguages": ["es", "fr"],
        "description": "Project description goes here."
    }
    project_response = gl_client.create_project(project_data)
    print(project_response)

    # Check project status (if project_response contains a valid project ID)
    if project_response and "id" in project_response:
        project_id = project_response["id"]
        status_response = gl_client.get_project_status(project_id)
        print(status_response)

    # Upload a file to the created project (if project_response contains a valid project ID)
    if project_response and "id" in project_response:
        file_path = "path/to/your/file.txt"
        upload_response = gl_client.upload_file(project_id, file_path)
        print(upload_response)
```
