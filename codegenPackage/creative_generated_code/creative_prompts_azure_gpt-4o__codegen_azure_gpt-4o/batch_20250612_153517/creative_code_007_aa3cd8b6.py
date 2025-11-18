"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fsromain.com
Prompt: Develop a script to track and analyze follower growth for influencers, similar to the profiles highlighted on fsromain.com.
Generated: DETERMINISTIC_aa3cd8b6d829c6c0
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/influencers": {
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
import time
from datetime import datetime

class FollowerGrowthTracker:
    """
    A class to track and analyze follower growth for influencers.
    """

    def __init__(self, usernames: list, api_endpoint: str, api_key: str):
        """
        Initialize the tracker with influencer data.

        :param usernames: List of influencer usernames to track.
        :param api_endpoint: API endpoint to fetch follower data.
        :param api_key: API key for authentication to the API.
        """
        self.usernames = usernames
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.data_file = "follower_data.json"
        self.interval = 86400  # Check every 24 hours (in seconds)

    def fetch_follower_count(self, username: str) -> int:
        """
        Fetch the follower count for a given username.

        :param username: The username of the influencer to track.
        :return: Follower count as an integer.
        :raises: Exception if API request fails or response is invalid.
        """
        try:
            response = requests.get(
                f"{self.api_endpoint}/{username}",
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()  # Raise HTTPError if status code is not 200
            data = response.json()
            return data.get("followers_count", 0)
        except requests.RequestException as e:
            raise Exception(f"Error fetching follower count for {username}: {e}")
        except (ValueError, KeyError) as e:
            raise Exception(f"Invalid response format for {username}: {e}")

    def save_data(self, data: dict) -> None:
        """
        Save follower data to a JSON file.

        :param data: A dictionary of follower data to save.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving data to {self.data_file}: {e}")

    def load_data(self) -> dict:
        """
        Load follower data from a JSON file.

        :return: A dictionary of follower data.
        """
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError):
            return {}  # Return an empty dictionary if the file is missing or invalid

    def track_growth(self) -> None:
        """
        Main function to track follower growth periodically.
        """
        print("Starting follower growth tracking...")
        while True:
            current_data = self.load_data()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for username in self.usernames:
                try:
                    follower_count = self.fetch_follower_count(username)
                    print(f"[{timestamp}] {username}: {follower_count} followers")
                    
                    # Update the data for the current timestamp
                    if username not in current_data:
                        current_data[username] = []
                    
                    current_data[username].append({
                        "timestamp": timestamp,
                        "followers_count": follower_count
                    })
                except Exception as e:
                    print(e)

            # Save updated data to the file
            self.save_data(current_data)

            print(f"Data saved. Sleeping for {self.interval} seconds...")
            time.sleep(self.interval)

if __name__ == "__main__":
    # Example configuration
    influencer_usernames = ["influencer1", "influencer2", "influencer3"]
    api_endpoint = "https://api.example.com/influencers"
    api_key = "your_api_key_here"

    tracker = FollowerGrowthTracker(influencer_usernames, api_endpoint, api_key)
    tracker.track_growth()
```
