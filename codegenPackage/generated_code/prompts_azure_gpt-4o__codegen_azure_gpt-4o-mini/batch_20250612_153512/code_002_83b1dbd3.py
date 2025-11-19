"""
Generated Code Metadata:
========================
Original URL: https://agora-ai.market
Prompt: Generate Python code to query Agora AI's Transparent Reputation System for community-driven ratings of AI agents.
Generated: DETERMINISTIC_83b1dbd3e3d5fae3
Batch ID: 20250612_153512
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.agora.ai/v1/reputation": {
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
import requests

class AgoraAIClient:
    """
    A client to interact with Agora AI's Transparent Reputation System.
    """

    BASE_URL = "https://api.agora.ai/v1/reputation"

    def __init__(self, api_key):
        """
        Initializes the AgoraAIClient with the provided API key.

        :param api_key: str - The API key for authenticating requests.
        """
        self.api_key = api_key

    def get_agent_rating(self, agent_id):
        """
        Queries the reputation system for the community-driven rating of a specific AI agent.

        :param agent_id: str - The unique identifier of the AI agent.
        :return: dict - The response containing the agent's rating information.
        :raises ValueError: If the agent_id is invalid.
        :raises Exception: For any other errors during the API request.
        """
        if not agent_id:
            raise ValueError("Agent ID must not be empty.")

        url = f"{self.BASE_URL}/{agent_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

            return response.json()  # Return the JSON response if successful

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log other request errors
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  # Log unexpected errors
            raise

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    agent_id = "example_agent_id"  # Replace with the actual agent ID you want to query

    client = AgoraAIClient(API_KEY)

    try:
        rating_info = client.get_agent_rating(agent_id)
        print("Agent Rating Information:", rating_info)
    except Exception as e:
        print(f"Failed to retrieve agent rating: {e}")
```
