"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looties-next-app.vercel.app
Prompt: Generate a code snippet that integrates with the Looties API to claim rewards from NFT cases.
Generated: DETERMINISTIC_cc7ca905419e3daf
Batch ID: 20250612_162504
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.looties.com/v1": {
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

class LootiesAPI:
    """
    A class to interact with the Looties API for claiming rewards from NFT cases.
    """

    BASE_URL = "https://api.looties.com/v1"

    def __init__(self, api_key):
        """
        Initializes the LootiesAPI instance.

        Args:
            api_key (str): The API key for authenticating with the Looties API.
        """
        self.api_key = api_key

    def claim_reward(self, user_id, case_id):
        """
        Claims a reward from a specified NFT case.

        Args:
            user_id (str): The ID of the user claiming the reward.
            case_id (str): The ID of the case from which to claim the reward.

        Returns:
            dict: The response from the API containing the claim status and reward details.

        Raises:
            ValueError: If the user ID or case ID is invalid.
            Exception: For other errors encountered during the API request.
        """
        if not user_id or not case_id:
            raise ValueError("Both user_id and case_id must be provided.")

        url = f"{self.BASE_URL}/users/{user_id}/cases/{case_id}/claim"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, headers=headers)

            # Raise an exception for HTTP errors
            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log any request-related errors
            raise
        except Exception as e:
            print(f"An error occurred: {e}")  # Log any other exceptions
            raise

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    USER_ID = "user_id_here"
    CASE_ID = "case_id_here"

    looties_api = LootiesAPI(API_KEY)

    try:
        reward_response = looties_api.claim_reward(USER_ID, CASE_ID)
        print("Reward claimed successfully:", reward_response)
    except Exception as e:
        print("Failed to claim reward:", e)
```
