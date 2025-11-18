"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jenniferaustin.typeform.com
Prompt: Demonstrate how to use Typeform's API to create a photo upload form and store the uploaded images in a cloud storage service like Google Drive.
Generated: DETERMINISTIC_4829af9f29c4c7c7
Batch ID: 20250612_151912
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://form.typeform.com/to/{form_id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.typeform.com/forms": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/auth/drive": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://drive.google.com/file/d/{file_id}/view": {
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
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Configuration constants
TYPEFORM_API_URL = "https://api.typeform.com/forms"
TYPEFORM_API_TOKEN = "your_typeform_api_token"
GOOGLE_DRIVE_FOLDER_ID = "your_google_drive_folder_id"
GOOGLE_CREDENTIALS_FILE = "path/to/your/google-service-account.json"
PHOTO_UPLOAD_FORM_TITLE = "Photo Upload Form"

# Function to create a photo upload form in Typeform
def create_photo_upload_form():
    """
    Creates a photo upload form in Typeform.
    Returns the form's URL.
    """
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "title": PHOTO_UPLOAD_FORM_TITLE,
        "fields": [
            {
                "title": "Please upload your photo",
                "type": "file_upload",
                "properties": {
                    "description": "Upload your photo here",
                    "max_file_size": 5242880  # Max file size: 5 MB
                }
            }
        ]
    }

    response = requests.post(TYPEFORM_API_URL, headers=headers, json=payload)

    # Error handling
    if response.status_code != 201:
        raise Exception(f"Failed to create Typeform: {response.json()}")

    form_id = response.json().get("id")
    form_url = f"https://form.typeform.com/to/{form_id}"
    return form_url

# Function to upload a file to Google Drive
def upload_to_google_drive(file_path, file_name):
    """
    Uploads a file to a specified Google Drive folder.
    Args:
        file_path (str): Local path to the file.
        file_name (str): Name of the file in Google Drive.
    Returns:
        str: URL of the uploaded file.
    """
    # Authenticate using Google service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_CREDENTIALS_FILE, scopes=["https://www.googleapis.com/auth/drive"]
    )

    service = build("drive", "v3", credentials=credentials)

    # Upload file
    file_metadata = {
        "name": file_name,
        "parents": [GOOGLE_DRIVE_FOLDER_ID]
    }
    media = MediaFileUpload(file_path, mimetype="image/jpeg")

    uploaded_file = service.files().create(
        body=file_metadata, media_body=media, fields="id"
    ).execute()

    # Generate file URL
    file_id = uploaded_file.get("id")
    file_url = f"https://drive.google.com/file/d/{file_id}/view"
    return file_url

if __name__ == "__main__":
    try:
        # Step 1: Create the Typeform photo upload form
        form_url = create_photo_upload_form()
        print(f"Photo upload form created successfully! Access it at: {form_url}")

        # Step 2: Simulate file upload to Google Drive (replace with actual upload logic)
        # For demo purposes, we use a local image file
        local_file_path = "path/to/local/photo.jpg"
        uploaded_file_name = "uploaded_photo.jpg"
        uploaded_file_url = upload_to_google_drive(local_file_path, uploaded_file_name)
        print(f"Photo uploaded successfully to Google Drive! Access it at: {uploaded_file_url}")

    except Exception as e:
        print(f"Error: {e}")
```
