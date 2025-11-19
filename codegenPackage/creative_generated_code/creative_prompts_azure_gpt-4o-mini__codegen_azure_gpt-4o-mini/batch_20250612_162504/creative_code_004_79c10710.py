"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokugroup.com
Prompt: Create a sample code snippet for a feature that allows users to interact with an intelligent platform for built environments.
Generated: DETERMINISTIC_79c10710d090d27f
Batch ID: 20250612_162504
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.intelligentplatform.com": {
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
import json
import requests

class IntelligentPlatformClient:
    """
    A client for interacting with an intelligent platform for built environments.
    
    Attributes:
        base_url (str): The base URL for the platform's API.
        api_key (str): The API key for authentication.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the IntelligentPlatformClient with base URL and API key.

        Args:
            base_url (str): The base URL for the platform's API.
            api_key (str): The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _handle_response(self, response: requests.Response):
        """
        Handles the API response, checking for errors and returning data.

        Args:
            response (requests.Response): The response from the API call.

        Returns:
            dict: Parsed JSON data from the response.

        Raises:
            Exception: If the response status code indicates an error.
        """
        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code} - {response.text}")
        return response.json()

    def get_environment_data(self, environment_id: str) -> dict:
        """
        Retrieves data for a specific environment.

        Args:
            environment_id (str): The ID of the environment to retrieve data for.

        Returns:
            dict: The environment data.

        Raises:
            ValueError: If the environment_id is not provided.
        """
        if not environment_id:
            raise ValueError("Environment ID must be provided.")

        url = f"{self.base_url}/environments/{environment_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        response = requests.get(url, headers=headers)
        return self._handle_response(response)

    def update_environment_settings(self, environment_id: str, settings: dict) -> dict:
        """
        Updates settings for a specific environment.

        Args:
            environment_id (str): The ID of the environment to update.
            settings (dict): A dictionary containing the new settings.

        Returns:
            dict: The updated environment data.

        Raises:
            ValueError: If the environment_id or settings are not provided.
        """
        if not environment_id:
            raise ValueError("Environment ID must be provided.")
        if not settings:
            raise ValueError("Settings must be provided.")

        url = f"{self.base_url}/environments/{environment_id}/settings"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.put(url, headers=headers, data=json.dumps(settings))
        return self._handle_response(response)

# Example usage:
if __name__ == "__main__":
    try:
        client = IntelligentPlatformClient(base_url="https://api.intelligentplatform.com", api_key="your_api_key")
        env_data = client.get_environment_data(environment_id="env123")
        print("Environment Data:", env_data)

        new_settings = {
            "temperature": 22,
            "lighting": "on"
        }
        updated_env_data = client.update_environment_settings(environment_id="env123", settings=new_settings)
        print("Updated Environment Data:", updated_env_data)

    except Exception as e:
        print(f"An error occurred: {e}")
```
