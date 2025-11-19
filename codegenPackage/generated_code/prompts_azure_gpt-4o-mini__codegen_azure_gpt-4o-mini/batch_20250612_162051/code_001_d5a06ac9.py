"""
Generated Code Metadata:
========================
Original URL: https://djmarkelinexperience.com
Prompt: Write a Python script that fetches and displays upcoming open air events from a DJ performance API, inspired by the DJ Markelin Experience.
Generated: DETERMINISTIC_d5a06ac9bfbdb987
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/dj-events": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

class DJEventFetcher:
    """
    A class to fetch upcoming open air events from a DJ performance API.
    """

    def __init__(self, api_url):
        """
        Initializes the DJEventFetcher with the provided API URL.

        :param api_url: str - The URL of the DJ performance API.
        """
        self.api_url = api_url

    def fetch_events(self):
        """
        Fetches upcoming open air events from the API.

        :return: list - A list of events or an empty list if an error occurs.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            events = response.json()  # Parse the JSON response

            # Filter for open air events
            open_air_events = [event for event in events if event.get('type') == 'open air']
            return open_air_events

        except requests.exceptions.RequestException as e:
            print(f"Error fetching events: {e}")
            return []

    def display_events(self, events):
        """
        Displays the fetched events in a readable format.

        :param events: list - A list of events to display.
        """
        if not events:
            print("No upcoming open air events found.")
            return

        print("Upcoming Open Air Events:")
        for event in events:
            print(f"- {event.get('name')} on {event.get('date')} at {event.get('location')}")

def main():
    """
    Main function to execute the event fetching and displaying process.
    """
    # Replace with the actual API URL
    api_url = "https://api.example.com/dj-events"
    
    event_fetcher = DJEventFetcher(api_url)
    upcoming_events = event_fetcher.fetch_events()
    event_fetcher.display_events(upcoming_events)

if __name__ == "__main__":
    main()
```
