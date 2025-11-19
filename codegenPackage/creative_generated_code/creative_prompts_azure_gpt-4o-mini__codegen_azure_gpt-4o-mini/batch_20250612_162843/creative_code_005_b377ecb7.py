"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webex.net.cn
Prompt: Provide a code example for connecting traditional H323/SIP hardware to a Webex meeting using the Webex connector.
Generated: DETERMINISTIC_b377ecb7366ad227
Batch ID: 20250612_162843
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://webexapis.com/v1": {
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

class WebexConnector:
    """
    A class to connect traditional H323/SIP hardware to a Webex meeting using the Webex API.
    """
    
    BASE_URL = "https://webexapis.com/v1"
    
    def __init__(self, access_token):
        """
        Initializes the WebexConnector with the provided access token.

        :param access_token: The OAuth token for authenticating API requests.
        """
        self.access_token = access_token

    def create_meeting(self, title, start_time, end_time):
        """
        Creates a Webex meeting.

        :param title: The title of the meeting.
        :param start_time: The start time of the meeting in ISO 8601 format.
        :param end_time: The end time of the meeting in ISO 8601 format.
        :return: The meeting details as a dictionary.
        :raises Exception: If the meeting creation fails.
        """
        url = f"{self.BASE_URL}/meetings"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "title": title,
            "start": start_time,
            "end": end_time,
            "invitees": [],
            "enabledAutoRecordMeeting": False
        }
        
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        if response.status_code != 200:
            raise Exception(f"Failed to create meeting: {response.text}")
        
        return response.json()

    def add_device_to_meeting(self, meeting_id, device_uri):
        """
        Adds a H323/SIP device to a Webex meeting.

        :param meeting_id: The ID of the Webex meeting.
        :param device_uri: The H323/SIP URI of the device.
        :return: The response from the API.
        :raises Exception: If adding the device fails.
        """
        url = f"{self.BASE_URL}/meetings/{meeting_id}/participants"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "invitee": {
                "email": "",  # Leave empty for H323/SIP devices
                "displayName": device_uri
            },
            "type": "H323",  # Can also be "SIP"
            "address": device_uri
        }
        
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        if response.status_code != 200:
            raise Exception(f"Failed to add device: {response.text}")
        
        return response.json()

# Example Usage
if __name__ == "__main__":
    access_token = "YOUR_ACCESS_TOKEN"
    webex_connector = WebexConnector(access_token)
    
    try:
        meeting = webex_connector.create_meeting("Test Meeting", "2023-10-25T10:00:00Z", "2023-10-25T11:00:00Z")
        print("Meeting created:", meeting)
        
        device_uri = "sip:device@example.com"  # Replace with actual device URI
        response = webex_connector.add_device_to_meeting(meeting["id"], device_uri)
        print("Device added:", response)
        
    except Exception as e:
        print("Error:", e)
```
