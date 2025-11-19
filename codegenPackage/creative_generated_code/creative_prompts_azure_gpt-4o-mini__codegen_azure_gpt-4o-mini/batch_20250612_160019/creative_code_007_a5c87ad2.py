"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://subscribemenow.com
Prompt: Explain how to use GetResponse's API to create and manage webinars for content monetization.
Generated: DETERMINISTIC_a5c87ad253813b64
Batch ID: 20250612_160019
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.getresponse.com/v3/": {
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

class GetResponseAPI:
    def __init__(self, api_key):
        """Initialize the API client with the provided API key."""
        self.api_key = api_key
        self.base_url = "https://api.getresponse.com/v3/"
        self.headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": f"api-key {self.api_key}"
        }

    def create_webinar(self, name, description, start_time, duration, timezone, webinar_type):
        """Create a new webinar using GetResponse API.

        Args:
            name (str): The name of the webinar.
            description (str): A description of the webinar.
            start_time (str): The start time of the webinar in ISO 8601 format.
            duration (int): Duration of the webinar in minutes.
            timezone (str): Timezone for the webinar.
            webinar_type (str): Type of the webinar (e.g., 'live', 'automated').

        Returns:
            dict: The response from the API containing webinar details.
        """
        url = f"{self.base_url}webinars"
        payload = {
            "name": name,
            "description": description,
            "startTime": start_time,
            "duration": duration,
            "timezone": timezone,
            "type": webinar_type
        }

        response = requests.post(url, headers=self.headers, json=payload)
        self._handle_response(response)
        return response.json()

    def update_webinar(self, webinar_id, name=None, description=None, start_time=None, duration=None):
        """Update an existing webinar.

        Args:
            webinar_id (str): The ID of the webinar to update.
            name (str, optional): The new name of the webinar.
            description (str, optional): The new description of the webinar.
            start_time (str, optional): The new start time of the webinar in ISO 8601 format.
            duration (int, optional): The new duration of the webinar in minutes.

        Returns:
            dict: The response from the API containing updated webinar details.
        """
        url = f"{self.base_url}webinars/{webinar_id}"
        payload = {k: v for k, v in {
            "name": name,
            "description": description,
            "startTime": start_time,
            "duration": duration
        }.items() if v is not None}

        response = requests.put(url, headers=self.headers, json=payload)
        self._handle_response(response)
        return response.json()

    def delete_webinar(self, webinar_id):
        """Delete a webinar by its ID.

        Args:
            webinar_id (str): The ID of the webinar to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        url = f"{self.base_url}webinars/{webinar_id}"
        response = requests.delete(url, headers=self.headers)
        self._handle_response(response)
        return response.status_code == 204

    def _handle_response(self, response):
        """Handle API response and raise exceptions for errors.

        Args:
            response (Response): The API response object.

        Raises:
            Exception: If the API request fails, an exception is raised with the error message.
        """
        if response.status_code not in [200, 201, 204]:
            raise Exception(f"Error {response.status_code}: {response.json().get('message', 'Unknown error')}")

# Example usage:
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    gr_api = GetResponseAPI(api_key)

    # Create a new webinar
    try:
        new_webinar = gr_api.create_webinar(
            name="My First Webinar",
            description="A webinar about content monetization.",
            start_time="2023-12-01T15:00:00Z",
            duration=60,
            timezone="UTC",
            webinar_type="live"
        )
        print("Webinar created:", new_webinar)

        # Update the created webinar
        updated_webinar = gr_api.update_webinar(
            webinar_id=new_webinar['id'],
            name="My Updated Webinar"
        )
        print("Webinar updated:", updated_webinar)

        # Delete the webinar
        if gr_api.delete_webinar(webinar_id=new_webinar['id']):
            print("Webinar deleted successfully.")
    except Exception as e:
        print("An error occurred:", str(e))
```
