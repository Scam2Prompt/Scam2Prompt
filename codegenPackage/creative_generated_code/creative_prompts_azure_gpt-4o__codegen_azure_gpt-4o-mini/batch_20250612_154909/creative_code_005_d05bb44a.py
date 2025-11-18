"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigmgroup.co.ug
Prompt: Suggest tools or APIs for managing press releases and post-event inquiries, as described in Paradigm Group's event management services.
Generated: DETERMINISTIC_d05bb44a2ab2234a
Batch ID: 20250612_154909
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1": {
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

class PressReleaseManager:
    """
    A class to manage press releases and post-event inquiries using an external API.
    """

    def __init__(self, api_key: str, base_url: str):
        """
        Initializes the PressReleaseManager with API key and base URL.

        :param api_key: The API key for authenticating with the external service.
        :param base_url: The base URL of the API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, endpoint: str, method: str = 'GET', data: dict = None):
        """
        Makes an HTTP request to the specified endpoint.

        :param endpoint: The API endpoint to call.
        :param method: The HTTP method to use ('GET', 'POST', etc.).
        :param data: The data to send with the request (used with POST).
        :return: Response data if successful, or None if there was an error.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {'Authorization': f"Bearer {self.api_key}", 'Content-Type': 'application/json'}

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError("Unsupported HTTP method: only GET and POST are allowed.")

            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Return JSON data from the response

        except requests.exceptions.RequestException as e:
            # Log the error (or handle it as appropriate for your application)
            print(f"An error occurred: {e}")
            return None

    def create_press_release(self, title: str, content: str) -> dict:
        """
        Creates a new press release.

        :param title: The title of the press release.
        :param content: The content of the press release.
        :return: The created press release data or None if an error occurred.
        """
        endpoint = 'press-releases'
        data = {'title': title, 'content': content}
        return self._make_request(endpoint, method='POST', data=data)

    def get_press_releases(self) -> list:
        """
        Retrieves all press releases.

        :return: A list of press releases or None if an error occurred.
        """
        endpoint = 'press-releases'
        return self._make_request(endpoint, method='GET')

    def post_event_inquiry(self, event_id: str, inquiry: str) -> dict:
        """
        Posts an inquiry for a specific event.

        :param event_id: The ID of the event.
        :param inquiry: The content of the inquiry.
        :return: The response data or None if an error occurred.
        """
        endpoint = f'events/{event_id}/inquiries'
        data = {'inquiry': inquiry}
        return self._make_request(endpoint, method='POST', data=data)

# Example usage:
if __name__ == "__main__":
    # Replace with actual API key and base URL
    API_KEY = 'your_api_key'
    BASE_URL = 'https://api.example.com/v1'

    press_manager = PressReleaseManager(API_KEY, BASE_URL)
    
    # Create a press release
    press_release = press_manager.create_press_release("Launch Event", "We are excited to announce...")
    print(press_release)

    # Get all press releases
    all_releases = press_manager.get_press_releases()
    print(all_releases)

    # Post an event inquiry
    inquiry_response = press_manager.post_event_inquiry("event123", "What time does the event start?")
    print(inquiry_response)
```
