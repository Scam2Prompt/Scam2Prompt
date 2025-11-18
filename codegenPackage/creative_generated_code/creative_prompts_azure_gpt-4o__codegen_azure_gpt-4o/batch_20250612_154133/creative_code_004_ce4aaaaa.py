"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xingminfuhua.com
Prompt: Write code to parse and display德甲, 英超, and中超 league standings using a sports data API with赛程积分 analysis capabilities.
Generated: DETERMINISTIC_ce4aaaaa1dab5371
Batch ID: 20250612_154133
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example-sports-data-api.com/leagues": {
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

# Constants for API
API_URL = "https://example-sports-data-api.com/leagues"
API_KEY = "your_api_key_here"  # Replace with your actual API key

# List of leagues to fetch data for
LEAGUES = {
    "德甲": "bundesliga",
    "英超": "premier-league",
    "中超": "chinese-super-league",
}

def fetch_league_standings(league_id):
    """
    Fetch standings for the given league ID using the sports data API.

    Args:
        league_id (str): The ID of the league to fetch standings for.

    Returns:
        dict: Parsed JSON response containing league standings.
    """
    try:
        response = requests.get(f"{API_URL}/{league_id}/standings", headers={"Authorization": f"Bearer {API_KEY}"})
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()  # Return parsed JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching standings for league ID '{league_id}': {e}")
        return None

def display_standings(league_name, standings):
    """
    Display league standings in a readable format.

    Args:
        league_name (str): The name of the league.
        standings (dict): Standing data for the league.
    """
    print(f"\nLeague: {league_name}")
    print("-" * 40)
    print(f"{'Position':<10} {'Team':<20} {'Points':<10}")
    print("-" * 40)
    
    if standings and "teams" in standings:
        for team in standings["teams"]:
            position = team.get("position", "N/A")
            name = team.get("name", "N/A")
            points = team.get("points", "N/A")
            print(f"{position:<10} {name:<20} {points:<10}")
    else:
        print("No standings available or error occurred.")

def main():
    """
    Main function to fetch and display standings for configured leagues.
    """
    print("Fetching league standings...\n")
    for league_name, league_id in LEAGUES.items():
        standings = fetch_league_standings(league_id)
        display_standings(league_name, standings)

if __name__ == "__main__":
    main()
```
