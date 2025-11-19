"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tangganglife.pages.dev
Prompt: How can I implement a leaderboard feature for guilds using the Tang Gang API?
Generated: DETERMINISTIC_55efab1ef2e2129e
Batch ID: 20250612_163502
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tanggang.com": {
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

class TangGangAPI:
    """
    A class to interact with the Tang Gang API for guild leaderboard features.
    """
    BASE_URL = "https://api.tanggang.com"

    def __init__(self, api_key):
        """
        Initializes the TangGangAPI with the provided API key.
        
        Args:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key

    def get_leaderboard(self, guild_id):
        """
        Fetches the leaderboard for a specific guild.
        
        Args:
            guild_id (str): The ID of the guild for which to fetch the leaderboard.

        Returns:
            dict: A dictionary containing leaderboard data.

        Raises:
            ValueError: If the response from the API is not valid.
            Exception: For any other errors encountered during the request.
        """
        url = f"{self.BASE_URL}/guilds/{guild_id}/leaderboard"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Validate the response structure
            if 'leaderboard' not in data:
                raise ValueError("Invalid response format: 'leaderboard' key is missing.")
            
            return data['leaderboard']

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except ValueError as val_err:
            print(f"Value error: {val_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

def main():
    """
    Main function to demonstrate the usage of the Tang Gang API leaderboard feature.
    """
    # Replace with your actual API key and guild ID
    api_key = "YOUR_API_KEY"
    guild_id = "YOUR_GUILD_ID"

    tg_api = TangGangAPI(api_key)

    try:
        leaderboard = tg_api.get_leaderboard(guild_id)
        print("Guild Leaderboard:")
        for entry in leaderboard:
            print(f"{entry['rank']}: {entry['username']} - {entry['score']} points")

    except Exception as e:
        print(f"Failed to retrieve leaderboard: {e}")

if __name__ == "__main__":
    main()
```
