"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deneme1-1gn.pages.dev
Prompt: Write a function to integrate Mocaverse's "Moca XP" system into a leaderboard application.
Generated: DETERMINISTIC_4ebdc9b116188c37
Batch ID: 20250612_152656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mocaverse.example": {
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

class Leaderboard:
    def __init__(self, api_url):
        """
        Initializes the Leaderboard class with the given API URL.
        
        Args:
            api_url (str): The base URL for the Mocaverse API.
        """
        self.api_url = api_url
        self.leaderboard_data = []

    def fetch_moca_xp_data(self):
        """
        Fetches Moca XP data from the Mocaverse API.
        
        Raises:
            Exception: If there is an error in fetching data from the API.
        """
        try:
            response = requests.get(f"{self.api_url}/moca_xp")
            response.raise_for_status()  # Raise an error for bad responses
            self.leaderboard_data = response.json()
        except requests.RequestException as e:
            raise Exception(f"Error fetching Moca XP data: {e}")

    def generate_leaderboard(self):
        """
        Generates a leaderboard based on the fetched Moca XP data.
        
        Returns:
            list: A sorted list of users and their corresponding Moca XP.
        """
        if not self.leaderboard_data:
            raise Exception("Leaderboard data is empty. Please fetch data first.")
        
        # Sort users by Moca XP in descending order
        leaderboard = sorted(self.leaderboard_data, key=lambda x: x['moca_xp'], reverse=True)
        
        return leaderboard

    def display_leaderboard(self):
        """
        Displays the leaderboard in a formatted manner.
        """
        leaderboard = self.generate_leaderboard()
        print("Leaderboard:")
        print("{:<20} {:<10}".format("Username", "Moca XP"))
        print("-" * 30)
        for user in leaderboard:
            print("{:<20} {:<10}".format(user['username'], user['moca_xp']))

if __name__ == "__main__":
    # Example usage of the Leaderboard class
    API_URL = "https://api.mocaverse.example"  # Replace with the actual API endpoint
    leaderboard = Leaderboard(API_URL)
    
    try:
        leaderboard.fetch_moca_xp_data()
        leaderboard.display_leaderboard()
    except Exception as e:
        print(f"An error occurred: {e}")
```
