"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportsbookcochilli.pages.dev
Prompt: Generate a script to display upcoming sports events with betting odds, similar to the format used on CoChilli SportsBook for UEFA EURO matches.
Generated: DETERMINISTIC_a499290d670f7bac
Batch ID: 20250612_152235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/sports/events": {
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
from datetime import datetime
from typing import List, Dict

# Constants for the API endpoint and the sport
API_URL = "https://api.example.com/sports/events"  # Replace with actual API URL
SPORT = "football"
TOURNAMENT = "UEFA EURO"

def fetch_upcoming_events() -> List[Dict]:
    """
    Fetches upcoming sports events from the API.

    Returns:
        List[Dict]: A list of upcoming sports events with betting odds.
    """
    try:
        response = requests.get(API_URL, params={"sport": SPORT, "tournament": TOURNAMENT})
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get("events", [])
    except requests.RequestException as e:
        print(f"Error fetching events: {e}")
        return []

def format_event(event: Dict) -> str:
    """
    Formats the event information into a display string.

    Args:
        event (Dict): A dictionary containing event information.

    Returns:
        str: A formatted string representing the event.
    """
    event_time = datetime.fromisoformat(event['date']).strftime('%Y-%m-%d %H:%M')
    home_team = event['homeTeam']
    away_team = event['awayTeam']
    odds = event['odds']
    
    # Format the odds for display
    odds_display = f"Home: {odds['home']:.2f}, Draw: {odds['draw']:.2f}, Away: {odds['away']:.2f}"
    
    return f"{event_time} - {home_team} vs {away_team} | Odds: {odds_display}"

def display_events(events: List[Dict]) -> None:
    """
    Displays the formatted events to the console.

    Args:
        events (List[Dict]): A list of events to display.
    """
    if not events:
        print("No upcoming events found.")
        return

    print(f"Upcoming {TOURNAMENT} Matches:")
    for event in events:
        print(format_event(event))

def main() -> None:
    """
    Main function to coordinate the fetching and displaying of sports events.
    """
    upcoming_events = fetch_upcoming_events()
    display_events(upcoming_events)

if __name__ == "__main__":
    main()
```

This code fetches and displays upcoming sports events with betting odds for the UEFA EURO tournament while following best practices and including error handling.
