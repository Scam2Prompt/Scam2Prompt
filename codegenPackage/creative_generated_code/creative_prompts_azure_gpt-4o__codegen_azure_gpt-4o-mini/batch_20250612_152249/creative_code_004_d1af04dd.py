"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paragraming-claims.live
Prompt: Write code to fetch and display unique in-game content rewards tied to $PARAM tokens in the Param Gaming ecosystem.
Generated: DETERMINISTIC_d1af04dddf3ad502
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paramgaming.com": {
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

class ParamGamingAPI:
    """
    A class to interact with the Param Gaming API to fetch unique in-game content rewards.
    """
    
    BASE_URL = "https://api.paramgaming.com"  # Base URL for the Param Gaming API

    def __init__(self, token):
        """
        Initializes the API client with the provided token.

        Args:
            token (str): The API token for authentication.
        """
        self.token = token

    def fetch_rewards(self, param_tokens):
        """
        Fetches unique in-game content rewards tied to the given PARAM tokens.

        Args:
            param_tokens (list): A list of PARAM tokens to fetch rewards for.

        Returns:
            list: A list of unique rewards associated with the given tokens.

        Raises:
            ValueError: If the input tokens list is empty.
            Exception: If there is an error fetching data from the API.
        """
        if not param_tokens:
            raise ValueError("The list of PARAM tokens cannot be empty.")

        rewards = set()  # Use a set to store unique rewards

        for token in param_tokens:
            try:
                response = requests.get(f"{self.BASE_URL}/rewards/{token}", headers=self._get_headers())
                response.raise_for_status()  # Raise an error for bad responses
                
                data = response.json()
                rewards.update(data.get("unique_rewards", []))  # Add unique rewards to the set

            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred while fetching rewards for token {token}: {http_err}")
            except Exception as err:
                print(f"An error occurred while fetching rewards for token {token}: {err}")

        return list(rewards)  # Convert the set back to a list

    def _get_headers(self):
        """
        Returns the headers required for API authentication.

        Returns:
            dict: A dictionary containing the required headers.
        """
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }


# Example usage:
if __name__ == "__main__":
    try:
        api_token = "YOUR_API_TOKEN_HERE"  # Replace with your actual API token
        param_tokens = ["TOKEN1", "TOKEN2", "TOKEN3"]  # Replace with actual PARAM tokens

        api_client = ParamGamingAPI(api_token)
        unique_rewards = api_client.fetch_rewards(param_tokens)

        print("Unique In-Game Rewards:")
        for reward in unique_rewards:
            print(f"- {reward}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
