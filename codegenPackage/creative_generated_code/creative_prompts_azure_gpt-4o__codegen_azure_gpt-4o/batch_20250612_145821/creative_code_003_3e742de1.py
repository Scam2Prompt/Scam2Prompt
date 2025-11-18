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
  "https://economic-calendar-api.example.com/events": {
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
from datetime import datetime, timedelta

# Constants
API_URL = "https://economic-calendar-api.example.com/events"  # Replace with the actual API endpoint
API_KEY = "your-api-key-here"  # Replace with your API key

# Function to fetch Forex events
def fetch_forex_events(api_url, api_key, days_ahead=7):
    """
    Fetch upcoming Forex-related events from an economic calendar API.

    Args:
        api_url (str): The endpoint URL of the economic calendar API.
        api_key (str): The API key for authentication.
        days_ahead (int): Number of days into the future to fetch events for.

    Returns:
        list: A list of upcoming events affecting Forex pairs.
    """
    try:
        # Define the time range for the request
        start_date = datetime.utcnow()
        end_date = start_date + timedelta(days=days_ahead)

        # Prepare query parameters
        params = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "filter": "forex",  # Filter events related to Forex
        }

        # Request headers
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        }

        # Make the API request
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the response JSON
        return response.json().get("events", [])

    except requests.exceptions.RequestException as e:
        # Handle API request errors
        print(f"Error fetching Forex events: {e}")
        return []

# Function to display Forex events in a user-friendly format
def display_events(events):
    """
    Display a list of Forex events in a user-friendly format.

    Args:
        events (list): A list of events to display.
    """
    if not events:
        print("No upcoming Forex events found.")
        return

    print("Upcoming Forex Events:")
    print("-" * 50)
    for event in events:
        # Extract event details
        name = event.get("name", "Unknown Event")
        date = event.get("date", "Unknown Date")
        impact = event.get("impact", "Low")  # Example: Low, Medium, High
        currency = event.get("currency", "N/A")

        # Format the date for display
        event_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
        formatted_date = event_date.strftime("%Y-%m-%d %H:%M:%S UTC")

        # Display the event details
        print(f"Event: {name}")
        print(f"Date: {formatted_date}")
        print(f"Currency: {currency}")
        print(f"Impact: {impact}")
        print("-" * 50)

# Main script logic
if __name__ == "__main__":
    # Fetch events
    forex_events = fetch_forex_events(API_URL, API_KEY)

    # Display the events
    display_events(forex_events)
```

### Notes:
1. Replace `API_URL` and `API_KEY` with the actual API endpoint and your API key.
2. The script assumes the API returns JSON data with an "events" field containing event details.
3. Error handling is included for connectivity issues or malformed responses.
