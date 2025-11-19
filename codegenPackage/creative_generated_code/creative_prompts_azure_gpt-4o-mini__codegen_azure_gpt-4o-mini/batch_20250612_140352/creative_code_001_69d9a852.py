"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frokai.pages.dev
Prompt: Write a code snippet that utilizes Frok AI's API to create customized visuals tailored to user preferences.
Generated: DETERMINISTIC_69d9a852c91358f3
Batch ID: 20250612_140352
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.frok.ai/v1/visuals": {
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

class FrokAIClient:
    def __init__(self, api_key):
        """
        Initializes the FrokAIClient with the provided API key.

        Args:
            api_key (str): The API key for authenticating requests to Frok AI's API.
        """
        self.api_key = api_key
        self.base_url = "https://api.frok.ai/v1/visuals"

    def create_visual(self, preferences):
        """
        Creates a customized visual based on user preferences.

        Args:
            preferences (dict): A dictionary containing user preferences for the visual.

        Returns:
            dict: The response from the API containing the visual details.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, data=json.dumps(preferences))

            # Check if the response status code indicates an error
            response.raise_for_status()
            
            return response.json()
        
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # e.g., 404 Not Found
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")  # e.g., network issues
        except json.JSONDecodeError as json_err:
            raise Exception(f"Failed to decode JSON response: {json_err}")

if __name__ == "__main__":
    # Example usage of the FrokAIClient
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    user_preferences = {
        "theme": "dark",
        "style": "abstract",
        "color_palette": ["#FF5733", "#33FF57", "#3357FF"],  # Example color palette
        "size": "1024x768"
    }

    client = FrokAIClient(API_KEY)
    
    try:
        visual = client.create_visual(user_preferences)
        print("Visual created successfully:", visual)
    except Exception as e:
        print("An error occurred:", e)
```
