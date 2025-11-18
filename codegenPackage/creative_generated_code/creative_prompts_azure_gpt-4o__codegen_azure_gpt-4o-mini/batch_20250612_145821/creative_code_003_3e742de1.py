"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-moca.com
Prompt: Create a script that uses an economic calendar API to fetch upcoming events affecting Forex pairs like GBP/USD and display them in a user-friendly format.
Generated: DETERMINISTIC_3e742de1fd2e7e09
Batch ID: 20250612_145821
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://economic-calendar-api.com/api/v1/events": {
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
from datetime import datetime, timedelta

# Constants for the API
API_URL = "https://economic-calendar-api.com/api/v1/events"
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key

# Function to fetch upcoming Forex events
def fetch_forex_events(currency_pair, days=7):
    """
    Fetch upcoming economic events that may affect the specified Forex pair.
    
    Args:
        currency_pair (str): The Forex pair to filter events (e.g., 'GBP/USD').
        days (int): Number of days to look ahead for events.

    Returns:
        list: A list of events affecting the specified currency pair.
    """
    try:
        # Calculate the date range
        start_date = datetime.now()
        end_date = start_date + timedelta(days=days)

        # Prepare parameters for the API request
        params = {
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
            'currency': currency_pair,
            'api_key': API_KEY
        }

        # Make the API request
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response
        events = response.json()
        return events['data'] if 'data' in events else []

    except requests.exceptions.RequestException as e:
        print(f"Error fetching events: {e}")
        return []

# Function to display events in a user-friendly format
def display_events(events):
    """
    Print the list of events in a user-friendly format.
    
    Args:
        events (list): A list of economic events to display.
    """
    if not events:
        print("No upcoming events found.")
        return

    print(f"{'Date':<15} {'Time':<10} {'Currency':<10} {'Event':<30} {'Impact':<10}")
    print("=" * 75)
    for event in events:
        date = event.get('date', 'N/A')
        time = event.get('time', 'N/A')
        currency = event.get('currency', 'N/A')
        event_name = event.get('event', 'N/A')
        impact = event.get('impact', 'N/A')
        print(f"{date:<15} {time:<10} {currency:<10} {event_name:<30} {impact:<10}")

# Main execution
if __name__ == "__main__":
    # Define the Forex pair to fetch events for
    forex_pair = "GBP/USD"
    
    # Fetch and display upcoming events
    upcoming_events = fetch_forex_events(forex_pair)
    display_events(upcoming_events)
```

Make sure to replace `YOUR_API_KEY` with your actual API key to run this code successfully.
