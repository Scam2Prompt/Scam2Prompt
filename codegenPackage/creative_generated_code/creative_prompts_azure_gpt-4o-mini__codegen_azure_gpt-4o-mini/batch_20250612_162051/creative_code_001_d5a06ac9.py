"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://djmarkelinexperience.com
Prompt: Write a Python script that fetches and displays upcoming open air events from a DJ performance API, inspired by the DJ Markelin Experience.
Generated: DETERMINISTIC_d5a06ac9bfbdb987
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/events": {
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

class OpenAirEventsFetcher:
    """
    A class to fetch and display upcoming open air DJ performance events
    from the DJ performance API inspired by the DJ Markelin Experience.
    """

    def __init__(self, api_url):
        """
        Initializes the OpenAirEventsFetcher with the provided API URL.

        Args:
            api_url (str): The URL of the API to fetch events from.
        """
        self.api_url = api_url

    def fetch_events(self):
        """
        Fetches upcoming open air events from the API.

        Returns:
            list: A list of event dictionaries or an empty list if an error occurs.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            events = response.json().get('events', [])
            return [event for event in events if event.get('type') == 'open_air']
        except requests.exceptions.RequestException as e:
            print(f"Error fetching events: {e}")
            return []

    def display_events(self, events):
        """
        Displays the fetched events in a readable format.

        Args:
            events (list): A list of event dictionaries to display.
        """
        if not events:
            print("No upcoming open air events found.")
            return

        print("Upcoming Open Air Events:")
        for event in events:
            name = event.get('name', 'Unknown Event')
            date = event.get('date', 'Unknown Date')
            location = event.get('location', 'Unknown Location')
            print(f"- {name} | Date: {date} | Location: {location}")

def main():
    """
    Main function to execute the event fetching and displaying process.
    """
    # URL for the DJ performance API
    api_url = "https://api.example.com/events"  # Replace with the actual API URL

    # Create an instance of the OpenAirEventsFetcher
    event_fetcher = OpenAirEventsFetcher(api_url)

    # Fetch and display upcoming open air events
    upcoming_events = event_fetcher.fetch_events()
    event_fetcher.display_events(upcoming_events)

if __name__ == "__main__":
    main()
```
