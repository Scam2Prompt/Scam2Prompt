"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thichmu.pro
Prompt: Generate a script that sends alerts for live football matches based on specific teams or leagues using a sports data API.
Generated: DETERMINISTIC_9f96a7eb1a1b7bb3
Batch ID: 20250612_160044
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sportsdata.io/v4/soccer/scores/json/LiveGames": {
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

def fetch_live_matches(api_url, api_key):
    """
    Fetch live football match data from the sports data API.
    
    :param api_url: URL of the sports data API.
    :param api_key: API key for authentication.
    :return: JSON response containing live match data.
    """
    try:
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching live matches: {e}")
        return None

def send_alert(match_details):
    """
    Send an alert for a specific football match.
    
    :param match_details: Dictionary containing match details to alert about.
    """
    # Example: Print alert (can replace with email, SMS, etc.)
    print(f"ALERT: Match Update - {match_details['home_team']} vs {match_details['away_team']} | Status: {match_details['status']}")

def filter_matches(matches, teams=None, leagues=None):
    """
    Filter live matches based on specific teams or leagues.
    
    :param matches: List of match data dictionaries.
    :param teams: List of team names to filter (optional).
    :param leagues: List of league names to filter (optional).
    :return: List of filtered matches.
    """
    filtered_matches = []
    for match in matches:
        if teams and match['home_team'] not in teams and match['away_team'] not in teams:
            continue
        if leagues and match['league'] not in leagues:
            continue
        filtered_matches.append(match)
    return filtered_matches

def main():
    """
    Main function to run the script.
    """
    # Configuration
    API_URL = "https://api.sportsdata.io/v4/soccer/scores/json/LiveGames"  # Replace with actual API endpoint
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    POLLING_INTERVAL = 60  # Time interval to fetch live matches (in seconds)
    TEAMS_TO_MONITOR = ["Team A", "Team B"]  # Replace with actual team names
    LEAGUES_TO_MONITOR = ["League A"]  # Replace with actual league names
    
    print("Starting live football match alerts...")
    
    while True:
        # Fetch live match data
        live_matches = fetch_live_matches(API_URL, API_KEY)
        
        if live_matches:
            # Filter matches based on teams or leagues
            relevant_matches = filter_matches(live_matches, TEAMS_TO_MONITOR, LEAGUES_TO_MONITOR)
            
            # Send alerts for relevant matches
            for match in relevant_matches:
                send_alert(match)
        
        # Wait for the next polling interval
        time.sleep(POLLING_INTERVAL)

if __name__ == "__main__":
    main()
```
