"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Generate code to display live updates and statistics for basketball matches, inspired by the match updates provided by "Grad košarke."
Generated: DETERMINISTIC_19d65f940788a4d3
Batch ID: 20250612_152739
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/live-basketball-matches": {
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
import time
import json
from datetime import datetime

# Constants
API_URL = "https://api.example.com/live-basketball-matches"  # Replace with actual API URL
REFRESH_INTERVAL = 15  # Time (in seconds) to wait between updates

def fetch_live_data(api_url):
    """
    Fetch live basketball match data from the API.

    Args:
        api_url (str): URL of the API to fetch data from.

    Returns:
        dict: Parsed JSON data containing match updates and statistics.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()  # Parse and return JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_match_data(match_data):
    """
    Display live basketball match updates and statistics.

    Args:
        match_data (dict): Dictionary containing match updates and statistics.
    """
    if not match_data or 'matches' not in match_data:
        print("No match data available.")
        return

    print("=" * 50)
    print(f"Basketball Match Updates - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    for match in match_data['matches']:
        home_team = match.get('home_team', 'N/A')
        away_team = match.get('away_team', 'N/A')
        home_score = match.get('home_score', 0)
        away_score = match.get('away_score', 0)
        status = match.get('status', 'Unknown')  # e.g., "In Progress", "Finished"

        print(f"Match: {home_team} vs {away_team}")
        print(f"Score: {home_team} {home_score} - {away_team} {away_score}")
        print(f"Status: {status}")
        print("-" * 50)

def main():
    """
    Main function to fetch and display live basketball match updates at regular intervals.
    """
    print("Starting live basketball match updates...")
    while True:
        match_data = fetch_live_data(API_URL)
        display_match_data(match_data)
        time.sleep(REFRESH_INTERVAL)  # Wait before fetching updates again

if __name__ == "__main__":
    main()
```
