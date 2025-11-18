"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--uda.at
Prompt: Generate code to integrate Google Workspace tools (Docs, Calendar, Meet, Chat, Drive) into a web application, as outlined on ý.at.
Generated: DETERMINISTIC_1c020aec7642ded4
Batch ID: 20250612_154756
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/meet": {
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
  "https://www.googleapis.com/auth/chat.bot": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/auth/calendar": {
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
# Import required libraries
from google.oauth2 import service_account
from googleapiclient.discovery import build
from flask import Flask, request, jsonify

# Flask application initialization
app = Flask(__name__)

# Google Workspace API setup
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'
SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/chat.bot',
    'https://www.googleapis.com/auth/meet'
]

# Load the service account credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# Function to create a new Google Doc
@app.route('/create-doc', methods=['POST'])
def create_google_doc():
    try:
        # Initialize the Docs API
        service = build('docs', 'v1', credentials=credentials)

        # Create a new document
        doc = service.documents().create(body={'title': 'New Document'}).execute()

        # Return the document ID
        return jsonify({'documentId': doc.get('documentId'), 'title': doc.get('title')})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to add a calendar event
@app.route('/add-event', methods=['POST'])
def add_calendar_event():
    try:
        # Initialize the Calendar API
        service = build('calendar', 'v3', credentials=credentials)

        # Parse the event details from the request
        event_details = request.json
        event = {
            'summary': event_details['summary'],
            'start': {'dateTime': event_details['start'], 'timeZone': 'UTC'},
            'end': {'dateTime': event_details['end'], 'timeZone': 'UTC'}
        }

        # Insert the event
        event_result = service.events().insert(calendarId='primary', body=event).execute()

        # Return the event details
        return jsonify({'eventId': event_result.get('id'), 'summary': event_result.get('summary')})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to list files in Google Drive
@app.route('/list-drive-files', methods=['GET'])
def list_google_drive_files():
    try:
        # Initialize the Drive API
        service = build('drive', 'v3', credentials=credentials)

        # List the files
        results = service.files().list(pageSize=10, fields="files(id, name)").execute()
        files = results.get('files', [])

        # Return the file list
        return jsonify({'files': files})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to send a Google Chat message (via a bot)
@app.route('/send-chat-message', methods=['POST'])
def send_google_chat_message():
    try:
        # Initialize the Chat API
        service = build('chat', 'v1', credentials=credentials)

        # Parse the message details from the request
        message_details = request.json
        message = {
            'text': message_details['text']
        }

        # Send the message to the specified space
        space_name = message_details['space_name']
        response = service.spaces().messages().create(
            parent=space_name, body=message).execute()

        # Return the message details
        return jsonify({'message': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to generate a Google Meet link
@app.route('/generate-meet-link', methods=['POST'])
def generate_google_meet_link():
    try:
        # Initialize the Calendar API (Meet links are generated via Calendar events)
        service = build('calendar', 'v3', credentials=credentials)

        # Parse the meeting details from the request
        meeting_details = request.json
        event = {
            'summary': meeting_details['summary'],
            'start': {'dateTime': meeting_details['start'], 'timeZone': 'UTC'},
            'end': {'dateTime': meeting_details['end'], 'timeZone': 'UTC'},
            'conferenceData': {
                'createRequest': {
                    'requestId': 'sample123',
                    'conferenceSolutionKey': {'type': 'hangoutsMeet'}
                }
            }
        }

        # Insert the event with Meet link
        event_result = service.events().insert(
            calendarId='primary', body=event, conferenceDataVersion=1).execute()

        # Return the Meet link
        meet_link = event_result.get('hangoutLink', '')
        return jsonify({'meetLink': meet_link})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Notes:
1. Replace `path/to/your/service-account-file.json` with the actual path to your Google Cloud service account JSON file.
2. Ensure that the service account has appropriate permissions for accessing Google Workspace APIs.
3. Set up OAuth scopes on Google Cloud and enable the APIs you plan to use.
4. This code assumes the use of Flask for the web application framework. Install dependencies (`flask`, `google-auth`, `google-api-python-client`) before running.
