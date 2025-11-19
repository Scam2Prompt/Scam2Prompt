"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfcloudpbx.com
Prompt: Generate a sample API call for managing voicemail transcripts through the PREMHost CloudPBX system.
Generated: DETERMINISTIC_991530ac61e6ef61
Batch ID: 20250612_155150
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.premhost.com/cloudpbx/v1": {
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

class PremHostCloudPBX:
    """
    A class to manage voicemail transcripts through the PREMHost CloudPBX system.
    """

    BASE_URL = "https://api.premhost.com/cloudpbx/v1"  # Base URL for the API
    TIMEOUT = 10  # Request timeout in seconds

    def __init__(self, api_key):
        """
        Initializes the PremHostCloudPBX class with the provided API key.

        :param api_key: The API key for authenticating requests
        """
        self.api_key = api_key

    def _make_request(self, method, endpoint, data=None):
        """
        Makes an API request to the specified endpoint.

        :param method: The HTTP method (GET, POST, PUT, DELETE)
        :param endpoint: The API endpoint to call
        :param data: The payload to send with the request (if applicable)
        :return: The response data
        :raises Exception: Raises an exception for HTTP errors
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.request(method, url, headers=headers, json=data, timeout=self.TIMEOUT)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")  # Handle other request errors

    def get_voicemail_transcripts(self):
        """
        Retrieves the list of voicemail transcripts.

        :return: A list of voicemail transcripts
        """
        return self._make_request("GET", "voicemail/transcripts")

    def add_voicemail_transcript(self, voicemail_id, transcript):
        """
        Adds a new voicemail transcript.

        :param voicemail_id: The ID of the voicemail
        :param transcript: The transcript of the voicemail
        :return: The created transcript data
        """
        payload = {
            "voicemail_id": voicemail_id,
            "transcript": transcript
        }
        return self._make_request("POST", "voicemail/transcripts", data=payload)

    def delete_voicemail_transcript(self, transcript_id):
        """
        Deletes a voicemail transcript.

        :param transcript_id: The ID of the transcript to delete
        :return: The response status
        """
        return self._make_request("DELETE", f"voicemail/transcripts/{transcript_id}")


# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual API key
    api_key = 'your_api_key_here'
    cloud_pbx = PremHostCloudPBX(api_key)

    try:
        # Retrieve voicemail transcripts
        transcripts = cloud_pbx.get_voicemail_transcripts()
        print("Voicemail Transcripts:", transcripts)

        # Add a new transcript
        new_transcript = cloud_pbx.add_voicemail_transcript("12345", "This is a sample voicemail transcript.")
        print("Added Transcript:", new_transcript)

        # Delete a transcript by ID
        delete_status = cloud_pbx.delete_voicemail_transcript(new_transcript['id'])
        print("Delete Status:", delete_status)

    except Exception as e:
        print("An error occurred:", e)
```
