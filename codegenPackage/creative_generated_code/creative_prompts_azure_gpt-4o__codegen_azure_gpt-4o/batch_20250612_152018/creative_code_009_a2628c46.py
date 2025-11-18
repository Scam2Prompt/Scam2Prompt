"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-protocol.net
Prompt: Suggest APIs or libraries for integrating Wattpad’s storytelling platform into a mobile app that allows offline reading and writing, as described on the website.
Generated: DETERMINISTIC_a2628c46101662c1
Batch ID: 20250612_152018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wattpad.com/v4": {
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
"""
Script Name: wattpad_integration.py
Description: A Python module that integrates with Wattpad's API for managing stories.
             This module includes offline reading and writing capabilities using local storage.
Author: [Your Name]
Creation Date: [Insert Date]
"""

import requests
import json
import os


class WattpadAPIIntegration:
    """
    Class for integrating with Wattpad's API to fetch, save, and update stories.
    Provides offline reading and writing capabilities using local storage.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.wattpad.com/v4"):
        """
        Initialize the Wattpad API Integration class.

        :param api_key: API key for authenticating with Wattpad API.
        :param base_url: Base URL of the Wattpad API (default is v4).
        """
        self.api_key = api_key
        self.base_url = base_url
        self.offline_storage_path = "offline_stories"  # Local directory for offline stories

        # Ensure the offline storage directory exists
        if not os.path.exists(self.offline_storage_path):
            os.makedirs(self.offline_storage_path)

    def _make_api_request(self, endpoint: str, params: dict = None) -> dict:
        """
        Helper method to make authenticated requests to the Wattpad API.

        :param endpoint: API endpoint to call (e.g., "stories").
        :param params: Additional query parameters for the API call.
        :return: JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making API request: {e}")
            return {}

    def fetch_story(self, story_id: str) -> dict:
        """
        Fetch a single story from Wattpad using its ID.

        :param story_id: ID of the story to fetch.
        :return: Story data as a dictionary.
        """
        return self._make_api_request(f"stories/{story_id}")

    def save_story_offline(self, story_id: str) -> None:
        """
        Save a story locally for offline reading.

        :param story_id: ID of the story to save offline.
        """
        story = self.fetch_story(story_id)
        if story:
            file_path = os.path.join(self.offline_storage_path, f"{story_id}.json")
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(story, file, indent=4)
            print(f"Story '{story_id}' saved offline at {file_path}.")
        else:
            print(f"Failed to fetch or save story '{story_id}'.")

    def read_story_offline(self, story_id: str) -> dict:
        """
        Read a story locally from offline storage.

        :param story_id: ID of the story to read offline.
        :return: Story data as a dictionary (or None if not found).
        """
        file_path = os.path.join(self.offline_storage_path, f"{story_id}.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        else:
            print(f"Offline story '{story_id}' not found.")
            return None

    def write_story_offline(self, story_id: str, updated_content: dict) -> None:
        """
        Update a locally stored story with new content.

        :param story_id: ID of the story to update.
        :param updated_content: Dictionary containing updated story content.
        """
        file_path = os.path.join(self.offline_storage_path, f"{story_id}.json")
        if os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(updated_content, file, indent=4)
            print(f"Story '{story_id}' updated offline.")
        else:
            print(f"Offline story '{story_id}' not found. Cannot update.")


# Example usage (replace YOUR_API_KEY with your valid Wattpad API key)
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your Wattpad API key
    wattpad_integration = WattpadAPIIntegration(api_key)

    # Fetch and save a story offline
    wattpad_integration.save_story_offline("123456")

    # Read a story offline
    offline_story = wattpad_integration.read_story_offline("123456")
    if offline_story:
        print(f"Offline story content: {offline_story}")

    # Update a story offline
    updated_content = {"title": "Updated Title", "content": "Updated content goes here."}
    wattpad_integration.write_story_offline("123456", updated_content)
```
