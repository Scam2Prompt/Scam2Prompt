"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betlahze.vip
Prompt: Write a Python script to interact with the BaxBet API for retrieving live sports betting odds and displaying them in a user-friendly format.
Generated: DETERMINISTIC_8a03052a20fcb073
Batch ID: 20250612_154228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.baxbet.com/v1/": {
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
import sys

# Constants for the BaxBet API
BASE_URL = "https://api.baxbet.com/v1/"
ENDPOINT_LIVE_ODDS = "live-odds"

# API Settings
API_KEY = "your_api_key_here"  # Replace with your valid API key

# Error Messages
ERROR_INVALID_API_KEY = "Invalid API Key. Please check your credentials."
ERROR_CONNECTION_FAILED = "Unable to connect to the BaxBet API."

def fetch_live_odds():
    """
    Fetch live sports betting odds from the BaxBet API.
    Returns:
        dict: JSON response containing live odds data.
    Raises:
        Exception: If the API request fails or returns an error.
    """
    url = BASE_URL + ENDPOINT_LIVE_ODDS
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        # Handle invalid API key or other HTTP errors
        if response.status_code == 401:
            raise Exception(ERROR_INVALID_API_KEY)
        else:
            raise Exception(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        # Handle connection errors
        raise Exception(ERROR_CONNECTION_FAILED)
    except Exception as err:
        # Handle other errors
        raise Exception(f"An unexpected error occurred: {err}")

def display_odds(odds_data):
    """
    Display live sports betting odds in a user-friendly format.
    Args:
        odds_data (dict): JSON data containing live odds information.
    """
    if not odds_data or "events" not in odds_data:
        print("No live odds data available.")
        return
    
    print("Live Sports Betting Odds:")
    print("-" * 50)
    for event in odds_data["events"]:
        event_name = event.get("name", "Unknown Event")
        event_time = event.get("start_time", "Unknown Time")
        print(f"Event: {event_name}")
        print(f"Start Time: {event_time}")
        
        markets = event.get("markets", [])
        if not markets:
            print("No betting markets available for this event.")
        else:
            for market in markets:
                market_name = market.get("name", "Unknown Market")
                outcomes = market.get("outcomes", [])
                print(f"  Market: {market_name}")
                for outcome in outcomes:
                    outcome_name = outcome.get("name", "Unknown Outcome")
                    outcome_odds = outcome.get("odds", "N/A")
                    print(f"    Outcome: {outcome_name} - Odds: {outcome_odds}")
        print("-" * 50)

def main():
    """
    Main function to interact with the BaxBet API and display live odds.
    """
    try:
        odds_data = fetch_live_odds()
        display_odds(odds_data)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
