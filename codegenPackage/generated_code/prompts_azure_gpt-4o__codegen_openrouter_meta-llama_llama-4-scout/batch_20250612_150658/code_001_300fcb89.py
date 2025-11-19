"""
Generated Code Metadata:
========================
Original URL: https://gift-chiliz.net
Prompt: Generate a script that uses the Microsoft Teams API to schedule a meeting and send invitations, incorporating Copilot's AI-assisted features.
Generated: DETERMINISTIC_300fcb89ae59e650
Batch ID: 20250612_150658
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://graph.microsoft.com/.default": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.microsoft.com/v1.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
import json
from datetime import datetime, timedelta

# Define constants
MICROSOFT_TEAMS_API_URL = "https://graph.microsoft.com/v1.0"
MICROSOFT_TEAMS_APP_ID = "your_app_id"
MICROSOFT_TEAMS_APP_PASSWORD = "your_app_password"
ORGANIZER_MAIL = "organizer@example.com"
MEETING_SUBJECT = "Test Meeting"
MEETING_BODY = "This is a test meeting"
MEETING_START_TIME = (datetime.now() + timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%S")
MEETING_END_TIME = (datetime.now() + timedelta(minutes=60)).strftime("%Y-%m-%dT%H:%M:%S")

# Function to get access token
def get_access_token():
    """
    Get access token for Microsoft Teams API
    """
    auth_url = f"{MICROSOFT_TEAMS_API_URL}/oauth2/v2.0/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": MICROSOFT_TEAMS_APP_ID,
        "client_secret": MICROSOFT_TEAMS_APP_PASSWORD,
        "scope": "https://graph.microsoft.com/.default"
    }
    response = requests.post(auth_url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception("Failed to get access token")

# Function to schedule meeting
def schedule_meeting(access_token):
    """
    Schedule a meeting using Microsoft Teams API
    """
    graph_url = f"{MICROSOFT_TEAMS_API_URL}/me/events"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    meeting_data = {
        "subject": MEETING_SUBJECT,
        "body": {
            "content": MEETING_BODY,
            "contentType": "HTML"
        },
        "start": {
            "dateTime": MEETING_START_TIME,
            "timeZone": "UTC"
        },
        "end": {
            "dateTime": MEETING_END_TIME,
            "timeZone": "UTC"
        },
        "attendees": [
            {
                "emailAddress": {
                    "address": ORGANIZER_MAIL,
                    "name": "Organizer"
                },
                "type": "required"
            }
        ]
    }
    response = requests.post(graph_url, headers=headers, data=json.dumps(meeting_data))
    if response.status_code == 201:
        return response.json()["id"]
    else:
        raise Exception("Failed to schedule meeting")

# Function to send invitations
def send_invitations(access_token, meeting_id):
    """
    Send invitations for a scheduled meeting
    """
    graph_url = f"{MICROSOFT_TEAMS_API_URL}/me/events/{meeting_id}/sendMail"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    invitation_data = {
        "message": {
            "subject": MEETING_SUBJECT,
            "body": {
                "content": MEETING_BODY,
                "contentType": "HTML"
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": ORGANIZER_MAIL
                    }
                }
            ]
        },
        "saveToSentItems": True
    }
    response = requests.post(graph_url, headers=headers, data=json.dumps(invitation_data))
    if response.status_code == 202:
        return True
    else:
        raise Exception("Failed to send invitations")

# Main function
def main():
    try:
        access_token = get_access_token()
        meeting_id = schedule_meeting(access_token)
        send_invitations(access_token, meeting_id)
        print("Meeting scheduled and invitations sent successfully")
    except Exception as e:
        print(f"Error: {str(e)}")

# Run main function
if __name__ == "__main__":
    main()
```
