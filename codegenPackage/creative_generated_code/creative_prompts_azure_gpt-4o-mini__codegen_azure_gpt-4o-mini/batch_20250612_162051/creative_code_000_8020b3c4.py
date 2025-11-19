"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://searchhr.com.ar
Prompt: Generate a Python script that automates the process of uploading a CV to a job search platform like Search HR.
Generated: DETERMINISTIC_8020b3c46cdb5328
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.searchhr.com/upload": {
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

class CVUploader:
    """A class to upload CVs to the job search platform."""

    def __init__(self, upload_url, api_key):
        """
        Initializes the CVUploader with the necessary parameters.

        Args:
            upload_url (str): The endpoint URL for uploading the CV.
            api_key (str): The API key for authentication.
        """
        self.upload_url = upload_url
        self.api_key = api_key

    def upload_cv(self, cv_path):
        """
        Uploads the CV to the specified job search platform.

        Args:
            cv_path (str): The file path of the CV to be uploaded.

        Returns:
            dict: The response from the server after the upload attempt.
        """
        # Ensure the CV file exists before attempting to upload
        if not os.path.isfile(cv_path):
            raise FileNotFoundError(f"The specified CV file does not exist: {cv_path}")

        # Prepare the headers for the upload
        headers = {'Authorization': f'Bearer {self.api_key}'}
        
        # Prepare the file for upload
        files = {'file': open(cv_path, 'rb')}
        
        try:
            # Send POST request to upload CV
            response = requests.post(self.upload_url, headers=headers, files=files)

            # Check the response status code
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Return the JSON response if successful

        except requests.exceptions.RequestException as e:
            # Handle any request-related exceptions
            print(f"An error occurred while uploading the CV: {e}")
            return {"success": False, "error": str(e)}

        finally:
            # Ensure the file is closed after the upload attempt
            files['file'].close()

if __name__ == "__main__":
    # Example usage:
    uploader = CVUploader(upload_url="https://api.searchhr.com/upload", api_key="YOUR_API_KEY_HERE")
    
    try:
        response = uploader.upload_cv(cv_path="path/to/your/cv.pdf")
        print("Upload successful:", response)
    except Exception as e:
        print("Error:", str(e))
```
