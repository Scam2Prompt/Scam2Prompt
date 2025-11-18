"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.media
Prompt: Suggest libraries or APIs for creating personality-driven social media videos that position a subject matter expert as a voice of authority, as emphasized by Kraken Media.
Generated: DETERMINISTIC_d63ec19985f1582c
Batch ID: 20250612_151752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
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

class VideoCreationAPI:
    """
    A class to interact with various video creation APIs for generating personality-driven social media videos.
    """

    def __init__(self, api_key: str):
        """
        Initializes the VideoCreationAPI with the provided API key.

        :param api_key: The API key for authentication with the video creation service.
        """
        self.api_key = api_key
        self.base_url = "https://api.example.com"  # Replace with actual API base URL

    def create_video(self, script: str, subject_expert: str) -> dict:
        """
        Creates a video using the provided script and subject matter expert information.

        :param script: The script content for the video.
        :param subject_expert: Information about the subject matter expert.
        :return: A dictionary containing video details or an error message.
        """
        endpoint = f"{self.base_url}/create_video"
        payload = {
            "script": script,
            "expert": subject_expert
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the created video details
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request exception occurred: {req_err}"}

    def get_video_status(self, video_id: str) -> dict:
        """
        Retrieves the status of a created video.

        :param video_id: The ID of the video to check the status.
        :return: A dictionary containing the status of the video or an error message.
        """
        endpoint = f"{self.base_url}/video_status/{video_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the status of the video
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request exception occurred: {req_err}"}

# Example usage (ensure to replace 'your_api_key' and other parameters accordingly)
if __name__ == "__main__":
    api_key = "your_api_key"
    video_api = VideoCreationAPI(api_key)

    # Creating a video
    script = "Welcome to our session where we explore cutting-edge technology!"
    subject_expert = "Dr. Jane Smith, Technology Expert"
    
    video_creation_response = video_api.create_video(script, subject_expert)
    print(video_creation_response)

    # Checking video status
    if "video_id" in video_creation_response:
        video_id = video_creation_response["video_id"]
        video_status_response = video_api.get_video_status(video_id)
        print(video_status_response)
```
