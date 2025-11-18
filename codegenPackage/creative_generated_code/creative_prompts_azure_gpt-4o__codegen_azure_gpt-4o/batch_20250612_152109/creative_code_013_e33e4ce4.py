"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinumult.pages.dev
Prompt: Write a script to interact with the leaderboard feature of the Diamond Hands app, fetching the top holders and their locking durations across all chains.
Generated: DETERMINISTIC_e33e4ce450c1760c
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.diamondhands.app/v1": {
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

# Constants for the API endpoint and headers
API_BASE_URL = "https://api.diamondhands.app/v1"
LEADERBOARD_ENDPOINT = "/leaderboard"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def fetch_leaderboard():
    """
    Function to fetch the leaderboard details from Diamond Hands API.

    Returns:
        list: A list of top holders with their locking durations across all chains.
    """
    try:
        # Make a GET request to fetch leaderboard data
        response = requests.get(f"{API_BASE_URL}{LEADERBOARD_ENDPOINT}", headers=HEADERS)
        
        # Raise an exception if the response status code is not 200 (OK)
        response.raise_for_status()
        
        # Parse the JSON response
        leaderboard_data = response.json()
        
        return leaderboard_data.get('top_holders', [])
    except requests.exceptions.RequestException as e:
        # Log or print the error message
        print(f"Error fetching leaderboard: {e}")
        return []

def display_leaderboard(holders):
    """
    Function to display leaderboard data in a readable format.

    Args:
        holders (list): List of top holders with their locking durations.
    """
    if not holders:
        print("No leaderboard data available.")
        return

    print(f"{'Rank':<5} {'Holder':<30} {'Locking Duration (Days)':<20}")
    print("-" * 55)
    
    for index, holder in enumerate(holders, start=1):
        name = holder.get("name", "Unknown")
        lock_duration = holder.get("locking_duration", "N/A")
        print(f"{index:<5} {name:<30} {lock_duration:<20}")

def main():
    """
    Main entry point of the script.
    Fetches and displays the leaderboard data from the Diamond Hands app.
    """
    print("Fetching leaderboard data...")
    leaderboard = fetch_leaderboard()
    display_leaderboard(leaderboard)

if __name__ == "__main__":
    main()
```
