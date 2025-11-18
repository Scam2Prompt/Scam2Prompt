"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://norion.loan
Prompt: Generate a script to integrate Google Workspace tools (Docs, Calendar, Meet, Chat, Drive) into a web hosting platform, referencing the collaboration tools mentioned on norion.loan.
Generated: DETERMINISTIC_c7c13d85453491a4
Batch ID: 20250612_154506
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/calendar": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/auth/chat.bot": {
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
  "https://www.googleapis.com/auth/documents": {
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
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Load Google API credentials from a service account JSON file
def load_credentials():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            'path/to/service_account.json',  # Update the path to the service account file
            scopes=[
                'https://www.googleapis.com/auth/documents',
                'https://www.googleapis.com/auth/calendar',
                'https://www.googleapis.com/auth/drive',
                'https://www.googleapis.com/auth/chat.bot',
            ]
        )
        return credentials
    except Exception as e:
        print("Error loading credentials:", e)
        return None

# Create a Google Docs document
@app.route('/create-doc', methods=['POST'])
def create_doc():
    credentials = load_credentials()
    if not credentials:
        return jsonify({'error': 'Failed to load credentials'}), 500

    service = build('docs', 'v1', credentials=credentials)

    # Create a new document
    doc = {
        'title': 'New Document from Norion Loan Integration'
    }
    try:
        doc_response = service.documents().create(body=doc).execute()
        return jsonify(doc_response), 201
    except Exception as e:
        print("Error creating document:", e)
        return jsonify({'error': 'Failed to create document'}), 500

# Create a Google Calendar event
@app.route('/create-event', methods=['POST'])
def create_event():
    credentials = load_credentials()
    if not credentials:
        return jsonify({'error': 'Failed to load credentials'}), 500

    service = build('calendar', 'v3', credentials=credentials)
    event_data = request.json

    # Ensure the required fields are provided
    if not event_data.get('summary') or not event_data.get('start') or not event_data.get('end'):
        return jsonify({'error': 'Summary, start, and end are required'}), 400

    event = {
        'summary': event_data['summary'],
        'start': event_data['start'],
        'end': event_data['end'],
    }
    
    try:
        event_response = service.events().insert(calendarId='primary', body=event).execute()
        return jsonify(event_response), 201
    except Exception as e:
        print("Error creating event:", e)
        return jsonify({'error': 'Failed to create event'}), 500

# Upload a file to Google Drive
@app.route('/upload-file', methods=['POST'])
def upload_file():
    credentials = load_credentials()
    if not credentials:
        return jsonify({'error': 'Failed to load credentials'}), 500

    service = build('drive', 'v3', credentials=credentials)
    file_data = request.files['file']

    file_metadata = {
        'name': file_data.filename,
        'mimeType': file_data.content_type
    }
    
    try:
        media = MediaFileUpload(file_data, mimetype=file_data.content_type)
        drive_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return jsonify({'file_id': drive_file.get('id')}), 201
    except Exception as e:
        print("Error uploading file:", e)
        return jsonify({'error': 'Failed to upload file'}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

**Note**: Ensure to replace `'path/to/service_account.json'` with the actual path to your service account credentials JSON file. The server also requires appropriate configurations for handling file uploads, and you might need to install the required packages like `Flask`, `google-auth`, and `google-api-python-client`.
