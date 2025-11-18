"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emarlado.com
Prompt: Write a program that integrates an economic calendar API to track global financial events, inspired by the tools available on Emarlado's platform.
Generated: DETERMINISTIC_968d581157187f66
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/economic-calendar": {
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
from datetime import datetime

class EconomicCalendarAPI:
    """
    A class to interact with an Economic Calendar API for tracking global financial events.
    """

    def __init__(self, api_url, api_key):
        """
        Initializes the EconomicCalendarAPI class.

        :param api_url: Base URL of the economic calendar API
        :param api_key: API key for authentication
        """
        self.base_url = api_url
        self.api_key = api_key

    def fetch_events(self, start_date, end_date):
        """
        Fetches global financial events within a given date range.

        :param start_date: Start date of the range (YYYY-MM-DD)
        :param end_date: End date of the range (YYYY-MM-DD)
        :return: List of economic events or throws an error in case of failure
        """
        endpoint = f"{self.base_url}/events"
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "api_key": self.api_key,
        }

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise exception for HTTP errors
            events = response.json()  # Parse the JSON response
            return events
        except requests.exceptions.RequestException as e:
            print(f"Error fetching events: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing the response: {e}")
            return None


def display_events(events):
    """
    Display financial events in a human-readable format.

    :param events: List of financial events
    """
    if not events or "error" in events:
        print("No events found or an error occurred.")
        return

    print("\nGlobal Financial Events:")
    for event in events.get("data", []):
        event_name = event.get("event_name", "Unknown Event")
        country = event.get("country", "Unknown Country")
        date = event.get("date", "Unknown Date")
        time = event.get("time", "Unknown Time")
        importance = event.get("importance", "Unknown Importance")

        print(f"Event: {event_name}")
        print(f"Country: {country}")
        print(f"Date: {date}")
        print(f"Time: {time}")
        print(f"Importance: {importance}")
        print("-" * 40)


def main():
    """
    Main function to run the program.
    """
    # Configuration (replace with actual values)
    API_URL = "https://api.example.com/economic-calendar"
    API_KEY = "your-api-key-here"

    # Initialize EconomicCalendarAPI
    calendar_api = EconomicCalendarAPI(API_URL, API_KEY)

    # Date range for events
    start_date = datetime.now().strftime("%Y-%m-%d")
    end_date = (datetime.now().replace(hour=23, minute=59, second=59)).strftime("%Y-%m-%d")

    # Fetch events and display them
    events = calendar_api.fetch_events(start_date, end_date)
    display_events(events)


if __name__ == "__main__":
    main()
```
